---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_CreateCampaign.html
---

# CreateCampaign
<a name="API_connect-outbound-campaigns-v2_CreateCampaign"></a>

 Creates an outbound campaign.

**Note**
For users to be able to view or edit a campaign at a later date by using the Amazon Connect user interface, you must add the instance ID as a tag. For example, `{ "tags": {"owner": "arn:aws:connect:{REGION}:{AWS_ACCOUNT_ID}:instance/{CONNECT_INSTANCE_ID}"}}`.
After a campaign is created, you can't add/remove source.

## Request Syntax
<a name="API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax"></a>

```
PUT /v2/campaigns HTTP/1.1
Content-type: application/json

{
   "channelSubtypeConfig": {
      "email": {
         "capacity": {{number}},
         "defaultOutboundConfig": {
            "connectSourceEmailAddress": "{{string}}",
            "sourceEmailAddressDisplayName": "{{string}}",
            "wisdomTemplateArn": "{{string}}"
         },
         "outboundMode": { ... }
      },
      "sms": {
         "capacity": {{number}},
         "defaultOutboundConfig": {
            "connectSourcePhoneNumberArn": "{{string}}",
            "wisdomTemplateArn": "{{string}}"
         },
         "outboundMode": { ... }
      },
      "telephony": {
         "capacity": {{number}},
         "connectQueueId": "{{string}}",
         "defaultOutboundConfig": {
            "answerMachineDetectionConfig": {
               "awaitAnswerMachinePrompt": {{boolean}},
               "enableAnswerMachineDetection": {{boolean}}
            },
            "connectContactFlowId": "{{string}}",
            "connectSourcePhoneNumber": "{{string}}",
            "ringTimeout": {{number}}
         },
         "outboundMode": { ... }
      },
      "whatsApp": {
         "capacity": {{number}},
         "defaultOutboundConfig": {
            "connectSourcePhoneNumberArn": "{{string}}",
            "wisdomTemplateArn": "{{string}}"
         },
         "outboundMode": { ... }
      }
   },
   "communicationLimitsOverride": {
      "allChannelSubtypes": { ... },
      "instanceLimitsHandling": "{{string}}"
   },
   "communicationTimeConfig": {
      "email": {
         "openHours": { ... },
         "restrictedPeriods": { ... }
      },
      "localTimeZoneConfig": {
         "defaultTimeZone": "{{string}}",
         "localTimeZoneDetection": [ "{{string}}" ],
         "localTimeZoneDetectionScope": "{{string}}"
      },
      "sms": {
         "openHours": { ... },
         "restrictedPeriods": { ... }
      },
      "telephony": {
         "openHours": { ... },
         "restrictedPeriods": { ... }
      },
      "whatsApp": {
         "openHours": { ... },
         "restrictedPeriods": { ... }
      }
   },
   "connectCampaignFlowArn": "{{string}}",
   "connectInstanceId": "{{string}}",
   "entryLimitsConfig": {
      "maxEntryCount": {{number}},
      "minEntryInterval": "{{string}}"
   },
   "name": "{{string}}",
   "schedule": {
      "endTime": "{{string}}",
      "refreshFrequency": "{{string}}",
      "startTime": "{{string}}"
   },
   "source": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns-v2_CreateCampaign_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_connect-outbound-campaigns-v2_CreateCampaign_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelSubtypeConfig](#API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-request-channelSubtypeConfig"></a>
Channel subtype configuration for an outbound campaign.
Type: [ChannelSubtypeConfig](API_connect-outbound-campaigns-v2_ChannelSubtypeConfig.md) object
Required: No

 ** [communicationLimitsOverride](#API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-request-communicationLimitsOverride"></a>
Communication limits configuration for an outbound campaign.
Type: [CommunicationLimitsConfig](API_connect-outbound-campaigns-v2_CommunicationLimitsConfig.md) object
Required: No

 ** [communicationTimeConfig](#API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-request-communicationTimeConfig"></a>
Communication time configuration for an outbound campaign.
Type: [CommunicationTimeConfig](API_connect-outbound-campaigns-v2_CommunicationTimeConfig.md) object
Required: No

 ** [connectCampaignFlowArn](#API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-request-connectCampaignFlowArn"></a>
The Amazon Resource Name (ARN) of the Connect Customer campaign flow.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.
Pattern: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-z]{2}-[a-z]+-\d{1,2}:[a-zA-Z0-9-]+:[^:]+(?:/[^:]+)*(?:/[^:]+)?(?:\:[^:]+)?`
Required: No

 ** [connectInstanceId](#API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-request-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

 ** [entryLimitsConfig](#API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-request-entryLimitsConfig"></a>
Entry limits configuration for an outbound campaign.
Type: [EntryLimitsConfig](API_connect-outbound-campaigns-v2_EntryLimitsConfig.md) object
Required: No

 ** [name](#API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-request-name"></a>
The name of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

 ** [schedule](#API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-request-schedule"></a>
Schedule configuration for an outbound campaign.
Type: [Schedule](API_connect-outbound-campaigns-v2_Schedule.md) object
Required: No

 ** [source](#API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-request-source"></a>
Source configuration for an outbound campaign.
Type: [Source](API_connect-outbound-campaigns-v2_Source.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [tags](#API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-request-tags"></a>
The tags used to organize, track, or control access for this resource. For example, `{ "tags": {"key1":"value1", "key2":"value2"} }`.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [type](#API_connect-outbound-campaigns-v2_CreateCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-request-type"></a>
The type of campaign.
Type: String
Valid Values: `MANAGED | JOURNEY`
Required: No

## Response Syntax
<a name="API_connect-outbound-campaigns-v2_CreateCampaign_ResponseSyntax"></a>

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
<a name="API_connect-outbound-campaigns-v2_CreateCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_connect-outbound-campaigns-v2_CreateCampaign_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-response-arn"></a>
The Amazon Resource Name (ARN) of the outbound campaign.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.

 ** [id](#API_connect-outbound-campaigns-v2_CreateCampaign_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-response-id"></a>
The identifier of the outbound campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`

 ** [tags](#API_connect-outbound-campaigns-v2_CreateCampaign_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns-v2_CreateCampaign-response-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_connect-outbound-campaigns-v2_CreateCampaign_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of a conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
This exception occurs when there is an internal failure in the outbound campaigns.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota for your Connect Customer has been exceeded. Contact AWS Support.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns-v2_CreateCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaignsv2-2024-04-23/CreateCampaign)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaignsv2-2024-04-23/CreateCampaign)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/CreateCampaign)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaignsv2-2024-04-23/CreateCampaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/CreateCampaign)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaignsv2-2024-04-23/CreateCampaign)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaignsv2-2024-04-23/CreateCampaign)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaignsv2-2024-04-23/CreateCampaign)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaignsv2-2024-04-23/CreateCampaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/CreateCampaign)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
