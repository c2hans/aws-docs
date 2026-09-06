---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteUsageLimit.html
---

# DeleteUsageLimit
<a name="API_DeleteUsageLimit"></a>

Deletes a usage limit from a cluster.

## Request Parameters
<a name="API_DeleteUsageLimit_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** UsageLimitId **
The identifier of the usage limit to delete.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: Yes

## Errors
<a name="API_DeleteUsageLimit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** UnsupportedOperation **
The requested operation isn't supported.
HTTP Status Code: 400

 ** UsageLimitNotFound **
The usage limit identifier can't be found.
HTTP Status Code: 404

## See Also
<a name="API_DeleteUsageLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteUsageLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteUsageLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteUsageLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteUsageLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteUsageLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteUsageLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteUsageLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteUsageLimit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteUsageLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteUsageLimit)
