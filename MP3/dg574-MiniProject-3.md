<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Dhruv Gargi (dg574)</td></tr>
<tr><td> <em>Generated: </em> 12/14/2023 8:13:14 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/dg574" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T22.50.06image.png.webp?alt=media&token=c2cd11fb-f361-48ab-85c4-708b53b5562b"/></td></tr>
<tr><td> <em>Caption:</em> <p>homepage<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T22.50.31image.png.webp?alt=media&token=495a19fa-73a5-44a5-87fe-99586d6208fa"/></td></tr>
<tr><td> <em>Caption:</em> <p>index.html<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T22.54.08image.png.webp?alt=media&token=e6590b43-5ee8-41ff-9d57-0b1885cdc83d"/></td></tr>
<tr><td> <em>Caption:</em> <p>The links have been edited, the ucid has been replaced to dg574<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T22.54.39image.png.webp?alt=media&token=3b94cc42-c104-463e-b249-4fc2c96b790f"/></td></tr>
<tr><td> <em>Caption:</em> <p>The navbar has been edited, the ucid has been replaced to dg574<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.06.00image.png.webp?alt=media&token=f781d5db-4059-4ed1-8fdd-f71c897cfe92"/></td></tr>
<tr><td> <em>Caption:</em> <p> flash(&quot;Select only csv files&quot;)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.06.29image.png.webp?alt=media&token=cb0ded26-4726-4ea6-906f-168c3e746205"/></td></tr>
<tr><td> <em>Caption:</em> <p>csv_reader = csv.DictReader(stream)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.06.46image.png.webp?alt=media&token=d53a17b4-7cb2-4334-a075-e20ab860a50e"/></td></tr>
<tr><td> <em>Caption:</em> <p> try:<br>           <br>            <br>   organizations.append({<br>         <br>            <br>     &#39;name&#39;: row[&#39;organization_name&#39;],<br>      <br>            <br>        &#39;address&#39;: row[&#39;organization_address&#39;],<br>   <br>            <br>           &#39;city&#39;: row[&#39;organization_city&#39;],<br><br>            <br>            <br> &#39;country&#39;: row[&#39;organization_country&#39;],<br>          <br>            <br>    &#39;state&#39;: row[&#39;organization_state&#39;],<br>       <br>            <br>       &#39;zip&#39;: row[&#39;organization_zip&#39;],<br>    <br>            <br>          &#39;website&#39;: row[&#39;organization_website&#39;],<br> <br>            <br>            <br>&#39;description&#39;: row[&#39;organization_description&#39;],<br>           <br>            <br>   })<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.07.30image.png.webp?alt=media&token=78287125-520b-4d84-b7b5-b772d876c6d8"/></td></tr>
<tr><td> <em>Caption:</em> <p>donations.append({<br>            <br>            <br>      &#39;donor_firstname&#39;: row[&#39;donor_name&#39;].split()[0] if row[&quot;donor_name&quot;] else &#39;&#39;,<br> <br>            <br>            <br>    &#39;donor_lastname&#39;: row[&#39;donor_name&#39;].split()[1] if len(row[&quot;donor_name&quot;].split())&gt;1 else &#39;&#39;,<br>   <br>            <br>            <br>  &#39;donor_email&#39;: row[&#39;donor_email&#39;],<br>         <br>            <br>         &#39;item_name&#39;: row[&#39;item_name&#39;],<br>  <br>            <br>            <br>   &#39;item_description&#39;: row[&#39;item_description&#39;],<br>        <br>            <br>          &#39;quantity&#39;: row[&#39;quantity&#39;],<br> <br>            <br>            <br>    &#39;organization_name&#39;: row[&#39;organization_name&#39;],<br>       <br>            <br>           &#39;donation_date&#39;: row[&#39;donation_date&#39;],<br><br>            <br>            <br>     &#39;comments&#39;: row[&#39;comments&#39;],<br>      <br>            <br>        })<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.13.00image.png.webp?alt=media&token=1b754288-e586-4ff7-b71f-f917ca2218ae"/></td></tr>
<tr><td> <em>Caption:</em> <p>500 organizations inserted or updated <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.26.19image.png.webp?alt=media&token=79acdd7e-11b6-4665-ac29-5e7585e885fa"/></td></tr>
<tr><td> <em>Caption:</em> <p>create view<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.26.59image.png.webp?alt=media&token=a84ba824-d97e-43b8-8cba-e26199555914"/></td></tr>
<tr><td> <em>Caption:</em> <p>list of donations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.27.16image.png.webp?alt=media&token=2c81f13a-fb55-4583-98d2-0800b49a6e22"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit view<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.34.55image.png.webp?alt=media&token=e2b14cf6-2107-4dc3-965d-0cd0352ec34c"/></td></tr>
<tr><td> <em>Caption:</em> <p>the main donation page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.35.05image.png.webp?alt=media&token=4b7b3363-e6b2-4f8b-a2d7-756f5647455c"/></td></tr>
<tr><td> <em>Caption:</em> <p>the main donation page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.35.13image.png.webp?alt=media&token=5ba72807-8c43-423d-823a-8432deba8381"/></td></tr>
<tr><td> <em>Caption:</em> <p>the main donation page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.36.48image.png.webp?alt=media&token=190699f7-ab70-4da5-8f25-1a122d935fd6"/></td></tr>
<tr><td> <em>Caption:</em> <p>no filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.37.33image.png.webp?alt=media&token=375560b7-00db-48b7-a4e1-8257cbfb45d1"/></td></tr>
<tr><td> <em>Caption:</em> <p>donations for a particular company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.38.49image.png.webp?alt=media&token=c78bf941-b5b3-4f92-8614-f1f4efd455c5"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for the donations for a particular company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.39.00image.png.webp?alt=media&token=c550361e-35e7-4dc1-99e4-74c5e6ef8f25"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for the donations for a particular company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.39.08image.png.webp?alt=media&token=e4143974-01cd-435b-be8b-0d9f68f09b5e"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for the donations for a particular company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T23.39.15image.png.webp?alt=media&token=857b2cc5-773f-41ce-ab73-8c6d1f3e25e8"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for the donations for a particular company<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.12.43image.png.webp?alt=media&token=6884c693-306f-49c9-b4fe-c184c2ac3c3a"/></td></tr>
<tr><td> <em>Caption:</em> <p>search route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.13.43image.png.webp?alt=media&token=d5566191-cb74-4dca-94df-732782a46d50"/></td></tr>
<tr><td> <em>Caption:</em> <p>retrieval<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.15.20image.png.webp?alt=media&token=82d8be70-31ed-4fde-9193-f0be7b074ea2"/></td></tr>
<tr><td> <em>Caption:</em> <p>LIKE filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.21.48image.png.webp?alt=media&token=98772813-4e45-45be-bd3e-713be5a61917"/></td></tr>
<tr><td> <em>Caption:</em> <p>LIKE filter<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.25.28image.png.webp?alt=media&token=b0e486e6-e592-473c-96fe-684e6dbaa60e"/></td></tr>
<tr><td> <em>Caption:</em> <p>retrieval and validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.26.30image.png.webp?alt=media&token=66e4fa56-3848-4380-bbf2-47b9b10523f7"/></td></tr>
<tr><td> <em>Caption:</em> <p>adding remaining stuff and then running the query.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.27.21image.png.webp?alt=media&token=eaab8630-2997-4aaf-a11f-1de28651bbb7"/></td></tr>
<tr><td> <em>Caption:</em> <p>fetching args and added them<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.27.33image.png.webp?alt=media&token=d587bbde-bcba-4494-9f3a-02924d93a2f8"/></td></tr>
<tr><td> <em>Caption:</em> <p>adding more things<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.27.42image.png.webp?alt=media&token=2ce171ad-8035-4825-b476-a93d62959f9d"/></td></tr>
<tr><td> <em>Caption:</em> <p>running the query<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.29.23image.png.webp?alt=media&token=5a856f49-b5fd-4ef8-a84a-e544700f50cf"/></td></tr>
<tr><td> <em>Caption:</em> <p>deletion - which is quite straightforward.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.30.24image.png.webp?alt=media&token=98082587-6833-4407-b838-56c25acf3fe7"/></td></tr>
<tr><td> <em>Caption:</em> <p>record currently present<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.30.37image.png.webp?alt=media&token=5025c41e-b3d8-48fe-be7b-33b1a9fbf30e"/></td></tr>
<tr><td> <em>Caption:</em> <p>successfully deleted<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.31.50image.png.webp?alt=media&token=e9eb6514-70b9-449a-8953-ae38a1b1f3c2"/></td></tr>
<tr><td> <em>Caption:</em> <p>create<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.33.15image.png.webp?alt=media&token=b076d74a-b872-4251-9b35-2da2979a9394"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.39.33image.png.webp?alt=media&token=cf38ee7a-0157-4fe9-bbb8-0d5ecc8f311a"/></td></tr>
<tr><td> <em>Caption:</em> <p>this code renders the page responsible for managing the organizations.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.37.33image.png.webp?alt=media&token=0a46284b-253f-4d3d-9bd1-633da7abfd2a"/></td></tr>
<tr><td> <em>Caption:</em> <p>no filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.38.02image.png.webp?alt=media&token=7d5384f6-83a5-46d3-8d1d-aa5060e81bdf"/></td></tr>
<tr><td> <em>Caption:</em> <p>filtering country<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.38.33image.png.webp?alt=media&token=6c370164-452a-4215-8ee5-128ed1d3a673"/></td></tr>
<tr><td> <em>Caption:</em> <p>filtering country<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.41.43image.png.webp?alt=media&token=3887ca2e-c362-478b-81a0-2fdee7b309be"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for listing organization<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.42.46image.png.webp?alt=media&token=10133210-37a1-4d69-b6b4-c839b5b85b0b"/></td></tr>
<tr><td> <em>Caption:</em> <p>It contains everything, just like donations.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.43.50image.png.webp?alt=media&token=7e9577f6-a83d-4989-a1a9-4ce1b95e2ce2"/></td></tr>
<tr><td> <em>Caption:</em> <p>it contains everything for add just like donations.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.44.01image.png.webp?alt=media&token=2c6e006a-2910-47d8-a7a6-1921e5b9d844"/></td></tr>
<tr><td> <em>Caption:</em> <p>it contains everything for add just like donations.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.44.53image.png.webp?alt=media&token=15ba510d-9c44-4113-a707-05c28500bc01"/></td></tr>
<tr><td> <em>Caption:</em> <p>it contains everything for edit just like donations.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.45.04image.png.webp?alt=media&token=73fbd490-a16b-4d7a-ac32-febfc93505e9"/></td></tr>
<tr><td> <em>Caption:</em> <p>it contains everything for edit just like donations.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.45.49image.png.webp?alt=media&token=2cb023da-8fb0-4c5b-821b-9abf41a52797"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete functionality for organizations has been implemented over here.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.46.29image.png.webp?alt=media&token=5714cc88-1f03-4f57-8071-2d6697a6f65d"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization deleted<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T00.59.59image.png.webp?alt=media&token=23296206-4d4c-45d3-b6d3-db8b766fe374"/></td></tr>
<tr><td> <em>Caption:</em> <p>3 test cases failed sadly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T01.05.25image.png.webp?alt=media&token=f8c4efdd-0675-41ab-90dd-ba822d1e3c4c"/></td></tr>
<tr><td> <em>Caption:</em> <p>8 failed test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T01.06.08image.png.webp?alt=media&token=0f27a197-785a-4b4a-97b4-a59eaea270a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>test case failed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T01.03.27image.png.webp?alt=media&token=daa8c5ee-f5a9-4620-ab1a-e4bb201d7ab5"/></td></tr>
<tr><td> <em>Caption:</em> <p>test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>No, a lot of these test cases failed but due to lack of<br>time, I have not been able to debug them efficiently. The website is<br>pretty functional from what I see.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601-dg574-2023/pull/5">https://github.com/dslisanoob/is601-dg574-2023/pull/5</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T01.11.15image.png.webp?alt=media&token=aa10dea1-060a-45f6-bc44-04641cb6e817"/></td></tr>
<tr><td> <em>Caption:</em> <p>added commit history<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T01.12.22image.png.webp?alt=media&token=54b3be0b-5a44-4032-8403-ca5c3df30657"/></td></tr>
<tr><td> <em>Caption:</em> <p>added wakatime screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-007-dg574-mp3-e455a9891558.herokuapp.com/">https://is601-007-dg574-mp3-e455a9891558.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/dg574" target="_blank">Grading</a></td></tr></table>