---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryPipelines TelemetryPipelineStatusReason
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason"></a>

Provides detailed information about the status of a telemetry pipeline, including reasons for specific states.

## Syntax
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason-syntax.json"></a>

```
{
  "[Description](#cfn-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason-description)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason-syntax.yaml"></a>

```
  [Description](#cfn-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason-description): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason-properties"></a>

`Description`  <a name="cfn-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason-description"></a>
A description of the pipeline status reason, providing additional context about the current state.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
