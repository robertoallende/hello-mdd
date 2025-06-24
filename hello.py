#!/usr/bin/env python3
import random
import os

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    hellos_file = os.path.join(script_dir, 'hellos.txt')
    
    try:
        with open(hellos_file, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]
        
        if lines:
            greeting = random.choice(lines)
            print(greeting)
        else:
            print("No greetings found in the file!")
            
    except FileNotFoundError:
        print("Error: hellos.txt file not found!")
    except Exception as e:
        print(f"Error reading greetings: {e}")

if __name__ == "__main__":
    main()
