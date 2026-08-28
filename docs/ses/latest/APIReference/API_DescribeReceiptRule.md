---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeReceiptRule.html
---

# DescribeReceiptRule
<a name="API_DescribeReceiptRule"></a>

Returns the details of the specified receipt rule.

For information about setting up receipt rules, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_DescribeReceiptRule_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** RuleName **
The name of the receipt rule.
Type: String
Required: Yes

 ** RuleSetName **
The name of the receipt rule set that the receipt rule belongs to.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeReceiptRule_ResponseElements"></a>

The following element is returned by the service.

 ** Rule **
A data structure that contains the specified receipt rule's name, actions, recipients, domains, enabled status, scan status, and Transport Layer Security (TLS) policy.
Type: [ReceiptRule](API_ReceiptRule.md) object

## Errors
<a name="API_DescribeReceiptRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribeReceiptRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/DescribeReceiptRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/DescribeReceiptRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/DescribeReceiptRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/DescribeReceiptRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/DescribeReceiptRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/DescribeReceiptRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/DescribeReceiptRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/DescribeReceiptRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/DescribeReceiptRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/DescribeReceiptRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
