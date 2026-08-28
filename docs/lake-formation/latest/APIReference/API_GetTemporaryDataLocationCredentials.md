---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryDataLocationCredentials.html
---

# GetTemporaryDataLocationCredentials
<a name="API_GetTemporaryDataLocationCredentials"></a>

Allows a user or application in a secure environment to access data in a specific Amazon S3 location registered with AWS Lake Formation by providing temporary scoped credentials that are limited to the requested data location and the caller's authorized access level.

 The API operation returns an error in the following scenarios:
+ The data location is not registered with Lake Formation.
+ No AWS Glue table is associated with the data location.
+ The caller doesn't have required permissions on the associated table. The caller must have `SELECT` or `SUPER` permissions on the associated table, and credential vending for full table access must be enabled in the data lake settings.

  For more information, see [Application integration for full table access](https://docs.aws.amazon.com/lake-formation/latest/dg/full-table-credential-vending.html).
+ The data location is in a different AWS Region. Lake Formation doesn't support cross-Region access when vending credentials for a data location. Lake Formation only supports Amazon S3 paths registered within the same Region as the API call.

## Request Syntax
<a name="API_GetTemporaryDataLocationCredentials_RequestSyntax"></a>

```
POST /GetTemporaryDataLocationCredentials HTTP/1.1
Content-type: application/json

{
   "AuditContext": {
      "AdditionalAuditContext": "{{string}}"
   },
   "CredentialsScope": "{{string}}",
   "DataLocations": [ "{{string}}" ],
   "DurationSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_GetTemporaryDataLocationCredentials_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTemporaryDataLocationCredentials_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AuditContext](#API_GetTemporaryDataLocationCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryDataLocationCredentials-request-AuditContext"></a>
A structure used to include auditing information on the privileged API.
Type: [AuditContext](API_AuditContext.md) object
Required: No

 ** [CredentialsScope](#API_GetTemporaryDataLocationCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryDataLocationCredentials-request-CredentialsScope"></a>
The credential scope is determined by the caller's Lake Formation permission on the associated table. Credential scope can be either:
+ READ - Provides read-only access to the data location.
+ READ\_WRITE - Provides both read and write access to the data location.
Type: String
Valid Values: `READ | READWRITE`
Required: No

 ** [DataLocations](#API_GetTemporaryDataLocationCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryDataLocationCredentials-request-DataLocations"></a>
The Amazon S3 data location that you want to access.
Type: Array of strings
Required: No

 ** [DurationSeconds](#API_GetTemporaryDataLocationCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryDataLocationCredentials-request-DurationSeconds"></a>
The time period, between 900 and 43,200 seconds, for the timeout of the temporary credentials.
Type: Integer
Valid Range: Minimum value of 900. Maximum value of 43200.
Required: No

## Response Syntax
<a name="API_GetTemporaryDataLocationCredentials_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccessibleDataLocations": [ "string" ],
   "Credentials": {
      "AccessKeyId": "string",
      "Expiration": number,
      "SecretAccessKey": "string",
      "SessionToken": "string"
   },
   "CredentialsScope": "string"
}
```

## Response Elements
<a name="API_GetTemporaryDataLocationCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessibleDataLocations](#API_GetTemporaryDataLocationCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryDataLocationCredentials-response-AccessibleDataLocations"></a>
Refers to the Amazon S3 locations that can be accessed through the `GetTemporaryCredentialsForLocation` API operation.
Type: Array of strings

 ** [Credentials](#API_GetTemporaryDataLocationCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryDataLocationCredentials-response-Credentials"></a>
A temporary set of credentials for an AWS Lake Formation user. These credentials are scoped down to only access the raw data sources that the user has access to.
The temporary security credentials consist of an access key and a session token. The access key consists of an access key ID and a secret key. When the credentials are created, they are associated with an IAM access control policy that limits what the user can do when using the credentials.
Type: [TemporaryCredentials](API_TemporaryCredentials.md) object

 ** [CredentialsScope](#API_GetTemporaryDataLocationCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryDataLocationCredentials-response-CredentialsScope"></a>
The credential scope is determined by the caller's Lake Formation permission on the associated table. Credential scope can be either:
+ READ - Provides read-only access to the data location.
+ READ\_WRITE - Provides both read and write access to the data location.
Type: String
Valid Values: `READ | READWRITE`

## Errors
<a name="API_GetTemporaryDataLocationCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** ConflictException **
Multiple resources exist with the same Amazon S3 location
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetTemporaryDataLocationCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetTemporaryDataLocationCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetTemporaryDataLocationCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetTemporaryDataLocationCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetTemporaryDataLocationCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetTemporaryDataLocationCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetTemporaryDataLocationCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetTemporaryDataLocationCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetTemporaryDataLocationCredentials)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetTemporaryDataLocationCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetTemporaryDataLocationCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
