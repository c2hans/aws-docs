---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PutFileEntry.html
---

# PutFileEntry
<a name="API_PutFileEntry"></a>

Information about a file added or updated as part of a commit.

## Contents
<a name="API_PutFileEntry_Contents"></a>

 ** filePath **   <a name="CodeCommit-Type-PutFileEntry-filePath"></a>
The full path to the file in the repository, including the name of the file.
Type: String
Required: Yes

 ** fileContent **   <a name="CodeCommit-Type-PutFileEntry-fileContent"></a>
The content of the file, if a source file is not specified.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 6291456.
Required: No

 ** fileMode **   <a name="CodeCommit-Type-PutFileEntry-fileMode"></a>
The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.
Type: String
Valid Values: `EXECUTABLE | NORMAL | SYMLINK`
Required: No

 ** sourceFile **   <a name="CodeCommit-Type-PutFileEntry-sourceFile"></a>
The name and full path of the file that contains the changes you want to make as part of the commit, if you are not providing the file content directly.
Type: [SourceFileSpecifier](API_SourceFileSpecifier.md) object
Required: No

## See Also
<a name="API_PutFileEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/PutFileEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/PutFileEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/PutFileEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
