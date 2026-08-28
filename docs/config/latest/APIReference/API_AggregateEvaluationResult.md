---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AggregateEvaluationResult.html
---

# AggregateEvaluationResult
<a name="API_AggregateEvaluationResult"></a>

The details of an AWS Config evaluation for an account ID and region in an aggregator. Provides the AWS resource that was evaluated, the compliance of the resource, related time stamps, and supplementary information.

## Contents
<a name="API_AggregateEvaluationResult_Contents"></a>

 ** AccountId **   <a name="config-Type-AggregateEvaluationResult-AccountId"></a>
The 12-digit account ID of the source account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** Annotation **   <a name="config-Type-AggregateEvaluationResult-Annotation"></a>
Supplementary information about how the agrregate evaluation determined the compliance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** AwsRegion **   <a name="config-Type-AggregateEvaluationResult-AwsRegion"></a>
The source region from where the data is aggregated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ComplianceType **   <a name="config-Type-AggregateEvaluationResult-ComplianceType"></a>
The resource compliance status.
For the `AggregationEvaluationResult` data type, AWS Config supports only the `COMPLIANT` and `NON_COMPLIANT`. AWS Config does not support the `NOT_APPLICABLE` and `INSUFFICIENT_DATA` value.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`
Required: No

 ** ConfigRuleInvokedTime **   <a name="config-Type-AggregateEvaluationResult-ConfigRuleInvokedTime"></a>
The time when the AWS Config rule evaluated the AWS resource.
Type: Timestamp
Required: No

 ** EvaluationResultIdentifier **   <a name="config-Type-AggregateEvaluationResult-EvaluationResultIdentifier"></a>
Uniquely identifies the evaluation result.
Type: [EvaluationResultIdentifier](API_EvaluationResultIdentifier.md) object
Required: No

 ** ResultRecordedTime **   <a name="config-Type-AggregateEvaluationResult-ResultRecordedTime"></a>
The time when AWS Config recorded the aggregate evaluation result.
Type: Timestamp
Required: No

## See Also
<a name="API_AggregateEvaluationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AggregateEvaluationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AggregateEvaluationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AggregateEvaluationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
