---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ReceiptAction.html
---

# ReceiptAction
<a name="API_ReceiptAction"></a>

An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.

For information about setting up receipt rules, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html).

## Contents
<a name="API_ReceiptAction_Contents"></a>

 ** AddHeaderAction **
Adds a header to the received email.
Type: [AddHeaderAction](API_AddHeaderAction.md) object
Required: No

 ** BounceAction **
Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).
Type: [BounceAction](API_BounceAction.md) object
Required: No

 ** ConnectAction **
Parses the received message and starts an email contact in Amazon Connect on your behalf.
Type: [ConnectAction](API_ConnectAction.md) object
Required: No

 ** LambdaAction **
Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.
Type: [LambdaAction](API_LambdaAction.md) object
Required: No

 ** S3Action **
Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.
Type: [S3Action](API_S3Action.md) object
Required: No

 ** SNSAction **
Publishes the email content within a notification to Amazon SNS.
Type: [SNSAction](API_SNSAction.md) object
Required: No

 ** StopAction **
Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.
Type: [StopAction](API_StopAction.md) object
Required: No

 ** WorkmailAction **
Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.
Type: [WorkmailAction](API_WorkmailAction.md) object
Required: No

## See Also
<a name="API_ReceiptAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ReceiptAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ReceiptAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ReceiptAction)
