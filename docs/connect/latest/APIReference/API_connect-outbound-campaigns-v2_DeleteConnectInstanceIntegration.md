---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration.html
---

# DeleteConnectInstanceIntegration
<a name="API_connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration"></a>

Deletes integration for an Connect Customer instance.

## Request Syntax
<a name="API_connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration_RequestSyntax"></a>

```
POST /v2/connect-instance/{{connectInstanceId}}/integrations/delete HTTP/1.1
Content-type: application/json

{
   "integrationIdentifier": { ... }
}
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectInstanceId](#API_connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration-request-uri-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the `instanceId` in the ARN of the instance.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [integrationIdentifier](#API_connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration-request-integrationIdentifier"></a>
The identifier of the integration between an Connect Customer instance and other services.
Type: [IntegrationIdentifier](API_connect-outbound-campaigns-v2_IntegrationIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration_Errors"></a>

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
<a name="API_connect-outbound-campaigns-v2_DeleteConnectInstanceIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaignsv2-2024-04-23/DeleteConnectInstanceIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaignsv2-2024-04-23/DeleteConnectInstanceIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/DeleteConnectInstanceIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaignsv2-2024-04-23/DeleteConnectInstanceIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/DeleteConnectInstanceIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaignsv2-2024-04-23/DeleteConnectInstanceIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaignsv2-2024-04-23/DeleteConnectInstanceIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaignsv2-2024-04-23/DeleteConnectInstanceIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaignsv2-2024-04-23/DeleteConnectInstanceIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/DeleteConnectInstanceIntegration)
