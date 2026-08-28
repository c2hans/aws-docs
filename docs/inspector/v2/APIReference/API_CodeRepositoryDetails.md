---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeRepositoryDetails.html
---

# CodeRepositoryDetails
<a name="API_CodeRepositoryDetails"></a>

Contains details about a code repository associated with a finding.

## Contents
<a name="API_CodeRepositoryDetails_Contents"></a>

 ** integrationArn **   <a name="inspector2-Type-CodeRepositoryDetails-integrationArn"></a>
The Amazon Resource Name (ARN) of the code security integration associated with the repository.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration\/[a-f0-9-]{36}`
Required: No

 ** projectName **   <a name="inspector2-Type-CodeRepositoryDetails-projectName"></a>
The name of the project in the code repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** providerType **   <a name="inspector2-Type-CodeRepositoryDetails-providerType"></a>
The type of repository provider (such as GitHub, GitLab, etc.).
Type: String
Valid Values: `GITHUB | GITLAB_SELF_MANAGED`
Required: No

## See Also
<a name="API_CodeRepositoryDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeRepositoryDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeRepositoryDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeRepositoryDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
