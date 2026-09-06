---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_s3Buckets_ListTagsForResource"></a>

Lists all of the tags applied to a specified Amazon S3 Tables resource. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to resources.

**Note**
For a list of S3 resources that support tagging, see [Managing tags for Amazon S3 resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags).

Permissions
For tables and table buckets, you must have the `s3tables:ListTagsForResource` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_ListTagsForResource_RequestSyntax"></a>

```
GET /tag/{{resourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_s3Buckets_ListTagsForResource_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTagsForResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 Tables resource that you want to list tags for. The tagged resource can be a table bucket or a table. For a list of all S3 resources that support tagging, see [Managing tags for Amazon S3 resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags).
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/.+`
Required: Yes

## Request Body
<a name="API_s3Buckets_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_s3Buckets_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_s3Buckets_ListTagsForResource_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_ListTagsForResource-response-tags"></a>
The user-defined tags that are applied to the resource. For more information, see [Tagging for cost allocation or attribute-based access control (ABAC)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html).
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_s3Buckets_ListTagsForResource_Errors"></a>

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
<a name="API_s3Buckets_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/ListTagsForResource)
