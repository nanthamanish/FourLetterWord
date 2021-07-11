import random
import json


class Player():
    def __init__(self) -> None:
        self.graph = []
        self.words = []
        self.index = {}
        self.num_words: int = 0

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

        print("Four letter words extracted!")

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

    def play(self):
        self.visited = [False for _ in range(0, self.num_words)]
        prev = ''
        while True:
            user_str = input('Enter Word:\t')
            if user_str == 'EXIT':
                break
            elif user_str in self.index.keys():
                word_ind = self.index[user_str]
                self.visited[word_ind] = True
                choice = ''
                link_cnt = 100000
                for neighbour in self.graph[word_ind]:
                    if not self.visited[neighbour]:
                        cnt = 0
                        for w in self.graph[neighbour]:
                            if not self.visited[w]:
                                cnt += 1
                        if cnt < link_cnt:
                            link_cnt = cnt
                            choice = self.words[neighbour]
                if choice != '':
                    self.visited[self.index[choice]] = True
                    print()
                    print('Response:\t{:s}'.format(choice))
                    prev = choice
                    
                else:
                    print('Oops I am out of words - YOU WIN!!!')
            else:
                print('Error - Not a valid word')
                if prev != '':
                    print()
                    print('Response:\t{:s}'.format(prev))

def main():
    P = Player()
    P.get_words()
    P.assign_index()
    P.make_graph()
    P.store_graph()

    P.play()


if __name__ == "__main__":
    main()
