---
source_url: https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DeleteConnectInstanceConfig.html
---

# DeleteConnectInstanceConfig
<a name="API_connect-outbound-campaigns_DeleteConnectInstanceConfig"></a>

Deletes configuration information for an Connect Customer instance.

## Request Syntax
<a name="API_connect-outbound-campaigns_DeleteConnectInstanceConfig_RequestSyntax"></a>

```
DELETE /connect-instance/{{connectInstanceId}}/config HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns_DeleteConnectInstanceConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectInstanceId](#API_connect-outbound-campaigns_DeleteConnectInstanceConfig_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_DeleteConnectInstanceConfig-request-uri-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns_DeleteConnectInstanceConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-outbound-campaigns_DeleteConnectInstanceConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-outbound-campaigns_DeleteConnectInstanceConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-outbound-campaigns_DeleteConnectInstanceConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the outbound campaigns.
HTTP Status Code: 500

 ** InvalidStateException **
An attempt was made to modify a campaign state and the new campaign state is not valid. Check campaign state before retrying the operation.
HTTP Status Code: 409

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
<a name="API_connect-outbound-campaigns_DeleteConnectInstanceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaigns-2021-01-30/DeleteConnectInstanceConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaigns-2021-01-30/DeleteConnectInstanceConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/DeleteConnectInstanceConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaigns-2021-01-30/DeleteConnectInstanceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/DeleteConnectInstanceConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaigns-2021-01-30/DeleteConnectInstanceConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaigns-2021-01-30/DeleteConnectInstanceConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaigns-2021-01-30/DeleteConnectInstanceConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaigns-2021-01-30/DeleteConnectInstanceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/DeleteConnectInstanceConfig)
