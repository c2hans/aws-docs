---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-fleet-metrics.html
---

# Fleet metrics
<a name="iot-fleet-metrics"></a>

Fleet metrics is a feature of [fleet indexing](iot-indexing.md), a managed service that allows you to index, search, and aggregate your devices' data in AWS IoT. You can use fleet metrics, to monitor your fleet devices' aggregate state in [CloudWatch](https://console.aws.amazon.com/cloudwatch/) over time, including reviewing your fleet devices' disconnection rate or average battery level changes of a specified period.

Using fleet metrics, you can build [aggregation queries](index-aggregate.md) whose results are continually emitted to [CloudWatch](https://console.aws.amazon.com/cloudwatch/) as metrics for analyzing trends and creating alarms. For your monitoring tasks, you can specify the aggregation queries of different aggregation types (**Statistics**, **Cardinality**, and **Percentile**). You can save all of your aggregation queries to create fleet metrics for reuse in the future.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
