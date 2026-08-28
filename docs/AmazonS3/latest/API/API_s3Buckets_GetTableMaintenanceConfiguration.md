---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableMaintenanceConfiguration.html
---

# GetTableMaintenanceConfiguration
<a name="API_s3Buckets_GetTableMaintenanceConfiguration"></a>

Gets details about the maintenance configuration of a table. For more information, see [S3 Tables maintenance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
+ You must have the `s3tables:GetTableMaintenanceConfiguration` permission to use this operation.
+ You must have the `s3tables:GetTableData` permission to use set the compaction strategy to `sort` or `zorder`.

## Request Syntax
<a name="API_s3Buckets_GetTableMaintenanceConfiguration_RequestSyntax"></a>

```
GET /tables/{{tableBucketARN}}/{{namespace}}/{{name}}/maintenance HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_GetTableMaintenanceConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_s3Buckets_GetTableMaintenanceConfiguration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMaintenanceConfiguration-request-uri-name"></a>
The name of the table.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** [namespace](#API_s3Buckets_GetTableMaintenanceConfiguration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMaintenanceConfiguration-request-uri-namespace"></a>
The namespace associated with the table.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** [tableBucketARN](#API_s3Buckets_GetTableMaintenanceConfiguration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMaintenanceConfiguration-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_GetTableMaintenanceConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_GetTableMaintenanceConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": {
      "string" : {
         "settings": { ... },
         "status": "string"
      }
   },
   "tableARN": "string"
}
```

## Response Elements
<a name="API_s3Buckets_GetTableMaintenanceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_s3Buckets_GetTableMaintenanceConfiguration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMaintenanceConfiguration-response-configuration"></a>
Details about the maintenance configuration for the table bucket.
Type: String to [TableMaintenanceConfigurationValue](API_s3Buckets_TableMaintenanceConfigurationValue.md) object map
Valid Keys: `icebergCompaction | icebergSnapshotManagement`

 ** [tableARN](#API_s3Buckets_GetTableMaintenanceConfiguration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMaintenanceConfiguration-response-tableARN"></a>
The Amazon Resource Name (ARN) of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`

## Errors
<a name="API_s3Buckets_GetTableMaintenanceConfiguration_Errors"></a>

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
<a name="API_s3Buckets_GetTableMaintenanceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableMaintenanceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/GetTableMaintenanceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableMaintenanceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableMaintenanceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableMaintenanceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableMaintenanceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableMaintenanceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableMaintenanceConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableMaintenanceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableMaintenanceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
