# Lab 4: LED Light Show with Lists

Welcome to Lab 4! In this lab, you will create dynamic LED light shows using list programming concepts through hardware control.

## Learning Objectives

Master **Python lists** through interactive LED control:
- **List creation and organization** - group LED objects, colors, timings, and patterns
- **List indexing and iteration** - access specific LEDs and cycle through patterns
- **List methods** - use `len()`, slicing `[::-1]`, and `join()` for dynamic control
- **Scalable programming** - same code works with 3 or 6 LEDs automatically

*This assignment aligns with CMPSC 100 Learning Outcomes 1 and 2, focusing on Python programming fundamentals applied to hardware control. It builds on previous labs' concepts while introducing lists as a key programming tool for organizing and processing data. This lab also fulfills Allegheny College's Quantitative Reasoning (QR) distribution requirement through algorithmic thinking, data organization, and computational problem-solving applied to physical systems.*

## Prerequisites

Before starting this lab, ensure you have:
- VS Code with MicroPico extension installed (from Lab 2)
- Your Pico 2 W board and USB cable ready
- Understanding of IoT concepts from Lab 1 (sensor simulation and system monitoring)
- Experience with basic LED control from Lab 2 (pin configuration and hardware basics)
- Completed Lab 3 (for loops, nested loops, and conditional logic)
- Understanding of loops and conditionals from Weeks 3-5

### Hardware Components:
- **3 external LEDs** (any colors)
- **3 × 220Ω or 330Ω resistors** (both work fine - 330Ω makes LEDs slightly dimmer)
- **1 breadboard**
- **4-5 jumper wires** (male-to-male, any colors) - fewer needed with efficient wiring!

## Hardware Concepts

### GPIO (General Purpose Input/Output)
**GPIO pins** are programmable pins that can be set as inputs or outputs. For LEDs:
- **Pin.OUT mode**: Pin acts as an output, sending electrical signals
- **Digital control**: Pin can be HIGH (3.3V) or LOW (0V)
- **Current sourcing**: GPIO pins provide current to power LEDs

### Circuit Components

#### Breadboard
- **Horizontal rows**: Each 5-hole row is internally connected
- **Power rails**: Vertical columns for power distribution (+/-) 
- **Center gap**: Separates left and right sides

**Optional Watching**: [How to Use a Breadboard](https://www.youtube.com/watch?v=6WReFkfrUIk) - Helpful video tutorial on breadboard basics and connections

#### LEDs (Light Emitting Diodes)
- **Polarity matters**: Long leg (anode +) to power, short leg (cathode -) to ground
- **Forward voltage**: LEDs drop ~2-3V when conducting
- **Current limiting required**: Use resistors to prevent damage

#### Resistors (220Ω or 330Ω)
- **Current limiting**: Protects LEDs from excessive current
- **Ohm's law**: V = I × R determines current flow
- **220Ω** (Red-Red-Brown-Gold): Brighter LEDs, ~10mA current
- **330Ω** (Orange-Orange-Brown-Gold): Slightly dimmer LEDs, ~7mA current
- **Both work perfectly** - use whichever you have available

## Circuit Assembly

### Pinout Reference
![Pico 2 W Pinout](pico-2-r4-pinout.svg)

### Example Wiring (adapt to your chosen pins):
- **LED 1**: GPIO 15 → 220Ω/330Ω resistor → LED → Ground
- **LED 2**: GPIO 14 → 220Ω/330Ω resistor → LED → Ground  
- **LED 3**: GPIO 13 → 220Ω/330Ω resistor → LED → Ground
- **Power**: 3V3 (Pin 36) → breadboard power rail
- **Ground**: GND (Pin 38) → breadboard ground rail

### Detailed Assembly Steps:

#### Step 1: Prepare Your Workspace
- **Disconnect** your Pico from USB (very important for safety!)
- Lay out all components: Pico, breadboard, 3 LEDs, 3 resistors, 6-8 jumper wires
- Identify breadboard sections: horizontal rows (numbered 1-30+), vertical power rails (red/blue strips)

**Why disconnect USB for safety?**
- **Prevents accidental short circuits** that could damage your Pico or computer
- **Avoids power conflicts** between USB power and potential wiring mistakes
- **Protects against current spikes** if you accidentally connect power and ground
- **Industry standard practice** - professionals always power down before building circuits

#### Step 2: Place the Pico on Breadboard
- **Orient breadboard**: Power rails on top and bottom edges
- **Position Pico**: Place it across the center gap (groove) of the breadboard
  - USB connector should point toward one end (usually toward you)
  - **Left side pins**: Insert into column C, rows 1-20
  - **Right side pins**: Insert into column H, rows 1-20
- **Push firmly**: Ensure all pins are fully inserted and Pico sits flat

#### Step 3: Connect Power Rails (Critical!)
- **Power jumper wire**: Connect 3V3 (Pin 36, row 18 column C) to red power rail (+)
  - Insert one end of jumper wire into row 18, column D (same row as 3V3)
  - Insert other end into red power rail (marked with + or red line)
- **Ground jumper wire**: Connect to blue power rail (-) - **Efficient approach**
  - Insert one end into row 3, column J (or any convenient row)
  - Insert other end into blue power rail (marked with - or blue line)
  - This creates a **common ground point** for all LED cathodes

#### Step 4: Build LED Circuit #1 (Example: GPIO 15)
**Component Placement:**
- **LED placement**: Use row 25 (or any available row)
  - **Long leg (anode)**: Insert into row 25, column E (can use other columns C, D, or F)
  - **Short leg (cathode)**: Insert into row 25, column F (adjacent to long leg)
  - **LED direction**: Can point up or sideways

**Resistor Connection:**
- **Current-limiting resistor** (220Ω or 330Ω): Connect LED to GPIO pin
  - **One end**: Insert into row 25, column D (same row as LED long leg)
  - **Other end**: Insert into row 22, column D (or any available row)

**Wire Connections:**
- **GPIO wire**: Connect GPIO 15 to resistor
  - Find GPIO 15 on Pico (check pinout for exact row)
  - **One end**: Insert into same row as GPIO 15, column D
  - **Other end**: Insert into row 22, column C (same row as resistor)
- **Ground wire**: Connect LED cathode to common ground
  - **One end**: Insert into row 25, column G (same row as LED short leg)
  - **Other end**: Insert into row 3, column I (your common ground row)

#### Step 5: Build LED Circuit #2 (Example: GPIO 14)
**Component Placement:**
- **LED placement**: Use row 26
  - **Long leg**: Row 26, column E
  - **Short leg**: Row 26, column F

**Resistor Connection:**
- **Current-limiting resistor** (220Ω or 330Ω): 
  - **One end**: Row 26, column D (with LED long leg)
  - **Other end**: Row 23, column D

**Wire Connections:**
- **GPIO wire**: GPIO 14 pin (find exact row) → row 23, column C
- **Ground wire**: Row 26, column G → row 3, column H (common ground)

#### Step 6: Build LED Circuit #3 (Example: GPIO 13)
**Component Placement:**
- **LED placement**: Use row 27
  - **Long leg**: Row 27, column E
  - **Short leg**: Row 27, column F

**Resistor Connection:**
- **Current-limiting resistor** (220Ω or 330Ω):
  - **One end**: Row 27, column D
  - **Other end**: Row 24, column D

**Wire Connections:**
- **GPIO wire**: GPIO 13 pin (find exact row) → row 24, column C
- **Ground wire**: Row 27, column G → row 3, column G (common ground)

**💡 Efficient Wiring Tip:** You can place LEDs in different columns (C, D, E, F) as long as you maintain the same connection pattern. The key is using one common ground row for all LED cathodes!

#### Step 7: Final Safety Check
- **Visual inspection**: All wires fully inserted, no loose connections
- **LED polarity**: Long legs in column E, short legs in column F (or your chosen columns)
- **Common ground**: All LED cathodes connect to the same ground row (row 3)
- **No short circuits**: Wires not touching each other inappropriately
- **Component security**: All parts firmly seated in breadboard
- **Efficient design**: Only 4 jumper wires needed for complete circuit!

**⚠️ Safety**: Always disconnect USB when building circuits!

## Programming with Lists

Open `src/main.py` and work through the TODOs to create your list-powered LED show:

### Core Programming Tasks:
1. **LED Setup Lists** - Create lists to organize LED pins, names, and colors
2. **Pattern Lists** - Use lists to define light show patterns and timings  
3. **User Preference Lists** - Store speed choices and show options in lists
4. **List Iteration** - Use for loops to cycle through LED lists
5. **List Methods** - Apply `len()`, slicing, and indexing for dynamic control
6. **Interactive Programming** - Get user input and customize show parameters

### Understanding the Light Show Patterns

#### Chase Pattern
The **Chase pattern** lights LEDs one by one in sequence, creating a "chasing" effect:
```python
for i in range(9):  # Loop 9 times to show multiple cycles
    led_index = i % len(led_list)  # Use modulo to cycle through LEDs
    print(f"  Lighting {led_names[led_index]} LED...")
    led_list[led_index].on()   # Turn on current LED
    time.sleep(light_delay)    # Wait
    led_list[led_index].off()  # Turn off current LED
```

**What does `i % len(led_list)` do?**
- **Modulo operator (%)** gives the remainder after division
- With 3 LEDs: `i % 3` cycles through 0, 1, 2, 0, 1, 2, ...
- When `i=0`: `0 % 3 = 0` (first LED)
- When `i=3`: `3 % 3 = 0` (back to first LED)
- When `i=7`: `7 % 3 = 1` (second LED)
- This creates a repeating pattern that works with any number of LEDs!

#### All Blink Pattern
The **All Blink pattern** flashes all LEDs together multiple times:
```python
for count in flash_counts[:3]:  # Use first 3 values: [2, 3, 4]
    print(f"  All LEDs blinking {count} times...")
    for blink in range(count):  # Blink 2 times, then 3 times, then 4 times
        # Turn all LEDs on
        for led in led_list:
            led.on()
        time.sleep(light_delay)
        # Turn all LEDs off
        for led in led_list:
            led.off()
        time.sleep(light_delay * 0.3)
```

**List Slicing**: `flash_counts[:3]` takes the first 3 items from `[2, 3, 4, 5, 6]` → `[2, 3, 4]`

#### Reverse Chase Pattern
The **Reverse Chase pattern** creates a chase effect in the opposite direction:
```python
reversed_leds = led_list[::-1]  # Reverse the LED list
reversed_names = led_names[::-1]  # Reverse the names too
for i in range(len(reversed_leds)):
    print(f"  Lighting {reversed_names[i]} LED (reverse)...")
    reversed_leds[i].on()
    time.sleep(light_delay)
    reversed_leds[i].off()
```

**List Reversal**: `[::-1]` creates a reversed copy of the list without modifying the original.

#### Wave Pattern  
The **Wave pattern** creates a smooth wave effect going forward then backward.

**Backward Iteration**: `range(len(led_list) - 1, -1, -1)` counts backward from last index to 0.

#### Pulse Pattern
The **Pulse pattern** pulses each LED individually multiple times.

### Required Lists for Complete Implementation

Your program must create and use **all 9 lists** to demonstrate comprehensive list programming skills:

#### Essential Lists (6 required):
1. **`led_list`** - Pin objects for GPIO control
2. **`led_names`** - LED descriptions for user messages
3. **`led_pins`** - Pin numbers for reference
4. **`speed_options`** - Timing delays for user speed choices
5. **`speed_names`** - Speed descriptions for menu display
6. **`pattern_names`** - Pattern names for show sequence

#### Advanced Pattern Lists (3 required):
7. **`chase_speeds`** - Timing variations for chase pattern
8. **`flash_durations`** - Timing variations for wave pattern
9. **`flash_counts`** - Flash count variations for all blink pattern

**Important**: Each pattern must use its designated lists to create variety and demonstrate list programming concepts. Your TODOs specify which lists to use for each pattern - follow them carefully to ensure all lists are utilized!

## Optional Challenge: 6-LED Light Show

Ready for a bigger challenge? Expand your circuit and code to control **6 LEDs** instead of 3!

### Hardware Expansion:
- **Add 3 more LEDs** to rows 28, 29, and 30 using the same efficient wiring pattern
- **Use GPIO pins 12, 11, and 10** for the additional LEDs (or any available GPIO pins)
- **Same resistor values**: 220Ω or 330Ω work perfectly for all 6 LEDs
- **Common ground**: All 6 LED cathodes connect to your row 3 ground point
- **Total jumper wires**: Still only need 5-6 wires (1 power, 1 common ground, 4-5 GPIO)

*This challenge perfectly demonstrates why lists are essential for scalable programming - your core logic remains the same whether controlling 3 or 6 LEDs!*

## Optional Challenge: Input Validation

Want to make your program more robust? Add input validation to handle user errors gracefully!

### Validation Ideas:
- **Speed choice validation**: Check if user enters 1-5, default to "Medium" if invalid
- **Pattern count validation**: Ensure input is between 3-10, clamp to valid range
- **Finale choice validation**: Handle invalid finale selections
- **Non-numeric input**: Use try/except blocks to catch ValueError exceptions

## Testing Your Code

1. **Test circuit**: Run `src/test_LED.py` to verify all LEDs work
2. **Run main program**: Execute your list-powered light show
3. **Verify patterns**: Check that list iteration creates correct LED sequences
4. **Test user interaction**: Confirm input handling and show customization

## Troubleshooting

### Circuit Issues:
- **LEDs not lighting**: Check polarity, resistors, and GPIO pin numbers
- **Partial lighting**: Verify power rail connections (3V3 and GND)
- **Inconsistent behavior**: Ensure secure breadboard connections

### Code Issues:
- **List errors**: Check list syntax `[item1, item2, item3]` and indexing `list[0]`
- **Loop problems**: Verify indentation and range values
- **User input**: Test input validation and variable assignments

## Submission Instructions

Submit to GitHub frequently! Use this workflow:

```bash
git add src/main.py writing/reflection.md
git commit -m "Complete LED light show with lists programming"
git push
```

Verify your submission online and ensure GatorGrade passes automated testing.

## Getting Help

### During Lab
- Ask TLs or instructor for help with specific questions or hardware issues
- Work with classmates on understanding concepts (but write your own code)
- Use the lab time to understand list concepts and get started with your program

### Outside Lab  
- Post questions in Discord
- Attend [TL office hours](https://www.cis.allegheny.edu/teaching/technicalleaders/) and/or [instructor office hours](https://janyljumadinova.com/schedule/) to seek help outside of class
- Review the slides for concept reinforcement

### Resources
- [Python Documentation](https://docs.python.org/3/)
- [MicroPython Documentation](https://docs.micropython.org/)
- Course slides and examples from class activities

## Assessment Criteria - Total: 4.5 Points

### Technical Implementation (3.0 points)
- **Automated GatorGrade checks**: 2.0 points (based on 13 list programming checks)
- **Hardware execution verification**: 1.0 point (program runs correctly on Pico with LED circuit)

### Code Quality and Style (1.0 point)  
- **Descriptive variable names** and **clean organization** (0.6 pts)
- **Appropriate comments** explaining list logic (0.4 pts)

### Reflection and Engagement (0.5 points)
- **Thoughtful reflection** on list programming concepts and hardware integration

*GatorGrade checks verify: file structure, list creation/usage, LED control, loop patterns, and code organization*

### Grading Information
- **Grades will be released in Canvas** after manual code review is complete
- **Detailed feedback will be provided as a GitHub issue** in your Lab 4 repository
- Check your repository for personalized feedback on code quality and suggestions for improvement

## Sample Output

Example output from your list-powered LED light show (LEDs create visual patterns):

```
*** LED Light Show with Lists ***
====================================================
Welcome to your list-powered LED light show!
====================================================

What's your name? JJ

Hi JJ! Choose your light speed:
1. Very Slow (1.2s)
2. Slow (0.8s)
3. Medium (0.5s)
4. Fast (0.3s)
5. Lightning (0.1s)
Enter choice (1-5): 3

Testing LEDs using lists...
  Testing Red LED...
  Testing Yellow LED...
  Testing Green LED...
LED test complete!

How many patterns do you want? (3-10): 5

Starting JJ's list-controlled light show!

Pattern 1: Chase
  Lighting Red LED...
  Lighting Yellow LED...
  Lighting Green LED...
  Lighting Red LED...
  Lighting Yellow LED...
  Lighting Green LED...
  Lighting Red LED...
  Lighting Yellow LED...
  Lighting Green LED...

Pattern 2: All Blink
  All LEDs blinking 2 times...
  All LEDs blinking 3 times...
  All LEDs blinking 4 times...

Pattern 3: Reverse Chase
  Lighting Green LED (reverse)...
  Lighting Yellow LED (reverse)...
  Lighting Red LED (reverse)...
  Lighting Green LED (reverse)...
  Lighting Yellow LED (reverse)...
  Lighting Red LED (reverse)...
  Lighting Green LED (reverse)...
  Lighting Yellow LED (reverse)...
  Lighting Red LED (reverse)...

Pattern 4: Wave
  Wave forward: Red LED...
  Wave forward: Yellow LED...
  Wave forward: Green LED...
  Wave backward: Green LED...
  Wave backward: Yellow LED...
  Wave backward: Red LED...
  Wave forward: Red LED...
  Wave forward: Yellow LED...
  Wave forward: Green LED...
  Wave backward: Green LED...
  Wave backward: Yellow LED...
  Wave backward: Red LED...

Pattern 5: Pulse
  Pulsing Red LED...
  Pulsing Yellow LED...
  Pulsing Green LED...

Grand finale: Spectacular Light Storm!
Preparing the grand finale...

*** Light Show Complete! ***
Thanks JJ!
Show Summary:
  - Speed setting: Medium
  - Patterns shown: 5
  - LEDs used: Red, Yellow, Green
  - Finale: Spectacular Light Storm
Hope you enjoyed your list-powered LED show!
```

*Your LEDs will create dynamic visual patterns demonstrating list programming concepts.*
