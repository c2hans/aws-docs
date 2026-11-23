---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_DeploymentConfigurationDetail.html
---

# DeploymentConfigurationDetail

The deployment configuration. Exactly one member must be set, and it must match the delivery option type.

## Contents
<a name="API_marketplace-deployment_DeploymentConfigurationDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dataAsAService **   <a name="AWSMarketplaceService-Type-marketplace-deployment_DeploymentConfigurationDetail-dataAsAService"></a>
The deployment configuration settings for the Data as a Service delivery option, including the fulfillment URL that AWS Marketplace redirects buyers to after they subscribe.
Type: [DataAsAServiceConfigurationDetail](API_marketplace-deployment_DataAsAServiceConfigurationDetail.md) object
Required: No

## See Also
<a name="API_marketplace-deployment_DeploymentConfigurationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-deployment-2023-01-25/DeploymentConfigurationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-deployment-2023-01-25/DeploymentConfigurationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-deployment-2023-01-25/DeploymentConfigurationDetail)
