---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExternalMetricStatus.html
---

# ExternalMetricStatus
<a name="API_ExternalMetricStatus"></a>

 Describes Compute Optimizer's integration status with your chosen external metric provider. For example, Datadog.

## Contents
<a name="API_ExternalMetricStatus_Contents"></a>

 ** statusCode **   <a name="computeoptimizer-Type-ExternalMetricStatus-statusCode"></a>
 The status code for Compute Optimizer's integration with an external metrics provider.
Type: String
Valid Values: `NO_EXTERNAL_METRIC_SET | INTEGRATION_SUCCESS | DATADOG_INTEGRATION_ERROR | DYNATRACE_INTEGRATION_ERROR | NEWRELIC_INTEGRATION_ERROR | INSTANA_INTEGRATION_ERROR | INSUFFICIENT_DATADOG_METRICS | INSUFFICIENT_DYNATRACE_METRICS | INSUFFICIENT_NEWRELIC_METRICS | INSUFFICIENT_INSTANA_METRICS`
Required: No

 ** statusReason **   <a name="computeoptimizer-Type-ExternalMetricStatus-statusReason"></a>
 The reason for Compute Optimizer's integration status with your external metric provider.
Type: String
Required: No

## See Also
<a name="API_ExternalMetricStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ExternalMetricStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ExternalMetricStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ExternalMetricStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
