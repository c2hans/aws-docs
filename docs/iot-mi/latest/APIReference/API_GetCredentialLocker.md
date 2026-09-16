---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetCredentialLocker.html
---

# GetCredentialLocker
<a name="API_GetCredentialLocker"></a>

Get information on an existing credential locker

## Request Syntax
<a name="API_GetCredentialLocker_RequestSyntax"></a>

```
GET /credential-lockers/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCredentialLocker_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetCredentialLocker_RequestSyntax) **   <a name="managedintegrations-GetCredentialLocker-request-uri-Identifier"></a>
The identifier of the credential locker.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`
Required: Yes

## Request Body
<a name="API_GetCredentialLocker_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCredentialLocker_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreatedAt": number,
   "Id": "string",
   "Name": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetCredentialLocker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetCredentialLocker_ResponseSyntax) **   <a name="managedintegrations-GetCredentialLocker-response-Arn"></a>
The Amazon Resource Name (ARN) of the credential locker.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:credential-locker/[0-9a-zA-Z]+`

 ** [CreatedAt](#API_GetCredentialLocker_ResponseSyntax) **   <a name="managedintegrations-GetCredentialLocker-response-CreatedAt"></a>
The timestamp value of when the credential locker requset occurred.
Type: Timestamp

 ** [Id](#API_GetCredentialLocker_ResponseSyntax) **   <a name="managedintegrations-GetCredentialLocker-response-Id"></a>
The identifier of the credential locker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`

 ** [Name](#API_GetCredentialLocker_ResponseSyntax) **   <a name="managedintegrations-GetCredentialLocker-response-Name"></a>
The name of the credential locker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`

 ** [Tags](#API_GetCredentialLocker_ResponseSyntax) **   <a name="managedintegrations-GetCredentialLocker-response-Tags"></a>
A set of key/value pairs that are used to manage the credential locker.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetCredentialLocker_Errors"></a>

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
<a name="API_GetCredentialLocker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetCredentialLocker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetCredentialLocker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetCredentialLocker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetCredentialLocker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetCredentialLocker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetCredentialLocker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetCredentialLocker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetCredentialLocker)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetCredentialLocker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetCredentialLocker)
