import hashlib
import random

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


if(verifierKnowledge(hashedSecret, ExpectedSecret)):
  print("Same Path")
else:
  print("Not same Paths")
