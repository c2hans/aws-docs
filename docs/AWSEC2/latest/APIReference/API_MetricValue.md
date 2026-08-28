---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MetricValue.html
---

# MetricValue
<a name="API_MetricValue"></a>

 Represents a single metric value with its associated statistic, such as the sum or average of unused capacity hours.

## Contents
<a name="API_MetricValue_Contents"></a>

 ** metric **
 The name of the metric.
Type: String
Valid Values: `reservation-total-capacity-hrs-vcpu | reservation-total-capacity-hrs-inst | reservation-max-size-vcpu | reservation-max-size-inst | reservation-min-size-vcpu | reservation-min-size-inst | reservation-unused-total-capacity-hrs-vcpu | reservation-unused-total-capacity-hrs-inst | reservation-unused-total-estimated-cost | reservation-max-unused-size-vcpu | reservation-max-unused-size-inst | reservation-min-unused-size-vcpu | reservation-min-unused-size-inst | reservation-max-utilization | reservation-min-utilization | reservation-avg-utilization-vcpu | reservation-avg-utilization-inst | reservation-total-count | reservation-total-estimated-cost | reservation-avg-future-size-vcpu | reservation-avg-future-size-inst | reservation-min-future-size-vcpu | reservation-min-future-size-inst | reservation-max-future-size-vcpu | reservation-max-future-size-inst | reservation-avg-committed-size-vcpu | reservation-avg-committed-size-inst | reservation-max-committed-size-vcpu | reservation-max-committed-size-inst | reservation-min-committed-size-vcpu | reservation-min-committed-size-inst | reserved-total-usage-hrs-vcpu | reserved-total-usage-hrs-inst | reserved-total-estimated-cost | unreserved-total-usage-hrs-vcpu | unreserved-total-usage-hrs-inst | unreserved-total-estimated-cost | spot-total-usage-hrs-vcpu | spot-total-usage-hrs-inst | spot-total-estimated-cost | spot-avg-run-time-before-interruption-inst | spot-max-run-time-before-interruption-inst | spot-min-run-time-before-interruption-inst`
Required: No

 ** value **
 The numerical value of the metric for the specified statistic and time period.
Type: Double
Required: No

## See Also
<a name="API_MetricValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/MetricValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/MetricValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/MetricValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
