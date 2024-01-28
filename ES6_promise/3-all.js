import { uploadPhoto, createUser } from "./utils";

function handleProfileSignup() {
  const promises = [];

  promises.push(
    uploadPhoto()
      .then(({ body }) => body)
      .catch(() => Promise.reject('Signup system offline'))
  );

  promises.push(
    createUser()
      .then(({ firstName, lastName }) => `${firstName} ${lastName}`)
      .catch(() => Promise.reject('Signup system offline'))
  );

  Promise.all(promises)
    .then((results) => {
      results.forEach((result) => console.log(result));
    })
    .catch((error) => {
      console.error(error);
    });
}
