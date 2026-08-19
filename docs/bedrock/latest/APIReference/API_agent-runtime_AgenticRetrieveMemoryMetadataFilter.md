---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveMemoryMetadataFilter.html
---

# AgenticRetrieveMemoryMetadataFilter
<a name="API_agent-runtime_AgenticRetrieveMemoryMetadataFilter"></a>

A metadata filter expression, in the form accepted by the AgentCore Memory RetrieveMemoryRecords operation. The expression has a left operand that names the metadata key, an operator, and a right operand. For the EXISTS and NOT\_EXISTS operators, omit the right operand.

## Contents
<a name="API_agent-runtime_AgenticRetrieveMemoryMetadataFilter_Contents"></a>

 ** left **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryMetadataFilter-left"></a>
The metadata key that the expression evaluates.
Type: [AgenticRetrieveMemoryMetadataFilterLeft](API_agent-runtime_AgenticRetrieveMemoryMetadataFilterLeft.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** operator **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryMetadataFilter-operator"></a>
The relationship that the metadata key and value must have for a memory record to match.
Type: String
Valid Values: `EQUALS_TO | EXISTS | NOT_EXISTS | BEFORE | AFTER | CONTAINS | GREATER_THAN | GREATER_THAN_OR_EQUALS | LESS_THAN | LESS_THAN_OR_EQUALS`
Required: Yes

 ** right **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryMetadataFilter-right"></a>
The value that the expression compares the metadata key against. Supply this value for every operator except EXISTS and NOT\_EXISTS.
Type: [AgenticRetrieveMemoryMetadataFilterRight](API_agent-runtime_AgenticRetrieveMemoryMetadataFilterRight.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveMemoryMetadataFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryMetadataFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryMetadataFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryMetadataFilter)
