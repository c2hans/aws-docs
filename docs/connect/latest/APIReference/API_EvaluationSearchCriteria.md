---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationSearchCriteria.html
---

# EvaluationSearchCriteria
<a name="API_EvaluationSearchCriteria"></a>

The search criteria to be used to return evaluations.

## Contents
<a name="API_EvaluationSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-EvaluationSearchCriteria-AndConditions"></a>
A list of conditions which would be applied together with an AND condition.
Type: Array of [EvaluationSearchCriteria](#API_EvaluationSearchCriteria) objects
Required: No

 ** BooleanCondition **   <a name="connect-Type-EvaluationSearchCriteria-BooleanCondition"></a>
The boolean condition search criteria for searching evaluations.
Type: [BooleanCondition](API_BooleanCondition.md) object
Required: No

 ** DateTimeCondition **   <a name="connect-Type-EvaluationSearchCriteria-DateTimeCondition"></a>
The datetime condition search criteria for searching evaluations.
Type: [DateTimeCondition](API_DateTimeCondition.md) object
Required: No

 ** DecimalCondition **   <a name="connect-Type-EvaluationSearchCriteria-DecimalCondition"></a>
The decimal condition search criteria for searching evaluations.
Type: [DecimalCondition](API_DecimalCondition.md) object
Required: No

 ** NumberCondition **   <a name="connect-Type-EvaluationSearchCriteria-NumberCondition"></a>
A leaf node condition which can be used to specify a numeric condition.
The currently supported value for `FieldName` is `limit`.
Type: [NumberCondition](API_NumberCondition.md) object
Required: No

 ** OrConditions **   <a name="connect-Type-EvaluationSearchCriteria-OrConditions"></a>
A list of conditions which would be applied together with an OR condition.
Type: Array of [EvaluationSearchCriteria](#API_EvaluationSearchCriteria) objects
Required: No

 ** StringCondition **   <a name="connect-Type-EvaluationSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_EvaluationSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationSearchCriteria)
