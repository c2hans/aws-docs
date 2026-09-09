---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PreEvaluationFilters.html
---

# PreEvaluationFilters
<a name="API_PreEvaluationFilters"></a>

The pre-evaluation filters for a rule, that restrict a rule to be applied to only certain resources based on the resource's attributes, such as tags assigned to a contact. The pre-evaluation filters are applied even before rule conditions are evaluated and are used to enforce tag-based-access-control while applying rules.

## Contents
<a name="API_PreEvaluationFilters_Contents"></a>

 ** AndConditions **   <a name="connect-Type-PreEvaluationFilters-AndConditions"></a>
A list of conditions that the rule evaluates together using AND logic. All conditions must be met for the event to be evaluated by the rule.
Type: Array of [PreEvaluationFilter](API_PreEvaluationFilter.md) objects
Required: No

## See Also
<a name="API_PreEvaluationFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PreEvaluationFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PreEvaluationFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PreEvaluationFilters)
