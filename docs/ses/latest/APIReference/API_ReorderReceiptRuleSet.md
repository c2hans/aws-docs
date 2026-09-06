---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ReorderReceiptRuleSet.html
---

# ReorderReceiptRuleSet
<a name="API_ReorderReceiptRuleSet"></a>

Reorders the receipt rules within a receipt rule set.

**Note**
All of the rules in the rule set must be represented in this request. That is, it is error if the reorder request doesn't explicitly position all of the rules.

For information about managing receipt rule sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_ReorderReceiptRuleSet_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **RuleNames.member.N**
The specified receipt rule set's receipt rules, in order.
Type: Array of strings
Required: Yes

 ** RuleSetName **
The name of the receipt rule set to reorder.
Type: String
Required: Yes

## Errors
<a name="API_ReorderReceiptRuleSet_Errors"></a>

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
<a name="API_ReorderReceiptRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/ReorderReceiptRuleSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/ReorderReceiptRuleSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ReorderReceiptRuleSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/ReorderReceiptRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ReorderReceiptRuleSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/ReorderReceiptRuleSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/ReorderReceiptRuleSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/ReorderReceiptRuleSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/ReorderReceiptRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ReorderReceiptRuleSet)
