---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeActiveReceiptRuleSet.html
---

# DescribeActiveReceiptRuleSet
<a name="API_DescribeActiveReceiptRuleSet"></a>

Returns the metadata and receipt rules for the receipt rule set that is currently active.

For information about setting up receipt rule sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html#receiving-email-concepts-rules).

You can execute this operation no more than once per second.

## Response Elements
<a name="API_DescribeActiveReceiptRuleSet_ResponseElements"></a>

The following elements are returned by the service.

 ** Metadata **
The metadata for the currently active receipt rule set. The metadata consists of the rule set name and a timestamp of when the rule set was created.
Type: [ReceiptRuleSetMetadata](API_ReceiptRuleSetMetadata.md) object

 **Rules.member.N**
The receipt rules that belong to the active rule set.
Type: Array of [ReceiptRule](API_ReceiptRule.md) objects

## Errors
<a name="API_DescribeActiveReceiptRuleSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeActiveReceiptRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/DescribeActiveReceiptRuleSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/DescribeActiveReceiptRuleSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/DescribeActiveReceiptRuleSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/DescribeActiveReceiptRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/DescribeActiveReceiptRuleSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/DescribeActiveReceiptRuleSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/DescribeActiveReceiptRuleSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/DescribeActiveReceiptRuleSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/DescribeActiveReceiptRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/DescribeActiveReceiptRuleSet)
