---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeFilePath.html
---

# CodeFilePath
<a name="API_CodeFilePath"></a>

Contains information on where a code vulnerability is located in your Lambda function.

## Contents
<a name="API_CodeFilePath_Contents"></a>

 ** endLine **   <a name="inspector2-Type-CodeFilePath-endLine"></a>
The line number of the last line of code that a vulnerability was found in.
Type: Integer
Required: Yes

 ** fileName **   <a name="inspector2-Type-CodeFilePath-fileName"></a>
The name of the file the code vulnerability was found in.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** filePath **   <a name="inspector2-Type-CodeFilePath-filePath"></a>
The file path to the code that a vulnerability was found in.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** startLine **   <a name="inspector2-Type-CodeFilePath-startLine"></a>
The line number of the first line of code that a vulnerability was found in.
Type: Integer
Required: Yes

## See Also
<a name="API_CodeFilePath_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeFilePath)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeFilePath)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeFilePath)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
