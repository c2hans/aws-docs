---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Scope.html
---

# Scope
<a name="API_Scope"></a>

Defines the scope for recommendation generation, specifying which pillars and goals to focus on.

## Contents
<a name="API_Scope_Contents"></a>

 ** pillars **   <a name="wellarchitected-Type-Scope-pillars"></a>
The AWS Well-Architected Framework pillars to include in the generation scope.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: Yes

 ** goalIds **   <a name="wellarchitected-Type-Scope-goalIds"></a>
Specific goal IDs to focus on during recommendation generation. Use `ListAgentGoals` to retrieve goal IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** items **   <a name="wellarchitected-Type-Scope-items"></a>
An optional per-pillar filter. When you specify items, only the listed items are processed for each pillar. When you omit items, all items are processed.
Type: Array of [PillarItem](API_PillarItem.md) objects
Required: No

## See Also
<a name="API_Scope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/Scope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/Scope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/Scope)
