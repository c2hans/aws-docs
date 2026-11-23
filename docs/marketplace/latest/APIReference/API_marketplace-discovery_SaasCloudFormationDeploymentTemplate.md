---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SaasCloudFormationDeploymentTemplate.html
---

# SaasCloudFormationDeploymentTemplate

Contains a single AWS CloudFormation deployment template for a Software as a Service (SaaS) product.

## Contents
<a name="API_marketplace-discovery_SaasCloudFormationDeploymentTemplate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** defaultStackName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasCloudFormationDeploymentTemplate-defaultStackName"></a>
The default CloudFormation stack name used when deploying this template.
Type: String
Required: Yes

 ** iamPolicy **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasCloudFormationDeploymentTemplate-iamPolicy"></a>
The AWS Identity and Access Management (IAM) policy that you need to deploy this template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: Yes

 ** templateName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasCloudFormationDeploymentTemplate-templateName"></a>
The display name of the deployment template.
Type: String
Required: Yes

 ** templateUrl **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasCloudFormationDeploymentTemplate-templateUrl"></a>
The URL of the CloudFormation deployment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`
Required: Yes

 ** description **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasCloudFormationDeploymentTemplate-description"></a>
A description of the deployment template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

## See Also
<a name="API_marketplace-discovery_SaasCloudFormationDeploymentTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SaasCloudFormationDeploymentTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SaasCloudFormationDeploymentTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SaasCloudFormationDeploymentTemplate)
