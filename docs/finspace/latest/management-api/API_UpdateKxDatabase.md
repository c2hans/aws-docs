---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxDatabase.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# UpdateKxDatabase
<a name="API_UpdateKxDatabase"></a>

Updates information for the given kdb database.

## Request Syntax
<a name="API_UpdateKxDatabase_RequestSyntax"></a>

```
PUT /kx/environments/{{environmentId}}/databases/{{databaseName}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateKxDatabase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [databaseName](#API_UpdateKxDatabase_RequestSyntax) **   <a name="finspace-UpdateKxDatabase-request-uri-databaseName"></a>
The name of the kdb database.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [environmentId](#API_UpdateKxDatabase_RequestSyntax) **   <a name="finspace-UpdateKxDatabase-request-uri-environmentId"></a>
A unique identifier for the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_UpdateKxDatabase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateKxDatabase_RequestSyntax) **   <a name="finspace-UpdateKxDatabase-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [description](#API_UpdateKxDatabase_RequestSyntax) **   <a name="finspace-UpdateKxDatabase-request-description"></a>
A description of the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`
Required: No

## Response Syntax
<a name="API_UpdateKxDatabase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "databaseName": "string",
   "description": "string",
   "environmentId": "string",
   "lastModifiedTimestamp": number
}
```

## Response Elements
<a name="API_UpdateKxDatabase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [databaseName](#API_UpdateKxDatabase_ResponseSyntax) **   <a name="finspace-UpdateKxDatabase-response-databaseName"></a>
The name of the kdb database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [description](#API_UpdateKxDatabase_ResponseSyntax) **   <a name="finspace-UpdateKxDatabase-response-description"></a>
A description of the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`

 ** [environmentId](#API_UpdateKxDatabase_ResponseSyntax) **   <a name="finspace-UpdateKxDatabase-response-environmentId"></a>
A unique identifier for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`

 ** [lastModifiedTimestamp](#API_UpdateKxDatabase_ResponseSyntax) **   <a name="finspace-UpdateKxDatabase-response-lastModifiedTimestamp"></a>
The last time that the database was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

## Errors
<a name="API_UpdateKxDatabase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict with this action, and it could not be completed.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateKxDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/UpdateKxDatabase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/UpdateKxDatabase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/UpdateKxDatabase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/UpdateKxDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/UpdateKxDatabase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/UpdateKxDatabase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/UpdateKxDatabase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/UpdateKxDatabase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/UpdateKxDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/UpdateKxDatabase)
