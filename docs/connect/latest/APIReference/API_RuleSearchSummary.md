---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleSearchSummary.html
---

# RuleSearchSummary
<a name="API_RuleSearchSummary"></a>

A summary of information about a rule, returned as part of the response to a `SearchRules` operation.

## Contents
<a name="API_RuleSearchSummary_Contents"></a>

 ** ActionSummaries **   <a name="connect-Type-RuleSearchSummary-ActionSummaries"></a>
A list of `ActionTypes` associated with a rule.
Type: Array of [ActionSummary](API_ActionSummary.md) objects
Required: Yes

 ** CreatedTime **   <a name="connect-Type-RuleSearchSummary-CreatedTime"></a>
The timestamp for when the rule was created.
Type: Timestamp
Required: Yes

 ** LastUpdatedBy **   <a name="connect-Type-RuleSearchSummary-LastUpdatedBy"></a>
The Amazon Resource Name (ARN) of the user who last updated the rule.
Type: String
Required: Yes

 ** LastUpdatedTime **   <a name="connect-Type-RuleSearchSummary-LastUpdatedTime"></a>
The timestamp for when the rule was last updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="connect-Type-RuleSearchSummary-Name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

 ** PublishStatus **   <a name="connect-Type-RuleSearchSummary-PublishStatus"></a>
The publish status of the rule.
Type: String
Valid Values: `DRAFT | PUBLISHED`
Required: Yes

 ** RuleArn **   <a name="connect-Type-RuleSearchSummary-RuleArn"></a>
The Amazon Resource Name (ARN) of the rule.
Type: String
Required: Yes

 ** RuleId **   <a name="connect-Type-RuleSearchSummary-RuleId"></a>
A unique identifier for the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** TriggerEventSource **   <a name="connect-Type-RuleSearchSummary-TriggerEventSource"></a>
The event source to trigger the rule.
Type: [RuleTriggerEventSource](API_RuleTriggerEventSource.md) object
Required: Yes

 ** RuleCapabilityTiers **   <a name="connect-Type-RuleSearchSummary-RuleCapabilityTiers"></a>
The list of capability tiers associated with the rule. Used for categorizing rules by capability (for example, `GenerativeAI`).
Type: Array of strings
Valid Values: `GenerativeAI`
Required: No

 ** Tags **   <a name="connect-Type-RuleSearchSummary-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_RuleSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RuleSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RuleSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RuleSearchSummary)
