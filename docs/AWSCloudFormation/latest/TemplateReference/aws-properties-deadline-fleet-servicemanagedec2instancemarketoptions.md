---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet ServiceManagedEc2InstanceMarketOptions
<a name="aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions"></a>

The details of the Amazon EC2 instance market options for a service managed fleet.

## Syntax
<a name="aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions-syntax.json"></a>

```
{
  "[Type](#cfn-deadline-fleet-servicemanagedec2instancemarketoptions-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions-syntax.yaml"></a>

```
  [Type](#cfn-deadline-fleet-servicemanagedec2instancemarketoptions-type): {{String}}
```

## Properties
<a name="aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions-properties"></a>

`Type`  <a name="cfn-deadline-fleet-servicemanagedec2instancemarketoptions-type"></a>
The Amazon EC2 instance type.
*Required*: Yes
*Type*: String
*Allowed values*: `on-demand | spot | wait-and-save`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
