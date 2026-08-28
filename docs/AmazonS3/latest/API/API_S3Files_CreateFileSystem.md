---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_CreateFileSystem.html
---

# CreateFileSystem
<a name="API_S3Files_CreateFileSystem"></a>

Creates an S3 File System resource scoped to a bucket or prefix within a bucket, enabling file system access to S3 data. To create a file system, you need an S3 bucket and an IAM role that grants the service permission to access the bucket.

## Request Syntax
<a name="API_S3Files_CreateFileSystem_RequestSyntax"></a>

```
PUT /file-systems HTTP/1.1
Content-type: application/json

{
   "acceptBucketWarning": {{boolean}},
   "bucket": "{{string}}",
   "clientToken": "{{string}}",
   "kmsKeyId": "{{string}}",
   "prefix": "{{string}}",
   "roleArn": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_S3Files_CreateFileSystem_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_S3Files_CreateFileSystem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [acceptBucketWarning](#API_S3Files_CreateFileSystem_RequestSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-request-acceptBucketWarning"></a>
Set to true to acknowledge and accept any warnings about the bucket configuration. If not specified, the operation may fail if there are bucket configuration warnings.
Type: Boolean
Required: No

 ** [bucket](#API_S3Files_CreateFileSystem_RequestSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-request-bucket"></a>
The Amazon Resource Name (ARN) of the S3 bucket that will be accessible through the file system. The bucket must exist and be in the same AWS Region as the file system.
Type: String
Pattern: `(arn:aws[a-zA-Z0-9-]*:s3:::.+)`
Required: Yes

 ** [clientToken](#API_S3Files_CreateFileSystem_RequestSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure idempotent creation. Up to 64 ASCII characters are allowed. If you don't specify a client token, the AWS SDK automatically generates one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(.+)`
Required: No

 ** [kmsKeyId](#API_S3Files_CreateFileSystem_RequestSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-request-kmsKeyId"></a>
The ARN, key ID, or alias of the AWS KMS key to use for encryption. If not specified, the service uses a service-owned key for encryption. You can specify a KMS key using the following formats: key ID, ARN, key alias, or key alias ARN. If you use `KmsKeyId`, the file system will be encrypted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|mrk-[0-9a-f]{32}|alias/[a-zA-Z0-9/_-]+|(arn:aws[-a-z]*:kms:[a-z0-9-]+:\d{12}:((key/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})|(key/mrk-[0-9a-f]{32})|(alias/[a-zA-Z0-9/_-]+))))`
Required: No

 ** [prefix](#API_S3Files_CreateFileSystem_RequestSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-request-prefix"></a>
An optional prefix within the S3 bucket to scope the file system access. If specified, the file system provides access only to objects with keys that begin with this prefix. If not specified, the file system provides access to the entire bucket.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(|.*/)`
Required: No

 ** [roleArn](#API_S3Files_CreateFileSystem_RequestSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-request-roleArn"></a>
The ARN of the IAM role that grants the S3 Files service permission to read and write data between the file system and the S3 bucket. This role must have the necessary permissions to access the specified bucket and prefix.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [tags](#API_S3Files_CreateFileSystem_RequestSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-request-tags"></a>
An array of key-value pairs to apply as tags to the file system resource. Each tag is a user-defined key-value pair. You can use tags to categorize and manage your file systems. Each key must be unique for the resource.
Type: Array of [Tag](API_S3Files_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_S3Files_CreateFileSystem_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "bucket": "string",
   "clientToken": "string",
   "creationTime": number,
   "fileSystemArn": "string",
   "fileSystemId": "string",
   "kmsKeyId": "string",
   "name": "string",
   "ownerId": "string",
   "prefix": "string",
   "roleArn": "string",
   "status": "string",
   "statusMessage": "string",
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_S3Files_CreateFileSystem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [bucket](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-bucket"></a>
The Amazon Resource Name (ARN) of the S3 bucket associated with the file system.
Type: String
Pattern: `(arn:aws[a-zA-Z0-9-]*:s3:::.+)`

 ** [clientToken](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-clientToken"></a>
The client token used for idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(.+)`

 ** [creationTime](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-creationTime"></a>
The time when the file system was created, in seconds since 1970-01-01T00:00:00Z (Unix epoch time).
Type: Timestamp

 ** [fileSystemArn](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-fileSystemArn"></a>
The ARN for the S3 file system, in the format `arn:aws:s3files:region:account-id:file-system/file-system-id`.
Type: String
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40})`

 ** [fileSystemId](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-fileSystemId"></a>
The ID of the file system, assigned by S3 Files. This ID is used to reference the file system in subsequent API calls.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`

 ** [kmsKeyId](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-kmsKeyId"></a>
The ARN or alias of the AWS KMS key used for encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|mrk-[0-9a-f]{32}|alias/[a-zA-Z0-9/_-]+|(arn:aws[-a-z]*:kms:[a-z0-9-]+:\d{12}:((key/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})|(key/mrk-[0-9a-f]{32})|(alias/[a-zA-Z0-9/_-]+))))`

 ** [name](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-name"></a>
The name of the file system, derived from the `Name` tag if present.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

 ** [ownerId](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-ownerId"></a>
The AWS account ID of the file system owner.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `(\d{12})|(\d{4}-{4}-\d{4})`

 ** [prefix](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-prefix"></a>
The prefix within the S3 bucket that scopes the file system access.
Type: String

 ** [roleArn](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-roleArn"></a>
The ARN of the IAM role used for S3 access.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [status](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-status"></a>
The lifecycle state of the file system. Valid values are: `AVAILABLE` (the file system is available for use), `CREATING` (the file system is being created), `DELETING` (the file system is being deleted), `DELETED` (the file system has been deleted), `ERROR` (the file system is in an error state), or `UPDATING` (the file system is being updated).
Type: String
Valid Values: `available | creating | deleting | deleted | error | updating`

 ** [statusMessage](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-statusMessage"></a>
Additional information about the file system status. This field provides more details when the status is `ERROR`, or during state transitions.
Type: String

 ** [tags](#API_S3Files_CreateFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_CreateFileSystem-response-tags"></a>
The tags associated with the file system.
Type: Array of [Tag](API_S3Files_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

## Errors
<a name="API_S3Files_CreateFileSystem_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would exceed a service quota. Review your service quotas and either delete resources or request a quota increase.
 ** errorCode **
The error code associated with the exception.
HTTP Status Code: 402

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
<a name="API_S3Files_CreateFileSystem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/CreateFileSystem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/CreateFileSystem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/CreateFileSystem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/CreateFileSystem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/CreateFileSystem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/CreateFileSystem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/CreateFileSystem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/CreateFileSystem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/CreateFileSystem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/CreateFileSystem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
