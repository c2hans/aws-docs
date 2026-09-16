---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryGluePartitionCredentials.html
---

# GetTemporaryGluePartitionCredentials
<a name="API_GetTemporaryGluePartitionCredentials"></a>

This API is identical to `GetTemporaryTableCredentials` except that this is used when the target Data Catalog resource is of type Partition. Lake Formation restricts the permission of the vended credentials with the same scope down policy which restricts access to a single Amazon S3 prefix.

## Request Syntax
<a name="API_GetTemporaryGluePartitionCredentials_RequestSyntax"></a>

```
POST /GetTemporaryGluePartitionCredentials HTTP/1.1
Content-type: application/json

{
   "AuditContext": {
      "AdditionalAuditContext": "{{string}}"
   },
   "DurationSeconds": {{number}},
   "Partition": {
      "Values": [ "{{string}}" ]
   },
   "Permissions": [ "{{string}}" ],
   "SupportedPermissionTypes": [ "{{string}}" ],
   "TableArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetTemporaryGluePartitionCredentials_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTemporaryGluePartitionCredentials_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AuditContext](#API_GetTemporaryGluePartitionCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGluePartitionCredentials-request-AuditContext"></a>
A structure representing context to access a resource (column names, query ID, etc).
Type: [AuditContext](API_AuditContext.md) object
Required: No

 ** [DurationSeconds](#API_GetTemporaryGluePartitionCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGluePartitionCredentials-request-DurationSeconds"></a>
The time period, between 900 and 21,600 seconds, for the timeout of the temporary credentials.
Type: Integer
Valid Range: Minimum value of 900. Maximum value of 43200.
Required: No

 ** [Partition](#API_GetTemporaryGluePartitionCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGluePartitionCredentials-request-Partition"></a>
A list of partition values identifying a single partition.
Type: [PartitionValueList](API_PartitionValueList.md) object
Required: Yes

 ** [Permissions](#API_GetTemporaryGluePartitionCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGluePartitionCredentials-request-Permissions"></a>
Filters the request based on the user having been granted a list of specified permissions on the requested resource(s).
Type: Array of strings
Valid Values: `ALL | SELECT | ALTER | DROP | DELETE | INSERT | DESCRIBE | CREATE_DATABASE | CREATE_TABLE | DATA_LOCATION_ACCESS | CREATE_LF_TAG | ASSOCIATE | GRANT_WITH_LF_TAG_EXPRESSION | CREATE_LF_TAG_EXPRESSION | CREATE_CATALOG | SUPER_USER`
Required: No

 ** [SupportedPermissionTypes](#API_GetTemporaryGluePartitionCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGluePartitionCredentials-request-SupportedPermissionTypes"></a>
A list of supported permission types for the partition. Valid values are `COLUMN_PERMISSION` and `CELL_FILTER_PERMISSION`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 255 items.
Valid Values: `COLUMN_PERMISSION | CELL_FILTER_PERMISSION | NESTED_PERMISSION | NESTED_CELL_PERMISSION`
Required: No

 ** [TableArn](#API_GetTemporaryGluePartitionCredentials_RequestSyntax) **   <a name="lakeformation-GetTemporaryGluePartitionCredentials-request-TableArn"></a>
The ARN of the partitions' table.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetTemporaryGluePartitionCredentials_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccessKeyId": "string",
   "Expiration": number,
   "SecretAccessKey": "string",
   "SessionToken": "string"
}
```

## Response Elements
<a name="API_GetTemporaryGluePartitionCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessKeyId](#API_GetTemporaryGluePartitionCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryGluePartitionCredentials-response-AccessKeyId"></a>
The access key ID for the temporary credentials.
Type: String

 ** [Expiration](#API_GetTemporaryGluePartitionCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryGluePartitionCredentials-response-Expiration"></a>
The date and time when the temporary credentials expire.
Type: Timestamp

 ** [SecretAccessKey](#API_GetTemporaryGluePartitionCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryGluePartitionCredentials-response-SecretAccessKey"></a>
The secret key for the temporary credentials.
Type: String

 ** [SessionToken](#API_GetTemporaryGluePartitionCredentials_ResponseSyntax) **   <a name="lakeformation-GetTemporaryGluePartitionCredentials-response-SessionToken"></a>
The session token for the temporary credentials.
Type: String

## Errors
<a name="API_GetTemporaryGluePartitionCredentials_Errors"></a>

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
<a name="API_GetTemporaryGluePartitionCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetTemporaryGluePartitionCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetTemporaryGluePartitionCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetTemporaryGluePartitionCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetTemporaryGluePartitionCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetTemporaryGluePartitionCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetTemporaryGluePartitionCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetTemporaryGluePartitionCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetTemporaryGluePartitionCredentials)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetTemporaryGluePartitionCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetTemporaryGluePartitionCredentials)
