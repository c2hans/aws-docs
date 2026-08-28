---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_VmInstanceAggregationResponse.html
---

# VmInstanceAggregationResponse
<a name="API_VmInstanceAggregationResponse"></a>

A response that contains the results of a VM instance aggregation.

## Contents
<a name="API_VmInstanceAggregationResponse_Contents"></a>

 ** resourceId **   <a name="inspector2-Type-VmInstanceAggregationResponse-resourceId"></a>
The resource ID for the VM instance.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** accountId **   <a name="inspector2-Type-VmInstanceAggregationResponse-accountId"></a>
The account ID associated with the VM instance.
Type: String
Required: No

 ** cloudAccountId **   <a name="inspector2-Type-VmInstanceAggregationResponse-cloudAccountId"></a>
The cloud account ID for the VM instance aggregation.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(\d{12}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** cloudOrgId **   <a name="inspector2-Type-VmInstanceAggregationResponse-cloudOrgId"></a>
The cloud organization ID for the VM instance aggregation.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(o-[a-z0-9]{10,32}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** cloudPartition **   <a name="inspector2-Type-VmInstanceAggregationResponse-cloudPartition"></a>
The cloud infrastructure partition associated with this VM instance aggregation. Valid values:
+  `aws` – AWS commercial Regions.
+  `aws-cn` – AWS China Regions.
+  `aws-us-gov` – AWS GovCloud (US) Regions.
+  `AzureCloud` – Azure commercial Regions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(aws(-[a-z]+)*|Azure[A-Za-z]+)`
Required: No

 ** cloudProvider **   <a name="inspector2-Type-VmInstanceAggregationResponse-cloudProvider"></a>
The cloud service provider associated with this VM instance aggregation. Valid values:
+  `AWS` – Findings from AWS resources.
+  `AZURE` – Findings from Microsoft Azure resources.
Type: String
Valid Values: `AWS | AZURE`
Required: No

 ** cloudRegion **   <a name="inspector2-Type-VmInstanceAggregationResponse-cloudRegion"></a>
The cloud Region associated with this VM instance aggregation. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([a-z]{2}(-[a-z]+)+-\d+|[a-z][a-z0-9]+)`
Required: No

 ** exploitAvailableActiveFindingsCount **   <a name="inspector2-Type-VmInstanceAggregationResponse-exploitAvailableActiveFindingsCount"></a>
The number of active findings with an exploit available for the VM instance.
Type: Long
Required: No

 ** fixAvailableActiveFindingsCount **   <a name="inspector2-Type-VmInstanceAggregationResponse-fixAvailableActiveFindingsCount"></a>
The number of active findings with a fix available for the VM instance.
Type: Long
Required: No

 ** networkFindings **   <a name="inspector2-Type-VmInstanceAggregationResponse-networkFindings"></a>
The number of network findings for the VM instance. This field applies only to AWS resources.
Type: Long
Required: No

 ** operatingSystem **   <a name="inspector2-Type-VmInstanceAggregationResponse-operatingSystem"></a>
The operating system of the VM instance.
Type: String
Required: No

 ** severityCounts **   <a name="inspector2-Type-VmInstanceAggregationResponse-severityCounts"></a>
An object that contains the counts of aggregated finding per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

 ** tags **   <a name="inspector2-Type-VmInstanceAggregationResponse-tags"></a>
The tags attached to the VM instance.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** vmImageReference **   <a name="inspector2-Type-VmInstanceAggregationResponse-vmImageReference"></a>
The VM image reference for the VM instance.
Type: String
Required: No

## See Also
<a name="API_VmInstanceAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/VmInstanceAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/VmInstanceAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/VmInstanceAggregationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
