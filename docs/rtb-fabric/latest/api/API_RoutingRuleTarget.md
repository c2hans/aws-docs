---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_RoutingRuleTarget.html
---

# RoutingRuleTarget

The routing rule an update targeted.

## Contents
<a name="API_RoutingRuleTarget_Contents"></a>

 ** linkId **   <a name="rtbfabric-Type-RoutingRuleTarget-linkId"></a>
The unique identifier of the rule's link.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`
Required: Yes

 ** ruleId **   <a name="rtbfabric-Type-RoutingRuleTarget-ruleId"></a>
Identifier for a routing rule
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `rule-[a-z0-9-]{1,25}`
Required: Yes

## See Also
<a name="API_RoutingRuleTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/RoutingRuleTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/RoutingRuleTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/RoutingRuleTarget)
