export default function cleanSet(set, startString) {
  const resStr = [];

  if (startString.length === 0) return '';

  [...set].forEach((e) => {
    if (e.startsWith(startString)) {
      resStr.push(e.slice(startString.length));
    }
  });

  return resStr.join('-');
}
