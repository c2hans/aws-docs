---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringAlertSummary.html
---

# MonitoringAlertSummary
<a name="API_MonitoringAlertSummary"></a>

Provides summary information about a monitor alert.

## Contents
<a name="API_MonitoringAlertSummary_Contents"></a>

 ** Actions **   <a name="sagemaker-Type-MonitoringAlertSummary-Actions"></a>
A list of alert actions taken in response to an alert going into `InAlert` status.
Type: [MonitoringAlertActions](API_MonitoringAlertActions.md) object
Required: Yes

 ** AlertStatus **   <a name="sagemaker-Type-MonitoringAlertSummary-AlertStatus"></a>
The current status of an alert.
Type: String
Valid Values: `InAlert | OK`
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-MonitoringAlertSummary-CreationTime"></a>
A timestamp that indicates when a monitor alert was created.
Type: Timestamp
Required: Yes

 ** DatapointsToAlert **   <a name="sagemaker-Type-MonitoringAlertSummary-DatapointsToAlert"></a>
Within `EvaluationPeriod`, how many execution failures will raise an alert.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: Yes

 ** EvaluationPeriod **   <a name="sagemaker-Type-MonitoringAlertSummary-EvaluationPeriod"></a>
The number of most recent monitoring executions to consider when evaluating alert status.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-MonitoringAlertSummary-LastModifiedTime"></a>
A timestamp that indicates when a monitor alert was last updated.
Type: Timestamp
Required: Yes

 ** MonitoringAlertName **   <a name="sagemaker-Type-MonitoringAlertSummary-MonitoringAlertName"></a>
The name of a monitoring alert.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## See Also
<a name="API_MonitoringAlertSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringAlertSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringAlertSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringAlertSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
