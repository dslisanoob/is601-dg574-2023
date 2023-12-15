<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 API Project</td></tr>
<tr><td> <em>Student: </em> Dhruv Gargi (dg574)</td></tr>
<tr><td> <em>Generated: </em> 12/14/2023 11:07:34 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/dg574" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Which API did you choose?</td></tr>
<tr><td> <em>Response:</em> <div>Asos pricing API to fetch products listed on Asos.com (real shopping website) and<br>advertise the same products on my ECommerce website.</div><div>https://rapidapi.com/apidojo/api/asos2/<br></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Which endpoints will be used?</td></tr>
<tr><td> <em>Response:</em> <div><div style="color: #cccccc;background-color: #1f1f1f;font-family: Consolas, 'Courier New', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><span style="color:<br>#ce9178;">/products/v2/list</span></div></div></div><div>This only API endpoint that I will be using. Upon passing the category<br>id and the limit/offset, it returns a list of items belonging to that<br>category which are listed live on that website.<br></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What pieces of data will be used in your app?</td></tr>
<tr><td> <em>Response:</em> <div style="color: #cccccc;background-color: #1f1f1f;font-family: Consolas, 'Courier New', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><span style="color:<br>#ce9178;">&nbsp; &nbsp; &nbsp; {</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"id":203865402,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp;"name":"Columbia thrive revive sliders in black",</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp;"price":{</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "current":{</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"value":54,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp;"text":"$54.00"</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; },</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; "previous":{</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"value":null,</span></div><div><span<br>style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"text":""</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; },</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "rrp":{</span></div><div><span style="color:<br>#ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"value":null,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;"text":""</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; },</span></div><div><span style="color:<br>#ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "isMarkedDown":false,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; "isOutletPrice":false,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "currency":"USD"</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp;},</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"colour":"Black",</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp;"colourWayId":203865418,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"brandName":"Columbia",</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp;"hasVariantColours":false,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"hasMultiplePrices":false,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"groupId":null,</span></div><div><span<br>style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"productCode":123165213,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"productType":"Product",</span></div><div><span style="color:<br>#ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"url":"columbia/columbia-thrive-revive-sliders-in-black/prd/203865402?clr=black&amp;colourWayId=203865418",</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"imageUrl":"images.asos-media.com/products/columbia-thrive-revive-sliders-in-black/203865402-1-black",</span></div><div><span style="color: #ce9178;">&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;"additionalImageUrls":[</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "images.asos-media.com/products/columbia-thrive-revive-sliders-in-black/203865402-2",</span></div><div><span style="color:<br>#ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "images.asos-media.com/products/columbia-thrive-revive-sliders-in-black/203865402-3",</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; "images.asos-media.com/products/columbia-thrive-revive-sliders-in-black/203865402-4"</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;],</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp;"videoUrl":null,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"showVideo":false,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"isSellingFast":false,</span></div><div><span<br>style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"sponsoredCampaignId":null,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"facetGroupings":[</span></div><br><div><span style="color:<br>#ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;],</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"advertisement":null</span></div><div><span style="color: #ce9178;">&nbsp;<br>&nbsp; &nbsp; }</span></div><div><br></div><div><div style="color: #cccccc;background-color: #1f1f1f;font-family: Consolas, 'Courier New', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space:<br>pre;"><div><span style="color: #cccccc;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span style="color: #9cdcfe;">po</span><span style="color: #cccccc;"><br></span><span style="color: #d4d4d4;">=</span><span style="color: #cccccc;"> </span><span style="color: #4ec9b0;">DictToObject</span><span style="color: #cccccc;">(</span><span style="color: #9cdcfe;">product</span><span style="color:<br>#cccccc;">)</span></div><div><span style="color: #cccccc;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span style="color: #9cdcfe;">record</span><span style="color: #cccccc;"><br></span><span style="color: #d4d4d4;">=</span><span style="color: #cccccc;"> {</span></div><div><span style="color: #cccccc;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br></span><span style="color: #ce9178;">"name"</span><span style="color: #cccccc;">: </span><span style="color: #9cdcfe;">po</span><span style="color: #cccccc;">.name,</span></div><div><span style="color: #cccccc;">&nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; </span><span style="color: #ce9178;">"description"</span><span style="color: #cccccc;">: </span><span style="color: #569cd6;">f</span><span style="color:<br>#ce9178;">"Brand Name: </span><span style="color: #569cd6;">{</span><span style="color: #9cdcfe;">po</span><span style="color: #cccccc;">.brandName</span><span style="color: #569cd6;">}</span><span style="color: #ce9178;">,<br>Color: </span><span style="color: #569cd6;">{</span><span style="color: #9cdcfe;">po</span><span style="color: #cccccc;">.colour</span><span style="color: #569cd6;">}</span><span style="color: #ce9178;">"</span><span style="color:<br>#cccccc;">,</span></div><div><span style="color: #cccccc;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span style="color: #ce9178;">"category"</span><span style="color: #cccccc;">:<br></span><span style="color: #9cdcfe;">results</span><span style="color: #cccccc;">[</span><span style="color: #ce9178;">"categoryName"</span><span style="color: #cccccc;">],</span></div><div><span style="color: #cccccc;">&nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; </span><span style="color: #ce9178;">"stock"</span><span style="color: #cccccc;">: </span><span style="color: #b5cea8;">1</span><span style="color: #cccccc;">,</span></div><div><span<br>style="color: #cccccc;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span style="color: #ce9178;">"unit_price"</span><span style="color: #cccccc;">: </span><span<br>style="color: #9cdcfe;">product</span><span style="color: #cccccc;">[</span><span style="color: #ce9178;">"price"</span><span style="color: #cccccc;">][</span><span style="color: #ce9178;">"current"</span><span style="color: #cccccc;">][</span><span style="color:<br>#ce9178;">"value"</span><span style="color: #cccccc;">],</span></div><div><span style="color: #cccccc;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span style="color: #ce9178;">"visibility"</span><span<br>style="color: #cccccc;">: </span><span style="color: #b5cea8;">1</span><span style="color: #cccccc;">,</span></div><div><span style="color: #cccccc;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; </span><span style="color: #ce9178;">"image"</span><span style="color: #cccccc;">: </span><span style="color: #569cd6;">f</span><span style="color: #ce9178;">"https://</span><span style="color: #569cd6;">{</span><span<br>style="color: #9cdcfe;">po</span><span style="color: #cccccc;">.imageUrl</span><span style="color: #569cd6;">}</span><span style="color: #ce9178;">"</span><span style="color: #cccccc;">,</span></div><div><span style="color: #cccccc;">&nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; </span><span style="color: #ce9178;">"product_url"</span><span style="color: #cccccc;">: </span><span style="color: #569cd6;">f</span><span style="color:<br>#ce9178;">"https://www.asos.com/us/</span><span style="color: #569cd6;">{</span><span style="color: #9cdcfe;">po</span><span style="color: #cccccc;">.url</span><span style="color: #569cd6;">}</span><span style="color: #ce9178;">"</span><span style="color: #cccccc;">,</span></div><div><span<br>style="color: #cccccc;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span style="color: #ce9178;">"source"</span><span style="color: #cccccc;">: </span><span<br>style="color: #ce9178;">"api"</span></div><div><span style="color: #cccccc;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}<br><br>As we can see, I am<br>making use of name, brandName, colour, categoryName, value, visibility, imageURL, and URL fields<br>from the json body and adding that to the records.<br></span></div></div></div><div><span style="color: #ce9178;"><br></span></div></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> How will you use the mapped data?</td></tr>
<tr><td> <em>Response:</em> <p>These pieces of data will be stored in the database and used for<br>different purposes, like the name for displaying the name, description for the description,<br>category for filtering, price for doing the math, image to add an image<br>preview, product URL to redirect users to the real asos website if they<br>want to, and source for nothing that the source of this data element<br>is api (or manual).<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Create Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the create page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T02.59.32image.png.webp?alt=media&token=5185810a-c56b-4113-849c-43578fba3767"/></td></tr>
<tr><td> <em>Caption:</em> <p>stock cannot be negative<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.00.04image.png.webp?alt=media&token=bdc0dc09-f2fc-4dc0-8595-7210711e4a8e"/></td></tr>
<tr><td> <em>Caption:</em> <p>unit price cannot be negative<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.00.32image.png.webp?alt=media&token=a40cd997-0a81-45f9-9da9-3831fdf7ec3f"/></td></tr>
<tr><td> <em>Caption:</em> <p>successfully added item<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.01.00image.png.webp?alt=media&token=f9f207b2-9e1c-49d2-83e3-7e60d202f992"/></td></tr>
<tr><td> <em>Caption:</em> <p>Duplicate item insertion attempt: TestProduct<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.02.12image.png.webp?alt=media&token=d1135e84-b1cf-4dc7-8eef-ae040e3c8b76"/></td></tr>
<tr><td> <em>Caption:</em> <p>Backend code handling this<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.02.56image.png.webp?alt=media&token=eeb91375-5310-4c97-8cd7-8087d17a8e9a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Frontend HTML code for the page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show the new data in the database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.05.10image.png.webp?alt=media&token=e76d4c80-ddfc-4464-8ebb-fbec22597a74"/></td></tr>
<tr><td> <em>Caption:</em> <p>TestProduct has been added towards the end.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601-dg574-2023/pull/10">https://github.com/dslisanoob/is601-dg574-2023/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page that lists the application entities (both API and custom)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.48.53image.png.webp?alt=media&token=e95646c5-d8f9-4518-9ac9-4b88fd723e31"/></td></tr>
<tr><td> <em>Caption:</em> <p>The homepage contains all the entities regardless of whether its manual or api.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.50.08image.png.webp?alt=media&token=fe8425ad-ec4d-4c86-b5fb-b2988b045aaf"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sorting using name - converse<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.51.51image.png.webp?alt=media&token=c4970bb3-7fd3-491c-a293-7f76f5f04da7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Limit of 100 imposed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.52.50image.png.webp?alt=media&token=ca3b2ce5-956d-4060-834f-47b2f1925df5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Blank, in case there&#39;s no data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T04.03.11image.png.webp?alt=media&token=a9f88f93-2817-4410-b199-860c1af99cc5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Also listed in /admin/items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601-dg574-2023/pull/10">https://github.com/dslisanoob/is601-dg574-2023/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> View Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page showing a single entity with more details shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.58.22image.png.webp?alt=media&token=961e7b68-7aeb-488e-ab7f-b28cbd62b383"/></td></tr>
<tr><td> <em>Caption:</em> <p>more details<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601-dg574-2023/pull/10">https://github.com/dslisanoob/is601-dg574-2023/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page to edit a single entity</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T04.03.43image.png.webp?alt=media&token=9cf0ad5d-568e-41cf-97e0-5085e1bb84a7"/></td></tr>
<tr><td> <em>Caption:</em> <p>it does not return invalid id unfortunately upon entering an invalid id. but<br>it doesnt let you save a product with invalid id.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T04.04.28image.png.webp?alt=media&token=a4b45279-4859-4232-afde-3cf0fb945c50"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit was successful<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T04.05.21image.png.webp?alt=media&token=8ffc8b8b-42ea-483e-8212-e4568254aaeb"/></td></tr>
<tr><td> <em>Caption:</em> <p>price changed from 79.9 to 85 for id=59<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T04.05.37image.png.webp?alt=media&token=63a9fe56-80d1-4965-bae8-b73d42d9580f"/></td></tr>
<tr><td> <em>Caption:</em> <p>price changed from 79.9 to 85 for id=59<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601-dg574-2023/pull/10">https://github.com/dslisanoob/is601-dg574-2023/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a route for deletion logic</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.57.45image.png.webp?alt=media&token=06f95a53-dfb1-4d95-ab73-ac3f978f17cc"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete using id<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T04.06.33image.png.webp?alt=media&token=dc7be081-4862-42ec-a087-56eb31f6b734"/></td></tr>
<tr><td> <em>Caption:</em> <p>deleted 59<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T04.06.56image.png.webp?alt=media&token=5261c033-5ebe-4021-a019-8c0d2805f01c"/></td></tr>
<tr><td> <em>Caption:</em> <p>59 is gone<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601-dg574-2023/pull/10">https://github.com/dslisanoob/is601-dg574-2023/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> API Data Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show information related to API data loading</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.54.57image.png.webp?alt=media&token=c310e4b5-5778-478a-9379-bf7b2a6f6efa"/></td></tr>
<tr><td> <em>Caption:</em> <p>The data is fetched over here, converted to json object for easier access.<br>The data is called on demand using /fetch endpoint. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T03.56.30image.png.webp?alt=media&token=758bebb4-5695-4891-927e-755b444f0f02"/></td></tr>
<tr><td> <em>Caption:</em> <p>/admin/items/fetch endpoint which calls the API.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe the process</td></tr>
<tr><td> <em>Response:</em> <p>Go to Products -&gt; Fetch products. ONLY admins are able to fetch products,<br>since they are the ones who take care of the store. Users can<br>only visit the items, add them to cart, or buy them.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dslisanoob/is601-dg574-2023/pull/10">https://github.com/dslisanoob/is601-dg574-2023/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Nothing really, this was quite challenging and a LOT fun.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://dg574-is601-prod-f8b1dbc00119.herokuapp.com/">https://dg574-is601-prod-f8b1dbc00119.herokuapp.com/</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Include Screenshots from Wakatime</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdg574%2F2023-12-15T04.01.02image.png.webp?alt=media&token=ed57c0de-f398-4095-b083-025c5d7f96bc"/></td></tr>
<tr><td> <em>Caption:</em> <p>I worked even more on my other repo<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/dg574" target="_blank">Grading</a></td></tr></table>