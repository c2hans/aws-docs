---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_SourceCredentialsInfo.html
---

# SourceCredentialsInfo
<a name="API_SourceCredentialsInfo"></a>

 Information about the credentials for a GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, or Bitbucket repository.

## Contents
<a name="API_SourceCredentialsInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="CodeBuild-Type-SourceCredentialsInfo-arn"></a>
 The Amazon Resource Name (ARN) of the token.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** authType **   <a name="CodeBuild-Type-SourceCredentialsInfo-authType"></a>
 The type of authentication used by the credentials. Valid options are OAUTH, BASIC\_AUTH, PERSONAL\_ACCESS\_TOKEN, CODECONNECTIONS, or SECRETS\_MANAGER.
Type: String
Valid Values: `OAUTH | BASIC_AUTH | PERSONAL_ACCESS_TOKEN | CODECONNECTIONS | SECRETS_MANAGER`
Required: No

 ** resource **   <a name="CodeBuild-Type-SourceCredentialsInfo-resource"></a>
The connection ARN if your authType is CODECONNECTIONS or SECRETS\_MANAGER.
Type: String
Required: No

 ** serverType **   <a name="CodeBuild-Type-SourceCredentialsInfo-serverType"></a>
 The type of source provider. The valid options are GITHUB, GITHUB\_ENTERPRISE, GITLAB, GITLAB\_SELF\_MANAGED, or BITBUCKET.
Type: String
Valid Values: `GITHUB | BITBUCKET | GITHUB_ENTERPRISE | GITLAB | GITLAB_SELF_MANAGED`
Required: No

## See Also
<a name="API_SourceCredentialsInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/SourceCredentialsInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/SourceCredentialsInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/SourceCredentialsInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
