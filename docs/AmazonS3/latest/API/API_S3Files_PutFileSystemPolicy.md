---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_PutFileSystemPolicy.html
---

# PutFileSystemPolicy
<a name="API_S3Files_PutFileSystemPolicy"></a>

Creates or replaces the IAM resource policy for an S3 File System to control access permissions.

## Request Syntax
<a name="API_S3Files_PutFileSystemPolicy_RequestSyntax"></a>

```
PUT /file-systems/{{fileSystemId}}/policy HTTP/1.1
Content-type: application/json

{
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_S3Files_PutFileSystemPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [fileSystemId](#API_S3Files_PutFileSystemPolicy_RequestSyntax) **   <a name="AmazonS3-S3Files_PutFileSystemPolicy-request-uri-fileSystemId"></a>
The ID or Amazon Resource Name (ARN) of the S3 File System to apply the resource policy to.
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`
Required: Yes

## Request Body
<a name="API_S3Files_PutFileSystemPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policy](#API_S3Files_PutFileSystemPolicy_RequestSyntax) **   <a name="AmazonS3-S3Files_PutFileSystemPolicy-request-policy"></a>
The JSON-formatted resource policy to apply to the file system. The policy defines the permissions for accessing the file system. The policy must be a valid JSON document that follows IAM policy syntax.
Type: String
Required: Yes

## Response Syntax
<a name="API_S3Files_PutFileSystemPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_S3Files_PutFileSystemPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_S3Files_PutFileSystemPolicy_Errors"></a>

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
<a name="API_S3Files_PutFileSystemPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/PutFileSystemPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/PutFileSystemPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/PutFileSystemPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/PutFileSystemPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/PutFileSystemPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/PutFileSystemPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/PutFileSystemPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/PutFileSystemPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/PutFileSystemPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/PutFileSystemPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
