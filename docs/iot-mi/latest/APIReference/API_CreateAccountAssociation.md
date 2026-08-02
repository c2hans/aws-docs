---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateAccountAssociation.html
---

# CreateAccountAssociation
<a name="API_CreateAccountAssociation"></a>

Creates a new account association via the destination id.

## Request Syntax
<a name="API_CreateAccountAssociation_RequestSyntax"></a>

```
POST /account-associations HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ConnectorDestinationId": "{{string}}",
   "Description": "{{string}}",
   "GeneralAuthorization": {
      "AuthMaterialName": "{{string}}"
   },
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAccountAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAccountAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateAccountAssociation_RequestSyntax) **   <a name="managedintegrations-CreateAccountAssociation-request-ClientToken"></a>
An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [ConnectorDestinationId](#API_CreateAccountAssociation_RequestSyntax) **   <a name="managedintegrations-CreateAccountAssociation-request-ConnectorDestinationId"></a>
The identifier of the connector destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

 ** [Description](#API_CreateAccountAssociation_RequestSyntax) **   <a name="managedintegrations-CreateAccountAssociation-request-Description"></a>
A description of the account association request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [GeneralAuthorization](#API_CreateAccountAssociation_RequestSyntax) **   <a name="managedintegrations-CreateAccountAssociation-request-GeneralAuthorization"></a>
The General Authorization reference by authorization material name.
Type: [GeneralAuthorizationName](API_GeneralAuthorizationName.md) object
Required: No

 ** [Name](#API_CreateAccountAssociation_RequestSyntax) **   <a name="managedintegrations-CreateAccountAssociation-request-Name"></a>
The name of the destination for the new account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [Tags](#API_CreateAccountAssociation_RequestSyntax) **   <a name="managedintegrations-CreateAccountAssociation-request-Tags"></a>
A set of key/value pairs that are used to manage the account association.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAccountAssociation_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "AccountAssociationId": "string",
   "Arn": "string",
   "AssociationState": "string",
   "OAuthAuthorizationUrl": "string"
}
```

## Response Elements
<a name="API_CreateAccountAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [AccountAssociationId](#API_CreateAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-CreateAccountAssociation-response-AccountAssociationId"></a>
The identifier for the account association request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`

 ** [Arn](#API_CreateAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-CreateAccountAssociation-response-Arn"></a>
The Amazon Resource Name (ARN) of the account association.
Type: String
Length Constraints: Minimum length of 67. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:account-association/[0-9a-zA-Z]+`

 ** [AssociationState](#API_CreateAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-CreateAccountAssociation-response-AssociationState"></a>
The current state of the account association request.
Type: String
Valid Values: `ASSOCIATION_IN_PROGRESS | ASSOCIATION_FAILED | ASSOCIATION_SUCCEEDED | ASSOCIATION_DELETING | REFRESH_TOKEN_EXPIRED`

 ** [OAuthAuthorizationUrl](#API_CreateAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-CreateAccountAssociation-response-OAuthAuthorizationUrl"></a>
Third-party IoT platform OAuth authorization server URL backed with all the required parameters to perform end-user authentication. This field will be empty when using General Authorization flows that do not require OAuth.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `$|^(https):\/\/.*`

## Errors
<a name="API_CreateAccountAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict with the request.
HTTP Status Code: 409

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
HTTP Status Code: 401

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_CreateAccountAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/CreateAccountAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/CreateAccountAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CreateAccountAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/CreateAccountAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CreateAccountAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/CreateAccountAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/CreateAccountAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/CreateAccountAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/CreateAccountAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CreateAccountAssociation)
