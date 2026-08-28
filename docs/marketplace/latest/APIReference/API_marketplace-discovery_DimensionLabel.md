---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_DimensionLabel.html
---

# DimensionLabel
<a name="API_marketplace-discovery_DimensionLabel"></a>

A label used to group or categorize pricing dimensions, such as by region or SageMaker option.

## Contents
<a name="API_marketplace-discovery_DimensionLabel_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** labelType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_DimensionLabel-labelType"></a>
The type of the dimension label, such as `Region` or `SagemakerOption`.
Type: String
Valid Values: `Region | SagemakerOption`
Required: Yes

 ** labelValue **   <a name="AWSMarketplaceService-Type-marketplace-discovery_DimensionLabel-labelValue"></a>
The value used to group dimensions together.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_DimensionLabel-displayName"></a>
The human-readable display name of the label.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

## See Also
<a name="API_marketplace-discovery_DimensionLabel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/DimensionLabel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/DimensionLabel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/DimensionLabel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
