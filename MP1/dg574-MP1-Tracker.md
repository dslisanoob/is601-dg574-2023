<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Dhruv Gargi (dg574)</td></tr>
<tr><td> <em>Generated: </em> 12/14/2023 1:28:31 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/dg574" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T03.23.12image.png.webp?alt=media&token=253b3341-9bb5-4fc9-9d92-f2e47253c672"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task added successfully, it throws an error if the data is missing.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T03.29.34image.png.webp?alt=media&token=03cddc80-fa55-4edc-a45e-51e99148e8ed"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task failed: Error: The following required fields are missing: description, due<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <div>It updates lastActivity with the current datetime value</div><div>It matches due data format to<br>the one mentioned in str_to_datetime()</div><div>It adds new task to the list</div><div>It returns an<br>output message confirming if the new task was added or that it was<br>rejected due to some missing/invalid data.</div><div>It saves the data to tracker.json<br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T03.49.53image.png.webp?alt=media&token=04544539-9b4e-4d7f-a647-5904bb145019"/></td></tr>
<tr><td> <em>Caption:</em> <p>This image demonstrates the successful update of the task. If no changes are<br>made, a specific message stating &quot;no changes provided, task not updated&quot; is displayed,<br>informing the user that no modifications were necessary.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T03.51.36image.png.webp?alt=media&token=94d3763b-2367-423e-950c-b2d067d76d08"/></td></tr>
<tr><td> <em>Caption:</em> <p>This function facilitates the updating of tasks by utilizing the process_update function and<br>subsequently displaying them in the lists_tasks.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>We have implemented a code that handles various conditions. When no changes are<br>made during an update, a specific message stating &quot;no changes provided&quot; is displayed<br>to inform the user that the task was not updated. Additionally, if an<br>attempt is made to update a non-existent task, a &quot;invalid text index&quot; message<br>is generated, indicating an invalid bound exception.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T04.06.58image.png.webp?alt=media&token=d8d4bc1a-99fc-4a5e-a774-04ea942723f1"/></td></tr>
<tr><td> <em>Caption:</em> <p>This function facilitates the updating of tasks by utilizing the process_update function and<br>subsequently displaying them in the lists_tasks.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T04.20.25image.png.webp?alt=media&token=baff1803-7535-4a5a-99a4-4b7099b0ce66"/></td></tr>
<tr><td> <em>Caption:</em> <p>This image depicts a successful update of the task. If no changes were<br>made, a specific message stating &quot;no changes provided, task not updated&quot; is displayed<br>to inform the user that no modifications were necessary.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p>We have implemented a code that handles various conditions. When no changes are<br>made during an update, a specific message stating &quot;no changes provided, task not<br>updated&quot; is displayed to inform the user that no modifications were made. Additionally,<br>if an attempt is made to update a non-existent task, a &quot;invalid text<br>index&quot; message is generated, indicating an invalid bound exception and informing us that<br>the task does not exist.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T04.24.09image.png.webp?alt=media&token=9b2c44ba-9ea0-4381-8e15-a71ad65154cb"/></td></tr>
<tr><td> <em>Caption:</em> <p>By utilizing this function, we have the ability to designate a job as<br>completed, which then triggers an automatic change in the lists_tasks.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T04.26.16image.png.webp?alt=media&token=14b86fc7-9f0e-442e-8d76-5a995a87f02a"/></td></tr>
<tr><td> <em>Caption:</em> <p>As previously said, we ensure that the task is marked as completed. When<br>this action is performed, a corresponding message appears indicating success. If the task<br>has already been completed, a message stating that the task is already finished<br>is displayed. If the task is not in the list, an invalid message<br>is shown.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p>As previously said, all the necessary information is included in the code, meeting<br>all the specified criteria. I have also provided my UCID and the date<br>of code completion.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T04.37.30image.png.webp?alt=media&token=8133c012-d297-43b9-8e12-83d35c7baf80"/></td></tr>
<tr><td> <em>Caption:</em> <p>This image displays the necessary code that enables the comprehensive viewing of a<br>certain task, including its state. For instance, if the task is done, it<br>will indicate its completion, otherwise, a &#39;-&#39; symbol is displayed. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T04.40.56image.png.webp?alt=media&token=27d1df7e-604c-4d83-a5c3-506150daf8be"/></td></tr>
<tr><td> <em>Caption:</em> <p>This image shows the output that facilitates viewing a specific task and provides<br>all of its information. If we select a task that is not available<br>in the app, an error message such as &quot;invalid task index&quot; is displayed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T04.43.00image.png.webp?alt=media&token=f95e5112-4e3c-47c5-a68c-db5b937df185"/></td></tr>
<tr><td> <em>Caption:</em> <p>This indicates how many tasks are in the tracker app, and selecting the<br>list option from the options list prints all of the tasks that are<br>in the app.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T04.44.46image.png.webp?alt=media&token=cd496e20-7d14-46ca-8ad8-0e5d92fa0e1a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here we can use the above code to delete a particular task .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T04.44.49image.png.webp?alt=media&token=2b019694-2ade-4506-a360-bd323b42542f"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is where we can delete a task. If the operation is successful,<br>a message will appear; if not, it will indicate that the task is<br>invalid.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p>As previously stated, we can delete a specific task using the code above.<br>This<br>is where we can delete a task. If the operation is successful, a<br>message will appear; if not, it will state that the task is invalid.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T05.13.47image.png.webp?alt=media&token=d9af0e44-1db5-48f4-a2f1-a6489b69959c"/></td></tr>
<tr><td> <em>Caption:</em> <p>This section of the code uses the tracker app&#39;s incomplete task lists to<br>retrieve the relevant task names and deadline dates.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T16.58.19image.png.webp?alt=media&token=f1a0e002-97b4-43b5-ab53-04c42375498b"/></td></tr>
<tr><td> <em>Caption:</em> <p>As stated in the code, we print the incomplete tasks here. The output<br>shows the number of incomplete tasks and the corresponding due date; if all<br>tasks are marked as completed or done, then there are no pending tasks.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T16.58.34image.png.webp?alt=media&token=c91a5313-4825-47f8-bf85-f52956d41e8e"/></td></tr>
<tr><td> <em>Caption:</em> <p>As stated in the code, we print the incomplete tasks here. The output<br>shows the number of incomplete tasks and the corresponding due date; if all<br>tasks are marked as completed or done, then there are no pending tasks.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>Everything is satisfactorily stated in the code and all conditions are met. <br>This<br>section of the code uses the tracker app&#39;s incomplete task lists to retrieve<br>the relevant task names and due dates.<br>As stated in the code, we print<br>the incomplete tasks here. We also obtain an output that indicates the number<br>of incomplete tasks and the corresponding due date. If all tasks are marked<br>as completed or done, then there are no pending tasks.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T17.06.30image.png.webp?alt=media&token=907eb12f-312d-413c-8024-35de900bb6d0"/></td></tr>
<tr><td> <em>Caption:</em> <p>This section&#39;s code prints the overdue tasks, indicating which ones are out of<br>line—that is, when the specified due date is earlier than the current time—and<br>which ones are past due.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T17.12.29image.png.webp?alt=media&token=da545ab2-f7cd-459f-901c-ba82eb2c07ee"/></td></tr>
<tr><td> <em>Caption:</em> <p>After running the aforementioned code, the output appears as follows: it lists the<br>overdue tasks along with their names and the corresponding due date, just as<br>it does for incomplete tasks. If there are no overdue tasks—that is, if<br>everything is current—it indicates that &quot;No tasks overdue.&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>We have written the code to print the overdue tasks in this segment.<br>This code indicates which tasks are beyond the due date/time, or when the<br>specified due date is earlier than the current time, and it also tells<br>you which tasks are past due.<br>Here, we&#39;ve run the code mentioned above and<br>received the following output: it lists the overdue tasks along with their names<br>and the corresponding due date, just like it does for incomplete tasks. When<br>there are no overdue tasks—that is, when everything is current—it indicates that there<br>are no overdue tasks.<br><br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T17.23.11image.png.webp?alt=media&token=335b0072-cbf0-4245-b859-7e408d93dc4a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the code we wrote to find the remaining time for a<br>specific task. It not only tells us how much time is left on<br>the task, but it also displays the task&#39;s overdue date and even generates<br>an invalid bound message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T17.29.49image.png.webp?alt=media&token=81bf865e-e03d-40c7-ac81-7c79e042be12"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here, as stated in the code, everything is run and an output is<br>produced when we choose the remaining option from the menu bar. We then<br>receive the output for the task we selected, which is the time remaining<br>in days, hours, minutes, and seconds. If the task is overdue, it prints<br>the time in the same format as before and indicates that it is<br>overdue by a certain amount of time.In addition, if we choose a task<br>that doesn&#39;t exist, we will also receive an invalid message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>Here is the code we wrote to find the remaining time for a<br>specific task. It not only tells us how much time is left on<br>the task, but it also displays the task&#39;s overdue date and even provides<br>an invalid bound message.<br><br>Here, as stated in the code, everything is run and<br>the output is produced when we choose the remaining option from the menu<br>bar. We then receive the output as time remaining, which is the precise<br>amount of time left in days, hours, minutes, and seconds for the task<br>we chose. If the selected task is past due, the time is printed<br>in the same format as before and the message &quot;task is overdue by<br>so and so time&quot; is displayed.additionally, if we select a task that doesn&#39;t<br>exist, we will also receive an invalid message.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T17.34.44image.png.webp?alt=media&token=02afb982-b208-435c-85f1-733bb14a861c"/></td></tr>
<tr><td> <em>Caption:</em> <p>The output is indeed getting generated.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-14T17.35.15image.png.webp?alt=media&token=1806c795-277b-4dde-b4c4-cf9ca193df64"/></td></tr>
<tr><td> <em>Caption:</em> <p>These are the contents of the json file.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>Apart from the time management, I did not really face any issues while<br>working on this project, it helped me understand how CLI applications work.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601-dg574-2023/pull/1">https://github.com/dslisanoob/is601-dg574-2023/pull/1</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/dg574" target="_blank">Grading</a></td></tr></table>