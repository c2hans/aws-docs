---
source_url: https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_CreateCampaign.html
---

# CreateCampaign
<a name="API_connect-outbound-campaigns_CreateCampaign"></a>

Creates an outbound campaign.

**Note**
For users to be able to view or edit a campaign at a later date by using the Connect Customer user interface, you must add the instance ID as a tag.
After a campaign is saved, you can't change the dialer type for an agentless campaign, and you can't change the dialer type to agentless for progressive and predictive campaigns.

## Request Syntax
<a name="API_connect-outbound-campaigns_CreateCampaign_RequestSyntax"></a>

```
PUT /campaigns HTTP/1.1
Content-type: application/json

{
   "connectInstanceId": "{{string}}",
   "dialerConfig": { ... },
   "name": "{{string}}",
   "outboundCallConfig": {
      "answerMachineDetectionConfig": {
         "awaitAnswerMachinePrompt": {{boolean}},
         "enableAnswerMachineDetection": {{boolean}}
      },
      "connectContactFlowId": "{{string}}",
      "connectQueueId": "{{string}}",
      "connectSourcePhoneNumber": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns_CreateCampaign_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_connect-outbound-campaigns_CreateCampaign_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [connectInstanceId](#API_connect-outbound-campaigns_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_CreateCampaign-request-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

 ** [dialerConfig](#API_connect-outbound-campaigns_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_CreateCampaign-request-dialerConfig"></a>
Dialer configuration for an outbound campaign.
Type: [DialerConfig](API_connect-outbound-campaigns_DialerConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [name](#API_connect-outbound-campaigns_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_CreateCampaign-request-name"></a>
The name of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

 ** [outboundCallConfig](#API_connect-outbound-campaigns_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_CreateCampaign-request-outboundCallConfig"></a>
Outbound call configuration for an outbound campaign.
Type: [OutboundCallConfig](API_connect-outbound-campaigns_OutboundCallConfig.md) object
Required: Yes

 ** [tags](#API_connect-outbound-campaigns_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_CreateCampaign-request-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_connect-outbound-campaigns_CreateCampaign_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-outbound-campaigns_CreateCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_connect-outbound-campaigns_CreateCampaign_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_CreateCampaign-response-arn"></a>
The Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.

 ** [id](#API_connect-outbound-campaigns_CreateCampaign_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_CreateCampaign-response-id"></a>
The identifier of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`

 ** [tags](#API_connect-outbound-campaigns_CreateCampaign_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_CreateCampaign-response-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_connect-outbound-campaigns_CreateCampaign_Errors"></a>

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

 ** ServiceQuotaExceededException **
The service quota for your Connect Customer has been exceeded. Contact Support.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWSservice.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns_CreateCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaigns-2021-01-30/CreateCampaign)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaigns-2021-01-30/CreateCampaign)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/CreateCampaign)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaigns-2021-01-30/CreateCampaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/CreateCampaign)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaigns-2021-01-30/CreateCampaign)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaigns-2021-01-30/CreateCampaign)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaigns-2021-01-30/CreateCampaign)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaigns-2021-01-30/CreateCampaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/CreateCampaign)
