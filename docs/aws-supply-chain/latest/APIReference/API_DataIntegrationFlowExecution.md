---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowExecution.html
---

# DataIntegrationFlowExecution
<a name="API_DataIntegrationFlowExecution"></a>

The flow execution details.

## Contents
<a name="API_DataIntegrationFlowExecution_Contents"></a>

 ** executionId **   <a name="supplychain-Type-DataIntegrationFlowExecution-executionId"></a>
The flow executionId.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** flowName **   <a name="supplychain-Type-DataIntegrationFlowExecution-flowName"></a>
The flow execution's flowName.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9-]+`
Required: Yes

 ** instanceId **   <a name="supplychain-Type-DataIntegrationFlowExecution-instanceId"></a>
The flow execution's instanceId.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** endTime **   <a name="supplychain-Type-DataIntegrationFlowExecution-endTime"></a>
The flow execution end timestamp.
Type: Timestamp
Required: No

 ** message **   <a name="supplychain-Type-DataIntegrationFlowExecution-message"></a>
The failure message (if any) of failed flow execution.
Type: String
Required: No

 ** outputMetadata **   <a name="supplychain-Type-DataIntegrationFlowExecution-outputMetadata"></a>
The flow execution output metadata.
Type: [DataIntegrationFlowExecutionOutputMetadata](API_DataIntegrationFlowExecutionOutputMetadata.md) object
Required: No

 ** sourceInfo **   <a name="supplychain-Type-DataIntegrationFlowExecution-sourceInfo"></a>
The source information for a flow execution.
Type: [DataIntegrationFlowExecutionSourceInfo](API_DataIntegrationFlowExecutionSourceInfo.md) object
Required: No

 ** startTime **   <a name="supplychain-Type-DataIntegrationFlowExecution-startTime"></a>
The flow execution start timestamp.
Type: Timestamp
Required: No

 ** status **   <a name="supplychain-Type-DataIntegrationFlowExecution-status"></a>
The status of flow execution.
Type: String
Valid Values: `SUCCEEDED | IN_PROGRESS | FAILED`
Required: No

## See Also
<a name="API_DataIntegrationFlowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlowExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlowExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlowExecution)
