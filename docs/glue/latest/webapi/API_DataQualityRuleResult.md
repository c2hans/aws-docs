---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityRuleResult.html
---

# DataQualityRuleResult
<a name="API_DataQualityRuleResult"></a>

Describes the result of the evaluation of a data quality rule.

## Contents
<a name="API_DataQualityRuleResult_Contents"></a>

 ** Description **   <a name="Glue-Type-DataQualityRuleResult-Description"></a>
A description of the data quality rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** EvaluatedMetrics **   <a name="Glue-Type-DataQualityRuleResult-EvaluatedMetrics"></a>
A map of metrics associated with the evaluation of the rule.
Type: String to double map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** EvaluatedRule **   <a name="Glue-Type-DataQualityRuleResult-EvaluatedRule"></a>
The evaluated rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** EvaluationMessage **   <a name="Glue-Type-DataQualityRuleResult-EvaluationMessage"></a>
An evaluation message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Labels **   <a name="Glue-Type-DataQualityRuleResult-Labels"></a>
A map containing labels assigned to the data quality rule.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Name **   <a name="Glue-Type-DataQualityRuleResult-Name"></a>
The name of the data quality rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Result **   <a name="Glue-Type-DataQualityRuleResult-Result"></a>
A pass or fail status for the rule.
Type: String
Valid Values: `PASS | FAIL | ERROR`
Required: No

 ** RuleMetrics **   <a name="Glue-Type-DataQualityRuleResult-RuleMetrics"></a>
A map containing metrics associated with the evaluation of the rule based on row-level results.
Type: String to double map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_DataQualityRuleResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityRuleResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityRuleResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityRuleResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
