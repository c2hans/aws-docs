---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ResourceEvaluationFilters.html
---

# ResourceEvaluationFilters
<a name="API_ResourceEvaluationFilters"></a>

Returns details of a resource evaluation based on the selected filter.

## Contents
<a name="API_ResourceEvaluationFilters_Contents"></a>

 ** EvaluationContextIdentifier **   <a name="config-Type-ResourceEvaluationFilters-EvaluationContextIdentifier"></a>
Filters evaluations for a given infrastructure deployment. For example: CFN Stack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** EvaluationMode **   <a name="config-Type-ResourceEvaluationFilters-EvaluationMode"></a>
Filters all resource evaluations results based on an evaluation mode.
Currently, `DECTECTIVE` is not supported as a valid value. Ignore other documentation stating otherwise.
Type: String
Valid Values: `DETECTIVE | PROACTIVE`
Required: No

 ** TimeWindow **   <a name="config-Type-ResourceEvaluationFilters-TimeWindow"></a>
Returns a `TimeWindow` object.
Type: [TimeWindow](API_TimeWindow.md) object
Required: No

## See Also
<a name="API_ResourceEvaluationFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ResourceEvaluationFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ResourceEvaluationFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ResourceEvaluationFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
