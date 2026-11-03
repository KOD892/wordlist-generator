# wordlist-generator
a python based wordlist generator


* **regex pattern**
* **wordlist length**
* flags for **numbers**
* flags for **special characters**
* **output file name**

<--! This makes it flexible for generating many different password wordlists. -->



# Example Usage

### Generate 6000 passwords with numbers and symbols

```bash
python generator.py -n 6000 --include-numbers --include-symbols
```

### Save to a custom file

```bash
python generator.py -n 10000 --include-numbers --include-symbols -o passwords.txt
```

### Require a regex match

Example: ensure the password ends with **3 digits**

```bash
python generator.py -n 6000 --include-numbers --include-symbols --regex "\d{3}$"
```

### Custom symbols

```bash
python generator.py -n 5000 --include-symbols --symbols "!$?%"
```

---

# Example Generated Passwords

```
Something!449
SomethingPrime@8821
SomethingMatrix#101
Something!Gamma339
Something$Core901
SomethingNova@77
SomethingSecure#5500
Something@Pulse22
```

---
