---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketMaintenanceConfiguration.html
---

# GetTableBucketMaintenanceConfiguration
<a name="API_s3Buckets_GetTableBucketMaintenanceConfiguration"></a>

Gets details about a maintenance configuration for a given table bucket. For more information, see [Amazon S3 table bucket maintenance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
You must have the `s3tables:GetTableBucketMaintenanceConfiguration` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_GetTableBucketMaintenanceConfiguration_RequestSyntax"></a>

```
GET /buckets/{{tableBucketARN}}/maintenance HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_GetTableBucketMaintenanceConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableBucketARN](#API_s3Buckets_GetTableBucketMaintenanceConfiguration_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableBucketMaintenanceConfiguration-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_GetTableBucketMaintenanceConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_GetTableBucketMaintenanceConfiguration_ResponseSyntax"></a>

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
   "tableBucketARN": "string"
}
```

## Response Elements
<a name="API_s3Buckets_GetTableBucketMaintenanceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_s3Buckets_GetTableBucketMaintenanceConfiguration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableBucketMaintenanceConfiguration-response-configuration"></a>
Details about the maintenance configuration for the table bucket.
Type: String to [TableBucketMaintenanceConfigurationValue](API_s3Buckets_TableBucketMaintenanceConfigurationValue.md) object map
Valid Keys: `icebergUnreferencedFileRemoval`

 ** [tableBucketARN](#API_s3Buckets_GetTableBucketMaintenanceConfiguration_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableBucketMaintenanceConfiguration-response-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration.
Type: String
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`

## Errors
<a name="API_s3Buckets_GetTableBucketMaintenanceConfiguration_Errors"></a>

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
<a name="API_s3Buckets_GetTableBucketMaintenanceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableBucketMaintenanceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/GetTableBucketMaintenanceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableBucketMaintenanceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableBucketMaintenanceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableBucketMaintenanceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableBucketMaintenanceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableBucketMaintenanceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableBucketMaintenanceConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableBucketMaintenanceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableBucketMaintenanceConfiguration)
