---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SaasDeploymentTemplate.html
---

# SaasDeploymentTemplate

Contains a deployment template for a SaaS product. Exactly one member is set, indicating the deployment template type.

## Contents
<a name="API_marketplace-discovery_SaasDeploymentTemplate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cloudFormationDeploymentTemplate **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasDeploymentTemplate-cloudFormationDeploymentTemplate"></a>
An AWS CloudFormation deployment template.
Type: [SaasCloudFormationDeploymentTemplate](API_marketplace-discovery_SaasCloudFormationDeploymentTemplate.md) object
Required: No

## See Also
<a name="API_marketplace-discovery_SaasDeploymentTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SaasDeploymentTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SaasDeploymentTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SaasDeploymentTemplate)
