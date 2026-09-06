---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-parametergroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ParameterGroup
<a name="aws-resource-elasticache-parametergroup"></a>

The `AWS::ElastiCache::ParameterGroup` type creates a new cache parameter group. Cache parameter groups control the parameters for a cache cluster.

## Syntax
<a name="aws-resource-elasticache-parametergroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticache-parametergroup-syntax.json"></a>

```
{
  "Type" : "AWS::ElastiCache::ParameterGroup",
  "Properties" : {
      "[CacheParameterGroupFamily](#cfn-elasticache-parametergroup-cacheparametergroupfamily)" : {{String}},
      "[Description](#cfn-elasticache-parametergroup-description)" : {{String}},
      "[Properties](#cfn-elasticache-parametergroup-properties)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Tags](#cfn-elasticache-parametergroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-elasticache-parametergroup-syntax.yaml"></a>

```
Type: AWS::ElastiCache::ParameterGroup
Properties:
  [CacheParameterGroupFamily](#cfn-elasticache-parametergroup-cacheparametergroupfamily): {{String}}
  [Description](#cfn-elasticache-parametergroup-description): {{String}}
  [Properties](#cfn-elasticache-parametergroup-properties): {{
    {{Key}}: {{Value}}}}
  [Tags](#cfn-elasticache-parametergroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-elasticache-parametergroup-properties"></a>

`CacheParameterGroupFamily`  <a name="cfn-elasticache-parametergroup-cacheparametergroupfamily"></a>
The name of the cache parameter group family that this cache parameter group is compatible with.
Valid values are: `valkey8` \| `valkey7` \| `memcached1.4` \| `memcached1.5` \| `memcached1.6` \| `redis2.6` \| `redis2.8` \| `redis3.2` \| `redis4.0` \| `redis5.0` \| `redis6.x` \| `redis7`
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-elasticache-parametergroup-description"></a>
The description for this cache parameter group.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-elasticache-parametergroup-properties"></a>
A comma-delimited list of parameter name/value pairs.
For example:

```
"Properties" : {
   "cas_disabled" : "1",
   "chunk_size_growth_factor" : "1.02"
}
```
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-elasticache-parametergroup-tags"></a>
A tag that can be added to an ElastiCache parameter group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your parameter groups. A tag with a null Value is permitted.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticache-parametergroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elasticache-parametergroup-return-values"></a>

### Ref
<a name="aws-resource-elasticache-parametergroup-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticache-parametergroup-return-values-fn--getatt"></a>

####
<a name="aws-resource-elasticache-parametergroup-return-values-fn--getatt-fn--getatt"></a>

`CacheParameterGroupName`  <a name="CacheParameterGroupName-fn::getatt"></a>
A user-specified name for the cache parameter group. This value is stored as a lowercase string.

## Examples
<a name="aws-resource-elasticache-parametergroup--examples"></a>

###
<a name="aws-resource-elasticache-parametergroup--examples--"></a>

#### JSON
<a name="aws-resource-elasticache-parametergroup--examples----json"></a>

```
{
    "MyParameterGroup": {
        "Type": "AWS::ElastiCache::ParameterGroup",
        "Properties": {
            "Description": "MyNewParameterGroup",
            "CacheParameterGroupFamily": "memcached1.4",
            "Properties": {
                "cas_disabled": "1",
                "chunk_size_growth_factor": "1.02"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-elasticache-parametergroup--examples----yaml"></a>

```
MyParameterGroup:
  Type: 'AWS::ElastiCache::ParameterGroup'
  Properties:
    Description: MyNewParameterGroup
    CacheParameterGroupFamily: memcached1.4
    Properties:
      cas_disabled: '1'
      chunk_size_growth_factor: '1.02'
```

## See also
<a name="aws-resource-elasticache-parametergroup--seealso"></a>
+ [CreateCacheParameterGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheParameterGroup.html) in the *Amazon ElastiCache API Reference Guide*
+ [ModifyCacheParameterGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheParameterGroup.html) in the *Amazon ElastiCache API Reference Guide*
+  [CloudFormation Stacks Updates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html)
