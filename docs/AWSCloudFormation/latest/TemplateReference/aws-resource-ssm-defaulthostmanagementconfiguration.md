---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-defaulthostmanagementconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::DefaultHostManagementConfiguration
<a name="aws-resource-ssm-defaulthostmanagementconfiguration"></a>

The `AWS::SSM::DefaultHostManagementConfiguration` resource turns on Default Host Management Configuration for an AWS account and AWS Region. With Default Host Management Configuration, AWS Systems Manager manages your Amazon EC2 instances using an IAM role that you register for the account, without an instance profile on each instance.

Default Host Management Configuration is a single setting for each account and Region, so you can create at most one `AWS::SSM::DefaultHostManagementConfiguration` resource for each account and Region. Creating the resource fails if Default Host Management Configuration is already turned on. Deleting the resource turns off Default Host Management Configuration.

## Syntax
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::SSM::DefaultHostManagementConfiguration",
  "Properties" : {
      "[CustomerManagedRoleArn](#cfn-ssm-defaulthostmanagementconfiguration-customermanagedrolearn)" : {{String}},
      "[PermissionModel](#cfn-ssm-defaulthostmanagementconfiguration-permissionmodel)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-syntax.yaml"></a>

```
Type: AWS::SSM::DefaultHostManagementConfiguration
Properties:
  [CustomerManagedRoleArn](#cfn-ssm-defaulthostmanagementconfiguration-customermanagedrolearn): {{String}}
  [PermissionModel](#cfn-ssm-defaulthostmanagementconfiguration-permissionmodel): {{String}}
```

## Properties
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-properties"></a>

`CustomerManagedRoleArn`  <a name="cfn-ssm-defaulthostmanagementconfiguration-customermanagedrolearn"></a>
The ARN of the IAM role to use for Default Host Management Configuration. The role must trust `ssm.amazonaws.com`.
Required when `PermissionModel` is `SELF_MANAGED`. Don't specify this property when `PermissionModel` is `SERVICE_MANAGED`. If `PermissionModel` is `SELF_MANAGED` and you omit this property, the stack operation fails.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/[\w+=,.@/-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PermissionModel`  <a name="cfn-ssm-defaulthostmanagementconfiguration-permissionmodel"></a>
Specifies whether Systems Manager or you manage the IAM role that Default Host Management Configuration uses.
+ `SERVICE_MANAGED` – Systems Manager creates and manages the IAM role `AWSReservedSSM_DefaultHostManagement_{{region}}` for you.
+ `SELF_MANAGED` – Systems Manager uses the IAM role that you specify in `CustomerManagedRoleArn`.
*Required*: Yes
*Type*: String
*Allowed values*: `SERVICE_MANAGED | SELF_MANAGED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-return-values"></a>

### Ref
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the Default Host Management Configuration service setting, which is always `/ssm/managed-instance/default-ec2-instance-management-role`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-return-values-fn--getatt-fn--getatt"></a>

`LastModifiedDate`  <a name="LastModifiedDate-fn::getatt"></a>
The date and time that the service setting was last modified.

`LastModifiedUser`  <a name="LastModifiedUser-fn::getatt"></a>
The ARN of the principal that last modified the service setting.

`RoleArn`  <a name="RoleArn-fn::getatt"></a>
The ARN of the IAM role that Default Host Management Configuration uses. For `SERVICE_MANAGED`, this is the role that Systems Manager creates, for example: `arn:aws:iam::111122223333:role/aws-reserved/ssm.amazonaws.com/AWSReservedSSM_DefaultHostManagement_us-east-1`. For `SELF_MANAGED`, this is the role that you specify in `CustomerManagedRoleArn`.

`SettingArn`  <a name="SettingArn-fn::getatt"></a>
The ARN of the Default Host Management Configuration service setting. For example: `arn:aws:ssm:us-east-1:111122223333:servicesetting/ssm/managed-instance/default-ec2-instance-management-role`.

`SettingId`  <a name="SettingId-fn::getatt"></a>
The ID of the Default Host Management Configuration service setting: `/ssm/managed-instance/default-ec2-instance-management-role`.

`Status`  <a name="Status-fn::getatt"></a>
The status of the service setting. `Customized` means Default Host Management Configuration is turned on. `Default` means it's turned off.

## Examples
<a name="aws-resource-ssm-defaulthostmanagementconfiguration--examples"></a>

**Topics**
+ [Use a service-managed role for Default Host Management Configuration](#aws-resource-ssm-defaulthostmanagementconfiguration--examples--Use_a_service-managed_role_for_Default_Host_Management_Configuration)
+ [Use your own role for Default Host Management Configuration](#aws-resource-ssm-defaulthostmanagementconfiguration--examples--Use_your_own_role_for_Default_Host_Management_Configuration)

### Use a service-managed role for Default Host Management Configuration
<a name="aws-resource-ssm-defaulthostmanagementconfiguration--examples--Use_a_service-managed_role_for_Default_Host_Management_Configuration"></a>

The following example turns on Default Host Management Configuration and lets Systems Manager create and manage the IAM role.

#### JSON
<a name="aws-resource-ssm-defaulthostmanagementconfiguration--examples--Use_a_service-managed_role_for_Default_Host_Management_Configuration--json"></a>

```
{
    "Type": "AWS::SSM::DefaultHostManagementConfiguration",
    "Properties": {
        "PermissionModel": "SERVICE_MANAGED"
    }
}
```

#### YAML
<a name="aws-resource-ssm-defaulthostmanagementconfiguration--examples--Use_a_service-managed_role_for_Default_Host_Management_Configuration--yaml"></a>

```
Type: AWS::SSM::DefaultHostManagementConfiguration
Properties:
  PermissionModel: SERVICE_MANAGED
```

### Use your own role for Default Host Management Configuration
<a name="aws-resource-ssm-defaulthostmanagementconfiguration--examples--Use_your_own_role_for_Default_Host_Management_Configuration"></a>

The following example turns on Default Host Management Configuration using an IAM role that you manage.

#### JSON
<a name="aws-resource-ssm-defaulthostmanagementconfiguration--examples--Use_your_own_role_for_Default_Host_Management_Configuration--json"></a>

```
{
    "Type": "AWS::SSM::DefaultHostManagementConfiguration",
    "Properties": {
        "PermissionModel": "SELF_MANAGED",
        "CustomerManagedRoleArn": "arn:aws:iam::111122223333:role/MyDefaultHostManagementRole"
    }
}
```

#### YAML
<a name="aws-resource-ssm-defaulthostmanagementconfiguration--examples--Use_your_own_role_for_Default_Host_Management_Configuration--yaml"></a>

```
Type: AWS::SSM::DefaultHostManagementConfiguration
Properties:
  PermissionModel: SELF_MANAGED
  CustomerManagedRoleArn: arn:aws:iam::111122223333:role/MyDefaultHostManagementRole
```
