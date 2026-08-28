---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_WorkspaceConfigurationDescription.html
---

# WorkspaceConfigurationDescription
<a name="API_WorkspaceConfigurationDescription"></a>

This structure contains the description of the workspace configuration.

## Contents
<a name="API_WorkspaceConfigurationDescription_Contents"></a>

 ** status **   <a name="prometheus-Type-WorkspaceConfigurationDescription-status"></a>
This structure displays the current status of the workspace configuration, and might also contain a reason for that status.
Type: [WorkspaceConfigurationStatus](API_WorkspaceConfigurationStatus.md) object
Required: Yes

 ** limitsPerLabelSet **   <a name="prometheus-Type-WorkspaceConfigurationDescription-limitsPerLabelSet"></a>
This is an array of structures, where each structure displays one label sets for the workspace and the limits for that label set.
Type: Array of [LimitsPerLabelSet](API_LimitsPerLabelSet.md) objects
Required: No

 ** retentionPeriodInDays **   <a name="prometheus-Type-WorkspaceConfigurationDescription-retentionPeriodInDays"></a>
This field displays how many days that metrics are retained in the workspace.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_WorkspaceConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/WorkspaceConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/WorkspaceConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/WorkspaceConfigurationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
