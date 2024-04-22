facts = {
    'ai-history': ['The term "artificial intelligence" was first coined in 1956 at the Dartmouth conference.',
                   'In 1952 two checkers playing programs were developed one was made by Christopther Strachey at the University of Manchester and the other by Arthur Samuel at IBM.',
                   'Artificial intelligence was founded as an academic discipline in 1956.',
                   'In 1997 a chess playing computer from IBM known as DEEP BLUE was about to beat the current world chess champion at the time, Garry Kasparov.'
                   ],
    'turing-test-proposed-year': 1950,
    'turing-test': 'The Turing Test originally called the imitation game by Alan Turing in 1950, is a method for testing and determining whether or not a computer is capable of thinking like a human.\nIt involves giving participants and an AI system some questions to answer.\n\
Once done a researcher is tasked to try and distinguish which was written by AI. If they are unable to see a difference in answers it means the AI has succeed in thinking like a human.',
    'ai-types': 'Weak AI is considered weak as it usually only specialises in one area and can only perform a single task.\nStrong AI is AI that can perform well as a human across a range of measures and is able to adapt and problem solve just like a human.',
    'ai-definition': 'Artificial intelligence is the ability of a digital system or computer controlled robot/device to perform tasks in a similar manner to humans.',
    'ai-importance': 'AI has applications in various fields, including healthcare, finance, autonomous vehicles, and more.'
}

running = True

print("Hi, I'm an AI History/Definition Knowledge based system\n")


while running:
    question_asked = str(input(
        "What would you like to know? (note you can exit by typing end)\n")).lower()
    # if "ai" in question_asked or "artificial intelligence" in question_asked:
    if "history" in question_asked:

        print("There are many interesting facts about the history of AI such as:")
        for history in facts['ai-history']:
            print(history)

    elif "what" in question_asked \
        and ("types" in question_asked
             or "weak" in question_asked
             or "strong" in question_asked):
        print("AI can be categorized into weak/narrow AI and strong AI.")
        print(facts['ai-types'])
    elif "importance" in question_asked:
        print("AI has significant applications in various fields.")
        print(facts['ai-importance'])
    elif "what" in question_asked \
            and "turing test" in question_asked:
        # print("The Turing Test was proposed in the year:")
        print(facts['turing-test'])
    elif "when" in question_asked \
            and "turing test" in question_asked:
        print("The Turing Test was proposed in the year:")
        print(facts['turing-test-proposed-year'])
    elif ("definition" in question_asked
            or "what" in question_asked) \
            and ("ai" in question_asked
                 or "Artificial intelligence" in question_asked):
        print("Artificial intelligence is defined as:")
        print(facts['ai-definition'])

    elif "end" in question_asked \
            or "exit" in question_asked \
            or "quit" in question_asked \
            or 'q' in question_asked \
            or len(question_asked) == 0:
        print("Thank you for using me, I will shut down now")
        running = False
    else:
        print("I have no knowledge or I'm not sure what you mean?")
