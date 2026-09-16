---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRule.html
---

# CreateReceiptRule
<a name="API_CreateReceiptRule"></a>

Creates a receipt rule.

For information about setting up receipt rules, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_CreateReceiptRule_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** After **
The name of an existing rule after which the new rule is placed. If this parameter is null, the new rule is inserted at the beginning of the rule list.
Type: String
Required: No

 ** Rule **
A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.
Type: [ReceiptRule](API_ReceiptRule.md) object
Required: Yes

 ** RuleSetName **
The name of the rule set where the receipt rule is added.
Type: String
Required: Yes

## Errors
<a name="API_CreateReceiptRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExists **
Indicates that a resource could not be created because of a naming conflict.
 ** Name **
Indicates that a resource could not be created because the resource name already exists.
HTTP Status Code: 400

 ** InvalidLambdaFunction **
Indicates that the provided AWS Lambda function is invalid, or that Amazon SES could not execute the provided function, possibly due to permissions issues. For information about giving permissions, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html).
 ** FunctionArn **
Indicates that the ARN of the function was not found.
HTTP Status Code: 400

 ** InvalidS3Configuration **
Indicates that the provided Amazon S3 bucket or AWS KMS encryption key is invalid, or that Amazon SES could not publish to the bucket, possibly due to permissions issues. For information about giving permissions, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html).
 ** Bucket **
Indicated that the S3 Bucket was not found.
HTTP Status Code: 400

 ** InvalidSnsTopic **
Indicates that the provided Amazon SNS topic is invalid, or that Amazon SES could not publish to the topic, possibly due to permissions issues. For information about giving permissions, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html).
 ** Topic **
Indicates that the topic does not exist.
HTTP Status Code: 400

 ** LimitExceeded **
Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html).
HTTP Status Code: 400

 ** RuleDoesNotExist **
Indicates that the provided receipt rule does not exist.
 ** Name **
Indicates that the named receipt rule does not exist.
HTTP Status Code: 400

 ** RuleSetDoesNotExist **
Indicates that the provided receipt rule set does not exist.
 ** Name **
Indicates that the named receipt rule set does not exist.
HTTP Status Code: 400

## See Also
<a name="API_CreateReceiptRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/CreateReceiptRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/CreateReceiptRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/CreateReceiptRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/CreateReceiptRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/CreateReceiptRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/CreateReceiptRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/CreateReceiptRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/CreateReceiptRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/CreateReceiptRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/CreateReceiptRule)
