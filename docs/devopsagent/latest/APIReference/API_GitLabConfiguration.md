---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GitLabConfiguration.html
---

# GitLabConfiguration
<a name="API_GitLabConfiguration"></a>

Configuration for GitLab project integration.

## Contents
<a name="API_GitLabConfiguration_Contents"></a>

 ** projectId **   <a name="devopsagent-Type-GitLabConfiguration-projectId"></a>
GitLab numeric project ID.
Type: String
Required: Yes

 ** projectPath **   <a name="devopsagent-Type-GitLabConfiguration-projectPath"></a>
Full GitLab project path (e.g., namespace/project-name).
Type: String
Required: Yes

 ** instanceIdentifier **   <a name="devopsagent-Type-GitLabConfiguration-instanceIdentifier"></a>
GitLab instance identifier (e.g., gitlab.com or e2e.gamma.dev.us-east-1.gitlab.falco.ai.aws.dev)
Type: String
Required: No

 ** runtimeRoleArn **   <a name="devopsagent-Type-GitLabConfiguration-runtimeRoleArn"></a>
 *This member has been deprecated.*
Optional role ARN that AIDevOps assumes at runtime for automatic verification testing and VPC connectivity on this association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: No

## See Also
<a name="API_GitLabConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/GitLabConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/GitLabConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/GitLabConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
