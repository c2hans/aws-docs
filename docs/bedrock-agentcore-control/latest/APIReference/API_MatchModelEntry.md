---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_MatchModelEntry.html
---

# MatchModelEntry
<a name="API_MatchModelEntry"></a>

A model ID or pattern to match against the requested model, and the operator to use for the comparison.

## Contents
<a name="API_MatchModelEntry_Contents"></a>

 ** value **   <a name="bedrockagentcorecontrol-Type-MatchModelEntry-value"></a>
The model ID or pattern to match. With the `StringLike` operator, you can use `*` and `?` as wildcards, for example `anthropic.claude-*`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9\-\._\*\?@:]+(/[a-zA-Z0-9\-\._\*\?@:]+)*`
Required: Yes

 ** operator **   <a name="bedrockagentcorecontrol-Type-MatchModelEntry-operator"></a>
The operator to use when comparing the requested model to the value:
+  `StringEquals` – Requires an exact match.
+  `StringLike` – Supports wildcard patterns using `*` and `?`. This is the default.
Type: String
Valid Values: `StringEquals | StringLike`
Required: No

## See Also
<a name="API_MatchModelEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/MatchModelEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/MatchModelEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/MatchModelEntry)
