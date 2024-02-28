/*
codewars link: https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/javascript

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
*/


//solution
function count(string) {
    if (!string) {
      return {};
    }
  
    let arrayOfCharacters = string.split('')
    
    result = {}
  
    for (i=0; i < arrayOfCharacters.length; i++) {
      let key_value = arrayOfCharacters[i]
      if (key_value in result) {
        result[key_value] += 1
      }
      else
        result[key_value] = 1
    }
    return result
  }