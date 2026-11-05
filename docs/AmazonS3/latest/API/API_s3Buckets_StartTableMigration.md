---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_StartTableMigration.html
---

# StartTableMigration
<a name="API_s3Buckets_StartTableMigration"></a>

Starts migrating an AWS Glue Data Catalog table into a new table in a table bucket. The migration runs asynchronously: this operation returns the migration ID and its initial state, and you track progress with `GetTableMigration`.

The namespace must already exist, and a table with the specified name must not. The migration creates the table during planning and commits data to it as it runs. Until you call `CompleteTableMigration`, you can read the table but you can't write to it. If the migration fails or is cancelled, the table and the data already committed to it remain.

The migration first checks the source and the destination, and writes the table compatibility and object compatibility reports to the bucket that you specify in `migrationOutput`. If you set `reviewMigrationPlan` to `true`, the migration waits in the `pendingReview` state so that you can review the reports, and continues only when you call `UpdateTableMigration` with `requestedState` set to `queued`. If you don't continue or cancel the migration within 30 days, the migration fails. Otherwise it continues to migrate the data, and writes the object migration report when the migration ends. If planning fails, the migration writes no object migration report.

Permissions
+ You must have the `s3tables:StartTableMigration` permission to use this operation.
+ You must have the `iam:PassRole` permission on the role that you specify in `roleARN`, with a condition that allows passing it to `migration.s3tables.amazonaws.com`. The associated resource is the table bucket.
+ If `destinationTable` specifies SSE-KMS encryption, you must have the `kms:DescribeKey` and `kms:GenerateDataKey` permissions on the KMS key. You must also grant the S3 Tables maintenance principal access to the key. For more information, see [Permissions requirements for S3 Tables SSE-KMS encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html).

## Request Syntax
<a name="API_s3Buckets_StartTableMigration_RequestSyntax"></a>

```
POST /start-table-migration HTTP/1.1
Content-type: application/json

{
   "dataMigration": {
      "maintenanceSettings": {
         "icebergCompaction": {
            "strategy": "{{string}}",
            "targetFileSizeMB": {{number}}
         },
         "icebergSnapshotManagement": {
            "maxSnapshotAgeHours": {{number}},
            "minSnapshotsToKeep": {{number}}
         }
      },
      "migrationPolicies": {
         "incompatibleValuesPolicy": "{{string}}",
         "unmatchedSourceFieldsPolicy": "{{string}}"
      }
   },
   "destinationTable": {
      "encryptionConfiguration": {
         "kmsKeyArn": "{{string}}",
         "sseAlgorithm": "{{string}}"
      },
      "icebergSortOrder": {
         "fields": [
            {
               "direction": "{{string}}",
               "null-order": "{{string}}",
               "source-id": {{number}},
               "transform": "{{string}}"
            }
         ],
         "order-id": {{number}}
      },
      "name": "{{string}}",
      "namespace": "{{string}}",
      "properties": {
         "compressionCodec": "{{string}}",
         "dictionaryEncoding": {{boolean}},
         "icebergFormatVersion": {{number}},
         "writeFormat": "{{string}}"
      },
      "schema": {
         "fields": [
            {
               "doc": "{{string}}",
               "id": {{number}},
               "name": "{{string}}",
               "required": {{boolean}},
               "type": {{JSON value}}
            }
         ],
         "identifier-field-ids": [ {{number}} ],
         "schema-id": {{number}},
         "type": "{{string}}"
      },
      "storageClassConfiguration": {
         "storageClass": "{{string}}"
      },
      "tableBucketARN": "{{string}}",
      "tags": {
         "{{string}}" : "{{string}}"
      }
   },
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
   "source": { ... },
   "sourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_s3Buckets_StartTableMigration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_s3Buckets_StartTableMigration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dataMigration](#API_s3Buckets_StartTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_StartTableMigration-request-dataMigration"></a>
The maintenance settings and migration policies for the destination table.
Type: [DataMigrationSettings](API_s3Buckets_DataMigrationSettings.md) object
Required: No

 ** [destinationTable](#API_s3Buckets_StartTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_StartTableMigration-request-destinationTable"></a>
The table to create and migrate the source into.
Type: [DestinationTable](API_s3Buckets_DestinationTable.md) object
Required: Yes

 ** [migrationOutput](#API_s3Buckets_StartTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_StartTableMigration-request-migrationOutput"></a>
The bucket and prefixes that the migration writes its reports to. The bucket must be a general purpose bucket in your account and in the same Region as the table bucket, and the migration role must be able to write objects to it. Otherwise, the migration fails when it writes its first report.
Type: [MigrationOutputConfiguration](API_s3Buckets_MigrationOutputConfiguration.md) object
Required: Yes

 ** [reviewMigrationPlan](#API_s3Buckets_StartTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_StartTableMigration-request-reviewMigrationPlan"></a>
Specifies whether the migration waits in the `pendingReview` state, so that you can review the compatibility reports before it migrates any data. If `true`, the migration continues when you call `UpdateTableMigration` with `requestedState` set to `queued`. If you don't continue or cancel the migration within 30 days, the migration fails. The default is `false`.
Type: Boolean
Required: No

 ** [roleARN](#API_s3Buckets_StartTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_StartTableMigration-request-roleARN"></a>
The Amazon Resource Name (ARN) of the IAM role that the migration uses to read the source table and its data and to write the destination table and the reports. The role must be in your account, and its trust policy must allow `migration.s3tables.amazonaws.com` to assume it. You can limit the trust policy to the destination table bucket with the `aws:SourceArn` and `aws:SourceAccount` condition keys.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [source](#API_s3Buckets_StartTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_StartTableMigration-request-source"></a>
The source table to migrate.
Type: [SourceConfiguration](API_s3Buckets_SourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [sourceType](#API_s3Buckets_StartTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_StartTableMigration-request-sourceType"></a>
The type of the source. It must match the member that you set in `source`.
Type: String
Valid Values: `glueTable`
Required: Yes

## Response Syntax
<a name="API_s3Buckets_StartTableMigration_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "migrationId": "string",
   "state": "string"
}
```

## Response Elements
<a name="API_s3Buckets_StartTableMigration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [migrationId](#API_s3Buckets_StartTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_StartTableMigration-response-migrationId"></a>
The ID of the migration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`

 ** [state](#API_s3Buckets_StartTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_StartTableMigration-response-state"></a>
The state of the migration when the request is accepted, such as `planning`.
Type: String
Valid Values: `new | planning | pendingReview | queued | migrating | succeeded | failed | cancelling | cancelled`

## Errors
<a name="API_s3Buckets_StartTableMigration_Errors"></a>

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
<a name="API_s3Buckets_StartTableMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/StartTableMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/StartTableMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/StartTableMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/StartTableMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/StartTableMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/StartTableMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/StartTableMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/StartTableMigration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/StartTableMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/StartTableMigration)
