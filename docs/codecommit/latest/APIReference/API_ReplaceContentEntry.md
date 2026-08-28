---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ReplaceContentEntry.html
---

# ReplaceContentEntry
<a name="API_ReplaceContentEntry"></a>

Information about a replacement content entry in the conflict of a merge or pull request operation.

## Contents
<a name="API_ReplaceContentEntry_Contents"></a>

 ** filePath **   <a name="CodeCommit-Type-ReplaceContentEntry-filePath"></a>
The path of the conflicting file.
Type: String
Required: Yes

 ** replacementType **   <a name="CodeCommit-Type-ReplaceContentEntry-replacementType"></a>
The replacement type to use when determining how to resolve the conflict.
Type: String
Valid Values: `KEEP_BASE | KEEP_SOURCE | KEEP_DESTINATION | USE_NEW_CONTENT`
Required: Yes

 ** content **   <a name="CodeCommit-Type-ReplaceContentEntry-content"></a>
The base-64 encoded content to use when the replacement type is USE\_NEW\_CONTENT.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 6291456.
Required: No

 ** fileMode **   <a name="CodeCommit-Type-ReplaceContentEntry-fileMode"></a>
The file mode to apply during conflict resoltion.
Type: String
Valid Values: `EXECUTABLE | NORMAL | SYMLINK`
Required: No

## See Also
<a name="API_ReplaceContentEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ReplaceContentEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ReplaceContentEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ReplaceContentEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
