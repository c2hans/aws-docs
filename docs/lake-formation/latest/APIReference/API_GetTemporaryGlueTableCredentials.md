---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryGlueTableCredentials.html
---

# GetTemporaryGlueTableCredentials
<a name="API_GetTemporaryGlueTableCredentials"></a>

Allows a caller in a secure environment to assume a role with permission to access Amazon S3. In order to vend such credentials, AWS Lake Formation assumes the role associated with a registered location, for example an Amazon S3 bucket, with a scope down policy which restricts the access to a single prefix.

To call this API, the role that the service assumes must have `lakeformation:GetDataAccess` permission on the resource.

## Request Syntax
<a name="API_GetTemporaryGlueTableCredentials_RequestSyntax"></a>

```
POST /GetTemporaryGlueTableCredentials HTTP/1.1
Content-type: application/json

{
   "AuditContext": {
      "AdditionalAuditContext": "{{string}}"
   },
   "DurationSeconds": {{number}},
   "Permissions": [ "{{string}}" ],
   "QuerySessionContext": {
      "AdditionalContext": {
         "{{string}}" : "{{string}}"
      },
      "ClusterId": "{{string}}",
      "QueryAuthorizationId": "{{string}}",
      "QueryId": "{{string}}",
      "QueryStartTime": {{number}}
   },
   "S3Path": "{{string}}",
   "SupportedPermissionTypes": [ "{{string}}" ],
   "TableArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetTemporaryGlueTableCredentials_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTemporaryGlueTableCredentials_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AuditContext](#API_GetTemporaryGlueTableCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-request-AuditContext"></a>
A structure representing context to access a resource (column names, query ID, etc).
Type: [AuditContext](API_AuditContext.md) object
Required: No

 ** [DurationSeconds](#API_GetTemporaryGlueTableCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-request-DurationSeconds"></a>
The time period, between 900 and 21,600 seconds, for the timeout of the temporary credentials.
Type: Integer
Valid Range: Minimum value of 900. Maximum value of 43200.
Required: No

 ** [Permissions](#API_GetTemporaryGlueTableCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-request-Permissions"></a>
Filters the request based on the user having been granted a list of specified permissions on the requested resource(s).
Type: Array of strings
Valid Values: `ALL | SELECT | ALTER | DROP | DELETE | INSERT | DESCRIBE | CREATE_DATABASE | CREATE_TABLE | DATA_LOCATION_ACCESS | CREATE_LF_TAG | ASSOCIATE | GRANT_WITH_LF_TAG_EXPRESSION | CREATE_LF_TAG_EXPRESSION | CREATE_CATALOG | SUPER_USER`
Required: No

 ** [QuerySessionContext](#API_GetTemporaryGlueTableCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-request-QuerySessionContext"></a>
A structure used as a protocol between query engines and Lake Formation or AWS Glue. Contains both a Lake Formation generated authorization identifier and information from the request's authorization context.
Type: [QuerySessionContext](API_QuerySessionContext.md) object
Required: No

 ** [S3Path](#API_GetTemporaryGlueTableCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-request-S3Path"></a>
The Amazon S3 path for the table.
Type: String
Required: No

 ** [SupportedPermissionTypes](#API_GetTemporaryGlueTableCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-request-SupportedPermissionTypes"></a>
A list of supported permission types for the table. Valid values are `COLUMN_PERMISSION` and `CELL_FILTER_PERMISSION`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 255 items.
Valid Values: `COLUMN_PERMISSION | CELL_FILTER_PERMISSION | NESTED_PERMISSION | NESTED_CELL_PERMISSION`
Required: No

 ** [TableArn](#API_GetTemporaryGlueTableCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-request-TableArn"></a>
The ARN identifying a table in the Data Catalog for the temporary credentials request.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetTemporaryGlueTableCredentials_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccessKeyId": "string",
   "Expiration": number,
   "SecretAccessKey": "string",
   "SessionToken": "string",
   "VendedS3Path": [ "string" ]
}
```

## Response Elements
<a name="API_GetTemporaryGlueTableCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessKeyId](#API_GetTemporaryGlueTableCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-response-AccessKeyId"></a>
The access key ID for the temporary credentials.
Type: String

 ** [Expiration](#API_GetTemporaryGlueTableCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-response-Expiration"></a>
The date and time when the temporary credentials expire.
Type: Timestamp

 ** [SecretAccessKey](#API_GetTemporaryGlueTableCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-response-SecretAccessKey"></a>
The secret key for the temporary credentials.
Type: String

 ** [SessionToken](#API_GetTemporaryGlueTableCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-response-SessionToken"></a>
The session token for the temporary credentials.
Type: String

 ** [VendedS3Path](#API_GetTemporaryGlueTableCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryGlueTableCredentials-response-VendedS3Path"></a>
The Amazon S3 path for the temporary credentials.
Type: Array of strings

## Errors
<a name="API_GetTemporaryGlueTableCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** EntityNotFoundException **
A specified entity does not exist.
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

 ** PermissionTypeMismatchException **
The engine does not support filtering data based on the enforced permissions. For example, if you call the `GetTemporaryGlueTableCredentials` operation with `SupportedPermissionType` equal to `ColumnPermission`, but cell-level permissions exist on the table, this exception is thrown.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetTemporaryGlueTableCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetTemporaryGlueTableCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetTemporaryGlueTableCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetTemporaryGlueTableCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetTemporaryGlueTableCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetTemporaryGlueTableCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetTemporaryGlueTableCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetTemporaryGlueTableCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetTemporaryGlueTableCredentials)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetTemporaryGlueTableCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetTemporaryGlueTableCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
