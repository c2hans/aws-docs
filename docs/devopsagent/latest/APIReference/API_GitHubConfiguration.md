---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GitHubConfiguration.html
---

# GitHubConfiguration
<a name="API_GitHubConfiguration"></a>

Configuration for GitHub repository integration.

## Contents
<a name="API_GitHubConfiguration_Contents"></a>

 ** owner **   <a name="devopsagent-Type-GitHubConfiguration-owner"></a>
The GitHub repository owner name.
Type: String
Required: Yes

 ** ownerType **   <a name="devopsagent-Type-GitHubConfiguration-ownerType"></a>
Type of GitHub repository owner.
Type: String
Valid Values: `organization | user`
Required: Yes

 ** repoId **   <a name="devopsagent-Type-GitHubConfiguration-repoId"></a>
Associated Github repo ID
Type: String
Required: Yes

 ** repoName **   <a name="devopsagent-Type-GitHubConfiguration-repoName"></a>
Associated Github repo name
Type: String
Required: Yes

 ** instanceIdentifier **   <a name="devopsagent-Type-GitHubConfiguration-instanceIdentifier"></a>
GitHub instance identifier (e.g., github.com or github.enterprise.com)
Type: String
Required: No

 ** runtimeRoleArn **   <a name="devopsagent-Type-GitHubConfiguration-runtimeRoleArn"></a>
Optional role ARN that AIDevOps assumes at runtime for automatic verification testing and VPC connectivity on this association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: No

## See Also
<a name="API_GitHubConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/GitHubConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/GitHubConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/GitHubConfiguration)
