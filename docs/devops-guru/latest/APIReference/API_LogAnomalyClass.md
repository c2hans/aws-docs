---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_LogAnomalyClass.html
---

# LogAnomalyClass
<a name="API_LogAnomalyClass"></a>

 Information about an anomalous log event found within a log group.

## Contents
<a name="API_LogAnomalyClass_Contents"></a>

 ** Explanation **   <a name="DevOpsGuru-Type-LogAnomalyClass-Explanation"></a>
 The explanation for why the log event is considered an anomaly.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** LogAnomalyToken **   <a name="DevOpsGuru-Type-LogAnomalyClass-LogAnomalyToken"></a>
 The token where the anomaly was detected. This may refer to an exception or another location, or it may be blank for log anomalies such as format anomalies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** LogAnomalyType **   <a name="DevOpsGuru-Type-LogAnomalyClass-LogAnomalyType"></a>
 The type of log anomaly that has been detected.
Type: String
Valid Values: `KEYWORD | KEYWORD_TOKEN | FORMAT | HTTP_CODE | BLOCK_FORMAT | NUMERICAL_POINT | NUMERICAL_NAN | NEW_FIELD_NAME`
Required: No

 ** LogEventId **   <a name="DevOpsGuru-Type-LogAnomalyClass-LogEventId"></a>
 The ID of the log event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** LogEventTimestamp **   <a name="DevOpsGuru-Type-LogAnomalyClass-LogEventTimestamp"></a>
 The time of the first occurrence of the anomalous log event.
Type: Timestamp
Required: No

 ** LogStreamName **   <a name="DevOpsGuru-Type-LogAnomalyClass-LogStreamName"></a>
 The name of the Amazon CloudWatch log stream that the anomalous log event belongs to. A log stream is a sequence of log events that share the same source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** NumberOfLogLinesOccurrences **   <a name="DevOpsGuru-Type-LogAnomalyClass-NumberOfLogLinesOccurrences"></a>
 The number of log lines where this anomalous log event occurs.
Type: Integer
Required: No

## See Also
<a name="API_LogAnomalyClass_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/LogAnomalyClass)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/LogAnomalyClass)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/LogAnomalyClass)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
