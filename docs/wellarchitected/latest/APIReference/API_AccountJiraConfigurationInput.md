---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AccountJiraConfigurationInput.html
---

# AccountJiraConfigurationInput
<a name="API_AccountJiraConfigurationInput"></a>

Account-level: Input for the Jira configuration.

## Contents
<a name="API_AccountJiraConfigurationInput_Contents"></a>

 ** IntegrationStatus **   <a name="wellarchitected-Type-AccountJiraConfigurationInput-IntegrationStatus"></a>
Account-level: Configuration status of the Jira integration.
Type: String
Valid Values: `NOT_CONFIGURED`
Required: No

 ** IssueManagementStatus **   <a name="wellarchitected-Type-AccountJiraConfigurationInput-IssueManagementStatus"></a>
Account-level: Jira issue management status.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** IssueManagementType **   <a name="wellarchitected-Type-AccountJiraConfigurationInput-IssueManagementType"></a>
Account-level: Jira issue management type.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** JiraProjectKey **   <a name="wellarchitected-Type-AccountJiraConfigurationInput-JiraProjectKey"></a>
Account-level: Jira project key to sync workloads to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[A-Z][A-Z0-9_]*$`
Required: No

## See Also
<a name="API_AccountJiraConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/AccountJiraConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/AccountJiraConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/AccountJiraConfigurationInput)
