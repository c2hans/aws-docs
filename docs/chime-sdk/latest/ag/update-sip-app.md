---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/update-sip-app.html
---

# Updating a SIP media application
<a name="update-sip-app"></a>

You can update the name and Amazon Resource Names (ARNs) of your Lambda function for your SIP media applications. You can't update the AWS Region.

**To update a SIP media application**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, choose **SIP media applications**.

   The **SIP media application** page appears.

1. Choose the name of the application that you want to update.

   The application appears on its own page.

1. Choose **Edit**.

1. As needed, change the following:
   + The application's name
   + The Lambda ARN, alias ARN, or version ARN
   + The tags. For more information about changing tags, see
**Note**
You can create alias and version ARNs when you build a Lambda function, and you must have an alias or version ARN if you want to enable Lambda concurrency. For more information about Lambda function aliases, version aliases, and concurrency, refer to [Lambda function aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html), [Lambda function versions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html), and [Managing Lambda provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) in the *AWS Lambda Developer Guide*.

1. Choose **Save**.

   A success message appears. If you see an error message, follow its instructions.
