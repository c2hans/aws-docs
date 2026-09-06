---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketPolicy.html
---

# PutTableBucketPolicy
<a name="API_s3Buckets_PutTableBucketPolicy"></a>

Creates a new table bucket policy or replaces an existing table bucket policy for a table bucket. For more information, see [Adding a table bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-add) in the *Amazon Simple Storage Service User Guide*.

Permissions
You must have the `s3tables:PutTableBucketPolicy` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_PutTableBucketPolicy_RequestSyntax"></a>

```
PUT /buckets/{{tableBucketARN}}/policy HTTP/1.1
Content-type: application/json

{
   "resourcePolicy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_s3Buckets_PutTableBucketPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableBucketARN](#API_s3Buckets_PutTableBucketPolicy_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketPolicy-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_PutTableBucketPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourcePolicy](#API_s3Buckets_PutTableBucketPolicy_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketPolicy-request-resourcePolicy"></a>
The `JSON` that defines the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Required: Yes

## Response Syntax
<a name="API_s3Buckets_PutTableBucketPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_s3Buckets_PutTableBucketPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_s3Buckets_PutTableBucketPolicy_Errors"></a>

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
<a name="API_s3Buckets_PutTableBucketPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTableBucketPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/PutTableBucketPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTableBucketPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTableBucketPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTableBucketPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTableBucketPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTableBucketPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTableBucketPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTableBucketPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTableBucketPolicy)
