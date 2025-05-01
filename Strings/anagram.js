/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (typeof s !== 'string' || typeof t !== 'string' || s.length !== t.length) {
    return false;
  }
  const clean = (s) => s.toLowerCase().split('').sort().join('');

  return clean(s) === clean(t);
};
