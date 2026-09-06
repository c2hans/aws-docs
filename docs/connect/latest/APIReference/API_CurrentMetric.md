---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CurrentMetric.html
---

# CurrentMetric
<a name="API_CurrentMetric"></a>

Contains information about a real-time metric. For a description of each metric, see [Metrics definitions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Connect Customer Administrator Guide*.

**Important**
Only one of either the Name or MetricId is required.

## Contents
<a name="API_CurrentMetric_Contents"></a>

 ** MetricId **   <a name="connect-Type-CurrentMetric-MetricId"></a>
Out of the box current metrics or custom metrics can be referenced via this field. This field is a valid AWS Connect Arn or a UUID.
Type: String
Pattern: `^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})|(arn:[a-z0-9-]+:connect:[a-z0-9-]+:(?:([0-9]{12}):instance/[a-z0-9-]+/metric/[a-z0-9-]+(?::[a-z0-9-]+)?|aws:metric/[A-Z_]+))$`
Required: No

 ** Name **   <a name="connect-Type-CurrentMetric-Name"></a>
The name of the metric.
Type: String
Valid Values: `AGENTS_ONLINE | AGENTS_AVAILABLE | AGENTS_ON_CALL | AGENTS_NON_PRODUCTIVE | AGENTS_AFTER_CONTACT_WORK | AGENTS_ERROR | AGENTS_STAFFED | CONTACTS_IN_QUEUE | OLDEST_CONTACT_AGE | CONTACTS_SCHEDULED | AGENTS_ON_CONTACT | SLOTS_ACTIVE | SLOTS_AVAILABLE | ESTIMATED_WAIT_TIME`
Required: No

 ** Unit **   <a name="connect-Type-CurrentMetric-Unit"></a>
The Unit parameter is not supported for custom metrics.
The unit for the metric.
Type: String
Valid Values: `SECONDS | COUNT | PERCENT`
Required: No

## See Also
<a name="API_CurrentMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CurrentMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CurrentMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CurrentMetric)
