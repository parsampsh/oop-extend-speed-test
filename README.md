# OOP Extend Speed Test
This repository contains a script for genrating a class extending chain in diffrent languages.
To test that how much extend chain takes how much time for the interpreter.

What do i mean from **Extend Chain**?
This is an example:

```php
class c1 {}
class c2 extends c1 {}
class c3 extneds c2 {}
class c4 extneds c3 {}
class c5 extneds c4 {}
// ...
```

## Script usage
To generate a extend chain:

```shell
$ ./generate-code.py --help
Usage: ./generate_code.py <lang> <count>
```

For example:

```shell
$ ./generate_code.py python 3000
```

(The **Count** argument is the length of the extend chain).

After running the script, output code will be printed. You can put the output in a file:

```shell
$ ./generate_code.py python 3000 > code.py
```

Then, for testing the time:

```shell
$ time python code.py
```

Also you can see list of available languages in the script:

```shell
$ ./generate_code.py --langs
php
python
...
```

## Testing all of the languages
For testing all of the languages, you can use `test-all.sh` shell script:

```shell
$ ./test-all.sh
php:

<time report>
=================
python:

<time report>
=================
...
```

