import csv
import sys
import json
import openai
import string

openai.api_key = ""


def getPrompt(path):
    """

    :param path: test data set file path
    :return: inputs to fine-tuning model and the expected results
    """
    prompts = []
    # prompts_1_2_3 = []
    types = []
    with open(path, "r+") as testFile:
        recv = csv.reader(testFile)

        for row in recv:
            prompts.append(row[0])
            types.append(row[-1])
    return prompts, types


def results(prompts, types):
    """
    This is a function for getting accuracy, precision, recall and f1 score.
    :param prompts: Prompts Input
    :param types: Results of prompts they should be
    """

    n = len(prompts)
    """number of results which are the same as it should be"""
    true = 0
   
    for i in range(n):
        # print(prompts[i])
        response = openai.Completion.create(
            engine="ada:ft-llm-cybersecurity:newset-k-0-0-5-1-2023-06-15-16-23-23",
            prompt=prompts[i],
            max_tokens=1
        )
        result = str(response.choices[0].text.strip())
        # first = remove_punctuation(first)
        print(types[i], result)
        if types[i] == '0':
            if result == types[i]:
                true += 1
        elif types[i] == '1':
            if result == types[i]:
                true += 1

    accuracy = float(true / n)

    print("Accuracy:", accuracy)


if __name__ == '__main__':
    PATH = "./test_data/test.csv"
    prompts, types = getPrompt(PATH)
    results(prompts, types)


