---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/adding-images-to-your-answers.html
---

# Adding images to your answers
<a name="adding-images-to-your-answers"></a>

You can augment your answers with image attachments that can be displayed on an end user’s Amazon Lex web client user interface, Alexa smartphone app, or Amazon Echo Show device touch screen. For example, you can use images to display maps, diagrams, or photographs to depict places and products relevant to a question.

1. Sign in to the content designer, and choose **Add**.

1. Enter ID: `Alexa.001`.

1. Enter question: `What is an Amazon Echo Show?`

1. Enter answer: `Echo Show brings you everything you love about Alexa, and now she can show you things. She is the perfect companion for Q and A Bot.`

1. Choose **Advanced.**

1. Under **Response Card**, enter the following:

   1. Card Title: `Echo Show`

   1. Card ImageUrl: [https://images-na.ssl-images-amazon.com/images/I/61OddH8ddDL.*SL1000*.jpg](https://images-na.ssl-images-amazon.com/images/I/61OddH8ddDL._SL1000_.jpg)

1. Choose **CREATE** to save the new item.

1. Use the web UI chat window to ask: ` "What is an Echo Show?" `

   The photograph is displayed in the web UI chat.

    **Example image response in the web UI chat window**
![image14](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image14.jpeg)

1. Optionally, you can use an Amazon Echo or Echo Dot to say: ` "Ask Q and A, What is an Echo Show?" `

   The card shown in the Alexa smartphone app shows the photo attachment.

1. Optionally, you can use an Amazon Echo Show to say: ` "Ask Q and A, What is an Echo Show?" `

   The photo attachment is displayed on the Echo Show’s touch screen.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
