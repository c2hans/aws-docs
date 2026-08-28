---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ProactiveAnomalySummary.html
---

# ProactiveAnomalySummary
<a name="API_ProactiveAnomalySummary"></a>

Details about a proactive anomaly. This object is returned by `DescribeAnomaly.`

## Contents
<a name="API_ProactiveAnomalySummary_Contents"></a>

 ** AnomalyReportedTimeRange **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-AnomalyReportedTimeRange"></a>
 An `AnomalyReportedTimeRange` object that specifies the time range between when the anomaly is opened and the time when it is closed.
Type: [AnomalyReportedTimeRange](API_AnomalyReportedTimeRange.md) object
Required: No

 ** AnomalyResources **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-AnomalyResources"></a>
Information about a resource in which DevOps Guru detected anomalous behavior.
Type: Array of [AnomalyResource](API_AnomalyResource.md) objects
Required: No

 ** AnomalyTimeRange **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-AnomalyTimeRange"></a>
 A time range that specifies when the observed unusual behavior in an anomaly started and ended. This is different from `AnomalyReportedTimeRange`, which specifies the time range when DevOps Guru opens and then closes an anomaly.
Type: [AnomalyTimeRange](API_AnomalyTimeRange.md) object
Required: No

 ** AssociatedInsightId **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-AssociatedInsightId"></a>
 The ID of the insight that contains this anomaly. An insight is composed of related anomalies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w-]*$`
Required: No

 ** Description **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-Description"></a>
 A description of the proactive anomaly.
Type: String
Required: No

 ** Id **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-Id"></a>
The ID of the anomaly.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w~.-]*$`
Required: No

 ** Limit **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-Limit"></a>
 A threshold that was exceeded by behavior in analyzed resources. Exceeding this threshold is related to the anomalous behavior that generated this anomaly.
Type: Double
Required: No

 ** PredictionTimeRange **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-PredictionTimeRange"></a>
 The time range during which anomalous behavior in a proactive anomaly or an insight is expected to occur.
Type: [PredictionTimeRange](API_PredictionTimeRange.md) object
Required: No

 ** ResourceCollection **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-ResourceCollection"></a>
 A collection of AWS resources supported by DevOps Guru. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.
Type: [ResourceCollection](API_ResourceCollection.md) object
Required: No

 ** Severity **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-Severity"></a>
The severity of the anomaly. The severity of anomalies that generate an insight determine that insight's severity. For more information, see [Understanding insight severities](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities) in the *Amazon DevOps Guru User Guide*.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** SourceDetails **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-SourceDetails"></a>
 Details about the source of the analyzed operational data that triggered the anomaly. The one supported source is Amazon CloudWatch metrics.
Type: [AnomalySourceDetails](API_AnomalySourceDetails.md) object
Required: No

 ** SourceMetadata **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-SourceMetadata"></a>
The metadata of the source which detects proactive anomalies.
Type: [AnomalySourceMetadata](API_AnomalySourceMetadata.md) object
Required: No

 ** Status **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-Status"></a>
The status of the anomaly.
Type: String
Valid Values: `ONGOING | CLOSED`
Required: No

 ** UpdateTime **   <a name="DevOpsGuru-Type-ProactiveAnomalySummary-UpdateTime"></a>
 The time of the anomaly's most recent update.
Type: Timestamp
Required: No

## See Also
<a name="API_ProactiveAnomalySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ProactiveAnomalySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ProactiveAnomalySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ProactiveAnomalySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
