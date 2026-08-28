---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Condition.html
---

# Condition
<a name="API_Condition"></a>

A JSON string which you can use to limit the event bus permissions you are granting to only accounts that fulfill the condition. Currently, the only supported condition is membership in a certain AWS organization. The string must contain `Type`, `Key`, and `Value` fields. The `Value` field specifies the ID of the AWS organization. Following is an example value for `Condition`:

 `'{"Type" : "StringEquals", "Key": "aws:PrincipalOrgID", "Value": "o-1234567890"}'`

## Contents
<a name="API_Condition_Contents"></a>

 ** Key **   <a name="eventbridge-Type-Condition-Key"></a>
Specifies the key for the condition. Currently the only supported key is `aws:PrincipalOrgID`.
Type: String
Required: Yes

 ** Type **   <a name="eventbridge-Type-Condition-Type"></a>
Specifies the type of condition. Currently the only supported value is `StringEquals`.
Type: String
Required: Yes

 ** Value **   <a name="eventbridge-Type-Condition-Value"></a>
Specifies the value for the key. Currently, this must be the ID of the organization.
Type: String
Required: Yes

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/Condition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/Condition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/Condition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
