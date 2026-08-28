---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_AnomalyDetector.html
---

# AnomalyDetector
<a name="API_AnomalyDetector"></a>

Contains information about one anomaly detector in the account.

## Contents
<a name="API_AnomalyDetector_Contents"></a>

 ** anomalyDetectorArn **   <a name="CWL-Type-AnomalyDetector-anomalyDetectorArn"></a>
The ARN of the anomaly detector.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** anomalyDetectorStatus **   <a name="CWL-Type-AnomalyDetector-anomalyDetectorStatus"></a>
Specifies the current status of the anomaly detector. To pause an anomaly detector, use the `enabled` parameter in the [UpdateLogAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateLogAnomalyDetector.html) operation.
Type: String
Valid Values: `INITIALIZING | TRAINING | ANALYZING | FAILED | DELETED | PAUSED`
Required: No

 ** anomalyVisibilityTime **   <a name="CWL-Type-AnomalyDetector-anomalyVisibilityTime"></a>
The number of days used as the life cycle of anomalies. After this time, anomalies are automatically baselined and the anomaly detector model will treat new occurrences of similar event as normal.
Type: Long
Valid Range: Minimum value of 7. Maximum value of 90.
Required: No

 ** creationTimeStamp **   <a name="CWL-Type-AnomalyDetector-creationTimeStamp"></a>
The date and time when this anomaly detector was created.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** detectorName **   <a name="CWL-Type-AnomalyDetector-detectorName"></a>
The name of the anomaly detector.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** evaluationFrequency **   <a name="CWL-Type-AnomalyDetector-evaluationFrequency"></a>
Specifies how often the anomaly detector runs and look for anomalies.
Type: String
Valid Values: `ONE_MIN | FIVE_MIN | TEN_MIN | FIFTEEN_MIN | THIRTY_MIN | ONE_HOUR`
Required: No

 ** filterPattern **   <a name="CWL-Type-AnomalyDetector-filterPattern"></a>
A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event can contain timestamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** kmsKeyId **   <a name="CWL-Type-AnomalyDetector-kmsKeyId"></a>
The ARN of the AWS KMS key assigned to this anomaly detector, if any.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** lastModifiedTimeStamp **   <a name="CWL-Type-AnomalyDetector-lastModifiedTimeStamp"></a>
The date and time when this anomaly detector was most recently modified.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** logGroupArnList **   <a name="CWL-Type-AnomalyDetector-logGroupArnList"></a>
A list of the ARNs of the log groups that this anomaly detector watches.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

## See Also
<a name="API_AnomalyDetector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/AnomalyDetector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/AnomalyDetector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/AnomalyDetector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
