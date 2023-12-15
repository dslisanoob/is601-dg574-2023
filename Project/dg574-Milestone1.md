<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Dhruv Gargi (dg574)</td></tr>
<tr><td> <em>Generated: </em> 12/14/2023 9:27:23 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/dg574" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T11.14.03image.png.webp?alt=media&token=265e8ac7-8337-405b-bfae-39a7a2cf8e35"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid email without &#39;@&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T11.14.34image.png.webp?alt=media&token=0e4a5ca1-587a-4e89-bf55-873691839c2a"/></td></tr>
<tr><td> <em>Caption:</em> <p>6 character invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T11.15.38image.png.webp?alt=media&token=a503663c-4c3a-460a-b20b-1586b0d9e6bb"/></td></tr>
<tr><td> <em>Caption:</em> <p>passwords dont match<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T11.16.25image.png.webp?alt=media&token=6a3ef32c-f3e0-4f07-acbc-6b657e501b6c"/></td></tr>
<tr><td> <em>Caption:</em> <p>username already taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T11.16.58image.png.webp?alt=media&token=216b98e0-d5f2-4c95-83cd-601294dca663"/></td></tr>
<tr><td> <em>Caption:</em> <p>email already taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T11.24.05image.png.webp?alt=media&token=58d9d7ea-e5eb-43f3-a4b5-f1eb51b79fdc"/></td></tr>
<tr><td> <em>Caption:</em> <p>account successfully created.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T11.25.44image.png.webp?alt=media&token=3884030c-ebb0-43c4-a529-885d43d87fa9"/></td></tr>
<tr><td> <em>Caption:</em> <p>1 user account in the data, row 1.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601fall2023/pull/1">https://github.com/dslisanoob/is601fall2023/pull/1</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>auth/forms.py: This file contains validators like DataRequired and Email to ensure valid input.<b><br></b>Such validators also exist for the remaining fields.</div><div>Things like RegistrationForm enforces a username<br>length between 4 and 25 characters. HTML files in templates use form attributes<br>like required for basic client-side validation.</div><div>The User class has a method set_password to<br>hash the password before storing it as password_hash. check_password is used to verify<br>the password during login.</div><div>sql/db.py: Database class manages the database connection and provides a<br>method execute_query for executing SQL queries.<br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.05.33image.png.webp?alt=media&token=e2006619-e1b0-4250-9fa2-be37c8eac44d"/></td></tr>
<tr><td> <em>Caption:</em> <p><br>Invalid password<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.05.52image.png.webp?alt=media&token=019f15e2-b34c-45ae-88f6-03201addfd68"/></td></tr>
<tr><td> <em>Caption:</em> <p><br>Invalid user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.07.33image.png.webp?alt=media&token=a086e99c-0332-4471-bda9-e1cdb00b923f"/></td></tr>
<tr><td> <em>Caption:</em> <p><br>Log in successful<br><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601fall2023/pull/1">https://github.com/dslisanoob/is601fall2023/pull/1</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>auth/forms.py: This file contains validators like DataRequired and Email to ensure valid input.<b><br></b>Such validators also exist for the remaining fields.</div><div>Things<br> like RegistrationForm enforces a username<br>length between 4 and 25 <br>characters. HTML files in templates use form attributes<br>like required <br>for basic client-side validation.</div><div>The User class has a method <br>set_password to<br>hash the password before storing it as password_hash. <br>check_password is used to verify<br>the password during login.</div><div>sql/db.py: Database class manages the database connection and provides a<br>method execute_query for executing SQL queries.<br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.10.58image.png.webp?alt=media&token=fcc0f28c-8ad0-4b4f-9031-45d106677a9e"/></td></tr>
<tr><td> <em>Caption:</em> <p><br>Successfully logged out<br><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.11.41image.png.webp?alt=media&token=28eb29da-c989-4f74-a7ce-09b8c25464ce"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601fall2023/pull/1">https://github.com/dslisanoob/is601fall2023/pull/1</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>The session logic is implemented using Flask&#39;s session management, which stores a user&#39;s<br>ID securely after login. When a user logs in, the system verifies their<br>credentials and, upon success, stores their identity in the session. This session persists<br>across requests, allowing the system to recognize the user without re-authentication on each<br>page.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.17.33image.png.webp?alt=media&token=81caff81-7994-40bc-94ae-e8fa9aa81c3f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.22.32image.png.webp?alt=media&token=a41d7755-4058-438a-83a5-4c129a10b840"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission Denied, since the test2 user is not having the admin role.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.23.29image.png.webp?alt=media&token=f78cd067-8b14-42fe-b9f0-94e13f6e4c1c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Row 1 contains the Admin role.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.24.24image.png.webp?alt=media&token=4f83fa5c-48cd-436e-9160-a25b86ddcb86"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin user is the only user in the database with the user_id 5<br>- test.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601fall2023/pull/1">https://github.com/dslisanoob/is601fall2023/pull/1</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;&nbsp;&nbsp; Flask&#39;s session mechanism is utilized to maintain user state. When a user<br>successfully logs in, their user ID is stored in the session.<br>&nbsp;&nbsp;&nbsp; Helpers like<br>login_required from Flask-Login are used as decorators on view functions to protect pages.<br>If a user tries to access a protected page without being authenticated, the<br>helper redirects them to the login page.<br>&nbsp;&nbsp;&nbsp; The current_user proxy provided by Flask-Login<br>is used within views to access the session&#39;s user information and enforce access<br>controls based on user attributes or roles.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;&nbsp;&nbsp; Upon successful login, the user&#39;s roles are stored within the Flask session.<br>&nbsp;&nbsp;&nbsp;<br>Role-protected pages utilize a decorator that checks a user&#39;s stored roles in the<br>session against the required roles for the page.<br>&nbsp;&nbsp;&nbsp; If the user does not<br>have the required role, the decorator prevents access to the page&#39;s content, typically<br>redirecting to an error or login page.<br>&nbsp;&nbsp;&nbsp; This ensures that only users with<br>the appropriate roles can view or interact with certain protected pages.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.29.49image.png.webp?alt=media&token=2c1671e1-87f9-4335-9ea7-ad331135d8b5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Everything is formatted properly.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.30.03image.png.webp?alt=media&token=ca579694-3f70-430d-a31e-2f82618f2e6a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Everything is formatted properly.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.30.22image.png.webp?alt=media&token=7fb4b6b4-5017-4e59-8d61-0dc7dc011897"/></td></tr>
<tr><td> <em>Caption:</em> <p>Everything is formatted properly.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.30.36image.png.webp?alt=media&token=c1a626f2-a9af-44e2-b0a6-4214288fbff4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Everything is formatted properly.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601fall2023/pull/1">https://github.com/dslisanoob/is601fall2023/pull/1</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;&nbsp;&nbsp; The CSS defines a consistent visual theme across the application, applying a<br>color scheme and font styles that align with the branding.<br>&nbsp;&nbsp;&nbsp; Navigation (nav) elements<br>have a distinct style for easy accessibility, usually with a background color that<br>sets them apart from the rest of the page content.<br>&nbsp;&nbsp;&nbsp; Forms are styled<br>for clarity and ease of use, with input fields, labels, and buttons clearly<br>distinguishable and aligned.<br>&nbsp;&nbsp;&nbsp; Padding and margins are used throughout to ensure that the<br>content is well-spaced and readable.<br>&nbsp;&nbsp;&nbsp; Responsive design techniques are employed to ensure the<br>interface adapts to various screen sizes, maintaining usability on desktop and mobile devices.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.33.21image.png.webp?alt=media&token=70ced3fd-c47f-4a57-a176-6bf98a10f541"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission Denied if you&#39;re logged out and try accessing an admin only page.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.33.53image.png.webp?alt=media&token=ad09d4ad-e824-4f73-bbd8-47762828e7ea"/></td></tr>
<tr><td> <em>Caption:</em> <p>Frontend validation for enter valid email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-12T12.34.07image.png.webp?alt=media&token=80d8d0e2-1897-4912-95a0-4fab017bafcb"/></td></tr>
<tr><td> <em>Caption:</em> <p>If the passwords dont match<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601fall2023/pull/1">https://github.com/dslisanoob/is601fall2023/pull/1</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;&nbsp;&nbsp; The application employs Flask form validation which provides context-specific error messages. For<br>instance, when a form field fails validation, the code returns a clear and<br>actionable message, such as &quot;Please enter a valid email&quot; for email fields or<br>&quot;Passwords do not match&quot; for password confirmation fields.<br>&nbsp;&nbsp;&nbsp; The application uses try-except blocks<br>to catch exceptions during operations like database access. In the except block, the<br>error is logged for debugging purposes, and a user-friendly error message is returned<br>to the user.<br>&nbsp;&nbsp;&nbsp; For login and access control, decorators and Flask&#39;s flash() function<br>are used to present messages like &quot;Access denied&quot; or &quot;Please log in to<br>view this page&quot; when a user attempts to navigate to restricted areas without<br>proper credentials.<br>&nbsp;&nbsp;&nbsp; These messages are not drawn from a centralized message file but<br>are instead crafted within the view functions and form classes where they are<br>directly related to the user&#39;s action, ensuring relevance and clarity.<br><br>This approach ensures that<br>any technical or internal errors are translated into informative messages that guide the<br>user appropriately without exposing underlying system details.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T02.08.49image.png.webp?alt=media&token=46139cb5-9353-45b1-9491-e4dfc8ad4f08"/></td></tr>
<tr><td> <em>Caption:</em> <p>The username, and email fields are getting autofilled. My password is getting autofilled<br>too since I have my password saved in the password manager.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601-dg574-2023/pull/7">https://github.com/dslisanoob/is601-dg574-2023/pull/7</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>within profile.html, we make use of the form object sent by the backend<br>and render_field function to render the fields and prefill the fields like username<br>and email with their data. For the view itself, we make use of<br>layout.html extended which takes care of the layout of the page.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T02.20.26image.png.webp?alt=media&token=a585cc50-da7b-48b1-b381-9bc71a148e9d"/></td></tr>
<tr><td> <em>Caption:</em> <p>username invalid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T02.20.49image.png.webp?alt=media&token=36436319-b5aa-4f3b-ae51-085d0f5cf812"/></td></tr>
<tr><td> <em>Caption:</em> <p>email invalid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T02.21.09image.png.webp?alt=media&token=95490db2-bab7-4918-b3d7-e918acb6ec71"/></td></tr>
<tr><td> <em>Caption:</em> <p>password invalid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T02.22.05image.png.webp?alt=media&token=a6e98921-c8c0-4250-ac5e-6cd6cffff123"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T02.24.05image.png.webp?alt=media&token=226ee81c-3dde-4e57-9098-d71abbd4c3d4"/></td></tr>
<tr><td> <em>Caption:</em> <p>before email has changed. it changes the email column of the table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T02.24.35image.png.webp?alt=media&token=789d4a63-a546-4f0f-80f6-5f00964dd3ba"/></td></tr>
<tr><td> <em>Caption:</em> <p>after email has been changed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601-dg574-2023/pull/7">https://github.com/dslisanoob/is601-dg574-2023/pull/7</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;&nbsp;&nbsp; Email and Username:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; When editing email or username, the application first checks<br>if the new value is unique and not already taken by another user.<br>This is done through a query in the database.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The application employs form<br>validation to ensure that the new email is in a valid format and<br>that the username meets any specific requirements (like length, allowed characters).<br>&nbsp;&nbsp;&nbsp; Password:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For<br>password changes, the application includes logic to verify the current password before allowing<br>the update. This ensures that only the authorized user can change the password.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>The new password goes through a validation process checking for criteria like minimum<br>length, complexity, etc.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Once validated, the new password is hashed before being stored<br>in the database, replacing the old password hash.<br>&nbsp;&nbsp;&nbsp; Form Submission and Update Process:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>On form submission, the application checks all fields for validation errors.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If validation<br>passes, it updates the corresponding user record in the database with the new<br>email, username, or hashed password.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In case of validation failure, error messages are<br>returned to the user, prompting for the necessary corrections.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I was struggling with heroku and its environment variables, i realized that these<br>env variables dont get passed to the docker image. And so I learned<br>how to fix that.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://dg574-is601-prod-f8b1dbc00119.herokuapp.com/">https://dg574-is601-prod-f8b1dbc00119.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/dg574" target="_blank">Grading</a></td></tr></table>