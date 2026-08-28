---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteFileSystemWindowsConfiguration.html
---

# DeleteFileSystemWindowsConfiguration
<a name="API_DeleteFileSystemWindowsConfiguration"></a>

The configuration object for the Microsoft Windows file system used in the `DeleteFileSystem` operation.

## Contents
<a name="API_DeleteFileSystemWindowsConfiguration_Contents"></a>

 ** FinalBackupTags **   <a name="FSx-Type-DeleteFileSystemWindowsConfiguration-FinalBackupTags"></a>
A set of tags for your final backup.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** SkipFinalBackup **   <a name="FSx-Type-DeleteFileSystemWindowsConfiguration-SkipFinalBackup"></a>
By default, Amazon FSx for Windows takes a final backup on your behalf when the `DeleteFileSystem` operation is invoked. Doing this helps protect you from data loss, and we highly recommend taking the final backup. If you want to skip this backup, use this flag to do so.
Type: Boolean
Required: No

## See Also
<a name="API_DeleteFileSystemWindowsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteFileSystemWindowsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteFileSystemWindowsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteFileSystemWindowsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
