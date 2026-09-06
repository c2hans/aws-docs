---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowDedupeStrategy.html
---

# DataIntegrationFlowDedupeStrategy
<a name="API_DataIntegrationFlowDedupeStrategy"></a>

The deduplication strategy details.

## Contents
<a name="API_DataIntegrationFlowDedupeStrategy_Contents"></a>

 ** type **   <a name="supplychain-Type-DataIntegrationFlowDedupeStrategy-type"></a>
The type of the deduplication strategy.
+  **FIELD\_PRIORITY** - Field priority configuration for the deduplication strategy specifies an ordered list of fields used to tie-break the data records sharing the same primary key values. Fields earlier in the list have higher priority for evaluation. For each field, the sort order determines whether to retain data record with larger or smaller field value.
Type: String
Valid Values: `FIELD_PRIORITY`
Required: Yes

 ** fieldPriority **   <a name="supplychain-Type-DataIntegrationFlowDedupeStrategy-fieldPriority"></a>
The field priority deduplication strategy.
Type: [DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration](API_DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration.md) object
Required: No

## See Also
<a name="API_DataIntegrationFlowDedupeStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlowDedupeStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlowDedupeStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlowDedupeStrategy)
