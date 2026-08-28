---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FolderSummary.html
---

# FolderSummary
<a name="API_FolderSummary"></a>

A summary of information about an existing Quick Sight folder.

## Contents
<a name="API_FolderSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-FolderSummary-Arn"></a>
The Amazon Resource Name (ARN) of the folder.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-FolderSummary-CreatedTime"></a>
The time that the folder was created.
Type: Timestamp
Required: No

 ** FolderId **   <a name="QS-Type-FolderSummary-FolderId"></a>
The ID of the folder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+`
Required: No

 ** FolderType **   <a name="QS-Type-FolderSummary-FolderType"></a>
The type of folder.
Type: String
Valid Values: `SHARED | RESTRICTED`
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-FolderSummary-LastUpdatedTime"></a>
The time that the folder was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-FolderSummary-Name"></a>
The display name of the folder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** SharingModel **   <a name="QS-Type-FolderSummary-SharingModel"></a>
The sharing scope of the folder.
Type: String
Valid Values: `ACCOUNT | NAMESPACE`
Required: No

## See Also
<a name="API_FolderSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FolderSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FolderSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FolderSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
