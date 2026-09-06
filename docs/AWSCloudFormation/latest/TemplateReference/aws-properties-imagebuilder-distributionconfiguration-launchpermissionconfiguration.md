---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::DistributionConfiguration LaunchPermissionConfiguration
<a name="aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration"></a>

Describes the configuration for a launch permission. The launch permission modification request is sent to the [Amazon EC2 ModifyImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html) API on behalf of the user for each Region they have selected to distribute the AMI. To make an AMI public, set the launch permission authorized accounts to `all`. See the examples for making an AMI public at [Amazon EC2 ModifyImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html).

## Syntax
<a name="aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration-syntax.json"></a>

```
{
  "[OrganizationalUnitArns](#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationalunitarns)" : {{[ String, ... ]}},
  "[OrganizationArns](#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationarns)" : {{[ String, ... ]}},
  "[UserGroups](#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-usergroups)" : {{[ String, ... ]}},
  "[UserIds](#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-userids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration-syntax.yaml"></a>

```
  [OrganizationalUnitArns](#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationalunitarns): {{
    - String}}
  [OrganizationArns](#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationarns): {{
    - String}}
  [UserGroups](#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-usergroups): {{
    - String}}
  [UserIds](#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-userids): {{
    - String}}
```

## Properties
<a name="aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration-properties"></a>

`OrganizationalUnitArns`  <a name="cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationalunitarns"></a>
The ARN for an AWS Organizations organizational unit (OU) that you want to share your AMI with. For more information about key concepts for AWS Organizations, see [AWS Organizations terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html).
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrganizationArns`  <a name="cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationarns"></a>
The ARN for an AWS Organization that you want to share your AMI with. For more information, see [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserGroups`  <a name="cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-usergroups"></a>
The name of the group.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserIds`  <a name="cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-userids"></a>
The AWS account ID.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1536`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
