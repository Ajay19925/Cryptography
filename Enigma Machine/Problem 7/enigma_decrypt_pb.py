from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine
import itertools

rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')

reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')

pb = Plugboard.from_key_sheet('OY NR DL')

machine = EnigmaMachine([rL, rM, rR], reflector, pb)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Initialize an empty set to store unique combinations
unique_combinations = set()

# Generate and add all possible unique combinations of two two-letter alphabets
for combination in itertools.product(alphabet, repeat=2):
    combined = "".join(combination)
    tuple_combined = tuple(sorted(combined))  # Sort the letters and create a tuple
    if tuple_combined[0] != tuple_combined[1]:
        unique_combinations.add("".join(tuple_combined))
unique_combinations_list = sorted(list(unique_combinations))
#print(unique_combinations_list)
known_plugboard_setting='OY NR DL'
final=[]
final2=[]
final3=[]
for combined in unique_combinations_list:
    if combined[0] not in known_plugboard_setting and combined[1] not in known_plugboard_setting:
        #known_plugboard_setting=f'{known_plugboard_setting} {combined}'
        #print(known_plugboard_setting)
        pb = Plugboard.from_key_sheet(f'{known_plugboard_setting} {combined}')
        machine.plugboard = pb
        machine.set_display('UPV')
        if machine.process_text('A') == 'I':
            #print(f'{known_plugboard_setting} {combined}')
            for combined1 in unique_combinations_list:
                #print(f'{known_plugboard_setting} {combined} {combined1}')
                #known_plugboard_setting = f'{known_plugboard_setting} {combined}'
                #print(known_plugboard_setting)
                if combined1[0] not in known_plugboard_setting and combined1[1] not in known_plugboard_setting and combined1[0] not in combined and combined1[1] not in combined:
                    pb=Plugboard.from_key_sheet(f'{known_plugboard_setting} {combined} {combined1}')
                    machine.plugboard = pb
                    machine.set_display('UPW')
                    if machine.process_text('C') == 'U':
                        machine.set_display('UPS')
                        if machine.process_text('ATTAC') == 'YNLIU':
                            #print(f'{known_plugboard_setting} {combined} {combined1}')
                            for combined2 in unique_combinations_list:
                                if combined2[0] not in known_plugboard_setting and combined2[1] not in known_plugboard_setting and combined2[0] not in combined and combined2[1] not in combined and combined2[0] not in combined1 and combined2[1] not in combined1:
                                    pb = Plugboard.from_key_sheet(f'{known_plugboard_setting} {combined} {combined1} {combined2}')
                                    machine.plugboard = pb
                                    machine.set_display('UPX')
                                    if machine.process_text('K') == 'N':
                                        machine.set_display('UPS')
                                        if machine.process_text('ATTACK') == 'YNLIUN':
                                            for combined3 in unique_combinations_list:
                                                if combined3[0] not in known_plugboard_setting and combined3[1] not in known_plugboard_setting and combined3[0] not in combined and combined3[1] not in combined and combined3[0] not in combined1 and combined3[1] not in combined1 and combined3[0] not in combined2 and combined3[1] not in combined2:
                                                    pb = Plugboard.from_key_sheet(f'{known_plugboard_setting} {combined} {combined1} {combined2} {combined3}')
                                                    machine.plugboard = pb
                                                    machine.set_display('UPY')
                                                    if machine.process_text('X') == 'H':
                                                #print(f'{known_plugboard_setting} {combined} {combined1} {combined2} {combined3}')
                                                        machine.set_display('UPS')
                                                        if machine.process_text('ATTACKXAT') == 'YNLIUNHBN':
                                                    # print(f'{known_plugboard_setting} {combined} {combined1}')
                                                            #print(f'{known_plugboard_setting} {combined} {combined1} {combined2}')
                                                            final.append(f'{known_plugboard_setting} {combined} {combined1} {combined2}')
                                                            unique_set = set(final)
                                                            unique_list = list(unique_set)
                                                            #print(len(unique_list))


#
for plugboard in unique_list:
    for combined4 in unique_combinations_list:
        if combined4[0] not in plugboard and combined4[1] not in plugboard:
            pb = Plugboard.from_key_sheet(f'{plugboard} {combined4}')
            machine.plugboard = pb
            machine.set_display('UPB')
            if machine.process_text('X') == 'V':
                machine.set_display('UPS')
                if machine.process_text('ATTACKXATXX') == 'YNLIUNHBNVE':
                    # print(f'{known_plugboard_setting} {combined} {combined1}')
                    #print(f'{plugboard} {combined4}')
                    final2.append(f'{plugboard} {combined4}')
                    unique_set2 = set(final2)
                    unique_list2 = list(unique_set2)
#
for plugboard2 in unique_list2:
    for combined5 in unique_combinations_list:
        if combined5[0] not in plugboard2 and combined5[1] not in plugboard2:
            pb = Plugboard.from_key_sheet(f'{plugboard2} {combined5}')
            machine.plugboard = pb
            machine.set_display('UPD')
            if machine.process_text('P') == 'R':
                machine.set_display('UPS')
                if machine.process_text('ATTACKXATXXPMXATXATLANTICXZXISLAND') == 'YNLIUNHBNVERXKRBUHZEYMJVEZNRPNWOSV':
                    #print(f'{plugboard2} {combined5}')
                    final3.append(f'{plugboard2} {combined5}')
                    unique_set3 = set(final3)
                    unique_list3 = list(unique_set3)


print('Possible Stecker Settings')
for items in unique_list3:
    print(items)


# for plugboard3 in unique_list2:
#     for combined5 in unique_combinations_list:
#         if combined5[0] not in plugboard3 and combined5[1] not in plugboard3:
#             pb = Plugboard.from_key_sheet(f'{plugboard3} {combined5}')
#             machine.plugboard = pb
#             machine.set_display('UPD')
#             if machine.process_text('P') == 'R':
#                 machine.set_display('UPS')
#                 if machine.process_text('ATTACKXATXXPMXAT') == 'YNLIUNHBNVERXKRB':
#                     print(f'{plugboard3} {combined5}')
#                     final3.append(f'{plugboard} {combined5}')
#                     unique_set3 = set(final3)
#                     unique_list3 = list(unique_set3)

# Final_plugboard='OY NR DL CG FU HJ MX PW'
# #finding all possible settings
# for combined6 in unique_combinations_list:
#     if combined6[0] not in Final_plugboard and combined6[1] not in Final_plugboard:
#         pb = Plugboard.from_key_sheet(f'{Final_plugboard} {combined6}')
#         machine.set_display('UPS')
#         if machine.process_text('ATTACKXATXXPMXATXATLANTICXZXISLAND') == 'YNLIUNHBNVERXKRBUHZEYMJVEZNRPNWOSV':
#             print(f'{Final_plugboard} {combined6}')
