| I highly recommend to check [nori.ni](https://github.com/mkukiro/nori.ni) too! It is another esolang of mine, but oryx won't be updated since it's for a jam, nori.ni is upadated frequently instead! <img src="https://nukocities.neocities.org/nuko/act/cat4.gif">|
| - |

<img align="right" height="145" src=".meow/oryx.svg">

# oryx [<img src="https://nukocities.neocities.org/nuko/react/cat19.gif">](https://nukocities.neocities.org/)

oryx is a 2D, stack-based esolang made for an esojam, this esolang was made in under 2 hours!

To run `main.yx` just type `python main.py`, if you want to run another file, use `python main.py path/to/file.yx`

## Commands

oryx has a thing called energy, every programs starts with 100 energy, some commands may use a bit of it, to get more, run `·`!

The interpreter ignores every other character than these, making them no-op

Every program's first character should be a space and the default direction for a program is right.

### IP direction commands

| Arrow | Direction         |
| ----- | ----------------- |
| `\`   | Right mirror      |
| `/`   | Left mirror       |
| `^`   | Up                |
| `v`   | Down              |

### Main commands

| Command     | Energy | Description                                                           |
| ----------- | ------ | --------------------------------------------------------------------- |
| `0`-`F`     |        | Push the corrisponding hex number as an integer                       |
| `!`         |        | Pop the last value                                                    |
| `n`         | -5     | Push numeric user input                                               |
| `a`         | -10    | Push the user input as ASCII values                                   |
| `O`         | -5     | Output the last value to the console then pop it                      |
| `o`         | -5     | Output the last ASCII value to the console then pop it                |
| `:`         |        | Duplicate the top value                                               |
| `;`         |        | Swap the last two values                                              |
| `$`         |        | Reverse the whole stack                                               |
| `+`         |        | Add last two values together, leaving only the result                 |
| `-`         |        | Subtract last two values together, leaving only the result            |
| `*`         |        | Multiply last two values together, leaving only the result            |
| `\|`        |        | Divide last two values together, leaving only the result              |
| `°`         |        | Raise last two values together, leaving only the result               |
| `%`         |        | Modulo last two values together, leaving only the result              |
| `I`         |        | Push a random bit (either 0 or 1)                                     |
| `?`         |        | The next instruction is only executed if the popped value is non-zero |
| `·`         | +10    | Get a bit of energy                                                   |

oryx arithmetic is NOS × TOS, meaning that ` 32* &`, for example, will duplicate 3 (2nd value) by 2 (last value)

## Example programs

Here are some example programs!

### 1 char cat program [<img src="https://nukocities.neocities.org/nuko/act/cat1.gif">](https://github.com/mkukiro/nori.ni/tree/develop#cat-program-)

``` ao &```

### Numerical cat program

``` nO &```

### Infinite 1-char cat program

```yx
 v\
 n
 O
 \^
```


### Truth machine

```yx
 n?v0O &
   v\
   1·
   O 
   \^
```

### Bit inverter

``` 1;-```

### Random binary sequence screensaver

```yx
 v\
 I·
 O
 \^
```

<p align="center"><img src="https://nukocities.neocities.org/nuko/sets/cat80.gif"></img></p>
