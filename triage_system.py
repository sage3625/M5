import heapq

class TriageSystem:
   #create a class to include patient name and evaluate based on severity
    _arrival_counter = 0  # class-level counter

    def __init__(self):
        # internal min-heap: (priority_tuple, name, severity)
        # priority_tuple = (-severity, arrival_order)
        self._queue = []

    @classmethod
    def _next_arrival_order(cls):
#Return next arrival order and increment the counter.
        order = cls._arrival_counter
        cls._arrival_counter += 1
        return order
    #Add patient name and severity of issue
    def AddPatient(self, name, severity):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(severity, int) or severity < 1 or severity > 5:
            raise ValueError("Severity must be an integer between 1 and 5.")

        arrival_order = self._next_arrival_order()
        # Use negative severity so that higher severity comes first in min-heap
        priority = (-severity, arrival_order)
        heapq.heappush(self._queue, (priority, name, severity))

    def ProcessNext(self):
        #Process patient through queue
        if not self._queue:
            return None
        _, name, severity = heapq.heappop(self._queue)
        return name, severity

    def PeekNext(self):
        #return name of the next patient in queue
        if not self._queue:
            return None
        _, name, severity = self._queue[0]
        return name, severity

    def IsEmpty(self):
   #evaluate if patient value is empty return true
        return len(self._queue) == 0

    def Size(self):
        #return the number of patients in the queue
        return len(self._queue)

    def Clear(self):
        #Remove all patients from the queue
        self._queue = []