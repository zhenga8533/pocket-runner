def override(interface):
    def overrider(method):
        assert(method.__name__ in dir(interface))
        return method
    return overrider
