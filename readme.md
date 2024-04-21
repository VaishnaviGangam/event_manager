# Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

## Issues Fixed

### [Internal Server Error on User Creation](https://github.com/VaishnaviGangam/event_manager/issues/1)

  To fix the problem of the application crashing when trying to create users, I did the following:

  1. **Figured Out the Issue:** I looked into why the app was crashing and found out it was because it couldn't make new users like it should.

  2. **Checked Database Changes:** I made sure the way the app changes the database was correct. I saw that some things about creating users were missing or wrong.

  3. **Fixed Database Changes:** I corrected how the app changes the database. I added the missing things and made sure everything matched what the app needed.

  4. **Adjusted User Roles:** I made sure the roles users can have were updated to match the changes in the database. This helps keep everything working smoothly.

  5. **Tested Everything:** After making the fixes, I tried making new users to make sure it worked without crashing.

  6. **Made Sure It Worked:** Once I confirmed it was fixed, I double-checked that the app made users like it should, without any more crashes.

  7. **Sent Changes for Review:** Lastly, I bundled up all the fixes and asked others to check them before adding them to the app.

  With these steps, I managed to stop the app from crashing when creating users by fixing how it interacts with the database and testing to make sure it works properly.

### [Enforce Username Length Limit to 64 Characters](https://github.com/VaishnaviGangam/event_manager/issues/4)

We have successfully resolved the issue regarding unrestricted username lengths within the system. By enforcing a maximum limit of 64 characters for usernames, we have addressed potential UI display problems and database constraints.

1. **Frontend Validation:** Implemented client-side validation to restrict username inputs to a maximum of 64 characters.
Provided real-time feedback to users regarding username length limits.
2. **Backend Validation:** Updated backend API endpoints to incorporate server-side validation and implemented validation checks to ensure usernames adhere to the 64-character limit. Configured error responses to inform clients of validation failures.
3. **Database Schema Update:** Modified the database schema to enforce the 128-character limit on the username column. Applied length constraints using database migration scripts.
4. **Documentation Update:** Updated user guides and developer resources to reflect the new username length limitation. Provided clear instructions on the maximum allowed username length.

### [Limit Password Length to 64 Characters](https://github.com/VaishnaviGangam/event_manager/issues/6)

To boost security measures, I made the following upgrades:

1. **Password Length Limit:** Set a maximum limit of 64 characters for password to prevent potential security risks like buffer overflow attacks.

2. **Real-time Feedback:** Added instant feedback on the frontend to guide users within the password length limit, reducing the chance of errors.

3. **Backend Validation:** Strengthened backend validation to enforce password length restrictions, enhancing protection against malicious inputs.

4. **Database Update:** Updated the database schema to enforce the new password length limit, securing stored data.

5. **Documentation Update:** Updated user guides and developer docs to highlight the new password length rule, ensuring clarity for users and developers alike.

These changes aim to improve the application's security posture by minimizing potential vulnerabilities related to password inputs.


###  [Resolve Docker Scan Failures in CI/CD Pipeline](https://github.com/VaishnaviGangam/event_manager/issues/9)

To address the Docker scan failures in the CI/CD pipeline, I've fixed the issue by updating the Gunicorn dependency from version 21.2.0 to 22.0.0. This update ensures that our application is utilizing the latest version of Gunicorn, which may include security patches and improvements.

To update the Gunicorn dependency, follow these steps:

1. Open the `requirements.txt` file in your project directory.
2. Locate the line specifying the Gunicorn dependency, typically listed as `gunicorn==21.2.0`.
3. Replace `21.2.0` with `22.0.0`.
4. Save the changes to the `requirements.txt` file.

After updating the dependency, ensure to rebuild and redeploy your Docker images to incorporate the changes. This should resolve the Docker scan failures and ensure that your CI/CD pipeline consistently passes the Docker scan test, confirming the absence of known security vulnerabilities in your Docker images.

