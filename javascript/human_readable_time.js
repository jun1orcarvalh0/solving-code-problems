/*
codewars link: https://www.codewars.com/kata/52685f7382004e774f0001f7/train/javascript

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
*/


//solution
function humanReadable (seconds) {
    if (!seconds) {
      return '00:00:00';
    }
  
    const getHours = () => {
      const hours = Math.floor(totalSeconds / 3600)
      if (hours) {
        totalSeconds = totalSeconds - (hours * 3600)
        return formattedTime(hours)
      }
      return formattedTime(0)
    }
  
    const getMinutes = () => {
      const minutes = Math.floor(totalSeconds / 60)
      if (minutes) {
        totalSeconds = totalSeconds - (minutes * 60)
        return formattedTime(minutes)
      }
      return formattedTime(0)
    }
  
    const getSeconds = () => {
      return formattedTime(totalSeconds);
    }
    
    const formattedTime = (number) => {
      return ("0" + number).slice(-2);
    }
  
    let totalSeconds = seconds;
    let readableHours = getHours();
    let readableMinutes = getMinutes();
    let readableSeconds = getSeconds();
    return `${readableHours}:${readableMinutes}:${readableSeconds}`
  }