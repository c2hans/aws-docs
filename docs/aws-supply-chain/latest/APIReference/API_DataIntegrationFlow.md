---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlow.html
---

# DataIntegrationFlow
<a name="API_DataIntegrationFlow"></a>

The DataIntegrationFlow details.

## Contents
<a name="API_DataIntegrationFlow_Contents"></a>

 ** createdTime **   <a name="supplychain-Type-DataIntegrationFlow-createdTime"></a>
The DataIntegrationFlow creation timestamp.
Type: Timestamp
Required: Yes

 ** instanceId **   <a name="supplychain-Type-DataIntegrationFlow-instanceId"></a>
The DataIntegrationFlow instance ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** lastModifiedTime **   <a name="supplychain-Type-DataIntegrationFlow-lastModifiedTime"></a>
The DataIntegrationFlow last modified timestamp.
Type: Timestamp
Required: Yes

 ** name **   <a name="supplychain-Type-DataIntegrationFlow-name"></a>
The DataIntegrationFlow name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9-]+`
Required: Yes

 ** sources **   <a name="supplychain-Type-DataIntegrationFlow-sources"></a>
The DataIntegrationFlow source configurations.
Type: Array of [DataIntegrationFlowSource](API_DataIntegrationFlowSource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 40 items.
Required: Yes

 ** target **   <a name="supplychain-Type-DataIntegrationFlow-target"></a>
The DataIntegrationFlow target configuration.
Type: [DataIntegrationFlowTarget](API_DataIntegrationFlowTarget.md) object
Required: Yes

 ** transformation **   <a name="supplychain-Type-DataIntegrationFlow-transformation"></a>
The DataIntegrationFlow transformation configurations.
Type: [DataIntegrationFlowTransformation](API_DataIntegrationFlowTransformation.md) object
Required: Yes

## See Also
<a name="API_DataIntegrationFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlow)
