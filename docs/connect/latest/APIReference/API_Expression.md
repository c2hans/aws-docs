---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Expression.html
---

# Expression
<a name="API_Expression"></a>

A tagged union to specify expression for a routing step.

## Contents
<a name="API_Expression_Contents"></a>

 ** AndExpression **   <a name="connect-Type-Expression-AndExpression"></a>
List of routing expressions which will be AND-ed together.
Type: Array of [Expression](#API_Expression) objects
Required: No

 ** AttributeCondition **   <a name="connect-Type-Expression-AttributeCondition"></a>
An object to specify the predefined attribute condition.
Type: [AttributeCondition](API_AttributeCondition.md) object
Required: No

 ** NotAttributeCondition **   <a name="connect-Type-Expression-NotAttributeCondition"></a>
An object to specify the predefined attribute condition.
Type: [AttributeCondition](API_AttributeCondition.md) object
Required: No

 ** OrExpression **   <a name="connect-Type-Expression-OrExpression"></a>
List of routing expressions which will be OR-ed together.
Type: Array of [Expression](#API_Expression) objects
Required: No

## See Also
<a name="API_Expression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Expression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Expression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Expression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
