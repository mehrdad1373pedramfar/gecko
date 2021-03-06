import time

import pytest
from nanohttp import settings, HTTPStatus

from gecko.tests.helpers import LocalApplicationTestCase
from gecko.tokens import RegisterationToken, ResetPasswordToken


class TestTokens(LocalApplicationTestCase):

    def test_reset_password_token(self):

        # Create reset password token using dump and load mothods
        payload = dict(a=1, b=2)
        reset_password_token = ResetPasswordToken(payload)
        dump = reset_password_token.dump()
        load = ResetPasswordToken.load(dump.decode())
        assert load == payload

        # Trying to load token using bad signature token
        with pytest.raises(
            HTTPStatus('607 Malformed Token').__class__
        ):
            load = ResetPasswordToken.load('token')

        # Trying to load token when token is expired
        with pytest.raises(
            HTTPStatus('609 Token Expired').__class__
        ):
            settings.reset_password.max_age = 0.3
            reset_password_token = ResetPasswordToken(payload)
            dump = reset_password_token.dump()
            time.sleep(1)
            load = ResetPasswordToken.load(dump.decode())

    def test_registeration_token(self):

        # Create registeration token using dump and load mothods
        payload = dict(a=1, b=2)
        registeration_token = RegisterationToken(payload)
        dump = registeration_token.dump()
        load = RegisterationToken.load(dump.decode())
        assert load == payload

        # Trying to load token using bad signature token
        with pytest.raises(
            HTTPStatus('607 Malformed Token').__class__
        ):
            load = RegisterationToken.load('token')

        # Trying to load token when token is expired
        with pytest.raises(
            HTTPStatus('609 Token Expired').__class__
        ):
            settings.registeration.max_age = 0.3
            registeration_token = RegisterationToken(payload)
            dump = registeration_token.dump()
            time.sleep(1)
            load = RegisterationToken.load(dump.decode())

