---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-metricsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping MetricsConfig
<a name="aws-properties-lambda-eventsourcemapping-metricsconfig"></a>

The metrics configuration for your event source. Use this configuration object to define which metrics you want your event source mapping to produce.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-metricsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-metricsconfig-syntax.json"></a>

```
{
  "[Metrics](#cfn-lambda-eventsourcemapping-metricsconfig-metrics)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-metricsconfig-syntax.yaml"></a>

```
  [Metrics](#cfn-lambda-eventsourcemapping-metricsconfig-metrics): {{
    - String}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-metricsconfig-properties"></a>

`Metrics`  <a name="cfn-lambda-eventsourcemapping-metricsconfig-metrics"></a>
 The metrics you want your event source mapping to produce, including `EventCount`, `ErrorCount`, `KafkaMetrics`.
+ `EventCount` to receive metrics related to the number of events processed by your event source mapping.
+ `ErrorCount` (Amazon MSK and self-managed Apache Kafka) to receive metrics related to the number of errors in your event source mapping processing.
+ `KafkaMetrics` (Amazon MSK and self-managed Apache Kafka) to receive metrics related to the Kafka consumers from your event source mapping.
 For more information about these metrics, see [ Event source mapping metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics).
*Required*: No
*Type*: Array of String
*Allowed values*: `EventCount | ErrorCount | KafkaMetrics`
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
