import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  return Promise.allSettled([userPromise, photoPromise])
    .then((results) => {
      const [userResult, photoResult] = results;

      const userPayload = userResult.status === 'fulfilled' ? userResult.value : null;
      const photoPayload = photoResult.status === 'fulfilled' ? photoResult.value : null;

      return {
        user: userPayload,
        photo: photoPayload,
      };
    });
}
