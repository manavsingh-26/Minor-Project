import os
import time

os.chdir("D:\GoogleHashPractise\OnePizza")


def number_of_likings(client_like, client_dislike):
    all_ingredients = []
    like = {}
    dislike = {}
    for i in range(len(client_like)):
        for j in range(1, len(client_like[i])):
            if client_like[i][j] not in all_ingredients:
                all_ingredients.append(client_like[i][j])
            if client_like[i][j] in like:
                like[client_like[i][j]] += 1
            elif client_like[i][j] not in like:
                like[client_like[i][j]] = 1
    for i in range(len(client_dislike)):
        for j in range(1, len(client_dislike[i])):
            if client_dislike[i][j] not in all_ingredients:
                all_ingredients.append(client_dislike[i][j])
            if client_dislike[i][j] in dislike:
                dislike[client_dislike[i][j]] += 1
            elif client_dislike[i][j] not in dislike:
                dislike[client_dislike[i][j]] = 1
    # print(all_ingredients, like, dislike)
    one_pizza(all_ingredients, like, dislike)


def one_pizza(all_ingredients, like, dislike):
    n = like if len(like) > len(dislike) else dislike
    for key in like:
        if key not in dislike:
            pass
        elif key in dislike:
            like[key] -= dislike[key]
    # print(like)

    final_ing = []
    for key in like:
        if like[key] > 0:
            final_ing.append(key)
    final_ing.insert(0, len(final_ing))
    # print(final_ing)

    file = open("elaborate.txt", "w")
    for item in final_ing:
        print(item, end=" ")
        file.write(str(item) + " ")
    file.close()


def main():
    n = int(input())
    client_like = []
    client_dislike = []
    for i in range(n):
        client_like.append([n for n in input().split()])
        client_dislike.append([n for n in input().split()])
    number_of_likings(client_like, client_dislike)


if __name__ == "__main__":
    main()
