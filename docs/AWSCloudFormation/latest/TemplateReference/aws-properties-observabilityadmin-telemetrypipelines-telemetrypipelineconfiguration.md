---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryPipelines TelemetryPipelineConfiguration
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration"></a>

Defines the configuration for a pipeline, including how data flows from sources through processors to destinations. The configuration is specified in YAML format and must include a valid pipeline definition with required source and sink components. This pipeline enables end-to-end telemetry data collection, transformation, and delivery while supporting optional processing steps and extensions for enhanced functionality.

The primary pipeline configuration section are:
+ **Source:** Defines where log data originates from (S3 buckets, CloudWatch Logs, third-party APIs). Each pipeline must have exactly one source.
+ **Processors (optional):** Transform, parse, and enrich log data as it flows through the pipeline. Processors are applied sequentially in the order they are defined.
+ **Sink:** Defines the destination where processed log data is sent. Each pipeline must have exactly one sink.
+ **Extensions (optional):** Provide additional functionality such as AWS Secrets Manager integration for credential management.

For more details on each configuration section see [CloudWatch pipelines User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-pipelines.html). Additional comprehensive configuration examples can be found in the [CreateTelemetryPipeline API docs](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateTelemetryPipeline.html#API_CreateTelemetryPipeline_Examples).

## Syntax
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration-syntax.json"></a>

```
{
  "[Body](#cfn-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration-body)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration-syntax.yaml"></a>

```
  [Body](#cfn-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration-body): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration-properties"></a>

`Body`  <a name="cfn-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration-body"></a>
The pipeline configuration body that defines the data processing rules and transformations.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `24000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
