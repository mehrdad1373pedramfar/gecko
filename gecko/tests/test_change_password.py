from bddrest import Update, Remove, when, status

from gecko.models import Member
from gecko.tests.helpers import LocalApplicationTestCase


class TestChangePassword(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        member = Member(
            email='already.added@example.com',
            title='username',
            password='123abcABC'
        )
        session = cls.create_session()
        session.add(member)
        session.commit()

    def test_change_password(self):
        session = self.create_session()
        old_password_hash = session.query(Member).one().password

        self.login(
            email='already.added@example.com',
            password='123abcABC',
            url='/apiv1/tokens',
            verb='CREATE'
        )

        with self.given(
            'The password has been successfully changed',
            '/apiv1/passwords',
            'change',
            form=dict(
                currentPassword='123abcABC',
                newPassword='NewPassword123'
            )
        ):
            assert status == 200

            new_password_hash = session.query(Member).one().password
            assert new_password_hash != old_password_hash

            when(
                'Trying to pass using the wrong password',
                form=Update(
                    currentPassword='123abc',
                    newPassword='NewPassword123'
                )
            )
            assert status == '602 Invalid Current Password'

            when(
                'Trying to pass without current password parameter',
                form=Remove('currentPassword')
            )
            assert status == '602 Invalid Current Password'

            when(
                'Trying to pass a simple password',
                form=Update(newPassword='123')
            )
            assert status == '703 Password Not Complex Enough'

            when(
                'Trying to pass a short password',
                form=Update(newPassword='1aA')
            )
            assert status == '702 Invalid Password Length'

            when(
                'Trying to pass a long password',
                form=Update(newPassword='1aA123456789123456789')
            )
            assert status == '702 Invalid Password Length'

            when(
                'Trying to pass without new password parameter',
                form=Remove('newPassword')
            )
            assert status == '702 Invalid Password Length'

            when('Trying to pass with empty form', form={})
            assert status == '400 Empty Form'

