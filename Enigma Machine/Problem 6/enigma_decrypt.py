from enigma.machine import EnigmaMachine
from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine

rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')

reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')

pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

machine = EnigmaMachine([rL, rM, rR], reflector, pb)

# Define the ciphertext
ciphertext = "WVUVJCSQBFLWSGTHDREWOSXYIAYEUBHHXY"

# Brute-force through all possible rotor positions
for rotor_pos1 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    for rotor_pos2 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        for rotor_pos3 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            # Set the rotor positions
            machine.set_display(rotor_pos1 + rotor_pos2 + rotor_pos3)
            #print(rotor_pos1 + rotor_pos2 + rotor_pos3)

            # Decrypt the ciphertext
            plaintext = machine.process_text(ciphertext)
            #print(plaintext)

            # Check if the decrypted plaintext makes sense (e.g., contains meaningful words)
            if "ATTACK" in plaintext:
                print("Found possible initial rotor positions:", rotor_pos1 + rotor_pos2 + rotor_pos3)
                print("Decrypted plaintext:", plaintext)

#machine.set_display('UPS')       # set rotor positions or use its default
#position = machine.get_display()    # read rotor position
#print(position)

# Encrypt A letter
#print(machine.key_press('C'))
# Encrypt a text
#print(machine.process_text('Enigma machine is powerful for Q'))
