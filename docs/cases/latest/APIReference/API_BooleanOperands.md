---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_BooleanOperands.html
---

# BooleanOperands
<a name="API_connect-cases_BooleanOperands"></a>

Boolean operands for a condition. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Contents
<a name="API_connect-cases_BooleanOperands_Contents"></a>

 ** operandOne **   <a name="connect-Type-connect-cases_BooleanOperands-operandOne"></a>
Represents the left hand operand in the condition.
Type: [OperandOne](API_connect-cases_OperandOne.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** operandTwo **   <a name="connect-Type-connect-cases_BooleanOperands-operandTwo"></a>
Represents the right hand operand in the condition.
Type: [OperandTwo](API_connect-cases_OperandTwo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** result **   <a name="connect-Type-connect-cases_BooleanOperands-result"></a>
The value of the outer rule if the condition evaluates to true.
Type: Boolean
Required: Yes

## See Also
<a name="API_connect-cases_BooleanOperands_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/BooleanOperands)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/BooleanOperands)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/BooleanOperands)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
