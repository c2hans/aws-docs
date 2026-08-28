---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DataQuery.html
---

# DataQuery
<a name="API_DataQuery"></a>

A query used for retrieving network health data.

## Contents
<a name="API_DataQuery_Contents"></a>

 ** Destination **
The Region or Availability Zone that's the target for the data query. For example, `eu-north-1`.
Type: String
Required: No

 ** Id **
A user-defined ID associated with a data query that's returned in the `dataResponse` identifying the query. For example, if you set the Id to `MyQuery01`in the query, the `dataResponse` identifies the query as `MyQuery01`.
Type: String
Required: No

 ** Metric **
The metric used for the network performance request.
Type: String
Valid Values: `aggregate-latency`
Required: No

 ** Period **
The aggregation period used for the data query.
Type: String
Valid Values: `five-minutes | fifteen-minutes | one-hour | three-hours | one-day | one-week`
Required: No

 ** Source **
The Region or Availability Zone that's the source for the data query. For example, `us-east-1`.
Type: String
Required: No

 ** Statistic **
The metric data aggregation period, `p50`, between the specified `startDate` and `endDate`. For example, a metric of `five_minutes` is the median of all the data points gathered within those five minutes. `p50` is the only supported metric.
Type: String
Valid Values: `p50`
Required: No

## See Also
<a name="API_DataQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DataQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DataQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DataQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
