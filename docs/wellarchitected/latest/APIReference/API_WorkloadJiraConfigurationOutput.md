---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_WorkloadJiraConfigurationOutput.html
---

# WorkloadJiraConfigurationOutput
<a name="API_WorkloadJiraConfigurationOutput"></a>

Workload-level: Output configuration of the Jira integration.

## Contents
<a name="API_WorkloadJiraConfigurationOutput_Contents"></a>

 ** IssueManagementStatus **   <a name="wellarchitected-Type-WorkloadJiraConfigurationOutput-IssueManagementStatus"></a>
Workload-level: Jira issue management status.
Type: String
Valid Values: `ENABLED | DISABLED | INHERIT`
Required: No

 ** IssueManagementType **   <a name="wellarchitected-Type-WorkloadJiraConfigurationOutput-IssueManagementType"></a>
Workload-level: Jira issue management type.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** JiraProjectKey **   <a name="wellarchitected-Type-WorkloadJiraConfigurationOutput-JiraProjectKey"></a>
Workload-level: Jira project key to sync workloads to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[A-Z][A-Z0-9_]*$`
Required: No

 ** StatusMessage **   <a name="wellarchitected-Type-WorkloadJiraConfigurationOutput-StatusMessage"></a>
Workload-level: Status message on configuration of the Jira integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_WorkloadJiraConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/WorkloadJiraConfigurationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/WorkloadJiraConfigurationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/WorkloadJiraConfigurationOutput)
