---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryPipelines TelemetryPipeline
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline"></a>

Represents a complete telemetry pipeline resource with configuration, status, and metadata for data processing and transformation.

## Syntax
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline-syntax.json"></a>

```
{
  "[Arn](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-arn)" : {{String}},
  "[Configuration](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-configuration)" : {{TelemetryPipelineConfiguration}},
  "[CreatedTimeStamp](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-createdtimestamp)" : {{Number}},
  "[LastUpdateTimeStamp](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-lastupdatetimestamp)" : {{Number}},
  "[Name](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-name)" : {{String}},
  "[Status](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-status)" : {{String}},
  "[StatusReason](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-statusreason)" : {{TelemetryPipelineStatusReason}},
  "[Tags](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline-syntax.yaml"></a>

```
  [Arn](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-arn): {{String}}
  [Configuration](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-configuration): {{
    TelemetryPipelineConfiguration}}
  [CreatedTimeStamp](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-createdtimestamp): {{Number}}
  [LastUpdateTimeStamp](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-lastupdatetimestamp): {{Number}}
  [Name](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-name): {{String}}
  [Status](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-status): {{String}}
  [StatusReason](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-statusreason): {{
    TelemetryPipelineStatusReason}}
  [Tags](#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline-properties"></a>

`Arn`  <a name="cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-arn"></a>
The Amazon Resource Name (ARN) of the telemetry pipeline.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)$`
*Minimum*: `1`
*Maximum*: `1011`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configuration`  <a name="cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-configuration"></a>
The configuration that defines how the telemetry pipeline processes data. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Creating-pipelines.html).
*Required*: No
*Type*: [TelemetryPipelineConfiguration](aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatedTimeStamp`  <a name="cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-createdtimestamp"></a>
The timestamp when the telemetry pipeline was created.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastUpdateTimeStamp`  <a name="cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-lastupdatetimestamp"></a>
The timestamp when the telemetry pipeline was last updated.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-name"></a>
The name of the telemetry pipeline.
*Required*: No
*Type*: String
*Pattern*: `[a-z][a-z0-9\-]+`
*Minimum*: `3`
*Maximum*: `28`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-status"></a>
The current status of the telemetry pipeline.
*Required*: No
*Type*: String
*Allowed values*: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusReason`  <a name="cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-statusreason"></a>
Additional information about the pipeline status, including reasons for failure states.
*Required*: No
*Type*: [TelemetryPipelineStatusReason](aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-tags"></a>
The key-value pairs associated with the telemetry pipeline resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-observabilityadmin-telemetrypipelines-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
