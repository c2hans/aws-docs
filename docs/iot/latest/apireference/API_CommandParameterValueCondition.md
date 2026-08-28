---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CommandParameterValueCondition.html
---

# CommandParameterValueCondition
<a name="API_CommandParameterValueCondition"></a>

A condition for the command parameter that must be evaluated to true for successful creation of a command execution.

## Contents
<a name="API_CommandParameterValueCondition_Contents"></a>

 ** comparisonOperator **   <a name="iot-Type-CommandParameterValueCondition-comparisonOperator"></a>
The comparison operator for the command parameter.
IN\_RANGE, and NOT\_IN\_RANGE operators include boundary values.
Type: String
Valid Values: `EQUALS | NOT_EQUALS | LESS_THAN | LESS_THAN_EQUALS | GREATER_THAN | GREATER_THAN_EQUALS | IN_SET | NOT_IN_SET | IN_RANGE | NOT_IN_RANGE`
Required: Yes

 ** operand **   <a name="iot-Type-CommandParameterValueCondition-operand"></a>
The comparison operand for the command parameter.
Type: [CommandParameterValueComparisonOperand](API_CommandParameterValueComparisonOperand.md) object
Required: Yes

## See Also
<a name="API_CommandParameterValueCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CommandParameterValueCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CommandParameterValueCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CommandParameterValueCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
