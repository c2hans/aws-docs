---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_OperandTwo.html
---

# OperandTwo
<a name="API_connect-cases_OperandTwo"></a>

Represents the right hand operand in the condition. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Contents
<a name="API_connect-cases_OperandTwo_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** booleanValue **   <a name="connect-Type-connect-cases_OperandTwo-booleanValue"></a>
Boolean value type.
Type: Boolean
Required: No

 ** doubleValue **   <a name="connect-Type-connect-cases_OperandTwo-doubleValue"></a>
Double value type.
Type: Double
Required: No

 ** emptyValue **   <a name="connect-Type-connect-cases_OperandTwo-emptyValue"></a>
Empty value type.
Type: [EmptyOperandValue](API_connect-cases_EmptyOperandValue.md) object
Required: No

 ** stringValue **   <a name="connect-Type-connect-cases_OperandTwo-stringValue"></a>
String value type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1500.
Required: No

## See Also
<a name="API_connect-cases_OperandTwo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/OperandTwo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/OperandTwo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/OperandTwo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
