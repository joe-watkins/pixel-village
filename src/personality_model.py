class Personality:
    def __init__(self, openness, conscientiousness, extraversion, agreeableness, neuroticism):
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism

    def describe(self):
        return {
            "Openness": self.openness,
            "Conscientiousness": self.conscientiousness,
            "Extraversion": self.extraversion,
            "Agreeableness": self.agreeableness,
            "Neuroticism": self.neuroticism
        }

class Agent:
    def __init__(self, name, age, occupation, personality, quirks):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.personality = personality
        self.quirks = quirks

    def introduce(self):
        return f"Hi, I'm {self.name}, a {self.age}-year-old {self.occupation}. Here are my personality traits: {self.personality.describe()} and quirks: {', '.join(self.quirks)}"

# Example agent
hiro_personality = Personality(0.77, 0.91, 0.55, 0.80, 0.32)
hiro = Agent("Hiro Tanaka", 27, "Baker", hiro_personality, ["Always carries a baguette", "Gives bread to stray cats", "Obsessed with weather forecasts"])

print(hiro.introduce())
