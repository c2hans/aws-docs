---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-endpoint-configurationoverrides.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::Endpoint ConfigurationOverrides
<a name="aws-properties-emrcontainers-endpoint-configurationoverrides"></a>

A configuration specification to be used to override existing configurations.

## Syntax
<a name="aws-properties-emrcontainers-endpoint-configurationoverrides-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-endpoint-configurationoverrides-syntax.json"></a>

```
{
  "[ApplicationConfiguration](#cfn-emrcontainers-endpoint-configurationoverrides-applicationconfiguration)" : {{[ EMREKSConfiguration, ... ]}},
  "[MonitoringConfiguration](#cfn-emrcontainers-endpoint-configurationoverrides-monitoringconfiguration)" : {{MonitoringConfiguration}}
}
```

### YAML
<a name="aws-properties-emrcontainers-endpoint-configurationoverrides-syntax.yaml"></a>

```
  [ApplicationConfiguration](#cfn-emrcontainers-endpoint-configurationoverrides-applicationconfiguration): {{
    - EMREKSConfiguration}}
  [MonitoringConfiguration](#cfn-emrcontainers-endpoint-configurationoverrides-monitoringconfiguration): {{
    MonitoringConfiguration}}
```

## Properties
<a name="aws-properties-emrcontainers-endpoint-configurationoverrides-properties"></a>

`ApplicationConfiguration`  <a name="cfn-emrcontainers-endpoint-configurationoverrides-applicationconfiguration"></a>
The configurations for the application running by the job run.
*Required*: No
*Type*: Array of [EMREKSConfiguration](aws-properties-emrcontainers-endpoint-emreksconfiguration.md)
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MonitoringConfiguration`  <a name="cfn-emrcontainers-endpoint-configurationoverrides-monitoringconfiguration"></a>
The configurations for monitoring.
*Required*: No
*Type*: [MonitoringConfiguration](aws-properties-emrcontainers-endpoint-monitoringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
