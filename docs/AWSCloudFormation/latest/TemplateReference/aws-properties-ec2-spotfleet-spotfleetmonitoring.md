---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-spotfleetmonitoring.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet SpotFleetMonitoring
<a name="aws-properties-ec2-spotfleet-spotfleetmonitoring"></a>

Describes whether monitoring is enabled.

## Syntax
<a name="aws-properties-ec2-spotfleet-spotfleetmonitoring-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-spotfleetmonitoring-syntax.json"></a>

```
{
  "[Enabled](#cfn-ec2-spotfleet-spotfleetmonitoring-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-spotfleetmonitoring-syntax.yaml"></a>

```
  [Enabled](#cfn-ec2-spotfleet-spotfleetmonitoring-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-spotfleetmonitoring-properties"></a>

`Enabled`  <a name="cfn-ec2-spotfleet-spotfleetmonitoring-enabled"></a>
Enables monitoring for the instance.
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
