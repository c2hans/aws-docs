---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningClaim.html
---

# CreateProvisioningClaim
<a name="API_CreateProvisioningClaim"></a>

Creates a provisioning claim.

Requires permission to access the [CreateProvisioningClaim](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateProvisioningClaim_RequestSyntax"></a>

```
POST /provisioning-templates/{{templateName}}/provisioning-claim HTTP/1.1
```

## URI Request Parameters
<a name="API_CreateProvisioningClaim_RequestParameters"></a>

The request uses the following URI parameters.

 ** [templateName](#API_CreateProvisioningClaim_RequestSyntax) **   <a name="iot-CreateProvisioningClaim-request-uri-templateName"></a>
The name of the provisioning template to use.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`
Required: Yes

## Request Body
<a name="API_CreateProvisioningClaim_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CreateProvisioningClaim_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateId": "string",
   "certificatePem": "string",
   "expiration": number,
   "keyPair": {
      "PrivateKey": "string",
      "PublicKey": "string"
   }
}
```

## Response Elements
<a name="API_CreateProvisioningClaim_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateId](#API_CreateProvisioningClaim_ResponseSyntax) **   <a name="iot-CreateProvisioningClaim-response-certificateId"></a>
The ID of the certificate.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`

 ** [certificatePem](#API_CreateProvisioningClaim_ResponseSyntax) **   <a name="iot-CreateProvisioningClaim-response-certificatePem"></a>
The provisioning claim certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\s\S]*`

 ** [expiration](#API_CreateProvisioningClaim_ResponseSyntax) **   <a name="iot-CreateProvisioningClaim-response-expiration"></a>
The provisioning claim expiration time.
Type: Timestamp

 ** [keyPair](#API_CreateProvisioningClaim_ResponseSyntax) **   <a name="iot-CreateProvisioningClaim-response-keyPair"></a>
The provisioning claim key pair.
Type: [KeyPair](API_KeyPair.md) object

## Errors
<a name="API_CreateProvisioningClaim_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_CreateProvisioningClaim_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateProvisioningClaim)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateProvisioningClaim)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateProvisioningClaim)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateProvisioningClaim)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateProvisioningClaim)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateProvisioningClaim)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateProvisioningClaim)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateProvisioningClaim)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateProvisioningClaim)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateProvisioningClaim)
