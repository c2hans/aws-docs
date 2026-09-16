---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptFilters.html
---

# ListReceiptFilters
<a name="API_ListReceiptFilters"></a>

Lists the IP address filters associated with your AWS account in the current AWS Region.

For information about managing IP address filters, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-ip-filtering-console-walkthrough.html).

You can execute this operation no more than once per second.

## Response Elements
<a name="API_ListReceiptFilters_ResponseElements"></a>

The following element is returned by the service.

 **Filters.member.N**
A list of IP address filter data structures, which each consist of a name, an IP address range, and whether to allow or block mail from it.
Type: Array of [ReceiptFilter](API_ReceiptFilter.md) objects

## Errors
<a name="API_ListReceiptFilters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListReceiptFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/ListReceiptFilters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/ListReceiptFilters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ListReceiptFilters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/ListReceiptFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ListReceiptFilters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/ListReceiptFilters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/ListReceiptFilters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/ListReceiptFilters)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/ListReceiptFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ListReceiptFilters)
