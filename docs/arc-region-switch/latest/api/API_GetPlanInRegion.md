---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanInRegion.html
---

# GetPlanInRegion
<a name="API_GetPlanInRegion"></a>

Retrieves information about a Region switch plan in a specific AWS Region. This operation is useful for getting Region-specific information about a plan.

## Request Parameters
<a name="API_GetPlanInRegion_RequestParameters"></a>

 ** arn **
The Amazon Resource Name (ARN) of the plan in Region.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

## Response Elements
<a name="API_GetPlanInRegion_ResponseElements"></a>

The following element is returned by the service.

 ** plan **
The details of the Region switch plan.
Type: [Plan](API_Plan.md) object

## Errors
<a name="API_GetPlanInRegion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404
HTTP Status Code: 404

## See Also
<a name="API_GetPlanInRegion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/GetPlanInRegion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/GetPlanInRegion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/GetPlanInRegion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/GetPlanInRegion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/GetPlanInRegion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/GetPlanInRegion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/GetPlanInRegion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/GetPlanInRegion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/GetPlanInRegion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/GetPlanInRegion)
