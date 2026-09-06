---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-serverlesscachesnapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ServerlessCacheSnapshot
<a name="aws-resource-elasticache-serverlesscachesnapshot"></a>

The resource representing a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.

## Syntax
<a name="aws-resource-elasticache-serverlesscachesnapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticache-serverlesscachesnapshot-syntax.json"></a>

```
{
  "Type" : "AWS::ElastiCache::ServerlessCacheSnapshot",
  "Properties" : {
      "[KmsKeyId](#cfn-elasticache-serverlesscachesnapshot-kmskeyid)" : {{String}},
      "[ServerlessCacheName](#cfn-elasticache-serverlesscachesnapshot-serverlesscachename)" : {{String}},
      "[ServerlessCacheSnapshotName](#cfn-elasticache-serverlesscachesnapshot-serverlesscachesnapshotname)" : {{String}},
      "[Tags](#cfn-elasticache-serverlesscachesnapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-elasticache-serverlesscachesnapshot-syntax.yaml"></a>

```
Type: AWS::ElastiCache::ServerlessCacheSnapshot
Properties:
  [KmsKeyId](#cfn-elasticache-serverlesscachesnapshot-kmskeyid): {{String}}
  [ServerlessCacheName](#cfn-elasticache-serverlesscachesnapshot-serverlesscachename): {{String}}
  [ServerlessCacheSnapshotName](#cfn-elasticache-serverlesscachesnapshot-serverlesscachesnapshotname): {{String}}
  [Tags](#cfn-elasticache-serverlesscachesnapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-elasticache-serverlesscachesnapshot-properties"></a>

`KmsKeyId`  <a name="cfn-elasticache-serverlesscachesnapshot-kmskeyid"></a>
The ID of the AWS Key Management Service (KMS) key of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerlessCacheName`  <a name="cfn-elasticache-serverlesscachesnapshot-serverlesscachename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerlessCacheSnapshotName`  <a name="cfn-elasticache-serverlesscachesnapshot-serverlesscachesnapshotname"></a>
The identifier of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-elasticache-serverlesscachesnapshot-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticache-serverlesscachesnapshot-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elasticache-serverlesscachesnapshot-return-values"></a>

### Ref
<a name="aws-resource-elasticache-serverlesscachesnapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-elasticache-serverlesscachesnapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-elasticache-serverlesscachesnapshot-return-values-fn--getatt-fn--getatt"></a>

`ARN`  <a name="ARN-fn::getatt"></a>
The Amazon Resource Name (ARN) of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.

`BytesUsedForCache`  <a name="BytesUsedForCache-fn::getatt"></a>
The total size of a serverless cache snapshot, in bytes. Available for Valkey, Redis OSS and Serverless Memcached only.

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
The date and time that the source serverless cache's metadata and cache data set was obtained for the snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.

`SnapshotType`  <a name="SnapshotType-fn::getatt"></a>
The type of snapshot of serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.
