---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_BranchDiffSourceCodeType.html
---

# BranchDiffSourceCodeType
<a name="API_BranchDiffSourceCodeType"></a>

A type of [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies a code diff between a source and destination branch in an associated repository.

## Contents
<a name="API_BranchDiffSourceCodeType_Contents"></a>

 ** DestinationBranchName **   <a name="reviewer-Type-BranchDiffSourceCodeType-DestinationBranchName"></a>
The destination branch for a diff in an associated repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** SourceBranchName **   <a name="reviewer-Type-BranchDiffSourceCodeType-SourceBranchName"></a>
The source branch for a diff in an associated repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_BranchDiffSourceCodeType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/BranchDiffSourceCodeType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/BranchDiffSourceCodeType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/BranchDiffSourceCodeType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
