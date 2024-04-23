from poly_fuzzer.common.abstract_executor import AbstractExecutor
from poly_fuzzer.fuzzers.abstract_fuzzer import AbstractFuzzer
from poly_fuzzer.power_schedules.urlschedule import *
from poly_fuzzer.power_schedules.abstract_power_schedule import AbstractPowerSchedule
from urllib.parse import urlparse
import numpy as np
import random
from poly_fuzzer.common.abstract_seed import AbstractSeed
from poly_fuzzer.common.abstract_grammar import AbstractGrammar
from html.parser import HTMLParser

class UrlFuzzer(AbstractFuzzer):

    def __init__(
        self,
        executor,
        seeds: list[AbstractSeed],
        power_schedule: AbstractPowerSchedule = None,
        min_mutations: int = 1,
        max_mutations: int = 10,
    ):
        super().__init__(executor)
        self.seeds = seeds
        self.seed_index = 0
        self.executor = executor
        self.seed_index = 0
        self.power_schedule = power_schedule
        self.min_mutations = min_mutations
        self.max_mutations = max_mutations
        self.mutators = [self._delete_random_character, self._replace_random_character]

    def generate_input(self):

        """Mutate the seed to generate input for fuzzing.
        With this function we first use the gien seeds to generate inputs 
        and then we mutate the seeds to generate new inputs."""
        if self.seed_index < len(self.seeds):
            # Still seeding
            inp = self.seeds[self.seed_index].data
            self.seed_index += 1
        else:
            # Mutating
            inp = self._create_candidate()

        return inp

    def _update(self, input):
        """Update the fuzzer with the input and its coverage."""
        if len(self.data["coverage"]) > 1:
            if self.data["coverage"][-1] > self.data["coverage"][-2]:
                self.seeds.append(AbstractSeed(input))

    def _create_candidate(self):
        seed = np.random.choice(self.seeds)

        # Stacking: Apply multiple mutations to generate the candidate
        if self.power_schedule:
            candidate = self.power_schedule.choose(self.seeds).data
        else:
            candidate = seed.data
        # Apply power schedule to generate the candidate
        #
        trials = random.randint(self.min_mutations, self.max_mutations)
        for i in range(trials):
            candidate = self.mutate(candidate)
        return candidate

    def mutate(self, s):
        """Return s with a random mutation applied"""
        mutator = random.choice(self.mutators)
        return mutator(s)

    def _delete_random_character(self, s):
        """Returns s with a random character deleted"""
        if len(s) > 5:
            pos = random.randint(0, len(s) - 1)
            return s[:pos] + s[pos + 1 :]
        else:
            return s

    def _insert_random_character(self, s):
        """Returns s with a random character inserted"""
        pos = random.randint(0, len(s))
        random_character = chr(random.randrange(32, 127))
        return s[:pos] + random_character + s[pos:]

    def _replace_random_character(self, s):
        """Returns s with a random character replaced"""
        if s == "":
            return ""
        pos = random.randint(0, len(s) - 1)
        random_character = chr(random.randrange(32, 127))
        return s[:pos] + random_character + s[pos + 1 :]


def test_urlParse_without_grammar_and_powerSchedule(test_module):

    powerSchedule = UrlPowerSchedule()
    executor = AbstractExecutor(test_module)
    seeds = [AbstractSeed("www.yahoo.com"), AbstractSeed("alibaba.com"), AbstractSeed("www.amazon.ca"), AbstractSeed("www.google.com"),
             AbstractSeed("www.microsoft.com"), AbstractSeed("www.amazon.com"), AbstractSeed("www.facebook.com"), AbstractSeed("www.twitter.com"),
             AbstractSeed("www.linkedin.com"), AbstractSeed("www.slack.com")]
    fuzzer = UrlFuzzer(executor, seeds, powerSchedule)
    output = fuzzer.run_fuzzer(budget=200)
    print(output)

    assert output is not None

def test_urlParse_with_grammar_no_powerSchedule(test_module):

    executor = AbstractExecutor(test_module)
    gram_url_dict =  {
    "<start>":
        ["<url>"],
    "<url>":
        ["<scheme>://<authority><path><query>"],
    "<scheme>":
        ["http", "https", "ftp", "ftps"],
    "<authority>":
        ["<host>", "<host>:<port>", "<userinfo>@<host>", "<userinfo>@<host>:<port>"],
    "<host>":
        ["yahoo.com", "www.google.com", "bing.com", "opera.com", "safari.com"],
    "<port>":
        ["80", "8080", "<nat>"],
    "<nat>":
        ["<digit>", "<digit><digit>"],
    "<digit>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<userinfo>":
        ["user:password"],
    "<path>":
        ["", "/", "/<id>"],
    "<id>":
        ["abc", "def", "x<digit><digit>"],
    "<query>":
        ["", "?<params>"],
    "<params>":
        ["<param>", "<param>&<params>"],
    "<param>":
        ["<id>=<id>", "<id>=<nat>"],
    }
    grammar = AbstractGrammar(gram_url_dict)
    seeds = []
    for i in range(10):
        seeds.append(AbstractSeed(grammar.generate_input()))
    for seed in seeds:
        print(seed.data)
    fuzzer = UrlFuzzer(executor, seeds)
    output = fuzzer.run_fuzzer(budget=200)
    print(output)
    assert output is not None


def test_urlParse_with_grammar_with_powerSchedule(test_module):

    executor = AbstractExecutor(test_module)
    gram_url_dict =  {
    "<start>":
        ["<url>"],
    "<url>":
        ["<scheme>://<authority><path><query>"],
    "<scheme>":
        ["http", "https", "ftp", "ftps"],
    "<authority>":
        ["<host>", "<host>:<port>", "<userinfo>@<host>", "<userinfo>@<host>:<port>"],
    "<host>":
        ["yahoo.com", "www.google.com", "bing.com", "opera.com", "safari.com"],
    "<port>":
        ["80", "8080", "<nat>"],
    "<nat>":
        ["<digit>", "<digit><digit>"],
    "<digit>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<userinfo>":
        ["user:password"],
    "<path>":
        ["", "/", "/<id>"],
    "<id>":
        ["abc", "def", "x<digit><digit>"],
    "<query>":
        ["", "?<params>"],
    "<params>":
        ["<param>", "<param>&<params>"],
    "<param>":
        ["<id>=<id>", "<id>=<nat>"],
    }
    grammar = AbstractGrammar(gram_url_dict)
    seeds = []
    powerSchedule = UrlPowerSchedule()
    for i in range(10):
        seeds.append(AbstractSeed(grammar.generate_input()))
    for seed in seeds:
        print(seed.data)
    fuzzer = UrlFuzzer(executor, seeds, powerSchedule)
    output = fuzzer.run_fuzzer(budget=200)
    print(output)
    assert output is not None



def test_htmlParse_without_grammar_and_powerSchedule(test_module):

    powerSchedule = HtmlPowerSchedule()
    executor = AbstractExecutor(test_module)
    seeds = [AbstractSeed("<html><head><title>Goodness</title></head><body>Bonjour</body></html>"), AbstractSeed("<html><head><title>Test</title></head>"), AbstractSeed("<html><head><title>Goodness</title></head></html>"), AbstractSeed("<html><body>Bonjour</body></html>"),
             AbstractSeed("<html><head></head><body>Hello</body></html>"), AbstractSeed("<body>Just a body</body></html>"), AbstractSeed("<body><h1>Bonjour</h1></body></html>"), AbstractSeed("<html><head><title>Strong</title>"),
             AbstractSeed("<html><head><title><ul>List</ul>"), AbstractSeed("<html><li>item</li>")]
    fuzzer = UrlFuzzer(executor, seeds, powerSchedule)
    output = fuzzer.run_fuzzer(budget=500)
    print(output)

    assert output is not None


