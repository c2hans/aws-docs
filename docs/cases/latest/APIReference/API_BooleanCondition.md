---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_BooleanCondition.html
---

# BooleanCondition
<a name="API_connect-cases_BooleanCondition"></a>

Boolean condition for a rule. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Contents
<a name="API_connect-cases_BooleanCondition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** andAll **   <a name="connect-Type-connect-cases_BooleanCondition-andAll"></a>
Combines multiple conditions with AND operator. All conditions must be true for the compound condition to be true.
Type: [CompoundCondition](API_connect-cases_CompoundCondition.md) object
Required: No

 ** equalTo **   <a name="connect-Type-connect-cases_BooleanCondition-equalTo"></a>
Tests that operandOne is equal to operandTwo.
Type: [BooleanOperands](API_connect-cases_BooleanOperands.md) object
Required: No

 ** notEqualTo **   <a name="connect-Type-connect-cases_BooleanCondition-notEqualTo"></a>
Tests that operandOne is not equal to operandTwo.
Type: [BooleanOperands](API_connect-cases_BooleanOperands.md) object
Required: No

 ** orAll **   <a name="connect-Type-connect-cases_BooleanCondition-orAll"></a>
Combines multiple conditions with OR operator. At least one condition must be true for the compound condition to be true.
Type: [CompoundCondition](API_connect-cases_CompoundCondition.md) object
Required: No

## See Also
<a name="API_connect-cases_BooleanCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/BooleanCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/BooleanCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/BooleanCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
