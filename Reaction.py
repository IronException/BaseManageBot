
def test_new_relation(content, reactions):
    if content.startswith('!relate'):
        things = content.split(" ", 2)
        name = things[1]
        if not name.isnumeric():
            name = name[3: -1]

        reactions[name] = things[2]


def react(author, content, reactions):
    for r in reactions:
        if str(author.id) == str(r):
            return reactions[r]
    return test_new_relation(content, reactions)
