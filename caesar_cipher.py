def caesar(text, shift, encrypt=True):   
    #if shift is not an integer, will get 'Shift Needs to be an Integer'
    if not isinstance(shift, int):
        return 'Shift Needs to be an Integer'
    #shift needs to be between 1 and 25
    if shift < 1 or shift > 25:
        return 'Shift Needs to be an Integer Between 1 and 25'
    #if encrypt is false, the shift will reverse and go in the reverse direction to decrypt an encrypted message
    if not encrypt:
        shift = - shift
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift] #shifts alphabet to a certain shift length by starting the alphabet at the shift number and adding the remaining alphabet ending at the shift integer
    # Makes it so that you can replace the letters with the shifted alphabet using translate
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)
# use encrypt to encrypt and decrypt to decrypt and decrypt is done by turning encrypt to false which reverses the shif in the previous function
def encrypt(text, shift):
    return caesar(text, shift)
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
text = 'Hello'
shift = 5
encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(text, shift)