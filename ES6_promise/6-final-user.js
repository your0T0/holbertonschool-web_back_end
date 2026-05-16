export default async function handleProfileSignup(firstName, lastName, fileName) {
  const signUpUser = (await import('./4-user-promise')).default;
  const uploadPhoto = (await import('./5-photo-reject')).default;

  const results = await Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]);

  return results;
}
