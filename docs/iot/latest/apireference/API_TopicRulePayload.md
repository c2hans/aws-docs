---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TopicRulePayload.html
---

# TopicRulePayload
<a name="API_TopicRulePayload"></a>

Describes a rule.

## Contents
<a name="API_TopicRulePayload_Contents"></a>

 ** actions **   <a name="iot-Type-TopicRulePayload-actions"></a>
The actions associated with the rule.
Type: Array of [Action](API_Action.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** sql **   <a name="iot-Type-TopicRulePayload-sql"></a>
The SQL statement used to query the topic. For more information, see [AWS IoT SQL Reference](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html) in the * AWS IoT Developer Guide*.
Type: String
Required: Yes

 ** awsIotSqlVersion **   <a name="iot-Type-TopicRulePayload-awsIotSqlVersion"></a>
The version of the SQL rules engine to use when evaluating the rule.
Type: String
Required: No

 ** description **   <a name="iot-Type-TopicRulePayload-description"></a>
The description of the rule.
Type: String
Required: No

 ** errorAction **   <a name="iot-Type-TopicRulePayload-errorAction"></a>
The action to take when an error occurs.
Type: [Action](API_Action.md) object
Required: No

 ** ruleDisabled **   <a name="iot-Type-TopicRulePayload-ruleDisabled"></a>
Specifies whether the rule is disabled.
Type: Boolean
Required: No

## See Also
<a name="API_TopicRulePayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TopicRulePayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TopicRulePayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TopicRulePayload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
