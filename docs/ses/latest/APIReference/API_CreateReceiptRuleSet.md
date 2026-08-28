---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRuleSet.html
---

# CreateReceiptRuleSet
<a name="API_CreateReceiptRuleSet"></a>

Creates an empty receipt rule set.

For information about setting up receipt rule sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html#receiving-email-concepts-rules).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_CreateReceiptRuleSet_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** RuleSetName **
The name of the rule set to create. The name must meet the following requirements:
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), or dashes (-).
+ Start and end with a letter or number.
+ Contain 64 characters or fewer.
Type: String
Required: Yes

## Errors
<a name="API_CreateReceiptRuleSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExists **
Indicates that a resource could not be created because of a naming conflict.
 ** Name **
Indicates that a resource could not be created because the resource name already exists.
HTTP Status Code: 400

 ** LimitExceeded **
Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html).
HTTP Status Code: 400

## See Also
<a name="API_CreateReceiptRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/CreateReceiptRuleSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/CreateReceiptRuleSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/CreateReceiptRuleSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/CreateReceiptRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/CreateReceiptRuleSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/CreateReceiptRuleSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/CreateReceiptRuleSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/CreateReceiptRuleSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/CreateReceiptRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/CreateReceiptRuleSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
