---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_LinkRoutingRuleSummary.html
---

# LinkRoutingRuleSummary
<a name="API_LinkRoutingRuleSummary"></a>

A summary of a link routing rule.

## Contents
<a name="API_LinkRoutingRuleSummary_Contents"></a>

 ** conditions **   <a name="rtbfabric-Type-LinkRoutingRuleSummary-conditions"></a>
The conditions for the routing rule.
Type: [RuleCondition](API_RuleCondition.md) object
Required: Yes

 ** createdAt **   <a name="rtbfabric-Type-LinkRoutingRuleSummary-createdAt"></a>
The timestamp of when the routing rule was created.
Type: Timestamp
Required: Yes

 ** priority **   <a name="rtbfabric-Type-LinkRoutingRuleSummary-priority"></a>
The priority of the routing rule.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** ruleId **   <a name="rtbfabric-Type-LinkRoutingRuleSummary-ruleId"></a>
The unique identifier of the routing rule.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `rule-[a-z0-9-]{1,25}`
Required: Yes

 ** status **   <a name="rtbfabric-Type-LinkRoutingRuleSummary-status"></a>
The status of the routing rule.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | UPDATE_IN_PROGRESS | DELETION_IN_PROGRESS | DELETED | FAILED`
Required: Yes

 ** updatedAt **   <a name="rtbfabric-Type-LinkRoutingRuleSummary-updatedAt"></a>
The timestamp of when the routing rule was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_LinkRoutingRuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/LinkRoutingRuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/LinkRoutingRuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/LinkRoutingRuleSummary)
