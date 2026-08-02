---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_DeploymentParameterInput.html
---

# DeploymentParameterInput
<a name="API_marketplace-deployment_DeploymentParameterInput"></a>

The shape containing the requested deployment parameter name and secretString.

**Note**
To support AWS CloudFormation dynamic references to this resource using Quick Launch, this value must match a parameter defined in the CloudFormation templated provided to buyers.

## Contents
<a name="API_marketplace-deployment_DeploymentParameterInput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** name **   <a name="AWSMarketplaceService-Type-marketplace-deployment_DeploymentParameterInput-name"></a>
The desired name of the deployment parameter. This is the identifier on which deployment parameters are keyed for a given buyer and product. If this name matches an existing deployment parameter, this request will update the existing resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Pattern: `[a-zA-Z0-9/_+=.@-]+`
Required: Yes

 ** secretString **   <a name="AWSMarketplaceService-Type-marketplace-deployment_DeploymentParameterInput-secretString"></a>
The text to encrypt and store in the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15000.
Required: Yes

## See Also
<a name="API_marketplace-deployment_DeploymentParameterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-deployment-2023-01-25/DeploymentParameterInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-deployment-2023-01-25/DeploymentParameterInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-deployment-2023-01-25/DeploymentParameterInput)
