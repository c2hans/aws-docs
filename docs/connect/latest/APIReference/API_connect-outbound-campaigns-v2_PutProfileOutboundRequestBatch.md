---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch.html
---

# PutProfileOutboundRequestBatch
<a name="API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch"></a>

Takes in a list of profile outbound requests to be placed as part of an outbound campaign. For more information on profiles, see [What is a customer profile in Connect Customer?](https://docs.aws.amazon.com/connect/latest/adminguide/customer-profiles-what-data.html).

**Important**
Only Customer Profiles event triggers are permitted to invoke this API.

## Request Syntax
<a name="API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch_RequestSyntax"></a>

```
PUT /v2/campaigns/{{id}}/profile-outbound-requests HTTP/1.1
Content-type: application/json

{
   "profileOutboundRequests": [
      {
         "clientToken": "{{string}}",
         "eventTriggerContext": {
            "channelContext": {
               "webNotificationContext": {
                  "browserId": "{{string}}",
                  "sessionId": "{{string}}"
               }
            },
            "sourceEvent": "{{string}}"
         },
         "expirationTime": "{{string}}",
         "profileId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch-request-uri-id"></a>
The identifier of the outbound campaign.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [profileOutboundRequests](#API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch-request-profileOutboundRequests"></a>
Profile outbound requests for outreaching.
Type: Array of [ProfileOutboundRequest](API_connect-outbound-campaigns-v2_ProfileOutboundRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedRequests": [
      {
         "clientToken": "string",
         "failureCode": "string",
         "id": "string"
      }
   ],
   "successfulRequests": [
      {
         "clientToken": "string",
         "id": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedRequests](#API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch-response-failedRequests"></a>
Failed profile outbound requests.
Type: Array of [FailedProfileOutboundRequest](API_connect-outbound-campaigns-v2_FailedProfileOutboundRequest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [successfulRequests](#API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch-response-successfulRequests"></a>
Successful profile outbound requests.
Type: Array of [SuccessfulProfileOutboundRequest](API_connect-outbound-campaigns-v2_SuccessfulProfileOutboundRequest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

## Errors
<a name="API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch_Errors"></a>

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

 ** InvalidCampaignStateException **
An attempt was made to modify a campaign that is in a state that is not valid. Check your campaign to ensure that it is in a valid state before retrying the operation.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaignsv2-2024-04-23/PutProfileOutboundRequestBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaignsv2-2024-04-23/PutProfileOutboundRequestBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/PutProfileOutboundRequestBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaignsv2-2024-04-23/PutProfileOutboundRequestBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/PutProfileOutboundRequestBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaignsv2-2024-04-23/PutProfileOutboundRequestBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaignsv2-2024-04-23/PutProfileOutboundRequestBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaignsv2-2024-04-23/PutProfileOutboundRequestBatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaignsv2-2024-04-23/PutProfileOutboundRequestBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/PutProfileOutboundRequestBatch)
