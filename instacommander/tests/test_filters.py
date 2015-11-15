from . import fixtures
from .helpers import GeneralTestCase
from instacommander import renderers
from nose.plugins.attrib import attr


class FiltersTestCase(GeneralTestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # @attr('single')
    def test_to_ascii(self):
        'Testing InstaCommander.renderers.to_ascii'
        img_fp = fixtures.typical_picture()

        ascii_stream = renderers.to_ascii(img_fp)
        self.assertGreater(len(ascii_stream), 1, "ASCII successfully converted")
