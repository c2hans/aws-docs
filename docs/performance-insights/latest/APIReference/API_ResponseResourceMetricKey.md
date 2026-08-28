---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ResponseResourceMetricKey.html
---

# ResponseResourceMetricKey
<a name="API_ResponseResourceMetricKey"></a>

An object describing a Performance Insights metric and one or more dimensions for that metric.

## Contents
<a name="API_ResponseResourceMetricKey_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Metric **   <a name="performanceinsights-Type-ResponseResourceMetricKey-Metric"></a>
The name of a Performance Insights metric to be measured.
Valid values for `Metric` are:
+  `db.load.avg` - A scaled representation of the number of active sessions for the database engine.
+  `db.sampledload.avg` - The raw number of active sessions for the database engine.
+ The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon Aurora User Guide*.
+ The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon RDS User Guide*.
If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg`. For most use cases, you can query `db.load.avg` only.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** Dimensions **   <a name="performanceinsights-Type-ResponseResourceMetricKey-Dimensions"></a>
The valid dimensions for the metric.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ResponseResourceMetricKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/ResponseResourceMetricKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/ResponseResourceMetricKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/ResponseResourceMetricKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
