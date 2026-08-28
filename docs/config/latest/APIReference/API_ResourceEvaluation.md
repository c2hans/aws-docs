---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ResourceEvaluation.html
---

# ResourceEvaluation
<a name="API_ResourceEvaluation"></a>

Returns details of a resource evaluation.

## Contents
<a name="API_ResourceEvaluation_Contents"></a>

 ** EvaluationMode **   <a name="config-Type-ResourceEvaluation-EvaluationMode"></a>
The mode of an evaluation. The valid values are Detective or Proactive.
Type: String
Valid Values: `DETECTIVE | PROACTIVE`
Required: No

 ** EvaluationStartTimestamp **   <a name="config-Type-ResourceEvaluation-EvaluationStartTimestamp"></a>
The starting time of an execution.
Type: Timestamp
Required: No

 ** ResourceEvaluationId **   <a name="config-Type-ResourceEvaluation-ResourceEvaluationId"></a>
The ResourceEvaluationId of a evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ResourceEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ResourceEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ResourceEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ResourceEvaluation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
