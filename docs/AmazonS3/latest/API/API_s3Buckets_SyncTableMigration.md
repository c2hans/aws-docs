---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_SyncTableMigration.html
---

# SyncTableMigration
<a name="API_s3Buckets_SyncTableMigration"></a>

Migrates the changes in the source table since the previous start or sync, such as added and deleted source objects, into the destination table. The sync runs asynchronously: this operation returns the migration ID of the sync and its initial state, and you track progress with `GetTableMigration`.

A sync uses the source, destination and data migration settings of the table's migration, and plans the work and writes its reports in the same way as `StartTableMigration`. You can sync after a start or sync that succeeded, failed or was cancelled, if an earlier start or sync of the table has a valid plan (`hasValidPlan`). You can't sync a table while a start or sync is in progress for it, and you can sync a table until you call `CompleteTableMigration` for it. If a source object that an earlier migration migrated has since been overwritten, the sync fails.

Permissions
+ You must have the `s3tables:SyncTableMigration` permission to use this operation.
+ You must have the `iam:PassRole` permission on the role that you specify in `roleARN`, with a condition that allows passing it to `migration.s3tables.amazonaws.com`. The associated resource is the table.

## Request Syntax
<a name="API_s3Buckets_SyncTableMigration_RequestSyntax"></a>

```
POST /sync-table-migration HTTP/1.1
Content-type: application/json

{
   "migrationOutput": {
      "bucket": "{{string}}",
      "prefixes": {
         "objectCompatibilityReport": "{{string}}",
         "objectMigrationReport": "{{string}}",
         "tableCompatibilityReport": "{{string}}"
      }
   },
   "reviewMigrationPlan": {{boolean}},
   "roleARN": "{{string}}",
   "tableARN": "{{string}}"
}
```

## URI Request Parameters
<a name="API_s3Buckets_SyncTableMigration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_s3Buckets_SyncTableMigration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [migrationOutput](#API_s3Buckets_SyncTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_SyncTableMigration-request-migrationOutput"></a>
The bucket and prefixes that the sync writes its reports to. The bucket must be a general purpose bucket in your account and in the same Region as the table bucket, and the migration role must be able to write objects to it. Otherwise, the migration fails when it writes its first report.
Type: [MigrationOutputConfiguration](API_s3Buckets_MigrationOutputConfiguration.md) object
Required: Yes

 ** [reviewMigrationPlan](#API_s3Buckets_SyncTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_SyncTableMigration-request-reviewMigrationPlan"></a>
Specifies whether the sync waits in the `pendingReview` state, so that you can review the compatibility reports before it migrates any data. If `true`, the migration continues when you call `UpdateTableMigration` with `requestedState` set to `queued`. If you don't continue or cancel the migration within 30 days, the migration fails. The default is `false`.
Type: Boolean
Required: No

 ** [roleARN](#API_s3Buckets_SyncTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_SyncTableMigration-request-roleARN"></a>
The Amazon Resource Name (ARN) of the IAM role that the sync uses to read the source table and its data and to write the destination table and the reports. The role must be in your account, and its trust policy must allow `migration.s3tables.amazonaws.com` to assume it. You can limit the trust policy to the destination table bucket with the `aws:SourceArn` and `aws:SourceAccount` condition keys.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [tableARN](#API_s3Buckets_SyncTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_SyncTableMigration-request-tableARN"></a>
The Amazon Resource Name (ARN) of the destination table to sync. The table must have a migration, and you must not have called `CompleteTableMigration` for it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: Yes

## Response Syntax
<a name="API_s3Buckets_SyncTableMigration_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "migrationId": "string",
   "state": "string"
}
```

## Response Elements
<a name="API_s3Buckets_SyncTableMigration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [migrationId](#API_s3Buckets_SyncTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_SyncTableMigration-response-migrationId"></a>
The migration ID of the sync.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`

 ** [state](#API_s3Buckets_SyncTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_SyncTableMigration-response-state"></a>
The state of the migration when the request is accepted, such as `planning`.
Type: String
Valid Values: `new | planning | pendingReview | queued | migrating | succeeded | failed | cancelling | cancelled`

## Errors
<a name="API_s3Buckets_SyncTableMigration_Errors"></a>

 ** AccessDeniedException **
The action cannot be performed because you do not have the required permission.
HTTP Status Code: 403

 ** BadRequestException **
The request is invalid or malformed.
HTTP Status Code: 400

 ** ConflictException **
The request failed because there is a conflict with a previous write. You can retry the request.
HTTP Status Code: 409

 ** ForbiddenException **
The caller isn't authorized to make the request.
HTTP Status Code: 403

 ** InternalServerErrorException **
The request failed due to an internal server error.
HTTP Status Code: 500

 ** NotFoundException **
The request was rejected because the specified resource could not be found.
HTTP Status Code: 404

 ** TooManyRequestsException **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

## See Also
<a name="API_s3Buckets_SyncTableMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/SyncTableMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/SyncTableMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/SyncTableMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/SyncTableMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/SyncTableMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/SyncTableMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/SyncTableMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/SyncTableMigration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/SyncTableMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/SyncTableMigration)
