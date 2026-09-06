---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet FleetLaunchTemplateSpecificationRequest
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest"></a>

Specifies the launch template to be used by the EC2 Fleet for configuring Amazon EC2 instances.

You must specify the following:
+ The ID or the name of the launch template, but not both.
+ The version of the launch template.

`FleetLaunchTemplateSpecificationRequest` is a property of the [FleetLaunchTemplateConfigRequest](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest.html) property type.

For information about creating a launch template, see [AWS::EC2::LaunchTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html) and [Create a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template) in the *Amazon EC2 User Guide*.

For examples of launch templates, see [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#aws-resource-ec2-launchtemplate--examples).

## Syntax
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-syntax.json"></a>

```
{
  "[LaunchTemplateId](#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplateid)" : {{String}},
  "[LaunchTemplateName](#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplatename)" : {{String}},
  "[LaunchTemplateSpecificationUserData](#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplatespecificationuserdata)" : {{String}},
  "[Version](#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-syntax.yaml"></a>

```
  [LaunchTemplateId](#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplateid): {{String}}
  [LaunchTemplateName](#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplatename): {{String}}
  [LaunchTemplateSpecificationUserData](#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplatespecificationuserdata): {{String}}
  [Version](#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-version): {{String}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-properties"></a>

`LaunchTemplateId`  <a name="cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplateid"></a>
The ID of the launch template.
You must specify the `LaunchTemplateId` or the `LaunchTemplateName`, but not both.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LaunchTemplateName`  <a name="cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplatename"></a>
The name of the launch template.
You must specify the `LaunchTemplateName` or the `LaunchTemplateId`, but not both.
*Required*: Conditional
*Type*: String
*Pattern*: `[a-zA-Z0-9\(\)\.\-/_]+`
*Minimum*: `3`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LaunchTemplateSpecificationUserData`  <a name="cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplatespecificationuserdata"></a>
The base64-encoded user data for instances launched by the fleet. User data is limited to 16 KB, in raw form, before it is base64-encoded.
Supported only for fleets of type `instant`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Version`  <a name="cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-version"></a>
The launch template version number, `$Latest`, or `$Default`. You must specify a value, otherwise the request fails.
If the value is `$Latest`, Amazon EC2 uses the latest version of the launch template.
If the value is `$Default`, Amazon EC2 uses the default version of the launch template.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest--seealso"></a>
+ [ FleetLaunchTemplateSpecificationRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FleetLaunchTemplateSpecificationRequest.html) in the *Amazon EC2 API Reference*
