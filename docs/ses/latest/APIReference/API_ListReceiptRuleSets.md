---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptRuleSets.html
---

# ListReceiptRuleSets
<a name="API_ListReceiptRuleSets"></a>

Lists the receipt rule sets that exist under your AWS account in the current AWS Region. If there are additional receipt rule sets to be retrieved, you receive a `NextToken` that you can provide to the next call to `ListReceiptRuleSets` to retrieve the additional entries.

For information about managing receipt rule sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_ListReceiptRuleSets_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** NextToken **
A token returned from a previous call to `ListReceiptRuleSets` to indicate the position in the receipt rule set list.
Type: String
Required: No

## Response Elements
<a name="API_ListReceiptRuleSets_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
A token indicating that there are additional receipt rule sets available to be listed. Pass this token to successive calls of `ListReceiptRuleSets` to retrieve up to 100 receipt rule sets at a time.
Type: String

 **RuleSets.member.N**
The metadata for the currently active receipt rule set. The metadata consists of the rule set name and the timestamp of when the rule set was created.
Type: Array of [ReceiptRuleSetMetadata](API_ReceiptRuleSetMetadata.md) objects

## Errors
<a name="API_ListReceiptRuleSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListReceiptRuleSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/ListReceiptRuleSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/ListReceiptRuleSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ListReceiptRuleSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/ListReceiptRuleSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ListReceiptRuleSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/ListReceiptRuleSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/ListReceiptRuleSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/ListReceiptRuleSets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/ListReceiptRuleSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ListReceiptRuleSets)
