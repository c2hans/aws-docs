---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateCredentialLocker.html
---

# CreateCredentialLocker
<a name="API_CreateCredentialLocker"></a>

Create a credential locker.

**Note**
This operation will not trigger the creation of all the manufacturing resources.

## Request Syntax
<a name="API_CreateCredentialLocker_RequestSyntax"></a>

```
POST /credential-lockers HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateCredentialLocker_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCredentialLocker_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateCredentialLocker_RequestSyntax) **   <a name="managedintegrations-CreateCredentialLocker-request-ClientToken"></a>
An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [Name](#API_CreateCredentialLocker_RequestSyntax) **   <a name="managedintegrations-CreateCredentialLocker-request-Name"></a>
The name of the credential locker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [Tags](#API_CreateCredentialLocker_RequestSyntax) **   <a name="managedintegrations-CreateCredentialLocker-request-Tags"></a>
A set of key/value pairs that are used to manage the credential locker.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateCredentialLocker_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "CreatedAt": number,
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateCredentialLocker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateCredentialLocker_ResponseSyntax) **   <a name="managedintegrations-CreateCredentialLocker-response-Arn"></a>
The Amazon Resource Name (ARN) of the credential locker.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:credential-locker/[0-9a-zA-Z]+`

 ** [CreatedAt](#API_CreateCredentialLocker_ResponseSyntax) **   <a name="managedintegrations-CreateCredentialLocker-response-CreatedAt"></a>
The timestamp value of when the credential locker request occurred.
Type: Timestamp

 ** [Id](#API_CreateCredentialLocker_ResponseSyntax) **   <a name="managedintegrations-CreateCredentialLocker-response-Id"></a>
The identifier of the credential locker creation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`

## Errors
<a name="API_CreateCredentialLocker_Errors"></a>

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

 ** ServiceQuotaExceededException **
The service quota has been exceeded for this request.
HTTP Status Code: 402

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
<a name="API_CreateCredentialLocker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/CreateCredentialLocker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/CreateCredentialLocker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CreateCredentialLocker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/CreateCredentialLocker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CreateCredentialLocker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/CreateCredentialLocker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/CreateCredentialLocker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/CreateCredentialLocker)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/CreateCredentialLocker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CreateCredentialLocker)
