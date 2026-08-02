---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowTarget.html
---

# DataIntegrationFlowTarget
<a name="API_DataIntegrationFlowTarget"></a>

The DataIntegrationFlow target parameters.

## Contents
<a name="API_DataIntegrationFlowTarget_Contents"></a>

 ** targetType **   <a name="supplychain-Type-DataIntegrationFlowTarget-targetType"></a>
The DataIntegrationFlow target type.
Type: String
Valid Values: `S3 | DATASET`
Required: Yes

 ** datasetTarget **   <a name="supplychain-Type-DataIntegrationFlowTarget-datasetTarget"></a>
The dataset DataIntegrationFlow target. Note that for AWS Supply Chain dataset under **asc** namespace, it has a connection\_id internal field that is not allowed to be provided by client directly, they will be auto populated.
Type: [DataIntegrationFlowDatasetTargetConfiguration](API_DataIntegrationFlowDatasetTargetConfiguration.md) object
Required: No

 ** s3Target **   <a name="supplychain-Type-DataIntegrationFlowTarget-s3Target"></a>
The S3 DataIntegrationFlow target.
Type: [DataIntegrationFlowS3TargetConfiguration](API_DataIntegrationFlowS3TargetConfiguration.md) object
Required: No

## See Also
<a name="API_DataIntegrationFlowTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlowTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlowTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlowTarget)
