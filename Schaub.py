import random

class Zdania:
     def __init__(self, stwierdzenie, puenta):
         self.stwierdzenie = stwierdzenie
         self.puenta = puenta

     stwierdzenie = [
         "Just pushing myself for more rounds at a higher pace in training. Your focus should be grounded in what you do, and that's fighting.",
         "You can't connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future. You have to trust in something - your gut, destiny, life, karma, whatever."

     ]
     puenta = [
         "I'm getting my cardio that way.",
         "This approach has never let me down, and it has made all the difference in my life."
     ]
     def schaub_random():
         zart = random.choice(Zdania.stwierdzenie) + random.choice(Zdania.puenta)
         return "".join(zart)



print(Zdania.schaub_random())

