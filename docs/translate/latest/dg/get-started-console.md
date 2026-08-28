---
source_url: https://docs.aws.amazon.com/translate/latest/dg/get-started-console.html
---

# Getting started (console)
<a name="get-started-console"></a>

The easiest way to get started with Amazon Translate is to use the console to translate some text. You can translate up to 10,000 bytes of text using the console. If you haven't reviewed the concepts and terminology in [How Amazon Translate works](how-it-works.md), we recommend that you do so before proceeding.

Open the [Amazon Translate console](https://console.aws.amazon.com/translate/home).

If this is the first time that you've used Amazon Translate, choose **Launch real-time translation**.

In **Real-time translation**, choose the target language. Amazon Translate autodetects the source language, or you can choose a source language. Enter the text that you want to translate in the left-hand text box. The translated text appears in the right-hand text box.

![The translate text page of the Amazon Translate API Explorer.](http://docs.aws.amazon.com/translate/latest/dg/images/gs-10.png)

In the **Application integration** section you can see the JSON input and output for the [TranslateText](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateText.html) operation.

![JSON code samples for translating text.](http://docs.aws.amazon.com/translate/latest/dg/images/gs-20.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
