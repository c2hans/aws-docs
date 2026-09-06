---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-maintenanceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput MaintenanceConfiguration
<a name="aws-properties-mediaconnect-routerinput-maintenanceconfiguration"></a>

The maintenance configuration settings applied to this router input.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-maintenanceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-maintenanceconfiguration-syntax.json"></a>

```
{
  "[Default](#cfn-mediaconnect-routerinput-maintenanceconfiguration-default)" : {{Json}},
  "[PreferredDayTime](#cfn-mediaconnect-routerinput-maintenanceconfiguration-preferreddaytime)" : {{PreferredDayTimeMaintenanceConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-maintenanceconfiguration-syntax.yaml"></a>

```
  [Default](#cfn-mediaconnect-routerinput-maintenanceconfiguration-default): {{Json}}
  [PreferredDayTime](#cfn-mediaconnect-routerinput-maintenanceconfiguration-preferreddaytime): {{
    PreferredDayTimeMaintenanceConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-maintenanceconfiguration-properties"></a>

`Default`  <a name="cfn-mediaconnect-routerinput-maintenanceconfiguration-default"></a>
Configuration settings for default maintenance scheduling.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredDayTime`  <a name="cfn-mediaconnect-routerinput-maintenanceconfiguration-preferreddaytime"></a>
Configuration for preferred day and time maintenance settings.
*Required*: No
*Type*: [PreferredDayTimeMaintenanceConfiguration](aws-properties-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
