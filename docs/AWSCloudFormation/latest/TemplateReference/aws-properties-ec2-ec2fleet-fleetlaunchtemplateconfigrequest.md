---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet FleetLaunchTemplateConfigRequest
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest"></a>

Specifies a launch template and overrides for an EC2 Fleet.

`FleetLaunchTemplateConfigRequest` is a property of the [AWS::EC2::EC2Fleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html) resource.

## Syntax
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-syntax.json"></a>

```
{
  "[LaunchTemplateSpecification](#cfn-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-launchtemplatespecification)" : {{FleetLaunchTemplateSpecificationRequest}},
  "[Overrides](#cfn-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-overrides)" : {{[ FleetLaunchTemplateOverridesRequest, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-syntax.yaml"></a>

```
  [LaunchTemplateSpecification](#cfn-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-launchtemplatespecification): {{
    FleetLaunchTemplateSpecificationRequest}}
  [Overrides](#cfn-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-overrides): {{
    - FleetLaunchTemplateOverridesRequest}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-properties"></a>

`LaunchTemplateSpecification`  <a name="cfn-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-launchtemplatespecification"></a>
The launch template to use. You must specify either the launch template ID or launch template name in the request.
*Required*: No
*Type*: [FleetLaunchTemplateSpecificationRequest](aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Overrides`  <a name="cfn-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-overrides"></a>
Any parameters that you specify override the same parameters in the launch template.
For fleets of type `request` and `maintain`, a maximum of 300 items is allowed across all launch templates.
*Required*: No
*Type*: Array of [FleetLaunchTemplateOverridesRequest](aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest--seealso"></a>
+ [ FleetLaunchTemplateConfigRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FleetLaunchTemplateConfigRequest.html) in the *Amazon EC2 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
