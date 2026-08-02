---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlansInRegion.html
---

# ListPlansInRegion
<a name="API_ListPlansInRegion"></a>

Lists all Region switch plans in your AWS account that are available in the current AWS Region.

## Request Parameters
<a name="API_ListPlansInRegion_RequestParameters"></a>

 ** maxResults **
The number of objects that you want to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Elements
<a name="API_ListPlansInRegion_ResponseElements"></a>

The following elements are returned by the service.

 ** nextToken **
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** plans **
The plans that were requested.
Type: Array of [AbbreviatedPlan](API_AbbreviatedPlan.md) objects

## Errors
<a name="API_ListPlansInRegion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403
HTTP Status Code: 403

## See Also
<a name="API_ListPlansInRegion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/ListPlansInRegion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/ListPlansInRegion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ListPlansInRegion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/ListPlansInRegion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ListPlansInRegion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/ListPlansInRegion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/ListPlansInRegion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/ListPlansInRegion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/ListPlansInRegion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ListPlansInRegion)
