---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_IntervalDetails.html
---

# IntervalDetails
<a name="API_IntervalDetails"></a>

Information about the interval period to use for returning results.

## Contents
<a name="API_IntervalDetails_Contents"></a>

 ** IntervalPeriod **   <a name="connect-Type-IntervalDetails-IntervalPeriod"></a>
 `IntervalPeriod`: An aggregated grouping applied to request metrics. Valid `IntervalPeriod` values are: `FIFTEEN_MIN` \| `THIRTY_MIN` \| `HOUR` \| `DAY` \| `WEEK` \| `TOTAL`.
For example, if `IntervalPeriod` is selected `THIRTY_MIN`, `StartTime` and `EndTime` differs by 1 day, then Connect Customer returns 48 results in the response. Each result is aggregated by the THIRTY\_MIN period. By default Connect Customer aggregates results based on the `TOTAL` interval period.
The following list describes restrictions on `StartTime` and `EndTime` based on what `IntervalPeriod` is requested.
+  `FIFTEEN_MIN`: The difference between `StartTime` and `EndTime` must be less than 3 days.
+  `THIRTY_MIN`: The difference between `StartTime` and `EndTime` must be less than 3 days.
+  `HOUR`: The difference between `StartTime` and `EndTime` must be less than 3 days.
+  `DAY`: The difference between `StartTime` and `EndTime` must be less than 35 days.
+  `WEEK`: The difference between `StartTime` and `EndTime` must be less than 35 days.
+  `TOTAL`: The difference between `StartTime` and `EndTime` must be less than 35 days.
Type: String
Valid Values: `FIFTEEN_MIN | THIRTY_MIN | HOUR | DAY | WEEK | TOTAL`
Required: No

 ** TimeZone **   <a name="connect-Type-IntervalDetails-TimeZone"></a>
The timezone applied to requested metrics.
Type: String
Required: No

## See Also
<a name="API_IntervalDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/IntervalDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/IntervalDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/IntervalDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
