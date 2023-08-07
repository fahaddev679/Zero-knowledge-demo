import hashlib
import random
#here random is just used to increase difficulty level to solve the puzzle.
#prover
secret = 'Path is ABC'
#verifier
ExpectedSecret = 'Path is BC'

def hashing(secret):
  return hashlib.sha256(secret.encode()).hexdigest()

def challange():
  return random.randrange(0, 100, 1)

challangedValue = challange()

def proveKnowledge(secret):
  return hashing(secret + str(challangedValue))

hashedSecret = proveKnowledge(secret)

def verifierKnowledge(hashedSecret, ExpectedSecret):
    for i in range(0, 100, 1):
        hashedExpected = hashing(ExpectedSecret + str(i))
        if hashedExpected == hashedSecret:
            return True
    return False

#this is how instead of revealing the message just confirm whether either condition meets the requirement or not
if(verifierKnowledge(hashedSecret, ExpectedSecret)):
  print("Same Path")
else:
  print("Not same Paths")
