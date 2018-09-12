'''This module is used to simulate a running raspberry pi generating temperature data'''
import time
import threading

class Simulator:
    def __init__(self, function, period):
        '''
        Creates a simulator using the given function.

        The simulator is started when it is entered with a call to `__enter__(self)`.
        This is useful in combination the python `with` keyword

        Parameters
        ----------
        function : lambda
            A lambda that will be called with no arguments every period after the simulator has started.
        period : float
            The frequency in seconds to call function.
        '''
        self._timer = None
        self.function = function
        self.period = period
        self.is_running = False
        self.next_call = None # has not started so no next_call time yet

    def _run(self):
        self.is_running = False
        self._start()
        self.function()

    def _start(self):
        if not self.is_running:
          self.next_call += self.period
          self._timer = threading.Timer(self.next_call - time.time(), self._run)
          self._timer.start()
          self.is_running = True

    def __enter__(self):
        # start a timer that calls self.generate every self.period
        # this timer is stopped when __exit__ is called
        if self.next_call is None:
            self.next_call = time.time()
        self._start()


    def __exit__(self, exc_type, exc_value, traceback):
        # if we wish to process the exception, we should return true
        # otherwise do nothing and the caller will raise the exception
        self._timer.cancel()
        self.is_running = False
