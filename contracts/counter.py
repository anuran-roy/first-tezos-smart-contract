import smartpy as sp

class Counter(sp.Contract):
    def __init__(self, initial_value):
        self.init(stored_value=initial_value)

    @sp.entry_point
    def increment(self, params):
        self.data.stored_value += params.value

    @sp.entry_point
    def decrement(self, params):
        self.data.stored_value -= params.value


@sp.add_test(name="Counter")
def test():
    scenario = sp.test_scenario()
    counter = Counter(initial_value=0)
    scenario += counter

    scenario.verify(counter.data.stored_value == 0)

    scenario += counter.increment(value = 1)
    scenario.verify(counter.data.stored_value == 1)


    scenario += counter.decrement(value = 1)
    scenario.verify(counter.data.stored_value == 0)

sp.add_compilation_target("counter", Counter(initial_value=0))