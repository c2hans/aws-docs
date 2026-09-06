---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ListFileSystems.html
---

# ListFileSystems
<a name="API_S3Files_ListFileSystems"></a>

Returns a list of all S3 File Systems owned by the account with optional filtering by bucket.

## Request Syntax
<a name="API_S3Files_ListFileSystems_RequestSyntax"></a>

```
GET /file-systems?bucket={{bucket}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_S3Files_ListFileSystems_RequestParameters"></a>

The request uses the following URI parameters.

 ** [bucket](#API_S3Files_ListFileSystems_RequestSyntax) **   <a name="AmazonS3-S3Files_ListFileSystems-request-uri-bucket"></a>
Optional filter to list only file systems associated with the specified S3 bucket Amazon Resource Name (ARN). If provided, only file systems that provide access to this bucket will be returned in the response.
Pattern: `(arn:aws[a-zA-Z0-9-]*:s3:::.+)`

 ** [maxResults](#API_S3Files_ListFileSystems_RequestSyntax) **   <a name="AmazonS3-S3Files_ListFileSystems-request-uri-maxResults"></a>
The maximum number of file systems to return in a single response. If not specified, up to 100 file systems are returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_S3Files_ListFileSystems_RequestSyntax) **   <a name="AmazonS3-S3Files_ListFileSystems-request-uri-nextToken"></a>
A pagination token returned from a previous call to continue listing file systems.

## Request Body
<a name="API_S3Files_ListFileSystems_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_S3Files_ListFileSystems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "fileSystems": [
      {
         "bucket": "string",
         "creationTime": number,
         "fileSystemArn": "string",
         "fileSystemId": "string",
         "name": "string",
         "ownerId": "string",
         "roleArn": "string",
         "status": "string",
         "statusMessage": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_S3Files_ListFileSystems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fileSystems](#API_S3Files_ListFileSystems_ResponseSyntax) **   <a name="AmazonS3-S3Files_ListFileSystems-response-fileSystems"></a>
An array of file system descriptions.
Type: Array of [ListFileSystemsDescription](API_S3Files_ListFileSystemsDescription.md) objects

 ** [nextToken](#API_S3Files_ListFileSystems_ResponseSyntax) **   <a name="AmazonS3-S3Files_ListFileSystems-response-nextToken"></a>
A pagination token to use in a subsequent request if more results are available.
Type: String

## Errors
<a name="API_S3Files_ListFileSystems_Errors"></a>

 ** InternalServerException **
An internal server error occurred. Retry your request.
 ** errorCode **
The error code associated with the exception.
HTTP Status Code: 500

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
<a name="API_S3Files_ListFileSystems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/ListFileSystems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/ListFileSystems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/ListFileSystems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/ListFileSystems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/ListFileSystems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/ListFileSystems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/ListFileSystems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/ListFileSystems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/ListFileSystems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/ListFileSystems)
