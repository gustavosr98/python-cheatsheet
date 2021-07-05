from typing import List
import requests

class Calc:
  def __init__(self) -> None:
      self.name = name

  def add(numbers: List[int]) -> int:
    try:
      response = requests.post('http://localhost:3000/dev/calcs/add', json={ "numbers": numbers })
      if (response.status_code == 500): raise Exception("Server Error")
      return response.json()["result"]
    except Exception as e:
      print("[ERROR]: ", e)
    

print( (lambda numbers: sum(numbers))([1,2,3]))

calc = Calc("Me")
print(calc.name)