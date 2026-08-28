---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteFileSystemOpenZFSConfiguration.html
---

# DeleteFileSystemOpenZFSConfiguration
<a name="API_DeleteFileSystemOpenZFSConfiguration"></a>

The configuration object for the Amazon FSx for OpenZFS file system used in the `DeleteFileSystem` operation.

## Contents
<a name="API_DeleteFileSystemOpenZFSConfiguration_Contents"></a>

 ** FinalBackupTags **   <a name="FSx-Type-DeleteFileSystemOpenZFSConfiguration-FinalBackupTags"></a>
A list of tags to apply to the file system's final backup.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Options **   <a name="FSx-Type-DeleteFileSystemOpenZFSConfiguration-Options"></a>
To delete a file system if there are child volumes present below the root volume, use the string `DELETE_CHILD_VOLUMES_AND_SNAPSHOTS`. If your file system has child volumes and you don't use this option, the delete request will fail.
Type: Array of strings
Array Members: Maximum number of 1 item.
Valid Values: `DELETE_CHILD_VOLUMES_AND_SNAPSHOTS`
Required: No

 ** SkipFinalBackup **   <a name="FSx-Type-DeleteFileSystemOpenZFSConfiguration-SkipFinalBackup"></a>
By default, Amazon FSx for OpenZFS takes a final backup on your behalf when the `DeleteFileSystem` operation is invoked. Doing this helps protect you from data loss, and we highly recommend taking the final backup. If you want to skip taking a final backup, set this value to `true`.
Type: Boolean
Required: No

## See Also
<a name="API_DeleteFileSystemOpenZFSConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteFileSystemOpenZFSConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteFileSystemOpenZFSConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteFileSystemOpenZFSConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
