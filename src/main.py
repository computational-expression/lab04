"""
Lab 4: LED Light Show with Lists
CMPSC 100 - Computational Expression

Student Name: [Your name here]
Date: [Lab 4 Date]

Purpose: Create an LED light show using lists to organize and control multiple LEDs.
Practice working with lists, iteration, indexing, and list methods.
"""

# Import necessary modules for hardware control
from machine import Pin
import time

# TODO 1: Create lists to organize LEDs and their properties
# Set up 3 LEDs for light show control (GPIO pins 15, 14, 13)
# Create these lists, naming each list as specified below (exactly 3 items each):
# - led_list: List of Pin objects [Pin(15, Pin.OUT), Pin(14, Pin.OUT), Pin(13, Pin.OUT)]
# - led_names: List of descriptive names like ["Red", "Yellow", "Green"]
# - led_pins: List of pin numbers [15, 14, 13]

led_list = [Pin(15, Pin.OUT), Pin(14, Pin.OUT), Pin(13, Pin.OUT)]  # You can change GPIO pins
led_names = []  # Add your LED names here
led_pins = []  # Add your pin numbers here

# TODO 2: Create lists for user options and show control
# Create these lists with exact names and sizes as specified below:
# - speed_options: List of 5 timing delays, for example [1.2, 0.8, 0.5, 0.3, 0.1]
# - speed_names: List of 5 speed descriptions, for example ["Very Slow", "Slow", "Medium", "Fast", "Lightning"]
# - pattern_names: List of 5+ pattern names, must include ["Chase", "All Blink", "Reverse Chase", "Wave", "Pulse"]

# Your user option lists here:


# TODO 2b: Create additional lists for advanced patterns (minimum 3 lists, 5+ items each)
# Create at least these 3 lists to add variety to your patterns:
# - chase_speeds: List of 5+ timing values (example: [0.1, 0.2, 0.3, 0.4, 0.5])
# - flash_durations: List of 5+ flash timing values (example: [0.1, 0.15, 0.2, 0.25, 0.3])
# - flash_counts: List of 5+ flash count options (example: [2, 3, 4, 5, 6]) - USED in All Blink pattern

# Your additional pattern lists here:

def main():
    """Main function that runs the LED light show using lists"""
    
    # TODO 3: Print welcome banner, welcome message and get user name    
    
    # TODO 4: Display speed options and get user choice (USE speed_names and speed_options lists)
    # Print something similar to: "Hi {name}! Choose your light speed from:"
    # Use for loop with range(len(speed_names)) to display speed options from speed_names list
    # Get user choice with input(f"Enter choice (1-{len(speed_options)}): ")
    # Convert to index: light_delay = speed_options[choice - 1]
    # Store speed name: speed_name = speed_names[choice - 1]
    
    # TODO 5: Test LEDs using list iteration (USE led_list and led_names lists)
    # Print something like "\nTesting LEDs..."
    # Use a for loop: for each LED (iterate through led_list as `for num in range(len(led_list))`): 
    # - print f"Testing {led_names[i]} LED...", 
    # - turn on led_list[num] with led_list[num].on(), 
    # - wait a few seconds, 
    # - turn off that led
    # Print something similar to "LED test complete!"
    
    # TODO 6: Get show preferences
    # Ask: "\nHow many patterns do you want? (3-10): "
    # Store the number in num_patterns variable
    # Print: f"\nStarting {user_name}'s list-controlled light show!"
    
    # TODO 7: Run light show patterns using lists (USE pattern_names, led_list, led_names, flash_counts, chase_speeds, flash_durations)
    # Use for pattern_num in range(num_patterns): to create patterns
    # Print: f"\nPattern {pattern_num + 1}: {pattern_names[pattern_num % len(pattern_names)]}"
    # Use if elif to check for a specific pattern (pattern_index = pattern_num % len(pattern_names))
    # 
    # Chase pattern (pattern_index 0): USE led_list, led_names, and chase_speeds lists
    #   Use for i in range(9): and led_list[i % len(led_list)]
    #   Print: f"Lighting {led_names[i % len(led_names)]} LED..."
    #   Use chase_speeds list: chase_speed = chase_speeds[pattern_num % len(chase_speeds)]
    #   Turn on LED, sleep(chase_speed), turn off LED, sleep(chase_speed * 0.2)
    # 
    # All Blink pattern (pattern_index 1): USE flash_counts and led_list lists
    #   Use for count in flash_counts[:3]:  # Use first 3 from flash_counts list
    #   Print: f"  All LEDs blinking {count} times..."
    #   Use nested loop: for blink in range(count):
    #     Turn all LEDs on with: for led in led_list: led.on()
    #     Sleep, then turn all off with: for led in led_list: led.off()
    # 
    # Reverse Chase pattern (pattern_index 2): USE led_list and led_names lists
    #   Use led_list[::-1] to reverse the list
    #   Similar to chase but iterate through reversed LED list
    #   Hint: reversed_leds = led_list[::-1] and reversed_names = led_names[::-1]
    # 
    # Wave pattern (pattern_index 3): USE led_list and flash_durations lists
    #   Create a wave effect going forward then backward
    #   Use flash_durations list: flash_duration = flash_durations[pattern_num % len(flash_durations)]
    #   Wave forward: for i in range(len(led_list)): light LED i
    #   Wave backward: for i in range(len(led_list) - 1, -1, -1): light LED i
    #   Repeat the wave 2-3 times for full effect
    # 
    # Pulse pattern (pattern_index 4): USE led_list and led_names lists
    #   Individual LED pulses
    #   For each LED: for led_index in range(len(led_list)):
    #   Print: f"Pulsing {led_names[led_index]} LED..."
    #   Pulse each LED multiple times: for pulse in range(repeat_count):
    #   Use short on/off durations for pulse effect
    
    # TODO 8: Create your own grand finale!
    # Design an impressive finale pattern of your own choosing
    # Ideas: rapid flashing, wave effects, alternating patterns, fade effects
    # Use your creativity with lists and loops!
    # Example Strobe effect: 
    #   for strobe in range(15):
    #     for led in led_list: led.on()
    #     time.sleep(0.1)
    #     for led in led_list: led.off() 
    #     time.sleep(0.1)
    # Print what finale you're doing: print("\nGrand finale: [Your finale name]!")
    
    # Your creative finale code here:
    
    
    # TODO 9: Display summary using lists (USE led_names list with join method)
    # Print "\n*** Light Show Complete! ***"
    # Print f"Thanks {user_name}!"
    # Print "Show Summary:"
    # Print f"  - Speed setting: {speed_name}"
    # Print f"  - Patterns shown: {num_patterns}"
    # Print f"  - LEDs used: {', '.join(led_names)}"  # USE led_names list with join method
    # Print f"  - Finale: [Your finale name]"
    # Print "Hope you enjoyed your list-powered LED show!"
    # Turn off all LEDs using: for led in led_list: led.off()  # USE led_list
    
    # Your summary code here:
    
# Main guard is provided for you:
if __name__ == "__main__":
    main()

