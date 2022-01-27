import string
import argparse
import secrets

def generate_password(length=13, hasUpperCase=True, hasLowerCase=True, hasDigits=True, hasSymbols=True, symbolChars="!@#%^&*(_+-=[{|"):
  chars = \
    (string.ascii_uppercase if hasUpperCase else "" ) \
    + (string.ascii_lowercase if hasLowerCase else "") \
    + (string.digits if hasDigits else "") \
    + (symbolChars if hasSymbols else "")

  if chars.__len__ == 0:
    raise ValueError('no character')

  while True:
    password = ''.join(secrets.choice(chars) for x in range(length))
    # debug output
    # print(f"password: {password}")
    if (
      (not hasUpperCase or (any(c.isupper() for c in password))) and
      (not hasLowerCase or (any(c.islower() for c in password))) and
      (not hasDigits or (any(c.isdigit() for c in password))) and
      (not hasSymbols or (any(c in symbolChars for c in password)))):

      return password

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog='gen_password')
  parser.add_argument('--length', type=int, default=13, help='length of password')
  parser.add_argument('--no-include-symbols', action='store_true', default=False, help="don't include symbol characters")
  parser.add_argument('--symbol-chars', type=str, default='!@#%^&*(_+-=[{|', help="symbol characters to use in password")
  args = parser.parse_args()

  password = generate_password(length=args.length, hasSymbols=(not args.no_include_symbols), symbolChars=args.symbol_chars)
  print(password)