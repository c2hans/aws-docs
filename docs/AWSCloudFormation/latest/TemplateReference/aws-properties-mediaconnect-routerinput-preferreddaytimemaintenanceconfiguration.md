---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput PreferredDayTimeMaintenanceConfiguration
<a name="aws-properties-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration"></a>

Configuration for preferred day and time maintenance settings.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-syntax.json"></a>

```
{
  "[Day](#cfn-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-day)" : {{String}},
  "[Time](#cfn-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-time)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-syntax.yaml"></a>

```
  [Day](#cfn-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-day): {{String}}
  [Time](#cfn-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-time): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-properties"></a>

`Day`  <a name="cfn-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-day"></a>
The preferred day for maintenance operations.
*Required*: Yes
*Type*: String
*Allowed values*: `MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Time`  <a name="cfn-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-time"></a>
The preferred time for maintenance operations.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
