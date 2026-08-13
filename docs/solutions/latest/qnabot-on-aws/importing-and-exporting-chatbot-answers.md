---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/importing-and-exporting-chatbot-answers.html
---

# Importing and exporting chatbot answers
<a name="importing-and-exporting-chatbot-answers"></a>

The guidance’s content designer allows you to export and import your content using JSON and Excel files.

Use the export feature to create backup versions of your content that you can use to restore if you accidentally delete items or need to go back to a previous version. You can also use the exported files to load content into another instance of your chatbot to help with test deployments.

Follow these steps to export all the items that are in the QnABot on AWS category (Item IDs starting with `AWS-QnABot`).

1. Sign in to the content designer, choose the tools menu ( **☰** ), and then choose **Export.**

1. Enter `AWS-QnABot` in the optional filter field, and then choose **EXPORT** to generate a JSON file containing the filtered items.

1. After the export has completed, choose the download tool (bottom right) to download the exported file\*.\*

1. Open the exported file in a text editor and inspect the JSON structure.

   Sample JSON file for importing and exporting chatbot answers:

   ```
   {
     "qna": [
       {
         "q": [
           "What is Q and A Bot"
         ],
         "a": "The Q and A Bot uses Amazon Lex and Alexa to provide a natural language interface for your FAQ knowledge base, so your users can just ask a question and get a quick and relevant answer.",
         "r": {
           "title": "",
           "imageUrl": ""
         },
         "qid": "QnABot.001"
       },
       {
         "q": [
           "How do I use Q and A Bot"
         ],
         "a": "Create and administer your questions and answers using the Q and A Bot Content Designer UI. End users ask questions using the Lex web UI, which supports voice or chat, or using Alexa devices for hands free voice interaction. ",
         "r": {
           "title": "",
           "imageUrl": ""
         },
         "qid": "QnABot.002"
       }
     ]
   }
   ```

1. Add a new item to the `qna` list, as shown in the following example, and save the file.

   ```
   {
           "qid": "AWS-QnABot.003",
           "q": ["What can Q and A bot do"],
           "a": "You can integrate it with your website to provide quick and easy access to frequently asked questions. Use it with Alexa to provide hands free answers in the kitchen, in the factory or in the car. Since it can display images too, use it to provide illustrations and photographs to enrich your answers.",
           "r": {
               "title": "",
               "imageUrl": ""
           }
   }
   ```

1. From the content designer, select **Import/Export**, and then choose **From File**.

1. Import your modified JSON file. Importing items with the same ID as an existing item will overwrite the existing item with the definition contained in the JSON file.

1. From the content designer, enter `AWS-QnABot` in the filter field, and inspect the newly imported item, **AWS-QnABot.003**.

For a step-by-step procedure on importing Excel (`0xlsx`) workbooks, see [Excel workbooks import](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/excel_import) in the GitHub repository.
