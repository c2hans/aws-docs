---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MetricInterval.html
---

# MetricInterval
<a name="API_MetricInterval"></a>

The interval period with the start and end time for the metrics.

## Contents
<a name="API_MetricInterval_Contents"></a>

 ** EndTime **   <a name="connect-Type-MetricInterval-EndTime"></a>
The timestamp, in UNIX Epoch time format. End time is based on the interval period selected. For example, If `IntervalPeriod` is selected `THIRTY_MIN`, `StartTime` and `EndTime` in the API request differs by 1 day, then 48 results are returned in the response. Each result is aggregated by the 30 minutes period, with each `StartTime` and `EndTime` differing by 30 minutes.
Type: Timestamp
Required: No

 ** Interval **   <a name="connect-Type-MetricInterval-Interval"></a>
The interval period provided in the API request.
Type: String
Valid Values: `FIFTEEN_MIN | THIRTY_MIN | HOUR | DAY | WEEK | TOTAL`
Required: No

 ** StartTime **   <a name="connect-Type-MetricInterval-StartTime"></a>
The timestamp, in UNIX Epoch time format. Start time is based on the interval period selected.
Type: Timestamp
Required: No

## See Also
<a name="API_MetricInterval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MetricInterval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MetricInterval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MetricInterval)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
