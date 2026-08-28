---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormSearchCriteria.html
---

# EvaluationFormSearchCriteria
<a name="API_EvaluationFormSearchCriteria"></a>

The search criteria to be used to return evaluation forms.

## Contents
<a name="API_EvaluationFormSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-EvaluationFormSearchCriteria-AndConditions"></a>
A list of conditions which would be applied together with an AND condition.
Type: Array of [EvaluationFormSearchCriteria](#API_EvaluationFormSearchCriteria) objects
Required: No

 ** BooleanCondition **   <a name="connect-Type-EvaluationFormSearchCriteria-BooleanCondition"></a>
Boolean search condition.
Type: [BooleanCondition](API_BooleanCondition.md) object
Required: No

 ** DateTimeCondition **   <a name="connect-Type-EvaluationFormSearchCriteria-DateTimeCondition"></a>
Datetime search condition.
Type: [DateTimeCondition](API_DateTimeCondition.md) object
Required: No

 ** NumberCondition **   <a name="connect-Type-EvaluationFormSearchCriteria-NumberCondition"></a>
A leaf node condition which can be used to specify a numeric condition.
The currently supported value for `FieldName` is `limit`.
Type: [NumberCondition](API_NumberCondition.md) object
Required: No

 ** OrConditions **   <a name="connect-Type-EvaluationFormSearchCriteria-OrConditions"></a>
A list of conditions which would be applied together with an OR condition.
Type: Array of [EvaluationFormSearchCriteria](#API_EvaluationFormSearchCriteria) objects
Required: No

 ** StringCondition **   <a name="connect-Type-EvaluationFormSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_EvaluationFormSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormSearchCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
