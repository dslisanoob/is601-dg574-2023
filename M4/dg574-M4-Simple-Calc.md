<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Dhruv Gargi (dg574)</td></tr>
<tr><td> <em>Generated: </em> 12/15/2023 12:52:05 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/dg574" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.37.33image.png.webp?alt=media&token=360e58bb-4e9f-4a0a-b6af-84591dff558c"/></td></tr>
<tr><td> <em>Caption:</em> <p>2+3=5<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.38.18image.png.webp?alt=media&token=10566e9c-b011-4329-8aa9-9bdb8893d061"/></td></tr>
<tr><td> <em>Caption:</em> <p>4-5=-1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.38.57image.png.webp?alt=media&token=7866149a-94e5-402b-9d0c-04ba38cc7753"/></td></tr>
<tr><td> <em>Caption:</em> <p>4*5=20<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.38.59image.png.webp?alt=media&token=c19a9db6-5322-4771-bb33-6aba2a68b641"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans = 20. 20/5=4.0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.42.04image.png.webp?alt=media&token=c3edaa01-f10c-4b25-b5d6-40e6db46d541"/></td></tr>
<tr><td> <em>Caption:</em> <p>ZeroDivisionError: Can&#39;t divide by zero<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.44.16image.png.webp?alt=media&token=0505ccb0-2d27-444d-93eb-97e5623c0b1b"/></td></tr>
<tr><td> <em>Caption:</em> <p>cases are indeed passing.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.47.44image.png.webp?alt=media&token=7ccf356b-7188-4e0d-b59b-8aacbc8c2918"/></td></tr>
<tr><td> <em>Caption:</em> <p>it passes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.48.14image.png.webp?alt=media&token=5c1d064d-5338-4bfb-b9f0-a7c3118aa8c9"/></td></tr>
<tr><td> <em>Caption:</em> <p>It passes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.48.45image.png.webp?alt=media&token=c10897bb-ccdb-4a6f-bc93-b43b94d339ce"/></td></tr>
<tr><td> <em>Caption:</em> <p>it passes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.49.28image.png.webp?alt=media&token=627895a0-53bd-4d13-a3d2-33c6c83556d9"/></td></tr>
<tr><td> <em>Caption:</em> <p>it passes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.49.51image.png.webp?alt=media&token=d52e512e-b172-4d68-b3ac-57d077803bef"/></td></tr>
<tr><td> <em>Caption:</em> <p>it passes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.50.21image.png.webp?alt=media&token=7dfcee29-63a7-4dfe-aa92-f044dd5e6a8f"/></td></tr>
<tr><td> <em>Caption:</em> <p>it passes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T05.50.55image.png.webp?alt=media&token=ce3d91b0-dafc-4e0b-980d-042ab6c34b71"/></td></tr>
<tr><td> <em>Caption:</em> <p>it passes<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>Nothing major, I just got a good hands on experience with pytest.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <p>Test cases offer a means of confirming that the program is functioning as<br>intended and satisfies the necessary specifications. Test cases are functions that employ assertions<br>to confirm the behavior of the code under test in the Pytest framework.<br><br>With<br>a straightforward syntax and adaptable framework that enable tests to be written in<br>an understandable and succinct manner, Pytest facilitates the definition and organization of test<br>cases. A vast array of testing scenarios, from straightforward unit tests to intricate<br>integration and end-to-end tests, are also supported by Pytest. I discovered some new<br>methods for arranging and setting up test cases in Pytest while working on<br>this assignment.<br>For instance, I discovered that fixtures can be used to control the<br>assembly and disassembly of testing environments, thereby minimizing redundancy and enhancing test case<br>maintainability. Additionally, I learned how to use parametrized tests, which let me test<br>several inputs with just one test case. This method can help to write<br>and maintain tests with less code, and it can be helpful for testing<br>functions or methods that have several possible inputs.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601-dg574-2023/pull/22">https://github.com/dslisanoob/is601-dg574-2023/pull/22</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/dg574" target="_blank">Grading</a></td></tr></table>
