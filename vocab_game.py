import random

print(f"------------------------------------------------------------------------------------------\n")

print(f"\nBRUSH UP ON YOUR VOCABULARY\n")
print(f"Enter vocab word to defintition \n")

print(f"------------------------------------------------------------------------------------------\n")

def vocab_practice():
    while True:
        b=key,val=random.choice(list(glossary.items()))


        print("\nDefinition: "+val)

        a=input('\nEnter the correct word to the corresponding definition. Enter q to quit anytime.' )

        if a.lower()=='q':
            print("\nThanks for playing, BYE.")
            break

        elif a == key.lower():
            print(f"\nCorrect")
            continue

        else:
            print(f"Incorrect, the answer is {key}. \n")
            try_again=input("Play again? y/n")

            if try_again[0].lower()=='n':
                print(f"\nThanks for playing, BYE")
            else:
                continue

        break
    
                                            
glossary={   
'Granular': 'detailed.',
'Ubiquitous': 'omnipresent, common',
'Esoteric': 'limited to only a few',
'Superfluous ':'unnecessary, more than enough',
'Secular': "not religious, intelligent based",
'Eccentric': 'unique person or object does not conform to the norm. Strange.',
'Maxim':'An item associated with a key in a dictionary.',
'conditional test': 'A comparison between two values.',
'float': 'A numerical value with a decimal component.',
'boolean expression': 'An expression that evaluates to True or False.'   ,
'Admonitory':'giving or conveying a warning (ex- finger wag of disproval)',
'Cognizant':'mindful, aware',
'Vernacular':'saying specific to a group of people\slang (Ex-southern slang)',
'Iconoclast':'nonconformist.',
'Unscrupulous':'dishonest',
'Anecdotal':'an account, not necessarily true or reliable; based on personal account (observation)',
'Excoriate':'censored or criticize severely',
'Impalpable':'unable to be felt or touch',
'Implacable':'relentless; unstoppable',
'Minutia':'small, trivial details',
'Fervent':'passionate',
'Concurrent':'at the same time',
'Misnomer':'a wrong or inaccurate use of a name or term',
'Vet':'to make a careful or critical examination of something',
'Xenophobia': 'person afraid of foreigners',
'Demagogue': 'appealing to popular desires and prejudice rather than rational thinking',
'Febrile': 'having or showing the symptoms of a fever; having or showing a great deal of nervous excitement or energy.',
'Remunerative': '(adj)lucrative; financially rewarding',
'Sacrilegious' : '(adj)involving/performing sacrilege (violating/misuse of what is regarded as scare)',
'Cumbersome' : '(adj)slow or complicated, therefore inefficient',
'Credulous' : '(adj)showing too great a eagerness to believe things',
'Myriad': 'countless',
'Pilfer(v)': 'steal',
'Arcane': 'mysterious',
'Pugnacious': 'combatative',
'Semantic' : '(n) meaning of a word, phrase, sentence, or text',
'Isothymia': 'desire to be recognized as equal to other people',
'Megalothymia':'desire to be better than everyone else',
'Paroxysm': '(n) a sudden attack or outburst of a particular emotion or activity.' ,
'Indelible': '(adj) not able to be forgotten or removed.',
'Verisimilitude': '(n) the appearance of being true or real.',
'Apostasy': '(n) the renunciation of religious or political beliefs.',
'Statism': '(n) political system in which the state centralized control of social and economic affairs.',
'Supercilious' : '(adj) behaving or looking as though one think one is superior to others.',
'Entropy': '(n) relating to physics, it is the lack of order or predictability, a decline into disorder.',
'Zeitgeist' : '(n) the defining spirit or mood of a particular period of history as shown by the ideas and beliefs of the time (spirit of the time).',
'Obdurate': '(adj) stubbornly refusing to changes one’s opinion or course of action.',
'Spurious': '(adj) not being what it purports to be: false; fake',
'Scrupulous': 'diligent, thorough, and extremely attentive of details.',
'Unmoored' : '(adj) of a person-insecure, confused, or lacking contact with reality.',
'Nefarious' : '(adj) wicked or criminal (typically of an action).',
'Juxtaposition' : '(n) Juxtaposition is an act or instance of placing two elements close together or side by side. This is often done in order to compare/contrast the two, to show similarities or differences.',
'Pedantic' : '(adj) show off facts that are trivial; excessively concerned with minor details or rules; overscruplous.',
'Purport' : '(v) claiming to be what it is not; appear or claim to be or do something, especially falsely; profess.',
'Enumerate': '(v) mention (a number of things) one by one; list; itemize',
'judiciuous': '(adj) having, exercising, or characterized by sound judgment',
'bifurcated': '(adj) divided into two branches or parts',
}

    
glossary=vocab_practice()
