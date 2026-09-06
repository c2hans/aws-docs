---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_GetMountTarget.html
---

# GetMountTarget
<a name="API_S3Files_GetMountTarget"></a>

Returns detailed resource information for the specified mount target including network configuration.

## Request Syntax
<a name="API_S3Files_GetMountTarget_RequestSyntax"></a>

```
GET /mount-targets/{{mountTargetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_S3Files_GetMountTarget_RequestParameters"></a>

The request uses the following URI parameters.

 ** [mountTargetId](#API_S3Files_GetMountTarget_RequestSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-request-uri-mountTargetId"></a>
The ID of the mount target to retrieve information for.
Length Constraints: Minimum length of 22. Maximum length of 45.
Pattern: `fsmt-[0-9a-f]{17,40}`
Required: Yes

## Request Body
<a name="API_S3Files_GetMountTarget_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_S3Files_GetMountTarget_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "availabilityZoneId": "string",
   "fileSystemId": "string",
   "ipv4Address": "string",
   "ipv6Address": "string",
   "mountTargetId": "string",
   "networkInterfaceId": "string",
   "ownerId": "string",
   "securityGroups": [ "string" ],
   "status": "string",
   "statusMessage": "string",
   "subnetId": "string",
   "vpcId": "string"
}
```

## Response Elements
<a name="API_S3Files_GetMountTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [availabilityZoneId](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-availabilityZoneId"></a>
The Availability Zone ID where the mount target is located.
Type: String

 ** [fileSystemId](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-fileSystemId"></a>
The ID of the file system.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`

 ** [ipv4Address](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-ipv4Address"></a>
The IPv4 address of the mount target.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 15.
Pattern: `[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}`

 ** [ipv6Address](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-ipv6Address"></a>
The IPv6 address of the mount target.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 39.

 ** [mountTargetId](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-mountTargetId"></a>
The ID of the mount target.
Type: String
Length Constraints: Minimum length of 22. Maximum length of 45.
Pattern: `fsmt-[0-9a-f]{17,40}`

 ** [networkInterfaceId](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-networkInterfaceId"></a>
The ID of the network interface associated with the mount target.
Type: String

 ** [ownerId](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-ownerId"></a>
The AWS account ID of the mount target owner.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `(\d{12})|(\d{4}-{4}-\d{4})`

 ** [securityGroups](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-securityGroups"></a>
The security groups associated with the mount target.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 11. Maximum length of 43.
Pattern: `(sg-[0-9a-f]{8,40})`

 ** [status](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-status"></a>
The current status of the mount target.
Type: String
Valid Values: `available | creating | deleting | deleted | error | updating`

 ** [statusMessage](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-statusMessage"></a>
Additional information about the mount target status.
Type: String

 ** [subnetId](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-subnetId"></a>
The ID of the subnet where the mount target is located.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 47.
Pattern: `subnet-[0-9a-f]{8,40}`

 ** [vpcId](#API_S3Files_GetMountTarget_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetMountTarget-response-vpcId"></a>
The ID of the VPC where the mount target is located.
Type: String

## Errors
<a name="API_S3Files_GetMountTarget_Errors"></a>

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
<a name="API_S3Files_GetMountTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/GetMountTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/GetMountTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/GetMountTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/GetMountTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/GetMountTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/GetMountTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/GetMountTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/GetMountTarget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/GetMountTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/GetMountTarget)
