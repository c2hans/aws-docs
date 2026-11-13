---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-defaulthostmanagementconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::DefaultHostManagementConfiguration
<a name="aws-resource-ssm-defaulthostmanagementconfiguration"></a>

<a name="aws-resource-ssm-defaulthostmanagementconfiguration-description"></a>The `AWS::SSM::DefaultHostManagementConfiguration` resource Property description not available. for SSM.

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
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/[\w+=,.@/-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PermissionModel`  <a name="cfn-ssm-defaulthostmanagementconfiguration-permissionmodel"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `SERVICE_MANAGED | SELF_MANAGED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-return-values"></a>

### Ref
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-ssm-defaulthostmanagementconfiguration-return-values-fn--getatt-fn--getatt"></a>

`LastModifiedDate`  <a name="LastModifiedDate-fn::getatt"></a>
Property description not available.

`LastModifiedUser`  <a name="LastModifiedUser-fn::getatt"></a>
Property description not available.

`RoleArn`  <a name="RoleArn-fn::getatt"></a>
Property description not available.

`SettingArn`  <a name="SettingArn-fn::getatt"></a>
Property description not available.

`SettingId`  <a name="SettingId-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.
