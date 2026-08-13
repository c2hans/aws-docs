---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-usergroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::UserGroup
<a name="aws-resource-elasticache-usergroup"></a>

For Valkey 7.2 and onwards, or Redis OSS 6.0 and onwards: Creates a user group. For more information, see [Using Role Based Access Control (RBAC)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.RBAC.html)

## Syntax
<a name="aws-resource-elasticache-usergroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticache-usergroup-syntax.json"></a>

```
{
  "Type" : "AWS::ElastiCache::UserGroup",
  "Properties" : {
      "[Engine](#cfn-elasticache-usergroup-engine)" : {{String}},
      "[Tags](#cfn-elasticache-usergroup-tags)" : {{[ Tag, ... ]}},
      "[UserGroupId](#cfn-elasticache-usergroup-usergroupid)" : {{String}},
      "[UserIds](#cfn-elasticache-usergroup-userids)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-elasticache-usergroup-syntax.yaml"></a>

```
Type: AWS::ElastiCache::UserGroup
Properties:
  [Engine](#cfn-elasticache-usergroup-engine): {{String}}
  [Tags](#cfn-elasticache-usergroup-tags): {{
    - Tag}}
  [UserGroupId](#cfn-elasticache-usergroup-usergroupid): {{String}}
  [UserIds](#cfn-elasticache-usergroup-userids): {{
    - String}}
```

## Properties
<a name="aws-resource-elasticache-usergroup-properties"></a>

`Engine`  <a name="cfn-elasticache-usergroup-engine"></a>
The current supported values are valkey and redis.
*Required*: Yes
*Type*: String
*Allowed values*: `redis | valkey`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-elasticache-usergroup-tags"></a>
The list of tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticache-usergroup-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserGroupId`  <a name="cfn-elasticache-usergroup-usergroupid"></a>
The ID of the user group.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z][a-z0-9\\-]*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserIds`  <a name="cfn-elasticache-usergroup-userids"></a>
The list of user IDs that belong to the user group. For Redis OSS, a user named `default` must be included. For Valkey, the list can be empty.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elasticache-usergroup-return-values"></a>

### Ref
<a name="aws-resource-elasticache-usergroup-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticache-usergroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-elasticache-usergroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the user group.

`Status`  <a name="Status-fn::getatt"></a>
Indicates user group status. Can be "creating", "active", "modifying", "deleting".
