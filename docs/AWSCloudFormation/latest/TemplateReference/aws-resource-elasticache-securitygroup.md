---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-securitygroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::SecurityGroup
<a name="aws-resource-elasticache-securitygroup"></a>

The `AWS::ElastiCache::SecurityGroup` resource creates a cache security group. For more information about cache security groups, go to [CacheSecurityGroups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VPCs.html) in the *Amazon ElastiCache User Guide* or go to [CreateCacheSecurityGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheSecurityGroup.html) in the *Amazon ElastiCache API Reference Guide*.

For more information, see [CreateCacheSubnetGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheSubnetGroup.html).

## Syntax
<a name="aws-resource-elasticache-securitygroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticache-securitygroup-syntax.json"></a>

```
{
  "Type" : "AWS::ElastiCache::SecurityGroup",
  "Properties" : {
      "[Description](#cfn-elasticache-securitygroup-description)" : {{String}},
      "[Tags](#cfn-elasticache-securitygroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-elasticache-securitygroup-syntax.yaml"></a>

```
Type: AWS::ElastiCache::SecurityGroup
Properties:
  [Description](#cfn-elasticache-securitygroup-description): {{String}}
  [Tags](#cfn-elasticache-securitygroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-elasticache-securitygroup-properties"></a>

`Description`  <a name="cfn-elasticache-securitygroup-description"></a>
A description for the cache security group.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-elasticache-securitygroup-tags"></a>
A tag that can be added to an ElastiCache security group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your security groups. A tag with a null Value is permitted.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticache-securitygroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elasticache-securitygroup-return-values"></a>

### Ref
<a name="aws-resource-elasticache-securitygroup-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticache-securitygroup-return-values-fn--getatt"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
