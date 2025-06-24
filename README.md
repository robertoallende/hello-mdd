# Universal Hello World

A simple script that greets you with "Hello" in a random human language from around the world.

## What This Does

Run the script and get a friendly greeting in one of 74 different languages! Each time you run it, you'll see a different language and learn how to say hello in cultures from across the globe.

## Usage

Make sure you have Python 3 installed, then simply run:

```bash
python3 hello.py
```

Example outputs:
```
Spanish: Hola
Japanese: こんにちは
Swahili: Hujambo
Armenian: Բարև
```

## Requirements

- Python 3
- No additional dependencies needed!

## How It Works

The project consists of just two files:
- `hellos.txt` - Contains 74 greetings from languages around the world
- `hello.py` - Python script that randomly picks and displays one greeting

## Languages Included

The project includes greetings from major world languages, regional languages, and languages with different writing systems including Latin, Cyrillic, Arabic, Chinese characters, and many others.

## Contributing

Want to add more languages? Simply add a new line to `hellos.txt` following the format:
```
Language Name: Greeting
```

Make sure to use proper UTF-8 encoding for international characters.

## About This Project

This Universal Hello World project serves as a demonstration of [Micromanaged Driven Development (MDD)](https://github.com/robertoallende/micromanaged-driven-development) - a systematic approach to AI-assisted software development through granular task breakdown and chronological tracking.

The entire development process, from initial planning to implementation, has been documented using MDD principles. You can see the complete development log in the `dev_log/` directory.

## License

This project is open source. See the LICENSE file for details.
