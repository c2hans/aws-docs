---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_AggregatedLogOddsMetric.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# AggregatedLogOddsMetric
<a name="API_AggregatedLogOddsMetric"></a>

The log odds metric details.

Account Takeover Insights (ATI) model uses event variables from the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, your ATI model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are `IP address` and `user`.

## Contents
<a name="API_AggregatedLogOddsMetric_Contents"></a>

 ** aggregatedVariablesImportance **   <a name="FraudDetector-Type-AggregatedLogOddsMetric-aggregatedVariablesImportance"></a>
 The relative importance of the variables in the list to the other event variable.
Type: Float
Required: Yes

 ** variableNames **   <a name="FraudDetector-Type-AggregatedLogOddsMetric-variableNames"></a>
 The names of all the variables.
Type: Array of strings
Required: Yes

## See Also
<a name="API_AggregatedLogOddsMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/AggregatedLogOddsMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/AggregatedLogOddsMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/AggregatedLogOddsMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
