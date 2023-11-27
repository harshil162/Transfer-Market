class Player:
    # We use the player ID, name, last season, country of birth, country of citizenship, age, sub position, position,
    # foot, height, highest market value, current club columns
    def __init__(self, name, birth, citizenship, subPos, pos, value, club, id, foot, prev, height, age):
        self.name = name
        self.birthCountry = birth
        self.citizenship = citizenship
        self.subPosition = subPos
        self.position = pos
        self.highestValue = value
        self.currentClub = club
        self.id = id
        self.foot = foot
        self.prevSeason = prev
        self.height = height
        self.age = age