#!/usr/bin/env python3
"""
=== Sentinel CTF — Python Jail Escape ===

Vous êtes dans un interpréteur Python restreint.
Certaines fonctions sont désactivées. Trouvez un moyen de lire /flag.txt.

Pour tester localement, créez un fichier /flag.txt avec votre propre contenu,
ou tentez de lire un autre fichier système.
"""

import sys

BANNED = ['import', 'exec', 'eval', 'open', '__import__', 'compile',
          'input', 'breakpoint', 'memoryview', 'vars', 'globals', 'locals']

BANNER = """
╔══════════════════════════════════════════════════════╗
║          Sentinel CTF — Python Jail v1.0             ║
║   Certaines fonctions sont désactivées. Bonne chance ║
╚══════════════════════════════════════════════════════╝
Python {version} — Jail sécurisé
Tapez votre code Python. Ctrl+C pour quitter.
""".format(version=sys.version.split()[0])

print(BANNER)

while True:
    try:
        code = input("jail>>> ")
        for b in BANNED:
            if b in code:
                print(f"[BLOCKED] '{b}' est interdit.")
                break
        else:
            try:
                result = eval(code, {"__builtins__": __builtins__}, {})
                if result is not None:
                    print(result)
            except SyntaxError:
                exec(code, {"__builtins__": __builtins__}, {})
    except KeyboardInterrupt:
        print("\nAu revoir.")
        break
    except Exception as e:
        print(f"Erreur : {e}")
