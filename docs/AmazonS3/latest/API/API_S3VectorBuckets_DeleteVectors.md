---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectors.html
---

# DeleteVectors
<a name="API_S3VectorBuckets_DeleteVectors"></a>

Deletes one or more vectors in a vector index. To specify the vector index, you can either use both the vector bucket name and vector index name, or use the vector index Amazon Resource Name (ARN).

Permissions
You must have the `s3vectors:DeleteVectors` permission to use this operation.

## Request Syntax
<a name="API_S3VectorBuckets_DeleteVectors_RequestSyntax"></a>

```
POST /DeleteVectors HTTP/1.1
Content-type: application/json

{
   "indexArn": "{{string}}",
   "indexName": "{{string}}",
   "keys": [ "{{string}}" ],
   "vectorBucketName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_S3VectorBuckets_DeleteVectors_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_S3VectorBuckets_DeleteVectors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [indexArn](#API_S3VectorBuckets_DeleteVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_DeleteVectors-request-indexArn"></a>
The ARN of the vector index that contains a vector you want to delete.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]/index/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`
Required: No

 ** [indexName](#API_S3VectorBuckets_DeleteVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_DeleteVectors-request-indexName"></a>
The name of the vector index that contains a vector you want to delete.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

 ** [keys](#API_S3VectorBuckets_DeleteVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_DeleteVectors-request-keys"></a>
The keys of the vectors to delete.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [vectorBucketName](#API_S3VectorBuckets_DeleteVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_DeleteVectors-request-vectorBucketName"></a>
The name of the vector bucket that contains the vector index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

## Response Syntax
<a name="API_S3VectorBuckets_DeleteVectors_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_S3VectorBuckets_DeleteVectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_S3VectorBuckets_DeleteVectors_Errors"></a>

 ** AccessDeniedException **
Access denied.
HTTP Status Code: 403

 ** InternalServerException **
The request failed due to an internal server error.
HTTP Status Code: 500

 ** KmsDisabledException **
The specified AWS KMS key isn't enabled.
HTTP Status Code: 400

 ** KmsInvalidKeyUsageException **
The request was rejected for one of the following reasons:
+ The `KeyUsage` value of the KMS key is incompatible with the API operation.
+ The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key (`KeySpec`).
For more information, see [InvalidKeyUsageException](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors) in the * AWS Key Management Service API Reference*.
HTTP Status Code: 400

 ** KmsInvalidStateException **
The key state of the KMS key isn't compatible with the operation.
For more information, see [KMSInvalidStateException](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors) in the * AWS Key Management Service API Reference*.
HTTP Status Code: 400

 ** KmsNotFoundException **
The KMS key can't be found.
HTTP Status Code: 400

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
<a name="API_S3VectorBuckets_DeleteVectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/DeleteVectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3vectors-2025-07-15/DeleteVectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/DeleteVectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/DeleteVectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/DeleteVectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/DeleteVectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/DeleteVectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/DeleteVectors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/DeleteVectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/DeleteVectors)
