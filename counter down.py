import time

def countdown_timer(seconds):
    while seconds:
        # Calculate minutes and seconds
        mins, secs = divmod(seconds, 60)
        # Format the time as MM:SS
        timer = f"{mins:02d}:{secs:02d}"
        # Print the timer
        print(timer, end="\r")
        # Wait for 1 second
        time.sleep(1)
        # Decrement the seconds
        seconds -= 1

    print("Time's up!")

def main():
    try:
        # Ask the user for the countdown duration
        duration = int(input("Enter the countdown duration in seconds: "))
        if duration <= 0:
            print("Please enter a positive number.")
        else:
            # Start the countdown
            countdown_timer(duration)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
