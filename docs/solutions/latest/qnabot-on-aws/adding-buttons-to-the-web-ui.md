---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/adding-buttons-to-the-web-ui.html
---

# Adding buttons to the web UI
<a name="adding-buttons-to-the-web-ui"></a>

You can add buttons to your chatbot’s answers to help guide your end user by suggesting what they might want to do next.

1. From the content designer, edit item `Alexa.001` (` "What is an Amazon Echo Show?" `)

1. From the **Advanced** section, under **Response** card, enter a card title.

1. Under **Lex Buttons** enter the following:

   1. Display text: `AWS-QnABot`

   1. Button value: `What is Q and A bot?`

1. Select **ADD LEX BUTTON** to add another button.

   1. Display text: `FireTV`

   1. Button value: `What is Amazon Fire TV?`

1. Select **UPDATE** to save the item with your new buttons.

1. Use the web UI to ask: *"What is an Echo Show?"*

    **Choose a button to send the next question.**
![image16](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image16.jpeg)

1. Choose one of the buttons to automatically send the next question to QnABot on AWS.
**Note**
When integrating with Connect, QnABot on AWS maps to the Connect [List Picker](https://docs.aws.amazon.com/connect/latest/adminguide/interactive-messages.html#list-picker) Template. The client sets limits on the number of characters in a field and enforces formatting using text from the QnABot on AWS plaintext response. You might need to modify the QnABot on AWS plaintext response to accommodate these limitations with the Connect chat client.
