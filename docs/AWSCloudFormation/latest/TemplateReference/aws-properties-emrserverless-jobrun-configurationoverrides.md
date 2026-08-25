---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-jobrun-configurationoverrides.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::JobRun ConfigurationOverrides
<a name="aws-properties-emrserverless-jobrun-configurationoverrides"></a>

A configuration specification to be used to override existing configurations.

## Syntax
<a name="aws-properties-emrserverless-jobrun-configurationoverrides-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-jobrun-configurationoverrides-syntax.json"></a>

```
{
  "[ApplicationConfiguration](#cfn-emrserverless-jobrun-configurationoverrides-applicationconfiguration)" : {{[ Configuration, ... ]}},
  "[MonitoringConfiguration](#cfn-emrserverless-jobrun-configurationoverrides-monitoringconfiguration)" : {{MonitoringConfiguration}}
}
```

### YAML
<a name="aws-properties-emrserverless-jobrun-configurationoverrides-syntax.yaml"></a>

```
  [ApplicationConfiguration](#cfn-emrserverless-jobrun-configurationoverrides-applicationconfiguration): {{
    - Configuration}}
  [MonitoringConfiguration](#cfn-emrserverless-jobrun-configurationoverrides-monitoringconfiguration): {{
    MonitoringConfiguration}}
```

## Properties
<a name="aws-properties-emrserverless-jobrun-configurationoverrides-properties"></a>

`ApplicationConfiguration`  <a name="cfn-emrserverless-jobrun-configurationoverrides-applicationconfiguration"></a>
The override configurations for the application.
*Required*: No
*Type*: Array of [Configuration](aws-properties-emrserverless-jobrun-configuration.md)
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MonitoringConfiguration`  <a name="cfn-emrserverless-jobrun-configurationoverrides-monitoringconfiguration"></a>
The override configurations for monitoring.
*Required*: No
*Type*: [MonitoringConfiguration](aws-properties-emrserverless-jobrun-monitoringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
