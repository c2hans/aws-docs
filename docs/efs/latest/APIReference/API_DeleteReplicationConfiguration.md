---
source_url: https://docs.aws.amazon.com/efs/latest/APIReference/API_DeleteReplicationConfiguration.html
---

# DeleteReplicationConfiguration
<a name="API_DeleteReplicationConfiguration"></a>

Deletes a replication configuration. Deleting a replication configuration ends the replication process. After a replication configuration is deleted, the destination file system becomes `Writeable` and its replication overwrite protection is re-enabled. For more information, see [Delete a replication configuration](https://docs.aws.amazon.com/efs/latest/ug/delete-replications.html).

This operation requires permissions for the `elasticfilesystem:DeleteReplicationConfiguration` action.

## Request Syntax
<a name="API_DeleteReplicationConfiguration_RequestSyntax"></a>

```
DELETE /2015-02-01/file-systems/{{SourceFileSystemId}}/replication-configuration?deletionMode={{DeletionMode}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteReplicationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeletionMode](#API_DeleteReplicationConfiguration_RequestSyntax) **   <a name="efs-DeleteReplicationConfiguration-request-uri-DeletionMode"></a>
When replicating across AWS accounts or across AWS Regions, Amazon EFS deletes the replication configuration from both the source and destination account or Region (`ALL_CONFIGURATIONS`) by default. If there's a configuration or permissions issue that prevents Amazon EFS from deleting the replication configuration from both sides, you can use the `LOCAL_CONFIGURATION_ONLY` mode to delete the replication configuration from only the local side (the account or Region from which the delete is performed).
Only use the `LOCAL_CONFIGURATION_ONLY` mode in the case that Amazon EFS is unable to delete the replication configuration in both the source and destination account or Region. Deleting the local configuration leaves the configuration in the other account or Region unrecoverable.
Additionally, do not use this mode for same-account, same-region replication as doing so results in a BadRequest exception error.
Valid Values: `ALL_CONFIGURATIONS | LOCAL_CONFIGURATION_ONLY`

 ** [SourceFileSystemId](#API_DeleteReplicationConfiguration_RequestSyntax) **   <a name="efs-DeleteReplicationConfiguration-request-uri-SourceFileSystemId"></a>
The ID of the source file system in the replication configuration.
Length Constraints: Maximum length of 128.
Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`
Required: Yes

## Request Body
<a name="API_DeleteReplicationConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteReplicationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteReplicationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteReplicationConfiguration_Errors"></a>

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

 ** InternalServerError **
Returned if an error occurred on the server side.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 500

 ** ReplicationNotFound **
Returned if the specified file system does not have a replication configuration.
 ** ErrorCode **
ReplicationNotFound
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 404

## See Also
<a name="API_DeleteReplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticfilesystem-2015-02-01/DeleteReplicationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticfilesystem-2015-02-01/DeleteReplicationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticfilesystem-2015-02-01/DeleteReplicationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticfilesystem-2015-02-01/DeleteReplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DeleteReplicationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DeleteReplicationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticfilesystem-2015-02-01/DeleteReplicationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DeleteReplicationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticfilesystem-2015-02-01/DeleteReplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DeleteReplicationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
