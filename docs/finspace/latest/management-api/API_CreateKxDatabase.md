---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxDatabase.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# CreateKxDatabase
<a name="API_CreateKxDatabase"></a>

Creates a new kdb database in the environment.

## Request Syntax
<a name="API_CreateKxDatabase_RequestSyntax"></a>

```
POST /kx/environments/{{environmentId}}/databases HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "databaseName": "{{string}}",
   "description": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateKxDatabase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_CreateKxDatabase_RequestSyntax) **   <a name="finspace-CreateKxDatabase-request-uri-environmentId"></a>
A unique identifier for the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_CreateKxDatabase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateKxDatabase_RequestSyntax) **   <a name="finspace-CreateKxDatabase-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [databaseName](#API_CreateKxDatabase_RequestSyntax) **   <a name="finspace-CreateKxDatabase-request-databaseName"></a>
The name of the kdb database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [description](#API_CreateKxDatabase_RequestSyntax) **   <a name="finspace-CreateKxDatabase-request-description"></a>
A description of the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`
Required: No

 ** [tags](#API_CreateKxDatabase_RequestSyntax) **   <a name="finspace-CreateKxDatabase-request-tags"></a>
A list of key-value pairs to label the kdb database. You can add up to 50 tags to your kdb database
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `^[a-zA-Z0-9+-=._:@ ]+$`
Required: No

## Response Syntax
<a name="API_CreateKxDatabase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdTimestamp": number,
   "databaseArn": "string",
   "databaseName": "string",
   "description": "string",
   "environmentId": "string",
   "lastModifiedTimestamp": number
}
```

## Response Elements
<a name="API_CreateKxDatabase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdTimestamp](#API_CreateKxDatabase_ResponseSyntax) **   <a name="finspace-CreateKxDatabase-response-createdTimestamp"></a>
The timestamp at which the database is created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [databaseArn](#API_CreateKxDatabase_ResponseSyntax) **   <a name="finspace-CreateKxDatabase-response-databaseArn"></a>
The ARN identifier of the database.
Type: String

 ** [databaseName](#API_CreateKxDatabase_ResponseSyntax) **   <a name="finspace-CreateKxDatabase-response-databaseName"></a>
The name of the kdb database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [description](#API_CreateKxDatabase_ResponseSyntax) **   <a name="finspace-CreateKxDatabase-response-description"></a>
A description of the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`

 ** [environmentId](#API_CreateKxDatabase_ResponseSyntax) **   <a name="finspace-CreateKxDatabase-response-environmentId"></a>
A unique identifier for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`

 ** [lastModifiedTimestamp](#API_CreateKxDatabase_ResponseSyntax) **   <a name="finspace-CreateKxDatabase-response-lastModifiedTimestamp"></a>
The last time that the database was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

## Errors
<a name="API_CreateKxDatabase_Errors"></a>

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

 ** LimitExceededException **
A service limit or quota is exceeded.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource group already exists.
HTTP Status Code: 409

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
<a name="API_CreateKxDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/CreateKxDatabase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/CreateKxDatabase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/CreateKxDatabase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/CreateKxDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/CreateKxDatabase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/CreateKxDatabase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/CreateKxDatabase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/CreateKxDatabase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/CreateKxDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/CreateKxDatabase)
