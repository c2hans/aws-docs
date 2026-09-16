---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_GetInstanceOnboardingJobStatus.html
---

# GetInstanceOnboardingJobStatus
<a name="API_connect-outbound-campaigns_GetInstanceOnboardingJobStatus"></a>

Gets the status of the workflow to onboard to outbound campaigns.

**Note**
The `GetInstanceOnboardingJobStatus` API may return a 404 response in the following cases:
The requested resource does not exist.
If the instance was onboarded more than 14 days ago, this API will return a 404 response as expected. In such cases, you should call the [GetConnectInstanceConfig](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_GetConnectInstanceConfig.html) API to retrieve the instance details.

## Request Syntax
<a name="API_connect-outbound-campaigns_GetInstanceOnboardingJobStatus_RequestSyntax"></a>

```
GET /connect-instance/{{connectInstanceId}}/onboarding HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns_GetInstanceOnboardingJobStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectInstanceId](#API_connect-outbound-campaigns_GetInstanceOnboardingJobStatus_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_GetInstanceOnboardingJobStatus-request-uri-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns_GetInstanceOnboardingJobStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-outbound-campaigns_GetInstanceOnboardingJobStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectInstanceOnboardingJobStatus": {
      "connectInstanceId": "string",
      "failureCode": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_connect-outbound-campaigns_GetInstanceOnboardingJobStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectInstanceOnboardingJobStatus](#API_connect-outbound-campaigns_GetInstanceOnboardingJobStatus_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_GetInstanceOnboardingJobStatus-response-connectInstanceOnboardingJobStatus"></a>
The status of the onboarding workflow.
Type: [InstanceOnboardingJobStatus](API_connect-outbound-campaigns_InstanceOnboardingJobStatus.md) object

## Errors
<a name="API_connect-outbound-campaigns_GetInstanceOnboardingJobStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the outbound campaigns.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWSservice.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns_GetInstanceOnboardingJobStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaigns-2021-01-30/GetInstanceOnboardingJobStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaigns-2021-01-30/GetInstanceOnboardingJobStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/GetInstanceOnboardingJobStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaigns-2021-01-30/GetInstanceOnboardingJobStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/GetInstanceOnboardingJobStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaigns-2021-01-30/GetInstanceOnboardingJobStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaigns-2021-01-30/GetInstanceOnboardingJobStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaigns-2021-01-30/GetInstanceOnboardingJobStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcampaigns-2021-01-30/GetInstanceOnboardingJobStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/GetInstanceOnboardingJobStatus)
