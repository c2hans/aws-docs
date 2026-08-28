---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EntityMetricData.html
---

# EntityMetricData
<a name="API_EntityMetricData"></a>

A set of metrics that are associated with an entity, such as a specific service or resource. Contains the entity and the list of metric data associated with it.

## Contents
<a name="API_EntityMetricData_Contents"></a>

 ** Entity **   <a name="ACW-Type-EntityMetricData-Entity"></a>
The entity associated with the metrics.
Type: [Entity](API_Entity.md) object
Required: No

 ** MetricData **   <a name="ACW-Type-EntityMetricData-MetricData"></a>
The metric data.
Type: Array of [MetricDatum](API_MetricDatum.md) objects
Required: No

## See Also
<a name="API_EntityMetricData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/EntityMetricData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/EntityMetricData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/EntityMetricData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
