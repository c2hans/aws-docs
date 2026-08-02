---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/using-topics-to-support-follow-up-questions-and-contextual-user-journeys.html
---

# Using topics to support follow-up questions and contextual user journeys
<a name="using-topics-to-support-follow-up-questions-and-contextual-user-journeys"></a>

The solution remembers the topic from the last question you asked, which allows you to ask follow-up questions, for example: ` "How much does it cost?" ` The correct answer depends on the context set by the previous question. To use this feature, you must assign a value to the **Topic** field in the content designer.

1. From the content designer, edit item `Alexa.001` (*"What is an Amazon Echo Show?"*), and enter `EchoShow` as the topic in the **Advanced section**.

1. Choose **UPDATE** to save the item.

1. Edit item `AWS-QnABot.001` (*"What is Q and A bot?"*), and enter `AWS-QnABot` as the topic.

1. Choose **UPDATE** to save the item.

1. Choose **ADD** to create a new item for our first follow-up question:

   1. Enter ID: `Alexa.Cost`

   1. Enter question: `How much does it cost?`

   1. Enter answer: `For latest prices on the Echo Show, see the Amazon retail site or shopping app.`

   1. Enter topic: `EchoShow`

1. Choose **CREATE** to save the item.

1. Choose **ADD** to create a new item for our next follow-up question. Enter the following values:

   1. Enter ID: `QnABot on AWS.Cost`

   1. Enter question: `How much does it cost?`

   1. Enter answer: `Q and A Bot is priceless`

   1. Enter topic: `QnABot on AWS`

1. Choose **CREATE** to save the item.

1. Use the web UI to ask the following questions and observe the context appropriate answers:

   1.  ` "What is an Echo Show?" `

   1. The answer to this question now sets the conversation topic to: `'EchoShow'`.

   1.  ` "How much does it cost?" `

   1. The topic disambiguates this question, so it responds with the answer for the Echo Show.

   1.  ` "What is the Q and A bot?" `

   1. This question changes the Topic to: `'QnABot on AWS'`.

   1.  ` "How much does it cost?" `

   1. The new topic allows the QnABot on AWS to respond with the correct answer.
