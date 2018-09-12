
if __name__ == '__main__':
    from client.rpi.simulator import Simulator
    def function():
        print("Generating JSON payload...")

    period = 1 # seconds
    with Simulator(function, period):
        print("Simlating temperature reader, press enter to stop simulating...")
        while True:
            i = input()
            if not i:
                break
