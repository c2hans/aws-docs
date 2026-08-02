---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_S3Files_ListTagsForResource"></a>

Lists all tags for S3 Files resources.

## Request Syntax
<a name="API_S3Files_ListTagsForResource_RequestSyntax"></a>

```
GET /resource-tags/{{resourceId}}?MaxResults={{maxResults}}&NextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_S3Files_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_S3Files_ListTagsForResource_RequestSyntax) **   <a name="AmazonS3-S3Files_ListTagsForResource-request-uri-maxResults"></a>
The maximum number of tags to return in a single response.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_S3Files_ListTagsForResource_RequestSyntax) **   <a name="AmazonS3-S3Files_ListTagsForResource-request-uri-nextToken"></a>
A pagination token returned from a previous call to continue listing tags.

 ** [resourceId](#API_S3Files_ListTagsForResource_RequestSyntax) **   <a name="AmazonS3-S3Files_ListTagsForResource-request-uri-resourceId"></a>
The ID or Amazon Resource Name (ARN) of the resource to list tags for.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}(/access-point/fsap-[0-9a-f]{17,40})?|fs(ap)?-[0-9a-f]{17,40})`
Required: Yes

## Request Body
<a name="API_S3Files_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_S3Files_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_S3Files_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_S3Files_ListTagsForResource_ResponseSyntax) **   <a name="AmazonS3-S3Files_ListTagsForResource-response-nextToken"></a>
A pagination token to use in a subsequent request if more results are available.
Type: String

 ** [tags](#API_S3Files_ListTagsForResource_ResponseSyntax) **   <a name="AmazonS3-S3Files_ListTagsForResource-response-tags"></a>
An array of tags associated with the resource.
Type: Array of [Tag](API_S3Files_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

## Errors
<a name="API_S3Files_ListTagsForResource_Errors"></a>

 ** InternalServerException **
An internal server error occurred. Retry your request.
 ** errorCode **
The error code associated with the exception.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource exists and that you have permission to access it.
 ** errorCode **
The error code associated with the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled. Retry your request using exponential backoff.
 ** errorCode **
The error code associated with the exception.
HTTP Status Code: 429

 ** ValidationException **
The input parameters are not valid. Check the parameter values and try again.
 ** errorCode **
The error code associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_S3Files_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/ListTagsForResource)
