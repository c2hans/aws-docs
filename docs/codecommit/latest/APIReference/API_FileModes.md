---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_FileModes.html
---

# FileModes
<a name="API_FileModes"></a>

Information about file modes in a merge or pull request.

## Contents
<a name="API_FileModes_Contents"></a>

 ** base **   <a name="CodeCommit-Type-FileModes-base"></a>
The file mode of a file in the base of a merge or pull request.
Type: String
Valid Values: `EXECUTABLE | NORMAL | SYMLINK`
Required: No

 ** destination **   <a name="CodeCommit-Type-FileModes-destination"></a>
The file mode of a file in the destination of a merge or pull request.
Type: String
Valid Values: `EXECUTABLE | NORMAL | SYMLINK`
Required: No

 ** source **   <a name="CodeCommit-Type-FileModes-source"></a>
The file mode of a file in the source of a merge or pull request.
Type: String
Valid Values: `EXECUTABLE | NORMAL | SYMLINK`
Required: No

## See Also
<a name="API_FileModes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/FileModes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/FileModes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/FileModes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
