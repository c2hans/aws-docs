---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_RoutingRuleParameters.html
---

# RoutingRuleParameters

A requested routing rule.

## Contents
<a name="API_RoutingRuleParameters_Contents"></a>

 ** conditions **   <a name="rtbfabric-Type-RoutingRuleParameters-conditions"></a>
The conditions for a routing rule. All specified fields must match for the rule to apply (AND logic). At least one condition field must be set.
Type: [RuleCondition](API_RuleCondition.md) object
Required: Yes

 ** priority **   <a name="rtbfabric-Type-RoutingRuleParameters-priority"></a>
WAF-style evaluation priority. Lower number = evaluated first (priority 1 before 10). Gaps are allowed (1, 10, 20 is valid). Must be between 1 and 1000 inclusive. Uniqueness per link among non-deleted rules is enforced at the API layer (HTTP 409 on conflict).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

## See Also
<a name="API_RoutingRuleParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/RoutingRuleParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/RoutingRuleParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/RoutingRuleParameters)
