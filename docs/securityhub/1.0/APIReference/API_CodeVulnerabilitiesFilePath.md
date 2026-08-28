---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CodeVulnerabilitiesFilePath.html
---

# CodeVulnerabilitiesFilePath
<a name="API_CodeVulnerabilitiesFilePath"></a>

 Provides details about where a code vulnerability is located in your AWS Lambda function.

## Contents
<a name="API_CodeVulnerabilitiesFilePath_Contents"></a>

 ** EndLine **   <a name="securityhub-Type-CodeVulnerabilitiesFilePath-EndLine"></a>
 The line number of the last line of code in which the vulnerability is located.
Type: Integer
Required: No

 ** FileName **   <a name="securityhub-Type-CodeVulnerabilitiesFilePath-FileName"></a>
 The name of the file in which the code vulnerability is located.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FilePath **   <a name="securityhub-Type-CodeVulnerabilitiesFilePath-FilePath"></a>
 The file path to the code in which the vulnerability is located.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StartLine **   <a name="securityhub-Type-CodeVulnerabilitiesFilePath-StartLine"></a>
 The line number of the first line of code in which the vulnerability is located.
Type: Integer
Required: No

## See Also
<a name="API_CodeVulnerabilitiesFilePath_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CodeVulnerabilitiesFilePath)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CodeVulnerabilitiesFilePath)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CodeVulnerabilitiesFilePath)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
