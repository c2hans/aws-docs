---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/step-3-populate-the-chatbot-with-your-questions-and-answers.html
---

# Step 3: Populate the chatbot with your questions and answers
<a name="step-3-populate-the-chatbot-with-your-questions-and-answers"></a>

Create or upload question and answer data through the content designer before sharing the QnABot on AWS with your end users. Your data is stored in Amazon OpenSearch Service, which allows the data to be crawled when end users ask questions using either an Amazon Lex client UI or an Amazon Alexa hands-free device.

Use the following procedure to get started with customizing your chatbot using the solution’s sample questions. You can edit the sample questions to customize the data to meet your needs.

1. From the AWS CloudFormation console, launch the content designer user interface by selecting the **ContentDesignerURL** link from the **Outputs** tab of the primary CloudFormation stack.

1. Enter the administrator username you provided when you launched the stack and your new password.

    **QnABot on AWS content designer web user interface — QUESTIONS tab**
![image8](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image8.jpeg)

1. Choose **Add.**

1. Enter the ID: `AWS-QnABot.001 `
**Note**
Use a naming convention to identify your items within categories.

1. Enter the question: `What is Q and A bot?`

1. Enter the answer: `The Q and A Bot uses Amazon Lex and Alexa to provide a natural language interface for your FAQ knowledge base, so your users can just ask a question and get a quick and relevant answer. `

1. Select **CREATE**.

1. Repeat steps 3-7, entering the items from the following table (**Table 1: Sample Q and A data**).

   Alternatively, you can import the items directly from a file. Select **Import from the top left tools menu ( ☰ )**, then choose **Examples/Extensions**, find the package called **blog-samples**, and choose **LOAD.**
**Note**
We recommend that you always import the **QnaUtility** example of questions set because it enables support of `no_hits`, `no_verified_identity`, `help`, `repeat`, and thumbs up and down feedback.

1. When the import is complete, choose **Edit** from the top left tools menu ( **☰** ), and then choose **LEX REBUILD** from the top right edit card menu ( ⋮ ).

## Table 1: Sample Q and A data
<a name="sample-data-table"></a>

| Id | Question | Answer |
| --- | --- | --- |
|  `AWS-QnABot.002`  | How do I use Q and A Bot? | Create and administer your questions and answers using the **QnABot** content designer UI. End users ask questions using the Amazon Lex web UI that supports voice or chat, or using Alexa devices for hands free voice interaction. |
|  `Admin.001`  | How do I modify Q and A Bot content? | Use the content designer Question and Test tools to find your existing documents and edit them directly in the console. You can also export existing documents as a JSON file, make changes to the file, and re-import. |
|  `Admin.002`  | Can I back up Q and A Bot content? | Yes. Use the content designer to export your content as a JSON file. Maintain this file in your version control system or in an S3 bucket. Use the content designer UI import feature to restore content from the JSON file. |
|  `Admin.003`  | Can I import Q and A Bot content from a file? | Yes, the content designer has an import function that lets you load items from a formatted JSON file. You can create JSON files using the export feature, or you can write your own tools to create JSON files from existing content such as a website FAQ page. |
|  `Admin.004`  | How do I troubleshoot and fix problems with Q and A Bot? | Use the content designer test tool to test a question, and check what items are returned, ranked in order of score. If the desired item does not have the highest score, then add the question to the item and run the test again. The desired item should now have the highest score. Ensure that you aren’t creating items with duplicate questions to avoid unpredictable responses. |
|  `Admin.005`  | How can I find specific Q and A items in the Designer UI? | Use the filter feature in the **Questions** tab to filter the items list based on the ID field. Or use the **Test** tab to list all the items that match a question. |
|  `Media.001`  | How can I include pictures in Q and A Bot answers? | Add an image attachment to the item using the content designer. |
