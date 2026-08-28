---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_SourceFileSpecifier.html
---

# SourceFileSpecifier
<a name="API_SourceFileSpecifier"></a>

Information about a source file that is part of changes made in a commit.

## Contents
<a name="API_SourceFileSpecifier_Contents"></a>

 ** filePath **   <a name="CodeCommit-Type-SourceFileSpecifier-filePath"></a>
The full path to the file, including the name of the file.
Type: String
Required: Yes

 ** isMove **   <a name="CodeCommit-Type-SourceFileSpecifier-isMove"></a>
Whether to remove the source file from the parent commit.
Type: Boolean
Required: No

## See Also
<a name="API_SourceFileSpecifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/SourceFileSpecifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/SourceFileSpecifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/SourceFileSpecifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
