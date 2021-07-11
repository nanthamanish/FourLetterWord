import json


class Player():
    def __init__(self) -> None:
        self.graph = []
        self.words = []
        self.index = {}
        self.num_words: int = 0

        self.get_words()
        self.assign_index()
        self.make_graph()
        self.store_graph()
        self.print_rules()

    def get_words(self,
                  input_file='word_alpha.txt',
                  output_file='word_four_letter.txt'):
        four_words = []
        with open(input_file, 'r') as f_in:
            file_words = f_in.readlines()
            for word in file_words:
                if len(word.strip()) == 4:
                    four_words.append(word)
                    self.words.append(word.strip())

        self.num_words = len(self.words)
        with open(output_file, 'w') as f_out:
            f_out.writelines(four_words)

    def assign_index(self):
        i = 0
        for word in self.words:
            self.index[word] = i
            i += 1

    def make_graph(self):
        for i in range(0, self.num_words):
            self.graph.append([])

        for word in self.words:
            for pos in range(0, 4):
                for let in range(0, 26):
                    temp = ''
                    if pos > 0:
                        temp = word[0:pos] + (chr(let + ord('a'))) + word[pos +
                                                                          1:4]
                    else:
                        temp = chr(let + ord('a')) + word[pos + 1:4]
                    if temp[pos] != word[pos]:
                        if temp in self.index.keys():
                            i = self.index[word]
                            j = self.index[temp]
                            self.graph[i].append(j)

    def store_graph(self, output_file='links.json'):
        links = {}
        for word in self.words:
            links[word] = []
            word_ind = self.index[word]
            for i in self.graph[word_ind]:
                links[word].append(self.words[i])
        with open(output_file, 'w') as f_out:
            json.dump(links, f_out, indent=4)

    def print_neighbours(self, word=''):
        if word in self.index.keys():
            word_ind = self.index[word]
            for i in self.graph[word_ind]:
                print(self.words[i])
            print()
        else:
            print('Error - Not a valid word')

    def print_rules(self, input_file='rules.txt'):
        with open(input_file, 'r') as f_in:
            rules = f_in.readlines()
            for r in rules:
                print(r)


    def play(self):
        self.visited = [False for _ in range(0, self.num_words)]
        prev = ''
        while True:
            user_str = input('\tEnter Word:\t')
            if user_str == 'EXIT':
                print('\nGame aborted - Exitting\n')
                break

            user_str = user_str.lower()
            if user_str == 'resign':
                print("\nYay! I win. Better luck next time!\n")
                break

            if user_str not in self.index.keys():
                print('\nError - Not a valid word\n')
                if prev != '':
                    print('\tResponse:\t{:s}'.format(prev))
                continue

            word_ind = self.index[user_str]
            diff = 1
            if prev != '':
                diff = 0
                for i in range(0, 4):
                    if user_str[i] != prev[i]:
                        diff += 1

            if self.visited[word_ind]:
                print('\nError - Word already played\n')
                print('\tResponse:\t{:s}'.format(prev))
            elif diff != 1:
                print('\nError - Word does not differ exactly by 1 character\n')
                if prev != '':
                    print('\tResponse:\t{:s}'.format(prev))
            else:
                self.visited[word_ind] = True
                choice = ''
                link_cnt = -1
                for neighbour in self.graph[word_ind]:
                    if not self.visited[neighbour]:
                        cnt = 0
                        for w in self.graph[neighbour]:
                            if not self.visited[w]:
                                cnt += 1
                        if cnt > link_cnt:
                            link_cnt = cnt
                            choice = self.words[neighbour]
                        elif cnt == 0:
                            link_cnt = cnt
                            choice = self.words[neighbour]
                            break
                if choice != '':
                    self.visited[self.index[choice]] = True
                    print()
                    print('\tResponse:\t{:s}'.format(choice))
                    prev = choice
                else:
                    print('\t\tOops I am out of words - YOU WIN!!!')
            
import json


class Player():
    def __init__(self) -> None:
        self.graph = []
        self.words = []
        self.index = {}
        self.num_words: int = 0

        self.get_words()
        self.assign_index()
        self.make_graph()
        self.store_graph()
        self.print_rules()

    def get_words(self,
                  input_file='word_alpha.txt',
                  output_file='word_four_letter.txt'):
        four_words = []
        with open(input_file, 'r') as f_in:
            file_words = f_in.readlines()
            for word in file_words:
                if len(word.strip()) == 4:
                    four_words.append(word)
                    self.words.append(word.strip())

        self.num_words = len(self.words)
        with open(output_file, 'w') as f_out:
            f_out.writelines(four_words)

    def assign_index(self):
        i = 0
        for word in self.words:
            self.index[word] = i
            i += 1

    def make_graph(self):
        for i in range(0, self.num_words):
            self.graph.append([])

        for word in self.words:
            for pos in range(0, 4):
                for let in range(0, 26):
                    temp = ''
                    if pos > 0:
                        temp = word[0:pos] + (chr(let + ord('a'))) + word[pos +
                                                                          1:4]
                    else:
                        temp = chr(let + ord('a')) + word[pos + 1:4]
                    if temp[pos] != word[pos]:
                        if temp in self.index.keys():
                            i = self.index[word]
                            j = self.index[temp]
                            self.graph[i].append(j)

    def store_graph(self, output_file='links.json'):
        links = {}
        for word in self.words:
            links[word] = []
            word_ind = self.index[word]
            for i in self.graph[word_ind]:
                links[word].append(self.words[i])
        with open(output_file, 'w') as f_out:
            json.dump(links, f_out, indent=4)

    def print_neighbours(self, word=''):
        if word in self.index.keys():
            word_ind = self.index[word]
            for i in self.graph[word_ind]:
                print(self.words[i])
            print()
        else:
            print('Error - Not a valid word')

    def print_rules(self, input_file='rules.txt'):
        with open(input_file, 'r') as f_in:
            rules = f_in.readlines()
            for r in rules:
                print(r)


    def play(self):
        self.visited = [False for _ in range(0, self.num_words)]
        prev = ''
        while True:
            user_str = input('\tEnter Word:\t')
            if user_str == 'EXIT':
                print('\nGame aborted - Exitting\n')
                break

            user_str = user_str.lower()
            if user_str == 'resign':
                print("\nYay! I win. Better luck next time!\n")
                break

            if user_str not in self.index.keys():
                print('\nError - Not a valid word\n')
                if prev != '':
                    print('\tResponse:\t{:s}'.format(prev))
                continue

            word_ind = self.index[user_str]
            diff = 1
            if prev != '':
                diff = 0
                for i in range(0, 4):
                    if user_str[i] != prev[i]:
                        diff += 1

            if self.visited[word_ind]:
                print('\nError - Word already played\n')
                print('\tResponse:\t{:s}'.format(prev))
            elif diff != 1:
                print('\nError - Word does not differ exactly by 1 character\n')
                if prev != '':
                    print('\tResponse:\t{:s}'.format(prev))
            else:
                self.visited[word_ind] = True
                choice = ''
                link_cnt = -1
                for neighbour in self.graph[word_ind]:
                    if not self.visited[neighbour]:
                        cnt = 0
                        for w in self.graph[neighbour]:
                            if not self.visited[w]:
                                cnt += 1
                        if cnt > link_cnt:
                            link_cnt = cnt
                            choice = self.words[neighbour]
                        elif cnt == 0:
                            link_cnt = cnt
                            choice = self.words[neighbour]
                            break
                if choice != '':
                    self.visited[self.index[choice]] = True
                    print()
                    print('\tResponse:\t{:s}'.format(choice))
                    prev = choice
                else:
                    print('\t\tOops I am out of words - YOU WIN!!!')
            
