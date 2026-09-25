---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobtemplate-parametricconfigurationoverrides.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobTemplate ParametricConfigurationOverrides
<a name="aws-properties-emrcontainers-jobtemplate-parametricconfigurationoverrides"></a>

 A configuration specification to be used to override existing configurations. This data type allows job template parameters to be specified within.

## Syntax
<a name="aws-properties-emrcontainers-jobtemplate-parametricconfigurationoverrides-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobtemplate-parametricconfigurationoverrides-syntax.json"></a>

```
{
  "[ApplicationConfiguration](#cfn-emrcontainers-jobtemplate-parametricconfigurationoverrides-applicationconfiguration)" : {{[ Configuration, ... ]}},
  "[MonitoringConfiguration](#cfn-emrcontainers-jobtemplate-parametricconfigurationoverrides-monitoringconfiguration)" : {{ParametricMonitoringConfiguration}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobtemplate-parametricconfigurationoverrides-syntax.yaml"></a>

```
  [ApplicationConfiguration](#cfn-emrcontainers-jobtemplate-parametricconfigurationoverrides-applicationconfiguration): {{
    - Configuration}}
  [MonitoringConfiguration](#cfn-emrcontainers-jobtemplate-parametricconfigurationoverrides-monitoringconfiguration): {{
    ParametricMonitoringConfiguration}}
```

## Properties
<a name="aws-properties-emrcontainers-jobtemplate-parametricconfigurationoverrides-properties"></a>

`ApplicationConfiguration`  <a name="cfn-emrcontainers-jobtemplate-parametricconfigurationoverrides-applicationconfiguration"></a>
 The configurations for the application running by the job run.
*Required*: No
*Type*: Array of [Configuration](aws-properties-emrcontainers-jobtemplate-configuration.md)
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MonitoringConfiguration`  <a name="cfn-emrcontainers-jobtemplate-parametricconfigurationoverrides-monitoringconfiguration"></a>
 The configurations for monitoring.
*Required*: No
*Type*: [ParametricMonitoringConfiguration](aws-properties-emrcontainers-jobtemplate-parametricmonitoringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
