---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_DeleteMountTarget.html
---

# DeleteMountTarget
<a name="API_S3Files_DeleteMountTarget"></a>

Deletes the specified mount target. This operation is irreversible.

## Request Syntax
<a name="API_S3Files_DeleteMountTarget_RequestSyntax"></a>

```
DELETE /mount-targets/{{mountTargetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_S3Files_DeleteMountTarget_RequestParameters"></a>

The request uses the following URI parameters.

 ** [mountTargetId](#API_S3Files_DeleteMountTarget_RequestSyntax) **   <a name="AmazonS3-S3Files_DeleteMountTarget-request-uri-mountTargetId"></a>
The ID of the mount target to delete.
Length Constraints: Minimum length of 22. Maximum length of 45.
Pattern: `fsmt-[0-9a-f]{17,40}`
Required: Yes

## Request Body
<a name="API_S3Files_DeleteMountTarget_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_S3Files_DeleteMountTarget_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_S3Files_DeleteMountTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_S3Files_DeleteMountTarget_Errors"></a>

 ** ConflictException **
The request conflicts with the current state of the resource. This can occur when trying to create a resource that already exists or delete a resource that is in use.
 ** errorCode **
The error code associated with the exception.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of the resource that caused the conflict.
HTTP Status Code: 409

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
<a name="API_S3Files_DeleteMountTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/DeleteMountTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/DeleteMountTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/DeleteMountTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/DeleteMountTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/DeleteMountTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/DeleteMountTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/DeleteMountTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/DeleteMountTarget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/DeleteMountTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/DeleteMountTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
