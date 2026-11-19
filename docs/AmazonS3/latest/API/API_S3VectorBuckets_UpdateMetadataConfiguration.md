---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_UpdateMetadataConfiguration.html
---

# UpdateMetadataConfiguration

Adds or deletes text search configurations on a vector index. Specify either `add` or `delete`, but not both. The vector index must be in `ENHANCED` mode.

Permissions
You must have the `s3vectors:UpdateMetadataConfiguration` permission to use this operation.

## Request Syntax
<a name="API_S3VectorBuckets_UpdateMetadataConfiguration_RequestSyntax"></a>

```
POST /UpdateMetadataConfiguration HTTP/1.1
Content-type: application/json

{
   "add": {
      "textSearchConfigurations": [
         {
            "language": "{{string}}",
            "metadataKey": "{{string}}",
            "status": "{{string}}"
         }
      ]
   },
   "delete": {
      "textSearchConfigurations": [
         {
            "metadataKey": "{{string}}"
         }
      ]
   },
   "indexArn": "{{string}}",
   "indexName": "{{string}}",
   "vectorBucketName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_S3VectorBuckets_UpdateMetadataConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_S3VectorBuckets_UpdateMetadataConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [add](#API_S3VectorBuckets_UpdateMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_UpdateMetadataConfiguration-request-add"></a>
Text search configurations to add to the vector index.
Type: [MetadataConfigurationAdd](API_S3VectorBuckets_MetadataConfigurationAdd.md) object
Required: No

 ** [delete](#API_S3VectorBuckets_UpdateMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_UpdateMetadataConfiguration-request-delete"></a>
Text search configurations to delete from the vector index.
Type: [MetadataConfigurationDelete](API_S3VectorBuckets_MetadataConfigurationDelete.md) object
Required: No

 ** [indexArn](#API_S3VectorBuckets_UpdateMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_UpdateMetadataConfiguration-request-indexArn"></a>
The Amazon Resource Name (ARN) of the vector index to update.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]/index/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`
Required: No

 ** [indexName](#API_S3VectorBuckets_UpdateMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_UpdateMetadataConfiguration-request-indexName"></a>
The name of the vector index to update.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

 ** [vectorBucketName](#API_S3VectorBuckets_UpdateMetadataConfiguration_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_UpdateMetadataConfiguration-request-vectorBucketName"></a>
The name of the vector bucket that contains the vector index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

## Response Syntax
<a name="API_S3VectorBuckets_UpdateMetadataConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "indexArn": "string"
}
```

## Response Elements
<a name="API_S3VectorBuckets_UpdateMetadataConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [indexArn](#API_S3VectorBuckets_UpdateMetadataConfiguration_ResponseSyntax) **   <a name="AmazonS3-S3VectorBuckets_UpdateMetadataConfiguration-response-indexArn"></a>
The Amazon Resource Name (ARN) of the updated vector index.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]/index/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`

## Errors
<a name="API_S3VectorBuckets_UpdateMetadataConfiguration_Errors"></a>

 ** AccessDeniedException **
Access denied.
HTTP Status Code: 403

 ** ConflictException **
The request failed because a vector bucket name or a vector index name already exists. Vector bucket names must be unique within your AWS account for each AWS Region. Vector index names must be unique within your vector bucket. Choose a different vector bucket name or vector index name, and try again.
HTTP Status Code: 409

 ** InternalServerException **
The request failed due to an internal server error.
HTTP Status Code: 500

 ** NotFoundException **
The request was rejected because the specified resource can't be found.
HTTP Status Code: 404

 ** RequestTimeoutException **
The request timed out. Retry your request.
HTTP Status Code: 408

 ** ServiceUnavailableException **
The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The requested action isn't valid.
 ** fieldList **
A list of specific validation failures that are encountered during input processing. Each entry in the list contains a path to the field that failed validation and a detailed message that explains why the validation failed. To satisfy multiple constraints, a field can appear multiple times in this list if it failed. You can use the information to identify and fix the specific validation issues in your request.
HTTP Status Code: 400

## See Also
<a name="API_S3VectorBuckets_UpdateMetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/UpdateMetadataConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3vectors-2025-07-15/UpdateMetadataConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/UpdateMetadataConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/UpdateMetadataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/UpdateMetadataConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/UpdateMetadataConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/UpdateMetadataConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/UpdateMetadataConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/UpdateMetadataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/UpdateMetadataConfiguration)
