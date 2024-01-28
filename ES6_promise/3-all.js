import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([
    uploadPhoto(),
    createUser(),
  ])
    .then((values) => {
      const [photoResponse, userResponse] = values;

      console.log(photoResponse.body);
      console.log(userResponse.body, userResponse.firstName, userResponse.lastName);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
