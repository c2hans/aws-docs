---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableReplication.html
---

# PutTableReplication
<a name="API_s3Buckets_PutTableReplication"></a>

Creates or updates the replication configuration for a specific table. This operation allows you to define table-level replication independently of bucket-level replication, providing granular control over which tables are replicated and where.

Permissions
+ You must have the `s3tables:PutTableReplication` permission to use this operation. The IAM role specified in the configuration must have permissions to read from the source table and write to all destination tables.
+ You must also have the following permissions:
  +  `s3tables:GetTable` permission on the source table being replicated.
  +  `s3tables:CreateTable` permission for the destination.
  +  `s3tables:CreateNamespace` permission for the destination.
  +  `s3tables:GetTableMaintenanceConfig` permission for the source table.
  +  `s3tables:PutTableMaintenanceConfig` permission for the destination table.
+ You must have `iam:PassRole` permission with condition allowing roles to be passed to `replication.s3tables.amazonaws.com`.

## Request Syntax
<a name="API_s3Buckets_PutTableReplication_RequestSyntax"></a>

```
PUT /table-replication?tableArn={{tableArn}}&versionToken={{versionToken}} HTTP/1.1
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
<a name="API_s3Buckets_PutTableReplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableArn](#API_s3Buckets_PutTableReplication_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableReplication-request-uri-tableArn"></a>
The Amazon Resource Name (ARN) of the source table.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: Yes

 ** [versionToken](#API_s3Buckets_PutTableReplication_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableReplication-request-uri-versionToken"></a>
A version token from a previous GetTableReplication call. Use this token to ensure you're updating the expected version of the configuration.

## Request Body
<a name="API_s3Buckets_PutTableReplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_s3Buckets_PutTableReplication_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableReplication-request-configuration"></a>
The replication configuration to apply to the table, including the IAM role and replication rules.
Type: [TableReplicationConfiguration](API_s3Buckets_TableReplicationConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_s3Buckets_PutTableReplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string",
   "versionToken": "string"
}
```

## Response Elements
<a name="API_s3Buckets_PutTableReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_s3Buckets_PutTableReplication_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_PutTableReplication-response-status"></a>
The status of the replication configuration operation.
Type: String

 ** [versionToken](#API_s3Buckets_PutTableReplication_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_PutTableReplication-response-versionToken"></a>
A new version token representing the updated replication configuration.
Type: String

## Errors
<a name="API_s3Buckets_PutTableReplication_Errors"></a>

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
<a name="API_s3Buckets_PutTableReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTableReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/PutTableReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTableReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTableReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTableReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTableReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTableReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTableReplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTableReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTableReplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
