---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigRulesFilters.html
---

# DescribeConfigRulesFilters
<a name="API_DescribeConfigRulesFilters"></a>

Returns a filtered list of Detective or Proactive AWS Config rules. By default, if the filter is not defined, this API returns an unfiltered list. For more information on Detective or Proactive AWS Config rules, see [**Evaluation Mode**](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html) in the * AWS Config Developer Guide*.

## Contents
<a name="API_DescribeConfigRulesFilters_Contents"></a>

 ** EvaluationMode **   <a name="config-Type-DescribeConfigRulesFilters-EvaluationMode"></a>
The mode of an evaluation. The valid values are Detective or Proactive.
Type: String
Valid Values: `DETECTIVE | PROACTIVE`
Required: No

 ** RuleEvaluationVisibility **   <a name="config-Type-DescribeConfigRulesFilters-RuleEvaluationVisibility"></a>
Filters the results by `RuleEvaluationVisibility`.
Type: String
Valid Values: `EXTERNAL | INTERNAL`
Required: No

## See Also
<a name="API_DescribeConfigRulesFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeConfigRulesFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeConfigRulesFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeConfigRulesFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
