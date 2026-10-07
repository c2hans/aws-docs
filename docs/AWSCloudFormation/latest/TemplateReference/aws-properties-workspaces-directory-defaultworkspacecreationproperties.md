---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-defaultworkspacecreationproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory DefaultWorkspaceCreationProperties
<a name="aws-properties-workspaces-directory-defaultworkspacecreationproperties"></a>

Describes the default values that are used to create WorkSpaces. For more information, see [Update Directory Details for Your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html).

## Syntax
<a name="aws-properties-workspaces-directory-defaultworkspacecreationproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-defaultworkspacecreationproperties-syntax.json"></a>

```
{
  "[CustomSecurityGroupId](#cfn-workspaces-directory-defaultworkspacecreationproperties-customsecuritygroupid)" : {{String}},
  "[DefaultOu](#cfn-workspaces-directory-defaultworkspacecreationproperties-defaultou)" : {{String}},
  "[EnableInternetAccess](#cfn-workspaces-directory-defaultworkspacecreationproperties-enableinternetaccess)" : {{Boolean}},
  "[EnableMaintenanceMode](#cfn-workspaces-directory-defaultworkspacecreationproperties-enablemaintenancemode)" : {{Boolean}},
  "[InstanceIamRoleArn](#cfn-workspaces-directory-defaultworkspacecreationproperties-instanceiamrolearn)" : {{String}},
  "[UserEnabledAsLocalAdministrator](#cfn-workspaces-directory-defaultworkspacecreationproperties-userenabledaslocaladministrator)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-defaultworkspacecreationproperties-syntax.yaml"></a>

```
  [CustomSecurityGroupId](#cfn-workspaces-directory-defaultworkspacecreationproperties-customsecuritygroupid): {{String}}
  [DefaultOu](#cfn-workspaces-directory-defaultworkspacecreationproperties-defaultou): {{String}}
  [EnableInternetAccess](#cfn-workspaces-directory-defaultworkspacecreationproperties-enableinternetaccess): {{Boolean}}
  [EnableMaintenanceMode](#cfn-workspaces-directory-defaultworkspacecreationproperties-enablemaintenancemode): {{Boolean}}
  [InstanceIamRoleArn](#cfn-workspaces-directory-defaultworkspacecreationproperties-instanceiamrolearn): {{String}}
  [UserEnabledAsLocalAdministrator](#cfn-workspaces-directory-defaultworkspacecreationproperties-userenabledaslocaladministrator): {{Boolean}}
```

## Properties
<a name="aws-properties-workspaces-directory-defaultworkspacecreationproperties-properties"></a>

`CustomSecurityGroupId`  <a name="cfn-workspaces-directory-defaultworkspacecreationproperties-customsecuritygroupid"></a>
The identifier of the default security group to apply to WorkSpaces when they are created. For more information, see [ Security Groups for Your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-security-groups.html).
*Required*: No
*Type*: String
*Pattern*: `^(sg-([0-9a-f]{8}|[0-9a-f]{17}))$`
*Minimum*: `11`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultOu`  <a name="cfn-workspaces-directory-defaultworkspacecreationproperties-defaultou"></a>
The organizational unit (OU) in the directory for the WorkSpace machine accounts.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableInternetAccess`  <a name="cfn-workspaces-directory-defaultworkspacecreationproperties-enableinternetaccess"></a>
Specifies whether to automatically assign an Elastic public IP address to WorkSpaces in this directory by default. If enabled, the Elastic public IP address allows outbound internet access from your WorkSpaces when you’re using an internet gateway in the Amazon VPC in which your WorkSpaces are located. If you're using a Network Address Translation (NAT) gateway for outbound internet access from your VPC, or if your WorkSpaces are in public subnets and you manually assign them Elastic IP addresses, you should disable this setting. This setting applies to new WorkSpaces that you launch or to existing WorkSpaces that you rebuild. For more information, see [ Configure a VPC for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableMaintenanceMode`  <a name="cfn-workspaces-directory-defaultworkspacecreationproperties-enablemaintenancemode"></a>
Specifies whether maintenance mode is enabled for WorkSpaces. For more information, see [WorkSpace Maintenance](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceIamRoleArn`  <a name="cfn-workspaces-directory-defaultworkspacecreationproperties-instanceiamrolearn"></a>
Indicates the IAM role ARN of the instance.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z-]{0,7}:[A-Za-z0-9][A-za-z0-9_/.-]{0,62}:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserEnabledAsLocalAdministrator`  <a name="cfn-workspaces-directory-defaultworkspacecreationproperties-userenabledaslocaladministrator"></a>
Specifies whether WorkSpace users are local administrators on their WorkSpaces.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
