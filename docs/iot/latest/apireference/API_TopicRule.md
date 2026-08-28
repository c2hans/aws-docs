---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TopicRule.html
---

# TopicRule
<a name="API_TopicRule"></a>

Describes a rule.

## Contents
<a name="API_TopicRule_Contents"></a>

 ** actions **   <a name="iot-Type-TopicRule-actions"></a>
The actions associated with the rule.
Type: Array of [Action](API_Action.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** awsIotSqlVersion **   <a name="iot-Type-TopicRule-awsIotSqlVersion"></a>
The version of the SQL rules engine to use when evaluating the rule.
Type: String
Required: No

 ** createdAt **   <a name="iot-Type-TopicRule-createdAt"></a>
The date and time the rule was created.
Type: Timestamp
Required: No

 ** description **   <a name="iot-Type-TopicRule-description"></a>
The description of the rule.
Type: String
Required: No

 ** errorAction **   <a name="iot-Type-TopicRule-errorAction"></a>
The action to perform when an error occurs.
Type: [Action](API_Action.md) object
Required: No

 ** ruleDisabled **   <a name="iot-Type-TopicRule-ruleDisabled"></a>
Specifies whether the rule is disabled.
Type: Boolean
Required: No

 ** ruleName **   <a name="iot-Type-TopicRule-ruleName"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_]+$`
Required: No

 ** sql **   <a name="iot-Type-TopicRule-sql"></a>
The SQL statement used to query the topic. When using a SQL query with multiple lines, be sure to escape the newline characters.
Type: String
Required: No

## See Also
<a name="API_TopicRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TopicRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TopicRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TopicRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
