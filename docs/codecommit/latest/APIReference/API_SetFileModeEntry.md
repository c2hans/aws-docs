---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_SetFileModeEntry.html
---

# SetFileModeEntry
<a name="API_SetFileModeEntry"></a>

Information about the file mode changes.

## Contents
<a name="API_SetFileModeEntry_Contents"></a>

 ** fileMode **   <a name="CodeCommit-Type-SetFileModeEntry-fileMode"></a>
The file mode for the file.
Type: String
Valid Values: `EXECUTABLE | NORMAL | SYMLINK`
Required: Yes

 ** filePath **   <a name="CodeCommit-Type-SetFileModeEntry-filePath"></a>
The full path to the file, including the name of the file.
Type: String
Required: Yes

## See Also
<a name="API_SetFileModeEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/SetFileModeEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/SetFileModeEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/SetFileModeEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
