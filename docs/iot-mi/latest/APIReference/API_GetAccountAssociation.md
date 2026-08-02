---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetAccountAssociation.html
---

# GetAccountAssociation
<a name="API_GetAccountAssociation"></a>

Get an account association for an AWS account linked to a customer-managed destination.

## Request Syntax
<a name="API_GetAccountAssociation_RequestSyntax"></a>

```
GET /account-associations/{{AccountAssociationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountAssociationId](#API_GetAccountAssociation_RequestSyntax) **   <a name="managedintegrations-GetAccountAssociation-request-uri-AccountAssociationId"></a>
The unique identifier of the account association to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

## Request Body
<a name="API_GetAccountAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountAssociationId": "string",
   "Arn": "string",
   "AssociationState": "string",
   "ConnectorDestinationId": "string",
   "Description": "string",
   "ErrorMessage": "string",
   "GeneralAuthorization": {
      "AuthMaterialName": "string"
   },
   "Name": "string",
   "OAuthAuthorizationUrl": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetAccountAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountAssociationId](#API_GetAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-GetAccountAssociation-response-AccountAssociationId"></a>
The unique identifier of the retrieved account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`

 ** [Arn](#API_GetAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-GetAccountAssociation-response-Arn"></a>
The Amazon Resource Name (ARN) of the account association.
Type: String
Length Constraints: Minimum length of 67. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:account-association/[0-9a-zA-Z]+`

 ** [AssociationState](#API_GetAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-GetAccountAssociation-response-AssociationState"></a>
The current status state for the account association.
Type: String
Valid Values: `ASSOCIATION_IN_PROGRESS | ASSOCIATION_FAILED | ASSOCIATION_SUCCEEDED | ASSOCIATION_DELETING | REFRESH_TOKEN_EXPIRED`

 ** [ConnectorDestinationId](#API_GetAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-GetAccountAssociation-response-ConnectorDestinationId"></a>
The identifier of the connector destination associated with this account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

 ** [Description](#API_GetAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-GetAccountAssociation-response-Description"></a>
The description of the account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9-_ ]+`

 ** [ErrorMessage](#API_GetAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-GetAccountAssociation-response-ErrorMessage"></a>
The error message explaining the current account association error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9-_ ]+`

 ** [GeneralAuthorization](#API_GetAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-GetAccountAssociation-response-GeneralAuthorization"></a>
The General Authorization reference by authorization material name.
Type: [GeneralAuthorizationName](API_GeneralAuthorizationName.md) object

 ** [Name](#API_GetAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-GetAccountAssociation-response-Name"></a>
The name of the account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`

 ** [OAuthAuthorizationUrl](#API_GetAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-GetAccountAssociation-response-OAuthAuthorizationUrl"></a>
Third party IoT platform OAuth authorization server URL backed with all the required parameters to perform end-user authentication. This field will be empty when using General Authorization flows that do not require OAuth.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `$|^(https):\/\/.*`

 ** [Tags](#API_GetAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-GetAccountAssociation-response-Tags"></a>
A set of key/value pairs that are used to manage the account association.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetAccountAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

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

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_GetAccountAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetAccountAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetAccountAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetAccountAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetAccountAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetAccountAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetAccountAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetAccountAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetAccountAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetAccountAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetAccountAssociation)
