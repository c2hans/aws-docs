---
source_url: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateConnector.html
---

# CreateConnector
<a name="API_CreateConnector"></a>

Creates a SCEP connector. A SCEP connector links AWS Private Certificate Authority to your SCEP-compatible devices and mobile device management (MDM) systems. Before you create a connector, you must complete a set of prerequisites, including creation of a private certificate authority (CA) to use with this connector. For more information, see [Connector for SCEP prerequisites](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-prerequisites.html).

## Request Syntax
<a name="API_CreateConnector_RequestSyntax"></a>

```
POST /connectors HTTP/1.1
Content-type: application/json

{
   "CertificateAuthorityArn": "{{string}}",
   "ClientToken": "{{string}}",
   "MobileDeviceManagement": { ... },
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "VpcEndpointId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CertificateAuthorityArn](#API_CreateConnector_RequestSyntax) **   <a name="pcaconnectorscep-CreateConnector-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the AWS Private Certificate Authority certificate authority to use with this connector. Due to security vulnerabilities present in the SCEP protocol, we recommend using a private CA that's dedicated for use with the connector.
To retrieve the private CAs associated with your account, you can call [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html) using the AWS Private CA API.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:acm-pca:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:certificate-authority\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: Yes

 ** [ClientToken](#API_CreateConnector_RequestSyntax) **   <a name="pcaconnectorscep-CreateConnector-request-ClientToken"></a>
Custom string that can be used to distinguish between calls to the [CreateChallenge](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html) action. Client tokens for `CreateChallenge` time out after five minutes. Therefore, if you call `CreateChallenge` multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [MobileDeviceManagement](#API_CreateConnector_RequestSyntax) **   <a name="pcaconnectorscep-CreateConnector-request-MobileDeviceManagement"></a>
If you don't supply a value, by default Connector for SCEP creates a connector for general-purpose use. A general-purpose connector is designed to work with clients or endpoints that support the SCEP protocol, except Connector for SCEP for Microsoft Intune. With connectors for general-purpose use, you manage SCEP challenge passwords using Connector for SCEP. For information about considerations and limitations with using Connector for SCEP, see [Considerations and Limitations](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlc4scep-considerations-limitations.html).
If you provide an `IntuneConfiguration`, Connector for SCEP creates a connector for use with Microsoft Intune, and you manage the challenge passwords using Microsoft Intune. For more information, see [Using Connector for SCEP for Microsoft Intune](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html).
Type: [MobileDeviceManagement](API_MobileDeviceManagement.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [Tags](#API_CreateConnector_RequestSyntax) **   <a name="pcaconnectorscep-CreateConnector-request-Tags"></a>
The key-value pairs to associate with the resource.
Type: String to string map
Required: No

 ** [VpcEndpointId](#API_CreateConnector_RequestSyntax) **   <a name="pcaconnectorscep-CreateConnector-request-VpcEndpointId"></a>
If you don't supply a value, by default Connector for SCEP creates a connector accessible over the public internet. If you provide a VPC endpoint ID, creates a connector accessible only through that specific VPC endpoint.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 22.
Pattern: `vpce-[0-9a-f]{8}([0-9a-f]{9})?`
Required: No

## Response Syntax
<a name="API_CreateConnector_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "ConnectorArn": "string"
}
```

## Response Elements
<a name="API_CreateConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [ConnectorArn](#API_CreateConnector_ResponseSyntax) **   <a name="pcaconnectorscep-CreateConnector-response-ConnectorArn"></a>
Returns the Amazon Resource Name (ARN) of the connector.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`

## Errors
<a name="API_CreateConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your AWS Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an AWS Organizations service control policy (SCP) that affects your AWS account.
HTTP Status Code: 403

 ** ConflictException **
This request can't be completed for one of the following reasons because the requested resource was being concurrently modified by another request.
 ** ResourceId **
The identifier of the AWS resource.
 ** ResourceType **
The resource type, which can be either `Connector` or `Challenge`.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than `ACTIVE`.
 ** ResourceId **
The identifier of the AWS resource.
 ** ResourceType **
The resource type, which can be either `Connector` or `Challenge`.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** QuotaCode **
The quota identifier.
 ** ResourceType **
The resource type, which can be either `Connector` or `Challenge`.
 ** ServiceCode **
Identifies the originating service.
HTTP Status Code: 402

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.
 ** Reason **
The reason for the validation error, if available. The service doesn't return a reason for every validation exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pca-connector-scep-2018-05-10/CreateConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pca-connector-scep-2018-05-10/CreateConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-scep-2018-05-10/CreateConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pca-connector-scep-2018-05-10/CreateConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-scep-2018-05-10/CreateConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pca-connector-scep-2018-05-10/CreateConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pca-connector-scep-2018-05-10/CreateConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pca-connector-scep-2018-05-10/CreateConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pca-connector-scep-2018-05-10/CreateConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-scep-2018-05-10/CreateConnector)
