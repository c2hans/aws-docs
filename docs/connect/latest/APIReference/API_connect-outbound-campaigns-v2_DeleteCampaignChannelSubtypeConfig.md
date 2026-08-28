---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig.html
---

# DeleteCampaignChannelSubtypeConfig
<a name="API_connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig"></a>

Deletes the channel subtype configuration of an outbound campaign. Only campaigns in the `Initialized` state are valid for this operation.

## Request Syntax
<a name="API_connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig_RequestSyntax"></a>

```
DELETE /v2/campaigns/{{id}}/channel-subtype-config?channelSubtype={{channelSubtype}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelSubtype](#API_connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig-request-uri-channelSubtype"></a>
The name of the channel subtype configuration.
Valid Values: `TELEPHONY | SMS | EMAIL | WHATSAPP`
Required: Yes

 ** [id](#API_connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig-request-uri-id"></a>
The identifier of the outbound campaign.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig_Errors"></a>

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

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns-v2_DeleteCampaignChannelSubtypeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaignsv2-2024-04-23/DeleteCampaignChannelSubtypeConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaignsv2-2024-04-23/DeleteCampaignChannelSubtypeConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/DeleteCampaignChannelSubtypeConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaignsv2-2024-04-23/DeleteCampaignChannelSubtypeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/DeleteCampaignChannelSubtypeConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaignsv2-2024-04-23/DeleteCampaignChannelSubtypeConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaignsv2-2024-04-23/DeleteCampaignChannelSubtypeConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaignsv2-2024-04-23/DeleteCampaignChannelSubtypeConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaignsv2-2024-04-23/DeleteCampaignChannelSubtypeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/DeleteCampaignChannelSubtypeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
