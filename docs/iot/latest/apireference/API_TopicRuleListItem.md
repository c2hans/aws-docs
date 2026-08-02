---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TopicRuleListItem.html
---

# TopicRuleListItem
<a name="API_TopicRuleListItem"></a>

Describes a rule.

## Contents
<a name="API_TopicRuleListItem_Contents"></a>

 ** createdAt **   <a name="iot-Type-TopicRuleListItem-createdAt"></a>
The date and time the rule was created.
Type: Timestamp
Required: No

 ** ruleArn **   <a name="iot-Type-TopicRuleListItem-ruleArn"></a>
The rule ARN.
Type: String
Required: No

 ** ruleDisabled **   <a name="iot-Type-TopicRuleListItem-ruleDisabled"></a>
Specifies whether the rule is disabled.
Type: Boolean
Required: No

 ** ruleName **   <a name="iot-Type-TopicRuleListItem-ruleName"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_]+$`
Required: No

 ** topicPattern **   <a name="iot-Type-TopicRuleListItem-topicPattern"></a>
The pattern for the topic names that apply.
Type: String
Required: No

## See Also
<a name="API_TopicRuleListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TopicRuleListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TopicRuleListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TopicRuleListItem)
