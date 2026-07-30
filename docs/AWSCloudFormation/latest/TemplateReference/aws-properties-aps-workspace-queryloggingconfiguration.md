---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-workspace-queryloggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Workspace QueryLoggingConfiguration
<a name="aws-properties-aps-workspace-queryloggingconfiguration"></a>

The query logging configuration in an Amazon Managed Service for Prometheus workspace.

## Syntax
<a name="aws-properties-aps-workspace-queryloggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-workspace-queryloggingconfiguration-syntax.json"></a>

```
{
  "[Destinations](#cfn-aps-workspace-queryloggingconfiguration-destinations)" : {{[ LoggingDestination, ... ]}}
}
```

### YAML
<a name="aws-properties-aps-workspace-queryloggingconfiguration-syntax.yaml"></a>

```
  [Destinations](#cfn-aps-workspace-queryloggingconfiguration-destinations): {{
    - LoggingDestination}}
```

## Properties
<a name="aws-properties-aps-workspace-queryloggingconfiguration-properties"></a>

`Destinations`  <a name="cfn-aps-workspace-queryloggingconfiguration-destinations"></a>
Defines a destination and its associated filtering criteria for query logging.
*Required*: Yes
*Type*: Array of [LoggingDestination](aws-properties-aps-workspace-loggingdestination.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
