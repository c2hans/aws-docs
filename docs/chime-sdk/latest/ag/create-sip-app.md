---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/create-sip-app.html
---

# Creating a SIP media application
<a name="create-sip-app"></a>

You create a SIP media application when you need to enable calling to and from a Request URI hostname, Amazon Chime SDK Voice Connector group, or a private phone number.

**To create a SIP media application**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In navigation pane, under **PSTN Audio**, choose **SIP media applications**, and on the page that appears, choose **Create SIP media application**.

1. Under **Name**, enter a name for your application.

1. Copy one of the following values and paste it into the **ARN** box:
   + The ARN of a Lambda function
   + The ARN of the *alias* of a Lambda function
   + The ARN of a *version* of a Lambda function
**Note**
You can create alias and version ARNs when you build a Lambda function, and you must have an alias or version ARN if you want to enable Lambda concurrency. For more information about Lambda function aliases, version aliases, and concurrency, refer to [Lambda function aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html), [Lambda function versions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html), and [Managing Lambda provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) in the *AWS Lambda Developer Guide*.

1. (Optional) Under **Tags**, choose **Add new tag**, and then do the following:

   1. Enter a value in the **Key** box.

   1. (Optional) Enter a value in the **Value** box.

   1. As needed, choose **Add new tag** to add more tags.

1. Choose **Create SIP media applicaton.**.

   A success message appears at the top of the **Create a SIP media application** page, and your media application appears in the list of applications. If you see an error message, follow its instructions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
