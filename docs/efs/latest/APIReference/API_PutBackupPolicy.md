---
source_url: https://docs.aws.amazon.com/efs/latest/APIReference/API_PutBackupPolicy.html
---

# PutBackupPolicy
<a name="API_PutBackupPolicy"></a>

Updates the file system's backup policy. Use this action to start or stop automatic backups of the file system.

## Request Syntax
<a name="API_PutBackupPolicy_RequestSyntax"></a>

```
PUT /2015-02-01/file-systems/{{FileSystemId}}/backup-policy HTTP/1.1
Content-type: application/json

{
   "BackupPolicy": {
      "Status": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_PutBackupPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FileSystemId](#API_PutBackupPolicy_RequestSyntax) **   <a name="efs-PutBackupPolicy-request-uri-FileSystemId"></a>
Specifies which EFS file system to update the backup policy for.
Length Constraints: Maximum length of 128.
Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`
Required: Yes

## Request Body
<a name="API_PutBackupPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BackupPolicy](#API_PutBackupPolicy_RequestSyntax) **   <a name="efs-PutBackupPolicy-request-BackupPolicy"></a>
The backup policy included in the `PutBackupPolicy` request.
Type: [BackupPolicy](API_BackupPolicy.md) object
Required: Yes

## Response Syntax
<a name="API_PutBackupPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupPolicy": {
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_PutBackupPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupPolicy](#API_PutBackupPolicy_ResponseSyntax) **   <a name="efs-PutBackupPolicy-response-BackupPolicy"></a>
Describes the file system's backup policy, indicating whether automatic backups are turned on or off.
Type: [BackupPolicy](API_BackupPolicy.md) object

## Errors
<a name="API_PutBackupPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **
Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 400

 ** FileSystemNotFound **
Returned if the specified `FileSystemId` value doesn't exist in the requester's AWS account.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 404

 ** IncorrectFileSystemLifeCycleState **
Returned if the file system's lifecycle state is not "available".
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 409

 ** InternalServerError **
Returned if an error occurred on the server side.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 500

 ** ValidationException **
Returned if the AWS Backup service is not available in the AWS Region in which the request was made.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 400

## See Also
<a name="API_PutBackupPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticfilesystem-2015-02-01/PutBackupPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticfilesystem-2015-02-01/PutBackupPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticfilesystem-2015-02-01/PutBackupPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticfilesystem-2015-02-01/PutBackupPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticfilesystem-2015-02-01/PutBackupPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/PutBackupPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticfilesystem-2015-02-01/PutBackupPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticfilesystem-2015-02-01/PutBackupPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticfilesystem-2015-02-01/PutBackupPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticfilesystem-2015-02-01/PutBackupPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
