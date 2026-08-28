---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ScopeConfiguration.html
---

# ScopeConfiguration
<a name="API_ScopeConfiguration"></a>

Contains configuration information about the scope for a webhook.

## Contents
<a name="API_ScopeConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** name **   <a name="CodeBuild-Type-ScopeConfiguration-name"></a>
The name of either the group, enterprise, or organization that will send webhook events to CodeBuild, depending on the type of webhook.
Type: String
Required: Yes

 ** scope **   <a name="CodeBuild-Type-ScopeConfiguration-scope"></a>
The type of scope for a GitHub or GitLab webhook. The scope default is GITHUB\_ORGANIZATION.
Type: String
Valid Values: `GITHUB_ORGANIZATION | GITHUB_GLOBAL | GITLAB_GROUP`
Required: Yes

 ** domain **   <a name="CodeBuild-Type-ScopeConfiguration-domain"></a>
The domain of the GitHub Enterprise organization or the GitLab Self Managed group. Note that this parameter is only required if your project's source type is GITHUB\_ENTERPRISE or GITLAB\_SELF\_MANAGED.
Type: String
Required: No

## See Also
<a name="API_ScopeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ScopeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ScopeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ScopeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
