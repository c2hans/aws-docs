---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_GetCampaignState.html
---

# GetCampaignState
<a name="API_connect-outbound-campaigns-v2_GetCampaignState"></a>

Returns the state of an outbound campaign.

## Request Syntax
<a name="API_connect-outbound-campaigns-v2_GetCampaignState_RequestSyntax"></a>

```
GET /v2/campaigns/{{id}}/state HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns-v2_GetCampaignState_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_connect-outbound-campaigns-v2_GetCampaignState_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_GetCampaignState-request-uri-id"></a>
The identifier of the Connect Customer instance. You can find the `instanceId` in the ARN of the instance.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns-v2_GetCampaignState_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-outbound-campaigns-v2_GetCampaignState_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "state": "string"
}
```

## Response Elements
<a name="API_connect-outbound-campaigns-v2_GetCampaignState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [state](#API_connect-outbound-campaigns-v2_GetCampaignState_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns-v2_GetCampaignState-response-state"></a>
The state of a campaign. For detailed descriptions of each state, see Campaign status in the Connect Customer Administrator Guide.
Type: String
Valid Values: `Initialized | Running | Paused | Stopped | Failed | Completed`

## Errors
<a name="API_connect-outbound-campaigns-v2_GetCampaignState_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns-v2_GetCampaignState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaignsv2-2024-04-23/GetCampaignState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaignsv2-2024-04-23/GetCampaignState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/GetCampaignState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaignsv2-2024-04-23/GetCampaignState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/GetCampaignState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaignsv2-2024-04-23/GetCampaignState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaignsv2-2024-04-23/GetCampaignState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaignsv2-2024-04-23/GetCampaignState)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaignsv2-2024-04-23/GetCampaignState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/GetCampaignState)
