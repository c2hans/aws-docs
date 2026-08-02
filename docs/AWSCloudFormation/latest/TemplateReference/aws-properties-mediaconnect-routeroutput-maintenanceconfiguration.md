---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-maintenanceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput MaintenanceConfiguration
<a name="aws-properties-mediaconnect-routeroutput-maintenanceconfiguration"></a>

The configuration settings for maintenance operations, including preferred maintenance windows and schedules.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-maintenanceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-maintenanceconfiguration-syntax.json"></a>

```
{
  "[Default](#cfn-mediaconnect-routeroutput-maintenanceconfiguration-default)" : {{Json}},
  "[PreferredDayTime](#cfn-mediaconnect-routeroutput-maintenanceconfiguration-preferreddaytime)" : {{PreferredDayTimeMaintenanceConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-maintenanceconfiguration-syntax.yaml"></a>

```
  [Default](#cfn-mediaconnect-routeroutput-maintenanceconfiguration-default): {{Json}}
  [PreferredDayTime](#cfn-mediaconnect-routeroutput-maintenanceconfiguration-preferreddaytime): {{
    PreferredDayTimeMaintenanceConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-maintenanceconfiguration-properties"></a>

`Default`  <a name="cfn-mediaconnect-routeroutput-maintenanceconfiguration-default"></a>
Default maintenance configuration settings.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredDayTime`  <a name="cfn-mediaconnect-routeroutput-maintenanceconfiguration-preferreddaytime"></a>
Preferred day and time maintenance configuration settings.
*Required*: No
*Type*: [PreferredDayTimeMaintenanceConfiguration](aws-properties-mediaconnect-routeroutput-preferreddaytimemaintenanceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
