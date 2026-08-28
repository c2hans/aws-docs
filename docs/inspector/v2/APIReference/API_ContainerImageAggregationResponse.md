---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ContainerImageAggregationResponse.html
---

# ContainerImageAggregationResponse
<a name="API_ContainerImageAggregationResponse"></a>

A response that contains the results of a container image aggregation.

## Contents
<a name="API_ContainerImageAggregationResponse_Contents"></a>

 ** resourceId **   <a name="inspector2-Type-ContainerImageAggregationResponse-resourceId"></a>
The resource ID for the container image.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** accountId **   <a name="inspector2-Type-ContainerImageAggregationResponse-accountId"></a>
The account ID associated with the container image.
Type: String
Required: No

 ** architecture **   <a name="inspector2-Type-ContainerImageAggregationResponse-architecture"></a>
The architecture of the container image.
Type: String
Required: No

 ** cloudAccountId **   <a name="inspector2-Type-ContainerImageAggregationResponse-cloudAccountId"></a>
The cloud account ID for the container image aggregation.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(\d{12}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** cloudOrgId **   <a name="inspector2-Type-ContainerImageAggregationResponse-cloudOrgId"></a>
The cloud organization ID for the container image aggregation.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(o-[a-z0-9]{10,32}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** cloudPartition **   <a name="inspector2-Type-ContainerImageAggregationResponse-cloudPartition"></a>
The cloud infrastructure partition associated with this container image aggregation. Valid values:
+  `aws` – AWS commercial Regions.
+  `aws-cn` – AWS China Regions.
+  `aws-us-gov` – AWS GovCloud (US) Regions.
+  `AzureCloud` – Azure commercial Regions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(aws(-[a-z]+)*|Azure[A-Za-z]+)`
Required: No

 ** cloudProvider **   <a name="inspector2-Type-ContainerImageAggregationResponse-cloudProvider"></a>
The cloud service provider associated with this container image aggregation. Valid values:
+  `AWS` – Findings from AWS resources.
+  `AZURE` – Findings from Microsoft Azure resources.
Type: String
Valid Values: `AWS | AZURE`
Required: No

 ** cloudRegion **   <a name="inspector2-Type-ContainerImageAggregationResponse-cloudRegion"></a>
The cloud Region associated with this container image aggregation. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([a-z]{2}(-[a-z]+)+-\d+|[a-z][a-z0-9]+)`
Required: No

 ** exploitAvailableActiveFindingsCount **   <a name="inspector2-Type-ContainerImageAggregationResponse-exploitAvailableActiveFindingsCount"></a>
The number of active findings with an exploit available for the container image.
Type: Long
Required: No

 ** fixAvailableActiveFindingsCount **   <a name="inspector2-Type-ContainerImageAggregationResponse-fixAvailableActiveFindingsCount"></a>
The number of active findings with a fix available for the container image.
Type: Long
Required: No

 ** imageDigest **   <a name="inspector2-Type-ContainerImageAggregationResponse-imageDigest"></a>
The image digest for the container image.
Type: String
Required: No

 ** imageTags **   <a name="inspector2-Type-ContainerImageAggregationResponse-imageTags"></a>
The image tags attached to the container image.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** inUseCount **   <a name="inspector2-Type-ContainerImageAggregationResponse-inUseCount"></a>
The number of times the container image is in use.
Type: Long
Required: No

 ** lastInUseAt **   <a name="inspector2-Type-ContainerImageAggregationResponse-lastInUseAt"></a>
The last time the container image was in use.
Type: Timestamp
Required: No

 ** registry **   <a name="inspector2-Type-ContainerImageAggregationResponse-registry"></a>
The registry for the container image.
Type: String
Required: No

 ** repository **   <a name="inspector2-Type-ContainerImageAggregationResponse-repository"></a>
The repository for the container image.
Type: String
Required: No

 ** severityCounts **   <a name="inspector2-Type-ContainerImageAggregationResponse-severityCounts"></a>
An object that contains the counts of aggregated finding per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_ContainerImageAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ContainerImageAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ContainerImageAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ContainerImageAggregationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
