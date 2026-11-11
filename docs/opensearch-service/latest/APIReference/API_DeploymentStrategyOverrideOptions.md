---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeploymentStrategyOverrideOptions.html
---

# DeploymentStrategyOverrideOptions
<a name="API_DeploymentStrategyOverrideOptions"></a>

Overrides the deployment strategy for a single operation, such as a version upgrade.

## Contents
<a name="API_DeploymentStrategyOverrideOptions_Contents"></a>

 ** DeploymentStrategy **   <a name="opensearchservice-Type-DeploymentStrategyOverrideOptions-DeploymentStrategy"></a>
The deployment strategy to use for this operation. The only valid value is `ClonedBlueGreen`, which creates a cloned cluster on the target version next to the primary cluster so that you can validate it and shift traffic to it before you cut over.
Type: String
Valid Values: `ClonedBlueGreen`
Required: Yes

 ** ClonedBlueGreenOptions **   <a name="opensearchservice-Type-DeploymentStrategyOverrideOptions-ClonedBlueGreenOptions"></a>
Options that apply when `DeploymentStrategy` is `ClonedBlueGreen`.
Type: [ClonedBlueGreenOptions](API_ClonedBlueGreenOptions.md) object
Required: No

## See Also
<a name="API_DeploymentStrategyOverrideOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DeploymentStrategyOverrideOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DeploymentStrategyOverrideOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DeploymentStrategyOverrideOptions)
