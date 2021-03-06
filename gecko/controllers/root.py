from nanohttp import Controller, json
from restfulpy.controllers import RootController

import gecko
from .availabilities import AvailabilityController
from .email import EmailController
from .member import MemberController
from .password import PasswordController
from .reset_password_token import ResetPasswordTokenController
from .token import TokenController
from .foo import FooController


class ApiV1(Controller):
    emails = EmailController()
    members = MemberController()
    availabilities = AvailabilityController()
    tokens = TokenController()
    resetpasswordtokens = ResetPasswordTokenController()
    passwords = PasswordController()
    foos = FooController()

    @json
    def version(self):
        return {
            'version': gecko.__version__
        }


class Root(RootController):
    apiv1 = ApiV1()

