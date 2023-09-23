# ECC
# Cryptographie ECC avec Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
[![GitHub Stars](https://img.shields.io/github/stars/yugmerabtene/ECC?style=social)](https://github.com/yugmerabtene/ECC/stargazers)

Ce projet Python vous permet de travailler avec des clés ECC (Elliptic Curve Cryptography) pour signer et vérifier des messages.

## Table des matières

- [Introduction](#introduction)
- [Installation](#installation)
- [Exemple d'utilisation](#exemple-dutilisation)
- [Contribuer](#contribuer)
- [License](#license)

## Introduction

La cryptographie à courbes elliptiques est une technique de cryptage moderne et sécurisée utilisée pour signer et vérifier des données. Ce projet vous permet de générer des paires de clés ECC, de signer des messages et de vérifier des signatures à l'aide de la bibliothèque `cryptography` de Python.

## Installation

Pour utiliser ce projet, vous devez avoir Python 3.8 ou une version ultérieure installée. Suivez ces étapes pour configurer l'environnement :

1. Clonez ce dépôt sur votre machine :

    ```bash
    git clone https://github.com/yugmerabtene/ECC.git
    ```

2. Accédez au répertoire du projet :

    ```bash
    cd ECC
    ```

3. Installez les dépendances requises :

    ```bash
    pip install cryptography
    ```

## Exemple d'utilisation

Voici comment utiliser ce projet pour générer une paire de clés ECC, signer un message et vérifier la signature :

```python
# Importer la bibliothèque de courbes elliptiques
from cryptography.hazmat.primitives.asymmetric import ec

# Générer une paire de clés ECC (clé privée et clé publique)
def generate_ecc_keypair():
    # Créez un objet ECC avec une courbe elliptique spécifique (par exemple, la courbe P-256)
    curve = ec.SECP256R1()
    private_key = ec.generate_private_key(curve)
    public_key = private_key.public_key()
    return private_key, public_key

# Signer un message avec une clé privée ECC
def sign_message(private_key, message):
    signature = private_key.sign(message)
    return signature

# Vérifier une signature avec la clé publique ECC
def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message)
        return True
    except:
        return False

# Exemple d'utilisation
if __name__ == "__main__":
    # Générer une paire de clés ECC
    private_key, public_key = generate_ecc_keypair()

    # Message à signer
    message = b"Ce message est confidentiel."

    # Signer le message
    signature = sign_message(private_key, message)

    # Vérifier la signature
    is_valid = verify_signature(public_key, message, signature)
    if is_valid:
        print("La signature est valide.")
    else:
        print("La signature n'est pas valide.")
