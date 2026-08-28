---
source_url: https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_StartInstanceOnboardingJob.html
---

# StartInstanceOnboardingJob
<a name="API_connect-outbound-campaigns_StartInstanceOnboardingJob"></a>

Starts the workflow to onboard an Connect Customer instance to outbound campaigns.

**Note**
If the current [InstanceOnboardingJobStatus](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_InstanceOnboardingJobStatus.html) is **FAILED**, the `StartInstanceOnboardingJob` API will continue to return the existing status for 14 days from the initial attempt. To reattempt onboarding, first call the [DeleteInstanceOnboardingJob](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_DeleteInstanceOnboardingJob.html) API, then invoke the `StartInstanceOnboardingJob` API again.

## Request Syntax
<a name="API_connect-outbound-campaigns_StartInstanceOnboardingJob_RequestSyntax"></a>

```
PUT /connect-instance/{{connectInstanceId}}/onboarding HTTP/1.1
Content-type: application/json

{
   "encryptionConfig": {
      "enabled": {{boolean}},
      "encryptionType": "{{string}}",
      "keyArn": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns_StartInstanceOnboardingJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectInstanceId](#API_connect-outbound-campaigns_StartInstanceOnboardingJob_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_StartInstanceOnboardingJob-request-uri-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns_StartInstanceOnboardingJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [encryptionConfig](#API_connect-outbound-campaigns_StartInstanceOnboardingJob_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_StartInstanceOnboardingJob-request-encryptionConfig"></a>
Encryption configuration for an Connect Customer instance.
Type: [EncryptionConfig](API_connect-outbound-campaigns_EncryptionConfig.md) object
Required: Yes

## Response Syntax
<a name="API_connect-outbound-campaigns_StartInstanceOnboardingJob_ResponseSyntax"></a>

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
<a name="API_connect-outbound-campaigns_StartInstanceOnboardingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectInstanceOnboardingJobStatus](#API_connect-outbound-campaigns_StartInstanceOnboardingJob_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_StartInstanceOnboardingJob-response-connectInstanceOnboardingJobStatus"></a>
The status of the onboarding workflow.
Type: [InstanceOnboardingJobStatus](API_connect-outbound-campaigns_InstanceOnboardingJobStatus.md) object

## Errors
<a name="API_connect-outbound-campaigns_StartInstanceOnboardingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
This exception occurs when there is an internal failure in the outbound campaigns.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWSservice.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns_StartInstanceOnboardingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaigns-2021-01-30/StartInstanceOnboardingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaigns-2021-01-30/StartInstanceOnboardingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/StartInstanceOnboardingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaigns-2021-01-30/StartInstanceOnboardingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/StartInstanceOnboardingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaigns-2021-01-30/StartInstanceOnboardingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaigns-2021-01-30/StartInstanceOnboardingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaigns-2021-01-30/StartInstanceOnboardingJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaigns-2021-01-30/StartInstanceOnboardingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/StartInstanceOnboardingJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
