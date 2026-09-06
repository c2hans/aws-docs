---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FindingTypeAggregationResponse.html
---

# FindingTypeAggregationResponse
<a name="API_FindingTypeAggregationResponse"></a>

A response that contains the results of a finding type aggregation.

## Contents
<a name="API_FindingTypeAggregationResponse_Contents"></a>

 ** accountId **   <a name="inspector2-Type-FindingTypeAggregationResponse-accountId"></a>
The ID of the AWS account associated with the findings.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** cloudAccountId **   <a name="inspector2-Type-FindingTypeAggregationResponse-cloudAccountId"></a>
The cloud account ID for the finding type aggregation.
Type: String
Required: No

 ** cloudOrgId **   <a name="inspector2-Type-FindingTypeAggregationResponse-cloudOrgId"></a>
The cloud organization ID for the finding type aggregation.
Type: String
Required: No

 ** cloudPartition **   <a name="inspector2-Type-FindingTypeAggregationResponse-cloudPartition"></a>
The cloud infrastructure partition associated with this finding type aggregation. Valid values:
+  `aws` – AWS commercial Regions.
+  `aws-cn` – AWS China Regions.
+  `aws-us-gov` – AWS GovCloud (US) Regions.
+  `AzureCloud` – Azure commercial Regions.
Type: String
Required: No

 ** cloudProvider **   <a name="inspector2-Type-FindingTypeAggregationResponse-cloudProvider"></a>
The cloud service provider associated with this finding type aggregation. Valid values:
+  `AWS` – Findings from AWS resources.
+  `AZURE` – Findings from Microsoft Azure resources.
Type: String
Required: No

 ** cloudRegion **   <a name="inspector2-Type-FindingTypeAggregationResponse-cloudRegion"></a>
The cloud Region associated with this finding type aggregation. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
Type: String
Required: No

 ** exploitAvailableCount **   <a name="inspector2-Type-FindingTypeAggregationResponse-exploitAvailableCount"></a>
The number of findings that have an exploit available.
Type: Long
Required: No

 ** fixAvailableCount **   <a name="inspector2-Type-FindingTypeAggregationResponse-fixAvailableCount"></a>
 Details about the number of fixes.
Type: Long
Required: No

 ** severityCounts **   <a name="inspector2-Type-FindingTypeAggregationResponse-severityCounts"></a>
The value to sort results by.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_FindingTypeAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FindingTypeAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FindingTypeAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FindingTypeAggregationResponse)
