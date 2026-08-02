---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ReactiveAnomaly.html
---

# ReactiveAnomaly
<a name="API_ReactiveAnomaly"></a>

Details about a reactive anomaly. This object is returned by `ListAnomalies`.

## Contents
<a name="API_ReactiveAnomaly_Contents"></a>

 ** AnomalyReportedTimeRange **   <a name="DevOpsGuru-Type-ReactiveAnomaly-AnomalyReportedTimeRange"></a>
 An `AnomalyReportedTimeRange` object that specifies the time range between when the anomaly is opened and the time when it is closed.
Type: [AnomalyReportedTimeRange](API_AnomalyReportedTimeRange.md) object
Required: No

 ** AnomalyResources **   <a name="DevOpsGuru-Type-ReactiveAnomaly-AnomalyResources"></a>
The AWS resources in which anomalous behavior was detected by DevOps Guru.
Type: Array of [AnomalyResource](API_AnomalyResource.md) objects
Required: No

 ** AnomalyTimeRange **   <a name="DevOpsGuru-Type-ReactiveAnomaly-AnomalyTimeRange"></a>
 A time range that specifies when the observed unusual behavior in an anomaly started and ended. This is different from `AnomalyReportedTimeRange`, which specifies the time range when DevOps Guru opens and then closes an anomaly.
Type: [AnomalyTimeRange](API_AnomalyTimeRange.md) object
Required: No

 ** AssociatedInsightId **   <a name="DevOpsGuru-Type-ReactiveAnomaly-AssociatedInsightId"></a>
 The ID of the insight that contains this anomaly. An insight is composed of related anomalies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w-]*$`
Required: No

 ** CausalAnomalyId **   <a name="DevOpsGuru-Type-ReactiveAnomaly-CausalAnomalyId"></a>
The ID of the causal anomaly that is associated with this reactive anomaly. The ID of a `CAUSAL` anomaly is always `NULL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w~.-]*$`
Required: No

 ** Description **   <a name="DevOpsGuru-Type-ReactiveAnomaly-Description"></a>
A description of the reactive anomaly.
Type: String
Required: No

 ** Id **   <a name="DevOpsGuru-Type-ReactiveAnomaly-Id"></a>
The ID of the reactive anomaly.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w~.-]*$`
Required: No

 ** Name **   <a name="DevOpsGuru-Type-ReactiveAnomaly-Name"></a>
The name of the reactive anomaly.
Type: String
Required: No

 ** ResourceCollection **   <a name="DevOpsGuru-Type-ReactiveAnomaly-ResourceCollection"></a>
 A collection of AWS resources supported by DevOps Guru. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.
Type: [ResourceCollection](API_ResourceCollection.md) object
Required: No

 ** Severity **   <a name="DevOpsGuru-Type-ReactiveAnomaly-Severity"></a>
The severity of the anomaly. The severity of anomalies that generate an insight determine that insight's severity. For more information, see [Understanding insight severities](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities) in the *Amazon DevOps Guru User Guide*.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** SourceDetails **   <a name="DevOpsGuru-Type-ReactiveAnomaly-SourceDetails"></a>
 Details about the source of the analyzed operational data that triggered the anomaly. The one supported source is Amazon CloudWatch metrics.
Type: [AnomalySourceDetails](API_AnomalySourceDetails.md) object
Required: No

 ** Status **   <a name="DevOpsGuru-Type-ReactiveAnomaly-Status"></a>
 The status of the anomaly.
Type: String
Valid Values: `ONGOING | CLOSED`
Required: No

 ** Type **   <a name="DevOpsGuru-Type-ReactiveAnomaly-Type"></a>
The type of the reactive anomaly. It can be one of the following types.
+  `CAUSAL` - the anomaly can cause a new insight.
+  `CONTEXTUAL` - the anomaly contains additional information about an insight or its causal anomaly.
Type: String
Valid Values: `CAUSAL | CONTEXTUAL`
Required: No

## See Also
<a name="API_ReactiveAnomaly_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ReactiveAnomaly)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ReactiveAnomaly)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ReactiveAnomaly)
