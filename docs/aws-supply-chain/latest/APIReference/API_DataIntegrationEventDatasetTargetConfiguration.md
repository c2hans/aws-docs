---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationEventDatasetTargetConfiguration.html
---

# DataIntegrationEventDatasetTargetConfiguration
<a name="API_DataIntegrationEventDatasetTargetConfiguration"></a>

The target dataset configuration for a DATASET event type.

## Contents
<a name="API_DataIntegrationEventDatasetTargetConfiguration_Contents"></a>

 ** datasetIdentifier **   <a name="supplychain-Type-DataIntegrationEventDatasetTargetConfiguration-datasetIdentifier"></a>
The datalake dataset ARN identifier.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1011.
Pattern: `arn:aws:scn:([a-z0-9-]+):([0-9]+):instance/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/namespaces/[^/]+/datasets/[^/]+`
Required: Yes

 ** operationType **   <a name="supplychain-Type-DataIntegrationEventDatasetTargetConfiguration-operationType"></a>
The target dataset load operation type.
Type: String
Valid Values: `APPEND | UPSERT | DELETE`
Required: Yes

## See Also
<a name="API_DataIntegrationEventDatasetTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationEventDatasetTargetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationEventDatasetTargetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationEventDatasetTargetConfiguration)
