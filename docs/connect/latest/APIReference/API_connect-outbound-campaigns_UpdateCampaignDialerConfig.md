---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_UpdateCampaignDialerConfig.html
---

# UpdateCampaignDialerConfig
<a name="API_connect-outbound-campaigns_UpdateCampaignDialerConfig"></a>

Updates [DialerConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DialerConfig.html) for an outbound campaign.

## Request Syntax
<a name="API_connect-outbound-campaigns_UpdateCampaignDialerConfig_RequestSyntax"></a>

```
POST /campaigns/{{id}}/dialer-config HTTP/1.1
Content-type: application/json

{
   "dialerConfig": { ... }
}
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns_UpdateCampaignDialerConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_connect-outbound-campaigns_UpdateCampaignDialerConfig_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_UpdateCampaignDialerConfig-request-uri-id"></a>
The identifier of the campaign.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns_UpdateCampaignDialerConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dialerConfig](#API_connect-outbound-campaigns_UpdateCampaignDialerConfig_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_UpdateCampaignDialerConfig-request-dialerConfig"></a>
Dialer configuration for an outbound campaign.
Type: [DialerConfig](API_connect-outbound-campaigns_DialerConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_connect-outbound-campaigns_UpdateCampaignDialerConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-outbound-campaigns_UpdateCampaignDialerConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-outbound-campaigns_UpdateCampaignDialerConfig_Errors"></a>

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

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWSservice.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns_UpdateCampaignDialerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaigns-2021-01-30/UpdateCampaignDialerConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaigns-2021-01-30/UpdateCampaignDialerConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/UpdateCampaignDialerConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaigns-2021-01-30/UpdateCampaignDialerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/UpdateCampaignDialerConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaigns-2021-01-30/UpdateCampaignDialerConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaigns-2021-01-30/UpdateCampaignDialerConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaigns-2021-01-30/UpdateCampaignDialerConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcampaigns-2021-01-30/UpdateCampaignDialerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/UpdateCampaignDialerConfig)
