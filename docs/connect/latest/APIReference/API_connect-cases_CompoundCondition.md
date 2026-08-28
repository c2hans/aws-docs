---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CompoundCondition.html
---

# CompoundCondition
<a name="API_connect-cases_CompoundCondition"></a>

A compound condition that combines multiple boolean conditions using logical operators. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Contents
<a name="API_connect-cases_CompoundCondition_Contents"></a>

 ** conditions **   <a name="connect-Type-connect-cases_CompoundCondition-conditions"></a>
The list of conditions to combine using the logical operator.
For API users: A case rule can have a maximum of 5 conditions, spread across a maximum of 2 levels of nesting.
Type: Array of [BooleanCondition](API_connect-cases_BooleanCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

## See Also
<a name="API_connect-cases_CompoundCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CompoundCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CompoundCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CompoundCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
