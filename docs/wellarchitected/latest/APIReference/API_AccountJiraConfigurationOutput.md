---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AccountJiraConfigurationOutput.html
---

# AccountJiraConfigurationOutput
<a name="API_AccountJiraConfigurationOutput"></a>

Account-level: Output configuration of the Jira integration.

## Contents
<a name="API_AccountJiraConfigurationOutput_Contents"></a>

 ** IntegrationStatus **   <a name="wellarchitected-Type-AccountJiraConfigurationOutput-IntegrationStatus"></a>
Account-level: Configuration status of the Jira integration.
Type: String
Valid Values: `CONFIGURED | NOT_CONFIGURED`
Required: No

 ** IssueManagementStatus **   <a name="wellarchitected-Type-AccountJiraConfigurationOutput-IssueManagementStatus"></a>
Account-level: Jira issue management status.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** IssueManagementType **   <a name="wellarchitected-Type-AccountJiraConfigurationOutput-IssueManagementType"></a>
Account-level: Jira issue management type.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** JiraProjectKey **   <a name="wellarchitected-Type-AccountJiraConfigurationOutput-JiraProjectKey"></a>
Account-level: Jira project key to sync workloads to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[A-Z][A-Z0-9_]*$`
Required: No

 ** StatusMessage **   <a name="wellarchitected-Type-AccountJiraConfigurationOutput-StatusMessage"></a>
Account-level: Status message on configuration of the Jira integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Subdomain **   <a name="wellarchitected-Type-AccountJiraConfigurationOutput-Subdomain"></a>
Account-level: Jira subdomain URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_AccountJiraConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/AccountJiraConfigurationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/AccountJiraConfigurationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/AccountJiraConfigurationOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
