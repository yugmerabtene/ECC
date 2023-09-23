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
