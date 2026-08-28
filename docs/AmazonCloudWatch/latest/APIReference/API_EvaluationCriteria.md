---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EvaluationCriteria.html
---

# EvaluationCriteria
<a name="API_EvaluationCriteria"></a>

The evaluation criteria for an alarm. This is a union type that currently supports `PromQLCriteria`.

## Contents
<a name="API_EvaluationCriteria_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** PromQLCriteria **   <a name="ACW-Type-EvaluationCriteria-PromQLCriteria"></a>
The PromQL criteria for the alarm evaluation.
Type: [AlarmPromQLCriteria](API_AlarmPromQLCriteria.md) object
Required: No

## See Also
<a name="API_EvaluationCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/EvaluationCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/EvaluationCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/EvaluationCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
