import os
import json
from classes import Parser
from classes import Grammer
from classes import Terminal
from classes import Production
from classes import NonTerminal

with open(os.path.join(os.getcwd(), "config.json"), "r") as source:
    config = json.load(source)
    source.close()

def splitter(line):
    def stripper(word):
        return word.strip()
    return list(map(stripper, line.split(" ")))

def load_file(path):
    with open(path, "r") as source:
        data = [ line.strip().replace("\n", "") for line in source ]
        source.close()
    return data

def load_grammers():
    location = os.path.join(os.getcwd(), config["grammer-location"])
    folders = os.listdir(location)
    grammers = []

    for folder_name in folders:
        productions = load_file(os.path.join(location, folder_name, config["folder-structure"]["productions"]))
        productions = list(map(splitter, productions))
        tests = load_file(os.path.join(location, folder_name, config["folder-structure"]["test-inputs"]))
        tests = list(map(splitter, tests))
        terminals = { "$": Terminal("$") }
        non_terminals = { production[0]: NonTerminal(production[0]) for production in productions }
        grammers.append(Grammer(terminals, non_terminals, productions, tests))

    parser = Parser(terminals, non_terminals)
    for test in tests:
        print()
        print("####### Testing '{}' #######".format(" ".join(test)))
        steps = parser.test(test, terminals, non_terminals, productions[0][0])
        for step in steps:
            print(step[0], "::", step[1], "=>", step[2])
            # if(step[-1]):
            #     print(step[-2])
        print("####### Test Case 'Accepted' #######")
        print()

if __name__ == '__main__':
    load_grammers()
