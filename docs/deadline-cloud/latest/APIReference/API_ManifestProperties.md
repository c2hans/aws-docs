---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ManifestProperties.html
---

# ManifestProperties
<a name="API_ManifestProperties"></a>

The details of the manifest that links a job's source information.

## Contents
<a name="API_ManifestProperties_Contents"></a>

 ** rootPath **   <a name="deadlinecloud-Type-ManifestProperties-rootPath"></a>
The file's root path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** rootPathFormat **   <a name="deadlinecloud-Type-ManifestProperties-rootPathFormat"></a>
The format of the root path.
Type: String
Valid Values: `windows | posix`
Required: Yes

 ** fileSystemLocationName **   <a name="deadlinecloud-Type-ManifestProperties-fileSystemLocationName"></a>
The file system location name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9A-Za-z ]*`
Required: No

 ** inputManifestHash **   <a name="deadlinecloud-Type-ManifestProperties-inputManifestHash"></a>
The hash value of the file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** inputManifestPath **   <a name="deadlinecloud-Type-ManifestProperties-inputManifestPath"></a>
The file path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** outputRelativeDirectories **   <a name="deadlinecloud-Type-ManifestProperties-outputRelativeDirectories"></a>
The file path relative to the directory.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ManifestProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ManifestProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ManifestProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ManifestProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
