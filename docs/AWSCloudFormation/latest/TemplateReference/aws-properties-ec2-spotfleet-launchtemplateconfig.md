---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-launchtemplateconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet LaunchTemplateConfig
<a name="aws-properties-ec2-spotfleet-launchtemplateconfig"></a>

Specifies a launch template and overrides.

## Syntax
<a name="aws-properties-ec2-spotfleet-launchtemplateconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-launchtemplateconfig-syntax.json"></a>

```
{
  "[LaunchTemplateSpecification](#cfn-ec2-spotfleet-launchtemplateconfig-launchtemplatespecification)" : {{FleetLaunchTemplateSpecification}},
  "[Overrides](#cfn-ec2-spotfleet-launchtemplateconfig-overrides)" : {{[ LaunchTemplateOverrides, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-launchtemplateconfig-syntax.yaml"></a>

```
  [LaunchTemplateSpecification](#cfn-ec2-spotfleet-launchtemplateconfig-launchtemplatespecification): {{
    FleetLaunchTemplateSpecification}}
  [Overrides](#cfn-ec2-spotfleet-launchtemplateconfig-overrides): {{
    - LaunchTemplateOverrides}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-launchtemplateconfig-properties"></a>

`LaunchTemplateSpecification`  <a name="cfn-ec2-spotfleet-launchtemplateconfig-launchtemplatespecification"></a>
The launch template to use. Make sure that the launch template does not contain the `NetworkInterfaceId` parameter because you can't specify a network interface ID in a Spot Fleet.
*Required*: No
*Type*: [FleetLaunchTemplateSpecification](aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Overrides`  <a name="cfn-ec2-spotfleet-launchtemplateconfig-overrides"></a>
Any parameters that you specify override the same parameters in the launch template.
*Required*: No
*Type*: Array of [LaunchTemplateOverrides](aws-properties-ec2-spotfleet-launchtemplateoverrides.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
