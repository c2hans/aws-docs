---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MetricPoint.html
---

# MetricPoint
<a name="API_MetricPoint"></a>

Indicates whether the network was healthy or degraded at a particular point. The value is aggregated from the `startDate` to the `endDate`. Currently only `five_minutes` is supported.

## Contents
<a name="API_MetricPoint_Contents"></a>

 ** endDate **
The end date for the metric point. The ending time must be formatted as `yyyy-mm-ddThh:mm:ss`. For example, `2022-06-12T12:00:00.000Z`.
Type: Timestamp
Required: No

 ** startDate **
The start date for the metric point. The starting date for the metric point. The starting time must be formatted as `yyyy-mm-ddThh:mm:ss`. For example, `2022-06-10T12:00:00.000Z`.
Type: Timestamp
Required: No

 ** status **
The status of the metric point.
Type: String
Required: No

 ** value **
Type: Float
Required: No

## See Also
<a name="API_MetricPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/MetricPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/MetricPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/MetricPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
