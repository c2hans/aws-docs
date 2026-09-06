---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_RepositoryAggregationResponse.html
---

# RepositoryAggregationResponse
<a name="API_RepositoryAggregationResponse"></a>

A response that contains details on the results of a finding aggregation by repository.

## Contents
<a name="API_RepositoryAggregationResponse_Contents"></a>

 ** repository **   <a name="inspector2-Type-RepositoryAggregationResponse-repository"></a>
The name of the repository associated with the findings.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** accountId **   <a name="inspector2-Type-RepositoryAggregationResponse-accountId"></a>
The ID of the AWS account associated with the findings.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** affectedImages **   <a name="inspector2-Type-RepositoryAggregationResponse-affectedImages"></a>
The number of container images impacted by the findings.
Type: Long
Required: No

 ** cloudAccountId **   <a name="inspector2-Type-RepositoryAggregationResponse-cloudAccountId"></a>
The cloud account ID for the repository aggregation.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(\d{12}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** cloudOrgId **   <a name="inspector2-Type-RepositoryAggregationResponse-cloudOrgId"></a>
The cloud organization ID for the repository aggregation.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(o-[a-z0-9]{10,32}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** cloudPartition **   <a name="inspector2-Type-RepositoryAggregationResponse-cloudPartition"></a>
The cloud infrastructure partition associated with this repository aggregation. Valid values:
+  `aws` – AWS commercial Regions.
+  `aws-cn` – AWS China Regions.
+  `aws-us-gov` – AWS GovCloud (US) Regions.
+  `AzureCloud` – Azure commercial Regions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(aws(-[a-z]+)*|Azure[A-Za-z]+)`
Required: No

 ** cloudProvider **   <a name="inspector2-Type-RepositoryAggregationResponse-cloudProvider"></a>
The cloud service provider associated with this repository aggregation. Valid values:
+  `AWS` – Findings from AWS resources.
+  `AZURE` – Findings from Microsoft Azure resources.
Type: String
Valid Values: `AWS | AZURE`
Required: No

 ** cloudRegion **   <a name="inspector2-Type-RepositoryAggregationResponse-cloudRegion"></a>
The cloud Region associated with this repository aggregation. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([a-z]{2}(-[a-z]+)+-\d+|[a-z][a-z0-9]+)`
Required: No

 ** severityCounts **   <a name="inspector2-Type-RepositoryAggregationResponse-severityCounts"></a>
An object that represent the count of matched findings per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_RepositoryAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/RepositoryAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/RepositoryAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/RepositoryAggregationResponse)
