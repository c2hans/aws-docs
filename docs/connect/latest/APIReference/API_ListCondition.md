---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListCondition.html
---

# ListCondition
<a name="API_ListCondition"></a>

A leaf node condition which can be used to specify a List condition to search users with attributes included in Lists like Proficiencies.

## Contents
<a name="API_ListCondition_Contents"></a>

 ** Conditions **   <a name="connect-Type-ListCondition-Conditions"></a>
A list of Condition objects which would be applied together with an AND condition.
Type: Array of [Condition](API_Condition.md) objects
Required: No

 ** TargetListType **   <a name="connect-Type-ListCondition-TargetListType"></a>
The type of target list that will be used to filter the users.
Type: String
Valid Values: `PROFICIENCIES`
Required: No

## See Also
<a name="API_ListCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
