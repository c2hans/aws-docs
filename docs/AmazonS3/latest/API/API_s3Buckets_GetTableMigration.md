---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableMigration.html
---

# GetTableMigration
<a name="API_s3Buckets_GetTableMigration"></a>

Gets the details of a migration, including its state, the reason it failed, its statistics and the location of its reports. Identify the migration by its `migrationId`, or specify the `tableARN` of a destination table to get that table's most recent migration.

Permissions
+ You must have the `s3tables:GetTableMigration` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_GetTableMigration_RequestSyntax"></a>

```
GET /get-table-migration?migrationId={{migrationId}}&tableARN={{tableARN}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_GetTableMigration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [migrationId](#API_s3Buckets_GetTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-request-uri-migrationId"></a>
The ID of the migration to get. Specify either `migrationId` or `tableARN`, not both.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`

 ** [tableARN](#API_s3Buckets_GetTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-request-uri-tableARN"></a>
The Amazon Resource Name (ARN) of the destination table. Gets the table's most recent migration. Specify either `tableARN` or `migrationId`, not both.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`

## Request Body
<a name="API_s3Buckets_GetTableMigration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_GetTableMigration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "dataMigration": {
      "maintenanceSettings": {
         "icebergCompaction": {
            "strategy": "string",
            "targetFileSizeMB": number
         },
         "icebergSnapshotManagement": {
            "maxSnapshotAgeHours": number,
            "minSnapshotsToKeep": number
         }
      },
      "migrationPolicies": {
         "incompatibleValuesPolicy": "string",
         "unmatchedSourceFieldsPolicy": "string"
      }
   },
   "failureReason": {
      "code": "string",
      "detail": "string"
   },
   "hasValidPlan": boolean,
   "migrationId": "string",
   "migrationOutput": {
      "bucket": "string",
      "objectCompatibilityReport": {
         "checksumCRC64NVME": "string",
         "invalidFindings": {
            "string" : number
         },
         "key": "string",
         "prefix": "string"
      },
      "objectMigrationReport": {
         "checksumCRC64NVME": "string",
         "invalidFindings": {
            "string" : number
         },
         "key": "string",
         "prefix": "string"
      },
      "tableCompatibilityReport": {
         "checksumCRC64NVME": "string",
         "invalidFindings": {
            "string" : number
         },
         "key": "string",
         "prefix": "string"
      }
   },
   "migrationStats": {
      "objectsFailedMigration": number,
      "objectsMigrated": number,
      "objectsPendingMigration": number
   },
   "name": "string",
   "namespace": "string",
   "planningStats": {
      "objectsPlanned": number,
      "objectsScanned": number,
      "partitionCount": number
   },
   "reviewMigrationPlan": boolean,
   "roleARN": "string",
   "source": { ... },
   "sourceType": "string",
   "state": "string",
   "stateUpdatedAt": "string",
   "tableARN": "string",
   "tableBucketARN": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_s3Buckets_GetTableMigration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-createdAt"></a>
The date and time that the migration was created.
Type: Timestamp

 ** [dataMigration](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-dataMigration"></a>
The maintenance settings and migration policies for the destination table.
Type: [DataMigrationOverview](API_s3Buckets_DataMigrationOverview.md) object

 ** [failureReason](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-failureReason"></a>
The reason that the migration failed. The code names the cause, such as a migration role that S3 Tables can't assume or an AWS Glue table that doesn't exist, or the report that lists the findings. This value is returned only when the migration is in the `failed` state.
Type: [MigrationFailureReason](API_s3Buckets_MigrationFailureReason.md) object

 ** [hasValidPlan](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-hasValidPlan"></a>
A Boolean value that specifies whether planning produced a plan that the migration can run. If planning hasn't finished, this value isn't returned.
Type: Boolean

 ** [migrationId](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-migrationId"></a>
The ID of the migration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`

 ** [migrationOutput](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-migrationOutput"></a>
The bucket and prefixes for the migration's reports, and the location of each report once it is written.
Type: [MigrationOutputOverview](API_s3Buckets_MigrationOutputOverview.md) object

 ** [migrationStats](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-migrationStats"></a>
The number of objects that migrated, failed or are pending. These counts are set when planning finishes and updated when the migration ends.
Type: [MigrationStats](API_s3Buckets_MigrationStats.md) object

 ** [name](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-name"></a>
The name of the destination table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`

 ** [namespace](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-namespace"></a>
The namespace of the destination table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`

 ** [planningStats](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-planningStats"></a>
Statistics about the source and the partitions in the migration. This value is returned after planning finishes.
Type: [PlanningStats](API_s3Buckets_PlanningStats.md) object

 ** [reviewMigrationPlan](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-reviewMigrationPlan"></a>
A Boolean value that specifies whether the migration waits in the `pendingReview` state, so that you can review the compatibility reports before it migrates any data.
Type: Boolean

 ** [roleARN](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-roleARN"></a>
The Amazon Resource Name (ARN) of the IAM role that the migration uses.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:iam::[0-9]{12}:role/.+`

 ** [source](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-source"></a>
The source table of the migration.
Type: [SourceConfiguration](API_s3Buckets_SourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [sourceType](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-sourceType"></a>
The type of the migration's source.
Type: String
Valid Values: `glueTable`

 ** [state](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-state"></a>
The state of the migration. Valid values:
+  `new` - S3 Tables accepted the request.
+  `planning` - The migration is checking the source table, its objects and the destination for compatibility, and writing the compatibility reports.
+  `pendingReview` - Planning finished, and the migration waits for you to continue or cancel it with `UpdateTableMigration`.
+  `queued` - The migration is waiting to start migrating data.
+  `migrating` - The migration is running the plan from the `planning` state: it copies data and commits it to the destination table. A migration reaches this state only if `hasValidPlan` is `true`.
+  `succeeded` - Every planned object migrated.
+  `failed` - The migration failed. Check `failureReason` for the cause.
+  `cancelling` - You cancelled the migration, and it is finishing the work in progress.
+  `cancelled` - The migration is cancelled.
A migration ends in the `succeeded`, `failed` or `cancelled` state. You can cancel it until it ends.
Type: String
Valid Values: `new | planning | pendingReview | queued | migrating | succeeded | failed | cancelling | cancelled`

 ** [stateUpdatedAt](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-stateUpdatedAt"></a>
The date and time that the migration's state last changed.
Type: Timestamp

 ** [tableARN](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-tableARN"></a>
The Amazon Resource Name (ARN) of the destination table, once the migration creates it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`

 ** [tableBucketARN](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket that contains the destination table.
Type: String
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`

 ** [type](#API_s3Buckets_GetTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMigration-response-type"></a>
The type of the migration. Valid values:
+  `start` - A migration that `StartTableMigration` started.
+  `sync` - A migration that `SyncTableMigration` started.
Type: String
Valid Values: `start | sync`

## Errors
<a name="API_s3Buckets_GetTableMigration_Errors"></a>

 ** AccessDeniedException **
The action cannot be performed because you do not have the required permission.
HTTP Status Code: 403

 ** BadRequestException **
The request is invalid or malformed.
HTTP Status Code: 400

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
<a name="API_s3Buckets_GetTableMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/GetTableMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableMigration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableMigration)
