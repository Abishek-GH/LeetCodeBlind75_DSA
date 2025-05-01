/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  if (typeof x !== 'number' && typeof x !== 'string') {
    return false;
  }
  const cleanedStr = String(x).toLowerCase();
  const reversedStr = cleanedStr.split('').reverse().join('');
  return reversedStr === cleanedStr;
};

console.log(isPalindrome(121));
