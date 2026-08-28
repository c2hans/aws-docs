---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_EventTriggerCondition.html
---

# EventTriggerCondition
<a name="API_connect-customer-profiles_EventTriggerCondition"></a>

Specifies the circumstances under which the event should trigger the destination.

## Contents
<a name="API_connect-customer-profiles_EventTriggerCondition_Contents"></a>

 ** EventTriggerDimensions **   <a name="connect-Type-connect-customer-profiles_EventTriggerCondition-EventTriggerDimensions"></a>
A list of dimensions to be evaluated for the event.
Type: Array of [EventTriggerDimension](API_connect-customer-profiles_EventTriggerDimension.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** LogicalOperator **   <a name="connect-Type-connect-customer-profiles_EventTriggerCondition-LogicalOperator"></a>
The operator used to combine multiple dimensions.
Type: String
Valid Values: `ANY | ALL | NONE`
Required: Yes

## See Also
<a name="API_connect-customer-profiles_EventTriggerCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/EventTriggerCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/EventTriggerCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/EventTriggerCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
