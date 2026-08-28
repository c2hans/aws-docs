---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ImageLayerAggregationResponse.html
---

# ImageLayerAggregationResponse
<a name="API_ImageLayerAggregationResponse"></a>

A response that contains the results of a finding aggregation by image layer.

## Contents
<a name="API_ImageLayerAggregationResponse_Contents"></a>

 ** accountId **   <a name="inspector2-Type-ImageLayerAggregationResponse-accountId"></a>
The ID of the AWS account that owns the container image hosting the layer image.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** layerHash **   <a name="inspector2-Type-ImageLayerAggregationResponse-layerHash"></a>
The layer hash.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** repository **   <a name="inspector2-Type-ImageLayerAggregationResponse-repository"></a>
The repository the layer resides in.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** resourceId **   <a name="inspector2-Type-ImageLayerAggregationResponse-resourceId"></a>
The resource ID of the container image layer.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** cloudAccountId **   <a name="inspector2-Type-ImageLayerAggregationResponse-cloudAccountId"></a>
The cloud account ID for the image layer aggregation.
Type: String
Required: No

 ** cloudOrgId **   <a name="inspector2-Type-ImageLayerAggregationResponse-cloudOrgId"></a>
The cloud organization ID for the image layer aggregation.
Type: String
Required: No

 ** cloudPartition **   <a name="inspector2-Type-ImageLayerAggregationResponse-cloudPartition"></a>
The cloud infrastructure partition associated with this image layer aggregation. Valid values:
+  `aws` – AWS commercial Regions.
+  `aws-cn` – AWS China Regions.
+  `aws-us-gov` – AWS GovCloud (US) Regions.
+  `AzureCloud` – Azure commercial Regions.
Type: String
Required: No

 ** cloudProvider **   <a name="inspector2-Type-ImageLayerAggregationResponse-cloudProvider"></a>
The cloud service provider associated with this image layer aggregation. Valid values:
+  `AWS` – Findings from AWS resources.
+  `AZURE` – Findings from Microsoft Azure resources.
Type: String
Required: No

 ** cloudRegion **   <a name="inspector2-Type-ImageLayerAggregationResponse-cloudRegion"></a>
The cloud Region associated with this image layer aggregation. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
Type: String
Required: No

 ** severityCounts **   <a name="inspector2-Type-ImageLayerAggregationResponse-severityCounts"></a>
An object that represents the count of matched findings per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_ImageLayerAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ImageLayerAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ImageLayerAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ImageLayerAggregationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
