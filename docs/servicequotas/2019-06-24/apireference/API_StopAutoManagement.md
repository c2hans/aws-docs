---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_StopAutoManagement.html
---

# StopAutoManagement
<a name="API_StopAutoManagement"></a>

Stops [Service Quotas Automatic Management](https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management.html) for an AWS account and removes all associated configurations. Automatic Management monitors your Service Quotas utilization and notifies you before you run out of your allocated quotas.

## Response Elements
<a name="API_StopAutoManagement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopAutoManagement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** IllegalArgumentException **
Invalid input was provided.
HTTP Status Code: 400

 ** NoSuchResourceException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceException **
Something went wrong.
HTTP Status Code: 500

 ** TooManyRequestsException **
Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.
HTTP Status Code: 400

## See Also
<a name="API_StopAutoManagement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/service-quotas-2019-06-24/StopAutoManagement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/service-quotas-2019-06-24/StopAutoManagement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/StopAutoManagement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/service-quotas-2019-06-24/StopAutoManagement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/StopAutoManagement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/service-quotas-2019-06-24/StopAutoManagement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/service-quotas-2019-06-24/StopAutoManagement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/service-quotas-2019-06-24/StopAutoManagement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/service-quotas-2019-06-24/StopAutoManagement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/StopAutoManagement)
