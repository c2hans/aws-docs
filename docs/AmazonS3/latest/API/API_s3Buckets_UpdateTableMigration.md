---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_UpdateTableMigration.html
---

# UpdateTableMigration
<a name="API_s3Buckets_UpdateTableMigration"></a>

Requests a state change for a migration. Identify the migration by its `migrationId` or by the `tableARN` of its destination table.

Set `requestedState` to `queued` to continue a migration in the `pendingReview` state; the migration moves to `queued` or `migrating`. Set it to `cancelled` to cancel a migration in the `new`, `planning`, `pendingReview`, `queued` or `migrating` state; the migration moves to `cancelling`, finishes the work in progress, and then ends in the `cancelled` state, or in the `failed` state if any objects failed to migrate. Data that the migration already committed stays in the destination table.

Permissions
+ You must have the `s3tables:UpdateTableMigration` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_UpdateTableMigration_RequestSyntax"></a>

```
POST /update-table-migration?migrationId={{migrationId}}&tableARN={{tableARN}} HTTP/1.1
Content-type: application/json

{
   "requestedState": "{{string}}",
   "updateDescription": "{{string}}"
}
```

## URI Request Parameters
<a name="API_s3Buckets_UpdateTableMigration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [migrationId](#API_s3Buckets_UpdateTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_UpdateTableMigration-request-uri-migrationId"></a>
The ID of the migration to update. Specify either `migrationId` or `tableARN`, not both.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`

 ** [tableARN](#API_s3Buckets_UpdateTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_UpdateTableMigration-request-uri-tableARN"></a>
The Amazon Resource Name (ARN) of the destination table. Updates the table's most recent migration. Until the migration creates the destination table, specify `migrationId`. Specify either `tableARN` or `migrationId`, not both.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`

## Request Body
<a name="API_s3Buckets_UpdateTableMigration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [requestedState](#API_s3Buckets_UpdateTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_UpdateTableMigration-request-requestedState"></a>
The state to move the migration to: `queued` to continue a migration in the `pendingReview` state, or `cancelled` to cancel a migration in the `new`, `planning`, `pendingReview`, `queued` or `migrating` state.
Type: String
Valid Values: `queued | cancelled`
Required: Yes

 ** [updateDescription](#API_s3Buckets_UpdateTableMigration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_UpdateTableMigration-request-updateDescription"></a>
A description of the update, up to 1,024 characters, with no control characters. `GetTableMigration` doesn't return it.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_s3Buckets_UpdateTableMigration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "migrationId": "string",
   "state": "string",
   "tableARN": "string"
}
```

## Response Elements
<a name="API_s3Buckets_UpdateTableMigration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [migrationId](#API_s3Buckets_UpdateTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_UpdateTableMigration-response-migrationId"></a>
The ID of the migration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`

 ** [state](#API_s3Buckets_UpdateTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_UpdateTableMigration-response-state"></a>
The state of the migration after the update, such as `queued`, `migrating` or `cancelling`.
Type: String
Valid Values: `new | planning | pendingReview | queued | migrating | succeeded | failed | cancelling | cancelled`

 ** [tableARN](#API_s3Buckets_UpdateTableMigration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_UpdateTableMigration-response-tableARN"></a>
The Amazon Resource Name (ARN) of the destination table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`

## Errors
<a name="API_s3Buckets_UpdateTableMigration_Errors"></a>

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
<a name="API_s3Buckets_UpdateTableMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/UpdateTableMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/UpdateTableMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/UpdateTableMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/UpdateTableMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/UpdateTableMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/UpdateTableMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/UpdateTableMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/UpdateTableMigration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/UpdateTableMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/UpdateTableMigration)
