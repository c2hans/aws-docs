---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowFieldPriorityDedupeField.html
---

# DataIntegrationFlowFieldPriorityDedupeField
<a name="API_DataIntegrationFlowFieldPriorityDedupeField"></a>

The field used in the field priority deduplication strategy.

## Contents
<a name="API_DataIntegrationFlowFieldPriorityDedupeField_Contents"></a>

 ** name **   <a name="supplychain-Type-DataIntegrationFlowFieldPriorityDedupeField-name"></a>
The name of the deduplication field. Must exist in the dataset and not be a primary key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9_]+`
Required: Yes

 ** sortOrder **   <a name="supplychain-Type-DataIntegrationFlowFieldPriorityDedupeField-sortOrder"></a>
The sort order for the deduplication field.
Type: String
Valid Values: `ASC | DESC`
Required: Yes

## See Also
<a name="API_DataIntegrationFlowFieldPriorityDedupeField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlowFieldPriorityDedupeField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlowFieldPriorityDedupeField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlowFieldPriorityDedupeField)
