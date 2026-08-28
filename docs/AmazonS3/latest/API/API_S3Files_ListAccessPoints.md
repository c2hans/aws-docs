---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ListAccessPoints.html
---

# ListAccessPoints
<a name="API_S3Files_ListAccessPoints"></a>

Returns resource information for all S3 File System Access Points associated with the specified S3 File System.

## Request Syntax
<a name="API_S3Files_ListAccessPoints_RequestSyntax"></a>

```
GET /access-points?fileSystemId={{fileSystemId}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_S3Files_ListAccessPoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [fileSystemId](#API_S3Files_ListAccessPoints_RequestSyntax) **   <a name="AmazonS3-S3Files_ListAccessPoints-request-uri-fileSystemId"></a>
The ID or Amazon Resource Name (ARN) of the S3 File System to list access points for.
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`
Required: Yes

 ** [maxResults](#API_S3Files_ListAccessPoints_RequestSyntax) **   <a name="AmazonS3-S3Files_ListAccessPoints-request-uri-maxResults"></a>
The maximum number of access points to return in a single response.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_S3Files_ListAccessPoints_RequestSyntax) **   <a name="AmazonS3-S3Files_ListAccessPoints-request-uri-nextToken"></a>
A pagination token returned from a previous call to continue listing access points.

## Request Body
<a name="API_S3Files_ListAccessPoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_S3Files_ListAccessPoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accessPoints": [
      {
         "accessPointArn": "string",
         "accessPointId": "string",
         "fileSystemId": "string",
         "name": "string",
         "ownerId": "string",
         "posixUser": {
            "gid": number,
            "secondaryGids": [ number ],
            "uid": number
         },
         "rootDirectory": {
            "creationPermissions": {
               "ownerGid": number,
               "ownerUid": number,
               "permissions": "string"
            },
            "path": "string"
         },
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_S3Files_ListAccessPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessPoints](#API_S3Files_ListAccessPoints_ResponseSyntax) **   <a name="AmazonS3-S3Files_ListAccessPoints-response-accessPoints"></a>
An array of access point descriptions.
Type: Array of [ListAccessPointsDescription](API_S3Files_ListAccessPointsDescription.md) objects

 ** [nextToken](#API_S3Files_ListAccessPoints_ResponseSyntax) **   <a name="AmazonS3-S3Files_ListAccessPoints-response-nextToken"></a>
A pagination token to use in a subsequent request if more results are available.
Type: String

## Errors
<a name="API_S3Files_ListAccessPoints_Errors"></a>

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
<a name="API_S3Files_ListAccessPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/ListAccessPoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/ListAccessPoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/ListAccessPoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/ListAccessPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/ListAccessPoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/ListAccessPoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/ListAccessPoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/ListAccessPoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/ListAccessPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/ListAccessPoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
