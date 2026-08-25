---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-permissionmodel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service PermissionModel
<a name="aws-properties-resiliencehubv2-service-permissionmodel"></a>

Defines the permission model for a service.

## Syntax
<a name="aws-properties-resiliencehubv2-service-permissionmodel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-permissionmodel-syntax.json"></a>

```
{
  "[CrossAccountRoleArns](#cfn-resiliencehubv2-service-permissionmodel-crossaccountrolearns)" : {{[ CrossAccountRoleConfiguration, ... ]}},
  "[InvokerRoleName](#cfn-resiliencehubv2-service-permissionmodel-invokerrolename)" : {{String}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-permissionmodel-syntax.yaml"></a>

```
  [CrossAccountRoleArns](#cfn-resiliencehubv2-service-permissionmodel-crossaccountrolearns): {{
    - CrossAccountRoleConfiguration}}
  [InvokerRoleName](#cfn-resiliencehubv2-service-permissionmodel-invokerrolename): {{String}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-permissionmodel-properties"></a>

`CrossAccountRoleArns`  <a name="cfn-resiliencehubv2-service-permissionmodel-crossaccountrolearns"></a>
Property description not available.
*Required*: No
*Type*: Array of [CrossAccountRoleConfiguration](aws-properties-resiliencehubv2-service-crossaccountroleconfiguration.md)
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvokerRoleName`  <a name="cfn-resiliencehubv2-service-permissionmodel-invokerrolename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(([A-Za-z0-9_+=,.@\-]+/){1,511})?[A-Za-z0-9_+=,.@\-]{1,64}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
