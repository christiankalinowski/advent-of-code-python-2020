from read_functions import read_resources
import re

rule_pattern = re.compile(r"^(\w+ \w+) bags contain ((?:(?:\d+ )?\w+ \w+ (?:bags|bag)(?:, )?)+)\.$")
bag_pattern = re.compile(r"(\d+) (\w+ \w+) (?:bags|bag)")


def solve():
    inputs = read_resources(__file__)
    bag_rules = list(map(map_rule, inputs))

    bag_stack = ["shiny gold"]
    parent_bags = []

    while len(bag_stack) > 0:
        bag = bag_stack.pop()
        for rule in bag_rules:
            if bag in rule[1].keys() and not rule[0] in parent_bags:
                parent_bags.append(rule[0])
                bag_stack.append(rule[0])

    bag_children = dict()
    while "shiny gold" not in bag_children:
        for rule in bag_rules:
            if contains_all(bag_children, rule):
                bag_children[rule[0]] = sum(map(calculate_child_bags(rule, bag_children), rule[1]))

    return len(parent_bags), bag_children["shiny gold"]


def calculate_child_bags(rule, children):
    return lambda k: (children[k] + 1) * int(rule[1][k])


def contains_all(bag_children, rule):
    return all(item in bag_children.keys() for item in rule[1].keys())


def map_rule(rule):
    matches = rule_pattern.match(rule).groups()
    bags = dict()
    if matches[1] != "no other bags":
        results = matches[1].split(", ")
        results = list(map(lambda r: bag_pattern.search(r).groups(), results))
        results = list(map(lambda r: r[::-1], results))
        bags = dict(results)
    return matches[0], bags


print(solve())
