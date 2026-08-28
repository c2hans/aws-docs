---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_WorkloadDeploymentPatternDataSummary.html
---

# WorkloadDeploymentPatternDataSummary
<a name="API_WorkloadDeploymentPatternDataSummary"></a>

Describes a workload deployment pattern.

## Contents
<a name="API_WorkloadDeploymentPatternDataSummary_Contents"></a>

 ** deploymentPatternName **   <a name="launchwizard-Type-WorkloadDeploymentPatternDataSummary-deploymentPatternName"></a>
The name of a workload deployment pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][a-zA-Z0-9-]*`
Required: No

 ** deploymentPatternVersionName **   <a name="launchwizard-Type-WorkloadDeploymentPatternDataSummary-deploymentPatternVersionName"></a>
The version name of a workload deployment pattern.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `(([A-Za-z0-9][a-zA-Z0-9-]*)|(\d+\.\d+\.\d+))`
Required: No

 ** description **   <a name="launchwizard-Type-WorkloadDeploymentPatternDataSummary-description"></a>
The description of a workload deployment pattern.
Type: String
Required: No

 ** displayName **   <a name="launchwizard-Type-WorkloadDeploymentPatternDataSummary-displayName"></a>
The display name of a workload deployment pattern.
Type: String
Required: No

 ** status **   <a name="launchwizard-Type-WorkloadDeploymentPatternDataSummary-status"></a>
The status of a workload deployment pattern.
Type: String
Valid Values: `ACTIVE | INACTIVE | DISABLED | DELETED`
Required: No

 ** statusMessage **   <a name="launchwizard-Type-WorkloadDeploymentPatternDataSummary-statusMessage"></a>
A message about a workload deployment pattern's status.
Type: String
Required: No

 ** workloadName **   <a name="launchwizard-Type-WorkloadDeploymentPatternDataSummary-workloadName"></a>
The name of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: No

 ** workloadVersionName **   <a name="launchwizard-Type-WorkloadDeploymentPatternDataSummary-workloadVersionName"></a>
The name of the workload deployment pattern version.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `(([A-Za-z0-9][a-zA-Z0-9-]*)|(\d+\.\d+\.\d+))`
Required: No

## See Also
<a name="API_WorkloadDeploymentPatternDataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/WorkloadDeploymentPatternDataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/WorkloadDeploymentPatternDataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/WorkloadDeploymentPatternDataSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Launch Wizard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query launchwizard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
