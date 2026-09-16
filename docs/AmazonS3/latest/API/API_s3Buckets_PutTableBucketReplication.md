---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketReplication.html
---

# PutTableBucketReplication
<a name="API_s3Buckets_PutTableBucketReplication"></a>

Creates or updates the replication configuration for a table bucket. This operation defines how tables in the source bucket are replicated to destination buckets. Replication helps ensure data availability and disaster recovery across regions or accounts.

Permissions
+ You must have the `s3tables:PutTableBucketReplication` permission to use this operation. The IAM role specified in the configuration must have permissions to read from the source bucket and write permissions to all destination buckets.
+ You must also have the following permissions:
  +  `s3tables:GetTable` permission on the source table.
  +  `s3tables:ListTables` permission on the bucket containing the table.
  +  `s3tables:CreateTable` permission for the destination.
  +  `s3tables:CreateNamespace` permission for the destination.
  +  `s3tables:GetTableMaintenanceConfig` permission for the source bucket.
  +  `s3tables:PutTableMaintenanceConfig` permission for the destination bucket.
+ You must have `iam:PassRole` permission with condition allowing roles to be passed to `replication.s3tables.amazonaws.com`.

## Request Syntax
<a name="API_s3Buckets_PutTableBucketReplication_RequestSyntax"></a>

```
PUT /table-bucket-replication?tableBucketARN={{tableBucketARN}}&versionToken={{versionToken}} HTTP/1.1
Content-type: application/json

{
   "configuration": {
      "role": "{{string}}",
      "rules": [
         {
            "destinations": [
               {
                  "destinationTableBucketARN": "{{string}}"
               }
            ]
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_s3Buckets_PutTableBucketReplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableBucketARN](#API_s3Buckets_PutTableBucketReplication_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketReplication-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the source table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

 ** [versionToken](#API_s3Buckets_PutTableBucketReplication_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketReplication-request-uri-versionToken"></a>
A version token from a previous GetTableBucketReplication call. Use this token to ensure you're updating the expected version of the configuration.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_s3Buckets_PutTableBucketReplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_s3Buckets_PutTableBucketReplication_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketReplication-request-configuration"></a>
The replication configuration to apply, including the IAM role and replication rules.
Type: [TableBucketReplicationConfiguration](API_s3Buckets_TableBucketReplicationConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_s3Buckets_PutTableBucketReplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string",
   "versionToken": "string"
}
```

## Response Elements
<a name="API_s3Buckets_PutTableBucketReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_s3Buckets_PutTableBucketReplication_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketReplication-response-status"></a>
The status of the replication configuration operation.
Type: String

 ** [versionToken](#API_s3Buckets_PutTableBucketReplication_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketReplication-response-versionToken"></a>
A new version token representing the updated replication configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_s3Buckets_PutTableBucketReplication_Errors"></a>

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
<a name="API_s3Buckets_PutTableBucketReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTableBucketReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/PutTableBucketReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTableBucketReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTableBucketReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTableBucketReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTableBucketReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTableBucketReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTableBucketReplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTableBucketReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTableBucketReplication)
