---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ListMountTargets.html
---

# ListMountTargets
<a name="API_S3Files_ListMountTargets"></a>

Returns resource information for all mount targets with optional filtering by file system, access point, and VPC.

## Request Syntax
<a name="API_S3Files_ListMountTargets_RequestSyntax"></a>

```
GET /mount-targets?accessPointId={{accessPointId}}&fileSystemId={{fileSystemId}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_S3Files_ListMountTargets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessPointId](#API_S3Files_ListMountTargets_RequestSyntax) **   <a name="AmazonS3-S3Files_ListMountTargets-request-uri-accessPointId"></a>
Optional filter to list only mount targets associated with the specified access point ID or Amazon Resource Name (ARN).
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}|fsap-[0-9a-f]{17,40})`

 ** [fileSystemId](#API_S3Files_ListMountTargets_RequestSyntax) **   <a name="AmazonS3-S3Files_ListMountTargets-request-uri-fileSystemId"></a>
Optional filter to list only mount targets associated with the specified S3 File System ID or Amazon Resource Name (ARN). If provided, only mount targets for this file system will be returned in the response.
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`

 ** [maxResults](#API_S3Files_ListMountTargets_RequestSyntax) **   <a name="AmazonS3-S3Files_ListMountTargets-request-uri-maxResults"></a>
The maximum number of mount targets to return in a single response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_S3Files_ListMountTargets_RequestSyntax) **   <a name="AmazonS3-S3Files_ListMountTargets-request-uri-nextToken"></a>
A pagination token returned from a previous call to continue listing mount targets.

## Request Body
<a name="API_S3Files_ListMountTargets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_S3Files_ListMountTargets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "mountTargets": [
      {
         "availabilityZoneId": "string",
         "fileSystemId": "string",
         "ipv4Address": "string",
         "ipv6Address": "string",
         "mountTargetId": "string",
         "networkInterfaceId": "string",
         "ownerId": "string",
         "status": "string",
         "statusMessage": "string",
         "subnetId": "string",
         "vpcId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_S3Files_ListMountTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [mountTargets](#API_S3Files_ListMountTargets_ResponseSyntax) **   <a name="AmazonS3-S3Files_ListMountTargets-response-mountTargets"></a>
An array of mount target descriptions.
Type: Array of [ListMountTargetsDescription](API_S3Files_ListMountTargetsDescription.md) objects

 ** [nextToken](#API_S3Files_ListMountTargets_ResponseSyntax) **   <a name="AmazonS3-S3Files_ListMountTargets-response-nextToken"></a>
A pagination token to use in a subsequent request if more results are available.
Type: String

## Errors
<a name="API_S3Files_ListMountTargets_Errors"></a>

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
<a name="API_S3Files_ListMountTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/ListMountTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/ListMountTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/ListMountTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/ListMountTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/ListMountTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/ListMountTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/ListMountTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/ListMountTargets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/ListMountTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/ListMountTargets)
