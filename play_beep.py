"""
This works on Ubuntu.
Similar operations can be performed in Terminal using the following methods.

Package install:
    $ sudo apt install beep
Turn on pcspkr:
    $ sudo modprobe pcspkr
Play a beep at 440Hz for 1 second:
    $ sudo env -u SUDO_GID -u SUDO_COMMAND -u SUDO_USER -u SUDO_UID beep -f 440 -l 1000
"""

import time
import subprocess

def apt_setup() -> None:
    """Turn on pcspkr."""
    turn_on_pcspkr_cmd = [ "sudo", "modprobe", "pcspkr" ]
    subprocess.run( turn_on_pcspkr_cmd )

def sleep( milliseconds:int ) -> None:
    """Sleep for the specified number of milliseconds.
    I don't use time.sleep() because it stops processing."""
    start_time = time.time()
    while time.time() - start_time < milliseconds /1000:
        pass

def play_beep( frequency :int, millisec:int ) -> None:
    """Play beep for frequency and millisec."""
    play_beep_cmd = [   "sudo", "env", "-u", "SUDO_GID", "-u", "SUDO_COMMAND", "-u",
                        "SUDO_USER", "-u", "SUDO_UID", "beep", "-f", str(frequency), "-l", str(millisec) ]
    subprocess.run( play_beep_cmd )

def play_time( sec:int, wait:int, count:int ) -> None:
    """Calculate the total time the beep will play"""
    sum = 0
    for i in range( count ):
        sum += sec
        sum += wait / ( 2**i )
    print( f"The total time the beep will play {sum/1000:.2}s." )

def main():
    # Parameters
    freq:int     = 880      # Hz
    sec:int      = 200      # ms
    last_sec:int = 3000     # ms
    wait:int     = 2000     # ms
    count:int    = 10       # number

    # Calculate the total time the beep will play
    # play_time( sec, wait, count )

    # Playback of beep sounds like a countdown until explosion!
    apt_setup()
    for i in range( count ):
        play_beep( freq, sec )
        print( count-i )
        sleep( wait / ( 2**i ) )
    play_beep( freq, last_sec )


if __name__ == "__main__":
    main()

