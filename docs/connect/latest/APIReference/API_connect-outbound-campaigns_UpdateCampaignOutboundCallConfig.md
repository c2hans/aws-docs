---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig.html
---

# UpdateCampaignOutboundCallConfig
<a name="API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig"></a>

Updates [OutboundCallConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_OutboundCallConfig.html) for an outbound campaign.

## Request Syntax
<a name="API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig_RequestSyntax"></a>

```
POST /campaigns/{{id}}/outbound-call-config HTTP/1.1
Content-type: application/json

{
   "answerMachineDetectionConfig": {
      "awaitAnswerMachinePrompt": {{boolean}},
      "enableAnswerMachineDetection": {{boolean}}
   },
   "connectContactFlowId": "{{string}}",
   "connectSourcePhoneNumber": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_UpdateCampaignOutboundCallConfig-request-uri-id"></a>
The identifier of the campaign.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [answerMachineDetectionConfig](#API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_UpdateCampaignOutboundCallConfig-request-answerMachineDetectionConfig"></a>
Information about answering machine detection.
Type: [AnswerMachineDetectionConfig](API_connect-outbound-campaigns_AnswerMachineDetectionConfig.md) object
Required: No

 ** [connectContactFlowId](#API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_UpdateCampaignOutboundCallConfig-request-connectContactFlowId"></a>
The identifier of the published flow associated with this campaign.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [connectSourcePhoneNumber](#API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_UpdateCampaignOutboundCallConfig-request-connectSourcePhoneNumber"></a>
The outbound phone number associated with this campaign. Only ported or claimed Connect Customer phone numbers are allowed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

## Response Syntax
<a name="API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig_Errors"></a>

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
<a name="API_connect-outbound-campaigns_UpdateCampaignOutboundCallConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaigns-2021-01-30/UpdateCampaignOutboundCallConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaigns-2021-01-30/UpdateCampaignOutboundCallConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/UpdateCampaignOutboundCallConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaigns-2021-01-30/UpdateCampaignOutboundCallConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/UpdateCampaignOutboundCallConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaigns-2021-01-30/UpdateCampaignOutboundCallConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaigns-2021-01-30/UpdateCampaignOutboundCallConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaigns-2021-01-30/UpdateCampaignOutboundCallConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcampaigns-2021-01-30/UpdateCampaignOutboundCallConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/UpdateCampaignOutboundCallConfig)
