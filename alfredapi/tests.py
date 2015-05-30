from django.test import TestCase
from .models import OnOffSwitch

class OnOffSwitchTests(TestCase):

    def toggle_flips_state(self):
        """
        toggle should invert the state
        """
        sut = OnOffSwitch()
        initialState = sut.getState()

        sut.toggle()

        self.assertNotEqual(sut.state, initialState)
        sut.toggle()
