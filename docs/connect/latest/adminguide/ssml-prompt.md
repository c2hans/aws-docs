---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/ssml-prompt.html
---

# Use SSML tags to personalize text-to-speech in Amazon Polly
<a name="ssml-prompt"></a>

When you add a prompt to a flow, you can use SSML tags to provide a more personalized experience for your customers. SSML tags are a way to control how Amazon Polly generates speech from the text you provide.

The default setting in a flow block for interpreting text-to-speech is **Text**. To use SSML for text to speech in your flow blocks, set the **Interpret as** field to **SSML** as shown in the following image.

![The settings for a flow block showing the Text to speech Interpret as field set to SSML.](http://docs.aws.amazon.com/connect/latest/adminguide/images/connect-interpret-as-ssml.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
