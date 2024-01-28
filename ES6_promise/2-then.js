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
      // En el caso de un rechazo, devolvemos un objeto con status y body.
      console.error('Error occurred while getting a response from the API');
      return Promise.reject({
        status: 500,
        body: 'error',
      });
    });
}
