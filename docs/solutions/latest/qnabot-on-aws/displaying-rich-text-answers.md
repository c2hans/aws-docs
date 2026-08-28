---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/displaying-rich-text-answers.html
---

# Displaying rich text answers
<a name="displaying-rich-text-answers"></a>

QnABot on AWS supports [Markdown](https://daringfireball.net/projects/markdown/syntax), allowing you to create rich text versions of your answers for displaying on the web user interface, or on Slack. To use this feature, populate the **Alternate Markdown answer** field in the content designer.

1. From the content designer, edit item `AWS-QnABot001` (What is Q and A bot?) by opening the **Advanced** section and entering the following text in the **Markdown Answer** field:

   ```
   # AWS QnABot
   The Q and A Bot uses [Amazon Lex](https://aws.amazon.com/lex) and [Alexa](https://developer.amazon.com/alexa) to provide a natural language interface for your FAQ knowledge base.
   Now your users can just ask a *question* and get a quick and relevant *answer*.
   ```

1. Choose **UPDATE** to save the modification.

1. Use the web user interface to ask: *"What is Q and A bot?"*.

   The answer now displays the heading, links, and emphasis specified in your markdown text.

    **Sample Markdown text**
![image15](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image15.jpeg)

   QnABot on AWS also supports inline HTML in the markdown field:

1. Choose **ADD** to create a new item in HTML:

   1. Enter ID: FireTV.001

   1. Enter question: What is Amazon Fire TV?

   1. Enter answer:

      ```
      Fire TV brings all the live TV and streaming content you love, and Alexa, onto the big screen. Use Alexa on the Fire TV to bring QnABot on AWS into your living room!
      ```

   1. Enter markdown answer:

      ```
       **Fire TV** brings all the live TV and streaming content you love, and Alexa, onto the big screen. Use Alexa on the Fire TV to bring QnABot on AWS into your living room!
      <iframe src="https://www.youtube.com/embed/OE4MrFx2XCs"></iframe>
      ```

1. Choose **CREATE** to save the item.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
