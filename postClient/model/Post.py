from dataclasses import dataclass


@dataclass
class Post:
    id: int
    message: str
    title: str

    def __repr__(self):
        return f'Post [{self.id}]\n {self.title} \n {self.message} \n\n'

    def __str__(self):
        return repr(self)
