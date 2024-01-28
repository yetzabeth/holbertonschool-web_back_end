export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('Got a response from the API');
      return {
        status: 200,
        body: 'success',
      };
    })
    .catch(() => {
      console.error('Error occurred while getting a response from the API');
      throw new Error('The fake API is not working currently');
    });
}
