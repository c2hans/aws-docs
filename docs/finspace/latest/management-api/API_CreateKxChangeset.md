---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxChangeset.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# CreateKxChangeset
<a name="API_CreateKxChangeset"></a>

 Creates a changeset for a kdb database. A changeset allows you to add and delete existing files by using an ordered list of change requests.

## Request Syntax
<a name="API_CreateKxChangeset_RequestSyntax"></a>

```
POST /kx/environments/{{environmentId}}/databases/{{databaseName}}/changesets HTTP/1.1
Content-type: application/json

{
   "changeRequests": [
      {
         "changeType": "{{string}}",
         "dbPath": "{{string}}",
         "s3Path": "{{string}}"
      }
   ],
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateKxChangeset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [databaseName](#API_CreateKxChangeset_RequestSyntax) **   <a name="finspace-CreateKxChangeset-request-uri-databaseName"></a>
The name of the kdb database.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [environmentId](#API_CreateKxChangeset_RequestSyntax) **   <a name="finspace-CreateKxChangeset-request-uri-environmentId"></a>
A unique identifier of the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_CreateKxChangeset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [changeRequests](#API_CreateKxChangeset_RequestSyntax) **   <a name="finspace-CreateKxChangeset-request-changeRequests"></a>
A list of change request objects that are run in order. A change request object consists of `changeType` , `s3Path`, and `dbPath`. A changeType can have the following values:
+ PUT – Adds or updates files in a database.
+ DELETE – Deletes files in a database.
All the change requests require a mandatory `dbPath` attribute that defines the path within the database directory. All database paths must start with a leading / and end with a trailing /. The `s3Path` attribute defines the s3 source file path and is required for a PUT change type. The `s3path` must end with a trailing / if it is a directory and must end without a trailing / if it is a file.
Here are few examples of how you can use the change request object:

1. This request adds a single sym file at database root location.

    `{ "changeType": "PUT", "s3Path":"s3://bucket/db/sym", "dbPath":"/"}`

1. This request adds files in the given `s3Path` under the 2020.01.02 partition of the database.

    `{ "changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/", "dbPath":"/2020.01.02/"}`

1. This request adds files in the given `s3Path` under the *taq* table partition of the database.

    `[ { "changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/taq/", "dbPath":"/2020.01.02/taq/"}]`

1. This request deletes the 2020.01.02 partition of the database.

    `[{ "changeType": "DELETE", "dbPath": "/2020.01.02/"} ]`

1. The *DELETE* request allows you to delete the existing files under the 2020.01.02 partition of the database, and the *PUT* request adds a new taq table under it.

    `[ {"changeType": "DELETE", "dbPath":"/2020.01.02/"}, {"changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/taq/", "dbPath":"/2020.01.02/taq/"}]`
Type: Array of [ChangeRequest](API_ChangeRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: Yes

 ** [clientToken](#API_CreateKxChangeset_RequestSyntax) **   <a name="finspace-CreateKxChangeset-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

## Response Syntax
<a name="API_CreateKxChangeset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "changeRequests": [
      {
         "changeType": "string",
         "dbPath": "string",
         "s3Path": "string"
      }
   ],
   "changesetId": "string",
   "createdTimestamp": number,
   "databaseName": "string",
   "environmentId": "string",
   "errorInfo": {
      "errorMessage": "string",
      "errorType": "string"
   },
   "lastModifiedTimestamp": number,
   "status": "string"
}
```

## Response Elements
<a name="API_CreateKxChangeset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [changeRequests](#API_CreateKxChangeset_ResponseSyntax) **   <a name="finspace-CreateKxChangeset-response-changeRequests"></a>
A list of change requests.
Type: Array of [ChangeRequest](API_ChangeRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.

 ** [changesetId](#API_CreateKxChangeset_ResponseSyntax) **   <a name="finspace-CreateKxChangeset-response-changesetId"></a>
A unique identifier for the changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]+$`

 ** [createdTimestamp](#API_CreateKxChangeset_ResponseSyntax) **   <a name="finspace-CreateKxChangeset-response-createdTimestamp"></a>
The timestamp at which the changeset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [databaseName](#API_CreateKxChangeset_ResponseSyntax) **   <a name="finspace-CreateKxChangeset-response-databaseName"></a>
The name of the kdb database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [environmentId](#API_CreateKxChangeset_ResponseSyntax) **   <a name="finspace-CreateKxChangeset-response-environmentId"></a>
A unique identifier for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`

 ** [errorInfo](#API_CreateKxChangeset_ResponseSyntax) **   <a name="finspace-CreateKxChangeset-response-errorInfo"></a>
The details of the error that you receive when creating a changeset. It consists of the type of error and the error message.
Type: [ErrorInfo](API_ErrorInfo.md) object

 ** [lastModifiedTimestamp](#API_CreateKxChangeset_ResponseSyntax) **   <a name="finspace-CreateKxChangeset-response-lastModifiedTimestamp"></a>
The timestamp at which the changeset was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [status](#API_CreateKxChangeset_ResponseSyntax) **   <a name="finspace-CreateKxChangeset-response-status"></a>
Status of the changeset creation process.
+ Pending – Changeset creation is pending.
+ Processing – Changeset creation is running.
+ Failed – Changeset creation has failed.
+ Complete – Changeset creation has succeeded.
Type: String
Valid Values: `PENDING | PROCESSING | FAILED | COMPLETED`

## Errors
<a name="API_CreateKxChangeset_Errors"></a>

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
<a name="API_CreateKxChangeset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/CreateKxChangeset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/CreateKxChangeset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/CreateKxChangeset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/CreateKxChangeset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/CreateKxChangeset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/CreateKxChangeset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/CreateKxChangeset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/CreateKxChangeset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/CreateKxChangeset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/CreateKxChangeset)
