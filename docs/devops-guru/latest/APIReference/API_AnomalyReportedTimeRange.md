---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_AnomalyReportedTimeRange.html
---

# AnomalyReportedTimeRange
<a name="API_AnomalyReportedTimeRange"></a>

 A time range that specifies when DevOps Guru opens and then closes an anomaly. This is different from `AnomalyTimeRange`, which specifies the time range when DevOps Guru actually observes the anomalous behavior.

## Contents
<a name="API_AnomalyReportedTimeRange_Contents"></a>

 ** OpenTime **   <a name="DevOpsGuru-Type-AnomalyReportedTimeRange-OpenTime"></a>
 The time when an anomaly is opened.
Type: Timestamp
Required: Yes

 ** CloseTime **   <a name="DevOpsGuru-Type-AnomalyReportedTimeRange-CloseTime"></a>
 The time when an anomaly is closed.
Type: Timestamp
Required: No

## See Also
<a name="API_AnomalyReportedTimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/AnomalyReportedTimeRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/AnomalyReportedTimeRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/AnomalyReportedTimeRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
