from django.test import TestCase
from .models import OnOffSwitch

class OnOffSwitchTests(TestCase):

    def toggle_flips_state(self):
        """
        toggle should invert the state
        """
        sut = OnOffSwitch()
        initialState = sut.getState()

        sut.toggleState()

        self.assertEqual(sut.state, initialState)
        sut.toggleState()
