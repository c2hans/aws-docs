---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/integrating-handlebars-templates.html
---

# Integrating Handlebars templates
<a name="integrating-handlebars-templates"></a>

This guidance supports the [Handlebars](https://handlebarsjs.com/) simple templating language in your answers (including in the markdown and SSML fields) which allows you to include variable substitution and conditional elements. Use the following procedure to integrate Handlebars.

1. From the content designer, choose **Add**.

   1. Enter ID: `Handlebars.001`

   1. Enter question: `What is my interaction count?`

   1. Enter answer: `So far, you have interacted with me {{UserInfo.InteractionCount}} times.`

1. Save the new item.

1. Use the web UI, or any Alexa device to say, ` "What is my interaction count?" ` to your chatbot, and listen to it respond.

1. Ask a few more questions, and then ask ` "What is my interaction count?" ` again. Notice that the value has increased.

1. From the content designer, edit item `Handlebars.001`

1. Modify the answer to:

   ```
   So far, you have interacted with me {{UserInfo.InteractionCount}} times.
   {{#ifCond UserInfo.TimeSinceLastInteraction '>' 60}}
   It's over a minute since I heard from you last.. I almost fell asleep!
   {{else}}
   Keep those questions coming fast.. It's been {{UserInfo.TimeSinceLastInteraction}} seconds since your last interaction.
   {{/ifCond}}
   ```

1. Use the web UI, or Alexa, to interact with the chatbot again. Wait over a minute between interactions and observe the conditional answer in action.

There’s a lot more that you can do with Handlebars, such as randomly selecting content from a list, setting and accessing session attributes, and generating Amazon S3 presigned URLs. For more information see the [Handlebars](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/docs/handlebars/README.md) section in the GitHub repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
