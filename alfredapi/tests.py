from django.test import TestCase
from .models import OnOffSwitch

class OnOffSwitchTests(TestCase):

    def test_toggle_flips_state(self):
        """
        toggle should invert the state
        """
        sut = OnOffSwitch()
        initialstate = sut.get_state()

        sut.toggle_state()

        self.assertEqual(sut.get_state(), initialstate)
        sut.toggle_state()
