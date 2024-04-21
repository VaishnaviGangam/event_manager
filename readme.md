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

1. **Username Length Limit:** Set a maximum limit of 64 characters for usernames to prevent potential security risks like buffer overflow attacks.

2. **Real-time Feedback:** Added instant feedback on the frontend to guide users within the username length limit, reducing the chance of errors.

3. **Backend Validation:** Strengthened backend validation to enforce username length restrictions, enhancing protection against malicious inputs.

4. **Database Update:** Updated the database schema to enforce the new username length limit, securing stored data.

5. **Documentation Update:** Updated user guides and developer docs to highlight the new username length rule, ensuring clarity for users and developers alike.

These changes aim to improve the application's security posture by minimizing potential vulnerabilities related to username inputs.