---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_DescribeCampaign.html
---

# DescribeCampaign
<a name="API_connect-outbound-campaigns-v2_DescribeCampaign"></a>

Describes an outbound campaign.

## Request Syntax
<a name="API_connect-outbound-campaigns-v2_DescribeCampaign_RequestSyntax"></a>

```
GET /v2/campaigns/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns-v2_DescribeCampaign_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_connect-outbound-campaigns-v2_DescribeCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_DescribeCampaign-request-uri-id"></a>
The identifier of the outbound campaign.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns-v2_DescribeCampaign_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-outbound-campaigns-v2_DescribeCampaign_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "campaign": {
      "arn": "string",
      "channelSubtypeConfig": {
         "email": {
            "capacity": number,
            "defaultOutboundConfig": {
               "connectSourceEmailAddress": "string",
               "sourceEmailAddressDisplayName": "string",
               "wisdomTemplateArn": "string"
            },
            "outboundMode": { ... }
         },
         "sms": {
            "capacity": number,
            "defaultOutboundConfig": {
               "connectSourcePhoneNumberArn": "string",
               "wisdomTemplateArn": "string"
            },
            "outboundMode": { ... }
         },
         "telephony": {
            "capacity": number,
            "connectQueueId": "string",
            "defaultOutboundConfig": {
               "answerMachineDetectionConfig": {
                  "awaitAnswerMachinePrompt": boolean,
                  "enableAnswerMachineDetection": boolean
               },
               "connectContactFlowId": "string",
               "connectSourcePhoneNumber": "string",
               "ringTimeout": number
            },
            "outboundMode": { ... }
         },
         "whatsApp": {
            "capacity": number,
            "defaultOutboundConfig": {
               "connectSourcePhoneNumberArn": "string",
               "wisdomTemplateArn": "string"
            },
            "outboundMode": { ... }
         }
      },
      "communicationLimitsOverride": {
         "allChannelSubtypes": { ... },
         "instanceLimitsHandling": "string"
      },
      "communicationTimeConfig": {
         "email": {
            "openHours": { ... },
            "restrictedPeriods": { ... }
         },
         "localTimeZoneConfig": {
            "defaultTimeZone": "string",
            "localTimeZoneDetection": [ "string" ],
            "localTimeZoneDetectionScope": "string"
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
      "connectCampaignFlowArn": "string",
      "connectInstanceId": "string",
      "entryLimitsConfig": {
         "maxEntryCount": number,
         "minEntryInterval": "string"
      },
      "id": "string",
      "name": "string",
      "schedule": {
         "endTime": "string",
         "refreshFrequency": "string",
         "startTime": "string"
      },
      "source": { ... },
      "tags": {
         "string" : "string"
      },
      "type": "string"
   }
}
```

## Response Elements
<a name="API_connect-outbound-campaigns-v2_DescribeCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [campaign](#API_connect-outbound-campaigns-v2_DescribeCampaign_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns-v2_DescribeCampaign-response-campaign"></a>
The configuration for an outbound campaign.
Type: [Campaign](API_connect-outbound-campaigns-v2_Campaign.md) object

## Errors
<a name="API_connect-outbound-campaigns-v2_DescribeCampaign_Errors"></a>

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
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns-v2_DescribeCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaignsv2-2024-04-23/DescribeCampaign)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaignsv2-2024-04-23/DescribeCampaign)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/DescribeCampaign)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaignsv2-2024-04-23/DescribeCampaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/DescribeCampaign)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaignsv2-2024-04-23/DescribeCampaign)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaignsv2-2024-04-23/DescribeCampaign)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaignsv2-2024-04-23/DescribeCampaign)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcampaignsv2-2024-04-23/DescribeCampaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/DescribeCampaign)
