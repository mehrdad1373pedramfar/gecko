from bddrest import when, status

from gecko.models import Member
from gecko.tests.helpers import LocalApplicationTestCase


class TestLogout(LocalApplicationTestCase):

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

    def test_logout(self):
        self.login(
            email='already.added@example.com',
            password='123abcABC',
            url='/apiv1/tokens',
            verb='CREATE'
        )

        with self.given(
            'The member has been successfully logout',
            '/apiv1/tokens',
            'INVALIDATE',
        ):
            assert status == 200

            when('Trying to pass unathorized member')
            assert status == 401

