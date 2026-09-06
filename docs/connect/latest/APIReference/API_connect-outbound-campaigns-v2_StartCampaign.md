---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_StartCampaign.html
---

# StartCampaign
<a name="API_connect-outbound-campaigns-v2_StartCampaign"></a>

Starts an outbound campaign.

**Note**
After a campaign is started, `schedule`, `source`, `associatedCampaignFlowArn`, `communicationTimeConfig`, `communicationLimitsOverride`, and `entryLimitsConfig` cannot be modified.
After a campaign is started, the queue of the telephony `channelSubtypeConfig` cannot be modified.
After a campaign is started, you can't change the outbound mode of the telephony `channelSubtypeConfig` from agentless to progressive/predictive, or the other way around.

## Request Syntax
<a name="API_connect-outbound-campaigns-v2_StartCampaign_RequestSyntax"></a>

```
POST /v2/campaigns/{{id}}/start HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns-v2_StartCampaign_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_connect-outbound-campaigns-v2_StartCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_StartCampaign-request-uri-id"></a>
The identifier of the outbound campaign.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns-v2_StartCampaign_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-outbound-campaigns-v2_StartCampaign_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-outbound-campaigns-v2_StartCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-outbound-campaigns-v2_StartCampaign_Errors"></a>

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
<a name="API_connect-outbound-campaigns-v2_StartCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaignsv2-2024-04-23/StartCampaign)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaignsv2-2024-04-23/StartCampaign)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/StartCampaign)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaignsv2-2024-04-23/StartCampaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/StartCampaign)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaignsv2-2024-04-23/StartCampaign)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaignsv2-2024-04-23/StartCampaign)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaignsv2-2024-04-23/StartCampaign)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaignsv2-2024-04-23/StartCampaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/StartCampaign)
