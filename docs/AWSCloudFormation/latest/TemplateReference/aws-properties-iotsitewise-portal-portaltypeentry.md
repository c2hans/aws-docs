---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-portal-portaltypeentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Portal PortalTypeEntry
<a name="aws-properties-iotsitewise-portal-portaltypeentry"></a>

<a name="aws-properties-iotsitewise-portal-portaltypeentry-description"></a>The `PortalTypeEntry` property type specifies Property description not available. for an [AWS::IoTSiteWise::Portal](aws-resource-iotsitewise-portal.md).

## Syntax
<a name="aws-properties-iotsitewise-portal-portaltypeentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-portal-portaltypeentry-syntax.json"></a>

```
{
  "[PortalTools](#cfn-iotsitewise-portal-portaltypeentry-portaltools)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-iotsitewise-portal-portaltypeentry-syntax.yaml"></a>

```
  [PortalTools](#cfn-iotsitewise-portal-portaltypeentry-portaltools): {{
    - String}}
```

## Properties
<a name="aws-properties-iotsitewise-portal-portaltypeentry-properties"></a>

`PortalTools`  <a name="cfn-iotsitewise-portal-portaltypeentry-portaltools"></a>
The array of tools associated with the specified portal type. The possible values are `ASSISTANT` and `DASHBOARD`.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
