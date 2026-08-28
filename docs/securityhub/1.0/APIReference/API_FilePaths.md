---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FilePaths.html
---

# FilePaths
<a name="API_FilePaths"></a>

Provides information about the file paths that were affected by the threat.

## Contents
<a name="API_FilePaths_Contents"></a>

 ** FileName **   <a name="securityhub-Type-FilePaths-FileName"></a>
The name of the infected or suspicious file corresponding to the hash.
Length Constraints: Minimum of 1 length. Maximum of 128 length.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FilePath **   <a name="securityhub-Type-FilePaths-FilePath"></a>
Path to the infected or suspicious file on the resource it was detected on.
Length Constraints: Minimum of 1 length. Maximum of 128 length.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Hash **   <a name="securityhub-Type-FilePaths-Hash"></a>
The hash value for the infected or suspicious file.
Length Constraints: Minimum of 1 length. Maximum of 128 length.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceId **   <a name="securityhub-Type-FilePaths-ResourceId"></a>
The Amazon Resource Name (ARN) of the resource on which the threat was detected.
Length Constraints: Minimum of 1 length. Maximum of 128 length.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_FilePaths_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FilePaths)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FilePaths)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FilePaths)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
