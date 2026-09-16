---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_UpdateAccountAssociation.html
---

# UpdateAccountAssociation
<a name="API_UpdateAccountAssociation"></a>

Updates the properties of an existing account association.

## Request Syntax
<a name="API_UpdateAccountAssociation_RequestSyntax"></a>

```
PUT /account-associations/{{AccountAssociationId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAccountAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountAssociationId](#API_UpdateAccountAssociation_RequestSyntax) **   <a name="managedintegrations-UpdateAccountAssociation-request-uri-AccountAssociationId"></a>
The unique identifier of the account association to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

## Request Body
<a name="API_UpdateAccountAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateAccountAssociation_RequestSyntax) **   <a name="managedintegrations-UpdateAccountAssociation-request-Description"></a>
The new description to assign to the account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [Name](#API_UpdateAccountAssociation_RequestSyntax) **   <a name="managedintegrations-UpdateAccountAssociation-request-Name"></a>
The new name to assign to the account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

## Response Syntax
<a name="API_UpdateAccountAssociation_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateAccountAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateAccountAssociation_Errors"></a>

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

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAccountAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/UpdateAccountAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/UpdateAccountAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/UpdateAccountAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/UpdateAccountAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/UpdateAccountAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/UpdateAccountAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/UpdateAccountAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/UpdateAccountAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/UpdateAccountAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/UpdateAccountAssociation)
