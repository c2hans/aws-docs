---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Anomaly.html
---

# Anomaly
<a name="API_Anomaly"></a>

Contains information about the anomalies.

## Contents
<a name="API_Anomaly_Contents"></a>

 ** profiles **   <a name="guardduty-Type-Anomaly-profiles"></a>
Information about the types of profiles.
Type: String to string to array of [AnomalyObject](API_AnomalyObject.md) objects map map
Required: No

 ** unusual **   <a name="guardduty-Type-Anomaly-unusual"></a>
Information about the behavior of the anomalies.
Type: [AnomalyUnusual](API_AnomalyUnusual.md) object
Required: No

## See Also
<a name="API_Anomaly_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Anomaly)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Anomaly)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Anomaly)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
