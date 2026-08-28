---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_WorkloadData.html
---

# WorkloadData
<a name="API_WorkloadData"></a>

Describes a workload.

## Contents
<a name="API_WorkloadData_Contents"></a>

 ** description **   <a name="launchwizard-Type-WorkloadData-description"></a>
The description of a workload.
Type: String
Required: No

 ** displayName **   <a name="launchwizard-Type-WorkloadData-displayName"></a>
The display name of a workload.
Type: String
Required: No

 ** documentationUrl **   <a name="launchwizard-Type-WorkloadData-documentationUrl"></a>
The URL of a workload document.
Type: String
Required: No

 ** iconUrl **   <a name="launchwizard-Type-WorkloadData-iconUrl"></a>
The URL of a workload icon.
Type: String
Required: No

 ** status **   <a name="launchwizard-Type-WorkloadData-status"></a>
The status of a workload.
 *You can list deployments in the `DISABLED` status.*
Type: String
Valid Values: `ACTIVE | INACTIVE | DISABLED | DELETED`
Required: No

 ** statusMessage **   <a name="launchwizard-Type-WorkloadData-statusMessage"></a>
The message about a workload's status.
Type: String
Required: No

 ** workloadName **   <a name="launchwizard-Type-WorkloadData-workloadName"></a>
The name of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: No

## See Also
<a name="API_WorkloadData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/WorkloadData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/WorkloadData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/WorkloadData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Launch Wizard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query launchwizard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
