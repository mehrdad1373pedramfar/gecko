from restfulpy.testing import ApplicableTestCase

from gecko import Gecko, cryptohelpers


class LocalApplicationTestCase(ApplicableTestCase):
    __application_factory__ = Gecko


class RandomMonkeyPatch:
    """
    For faking the random function
    """

    fake_random = None

    def __init__(self, fake_random):
        self.__class__.fake_random = fake_random

    @staticmethod
    def random(size):
        return RandomMonkeyPatch.fake_random[:size]

    def __enter__(self):
        self.real_random = cryptohelpers.random
        cryptohelpers.random = RandomMonkeyPatch.random

    def __exit__(self, exc_type, exc_val, exc_tb):
        cryptohelpers.random = self.real_random

