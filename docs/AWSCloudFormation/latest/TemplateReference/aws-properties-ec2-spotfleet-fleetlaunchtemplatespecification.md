---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet FleetLaunchTemplateSpecification
<a name="aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification"></a>

Specifies the launch template to be used by the Spot Fleet request for configuring Amazon EC2 instances.

You must specify the following:
+ The ID or the name of the launch template, but not both.
+ The version of the launch template.

`FleetLaunchTemplateSpecification` is a property of the [AWS::EC2::SpotFleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.html) resource.

For information about creating a launch template, see [AWS::EC2::LaunchTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html) and [Create a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template) in the *Amazon EC2 User Guide*.

For examples of launch templates, see [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#aws-resource-ec2-launchtemplate--examples).

## Syntax
<a name="aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification-syntax.json"></a>

```
{
  "[LaunchTemplateId](#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-launchtemplateid)" : {{String}},
  "[LaunchTemplateName](#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-launchtemplatename)" : {{String}},
  "[Version](#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification-syntax.yaml"></a>

```
  [LaunchTemplateId](#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-launchtemplateid): {{String}}
  [LaunchTemplateName](#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-launchtemplatename): {{String}}
  [Version](#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-version): {{String}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification-properties"></a>

`LaunchTemplateId`  <a name="cfn-ec2-spotfleet-fleetlaunchtemplatespecification-launchtemplateid"></a>
The ID of the launch template.
You must specify the `LaunchTemplateId` or the `LaunchTemplateName`, but not both.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LaunchTemplateName`  <a name="cfn-ec2-spotfleet-fleetlaunchtemplatespecification-launchtemplatename"></a>
The name of the launch template.
You must specify the `LaunchTemplateName` or the `LaunchTemplateId`, but not both.
*Required*: Conditional
*Type*: String
*Pattern*: `[a-zA-Z0-9\(\)\.\-/_]+`
*Minimum*: `3`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-ec2-spotfleet-fleetlaunchtemplatespecification-version"></a>
The version number of the launch template.
Specifying `$Latest` or `$Default` for the template version number is not supported. However, you can specify `LatestVersionNumber` or `DefaultVersionNumber` using the `Fn::GetAtt` intrinsic function. For more information, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#aws-resource-ec2-launchtemplate-return-values-fn--getatt).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
