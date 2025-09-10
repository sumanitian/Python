import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        # we are sleeping because this is complex process, this take some 1 second to perform.
        time.sleep(1)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing Chai for #{i}")
        time.sleep(2)

# Create the threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

#invoking the threads
order_thread.start()
brew_thread.start()

# i have to wait for both to have finish.

# Wait until the thread terminates.
order_thread.join()
brew_thread.join()

print(f"All orders take and chai brewed")