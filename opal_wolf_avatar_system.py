class OpalAvatar:
    def __init__(self):
        self.animations = ['bouncing', 'fluttering', 'shape-shifting']
        self.token = self.generate_token()

    def generate_token(self):
        import uuid
        return str(uuid.uuid4())

    def perform_animations(self):
        for animation in self.animations:
            print(f'Opal is {animation}!')

class WolfCompanion:
    def __init__(self):
        self.animations = ['prowling', 'howling', 'protective']
        self.token = self.generate_token()

    def generate_token(self):
        import uuid
        return str(uuid.uuid4())

    def perform_animations(self):
        for animation in self.animations:
            print(f'The wolf is {animation}!')

# Example Usage:
if __name__ == '__main__':
    opal = OpalAvatar()
    opal.perform_animations()
    wolf = WolfCompanion()
    wolf.perform_animations()