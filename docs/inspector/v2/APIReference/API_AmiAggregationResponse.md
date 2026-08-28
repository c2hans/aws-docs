---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AmiAggregationResponse.html
---

# AmiAggregationResponse
<a name="API_AmiAggregationResponse"></a>

A response that contains the results of a finding aggregation by AMI.

## Contents
<a name="API_AmiAggregationResponse_Contents"></a>

 ** ami **   <a name="inspector2-Type-AmiAggregationResponse-ami"></a>
The ID of the AMI that findings were aggregated for.
Type: String
Pattern: `ami-([a-z0-9]{8}|[a-z0-9]{17}|\*)`
Required: Yes

 ** accountId **   <a name="inspector2-Type-AmiAggregationResponse-accountId"></a>
The AWS account ID for the AMI.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** affectedInstances **   <a name="inspector2-Type-AmiAggregationResponse-affectedInstances"></a>
The IDs of Amazon EC2 instances using this AMI.
Type: Long
Required: No

 ** cloudAccountId **   <a name="inspector2-Type-AmiAggregationResponse-cloudAccountId"></a>
The cloud account ID for the AMI aggregation.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(\d{12}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** cloudOrgId **   <a name="inspector2-Type-AmiAggregationResponse-cloudOrgId"></a>
The cloud organization ID for the AMI aggregation.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(o-[a-z0-9]{10,32}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** cloudPartition **   <a name="inspector2-Type-AmiAggregationResponse-cloudPartition"></a>
The cloud infrastructure partition associated with this AMI aggregation. Valid values:
+  `aws` – AWS commercial Regions.
+  `aws-cn` – AWS China Regions.
+  `aws-us-gov` – AWS GovCloud (US) Regions.
+  `AzureCloud` – Azure commercial Regions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(aws(-[a-z]+)*|Azure[A-Za-z]+)`
Required: No

 ** cloudProvider **   <a name="inspector2-Type-AmiAggregationResponse-cloudProvider"></a>
The cloud service provider associated with this Amazon Machine Image (AMI) aggregation. Valid values:
+  `AWS` – Findings from AWS resources.
+  `AZURE` – Findings from Microsoft Azure resources.
Type: String
Valid Values: `AWS | AZURE`
Required: No

 ** cloudRegion **   <a name="inspector2-Type-AmiAggregationResponse-cloudRegion"></a>
The cloud Region associated with this AMI aggregation. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([a-z]{2}(-[a-z]+)+-\d+|[a-z][a-z0-9]+)`
Required: No

 ** severityCounts **   <a name="inspector2-Type-AmiAggregationResponse-severityCounts"></a>
An object that contains the count of matched findings per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_AmiAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AmiAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AmiAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AmiAggregationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
