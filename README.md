# wordlist-generator
a python based wordlist generator


* **regex pattern**
* **wordlist length**
* flags for **numbers**
* flags for **special characters**
* **output file name**

This makes it flexible for generating many different password wordlists.



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
Convexity!449
ConvexityPrime@8821
ConvexityMatrix#101
Convexity!Gamma339
Convexity$Core901
ConvexityNova@77
ConvexitySecure#5500
Convexity@Pulse22
```

---

✅ If you want, I can **upgrade this into a professional wordlist generator** with:

* **regex-driven generation engine**
* **multi-base words**
* **leet transformations (C0nv3xity)**
* **parallel generation (10M+ wordlists fast)**
* **Kali-style CLI tool like `crunch`**
* **GPU-speed generation for huge datasets**

Just tell me and I’ll build **a powerful password wordlist generator script**.
