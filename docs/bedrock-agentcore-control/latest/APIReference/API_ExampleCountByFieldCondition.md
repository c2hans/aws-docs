---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ExampleCountByFieldCondition.html
---

# ExampleCountByFieldCondition

 A condition on the number of examples that have the given fields. The count includes each example that has at least one of the fields in `anyOf`.

## Contents
<a name="API_ExampleCountByFieldCondition_Contents"></a>

 ** anyOf **   <a name="bedrockagentcorecontrol-Type-ExampleCountByFieldCondition-anyOf"></a>
 The fields to count. An example counts if it has at least one of these fields. Required.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `TURNS | INPUT | ACTOR_PROFILE`
Required: No

 ** max **   <a name="bedrockagentcorecontrol-Type-ExampleCountByFieldCondition-max"></a>
 The maximum count, inclusive.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** min **   <a name="bedrockagentcorecontrol-Type-ExampleCountByFieldCondition-min"></a>
 The minimum count, inclusive.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ExampleCountByFieldCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ExampleCountByFieldCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ExampleCountByFieldCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ExampleCountByFieldCondition)
