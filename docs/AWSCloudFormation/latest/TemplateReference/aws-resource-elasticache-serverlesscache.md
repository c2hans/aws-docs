---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-serverlesscache.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ServerlessCache
<a name="aws-resource-elasticache-serverlesscache"></a>

The resource representing a serverless cache.

## Syntax
<a name="aws-resource-elasticache-serverlesscache-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticache-serverlesscache-syntax.json"></a>

```
{
  "Type" : "AWS::ElastiCache::ServerlessCache",
  "Properties" : {
      "[CacheUsageLimits](#cfn-elasticache-serverlesscache-cacheusagelimits)" : {{CacheUsageLimits}},
      "[DailySnapshotTime](#cfn-elasticache-serverlesscache-dailysnapshottime)" : {{String}},
      "[Description](#cfn-elasticache-serverlesscache-description)" : {{String}},
      "[Endpoint](#cfn-elasticache-serverlesscache-endpoint)" : {{Endpoint}},
      "[Engine](#cfn-elasticache-serverlesscache-engine)" : {{String}},
      "[FinalSnapshotName](#cfn-elasticache-serverlesscache-finalsnapshotname)" : {{String}},
      "[KmsKeyId](#cfn-elasticache-serverlesscache-kmskeyid)" : {{String}},
      "[MajorEngineVersion](#cfn-elasticache-serverlesscache-majorengineversion)" : {{String}},
      "[ReaderEndpoint](#cfn-elasticache-serverlesscache-readerendpoint)" : {{Endpoint}},
      "[SecurityGroupIds](#cfn-elasticache-serverlesscache-securitygroupids)" : {{[ String, ... ]}},
      "[ServerlessCacheName](#cfn-elasticache-serverlesscache-serverlesscachename)" : {{String}},
      "[SnapshotArnsToRestore](#cfn-elasticache-serverlesscache-snapshotarnstorestore)" : {{[ String, ... ]}},
      "[SnapshotRetentionLimit](#cfn-elasticache-serverlesscache-snapshotretentionlimit)" : {{Integer}},
      "[SubnetIds](#cfn-elasticache-serverlesscache-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-elasticache-serverlesscache-tags)" : {{[ Tag, ... ]}},
      "[UserGroupId](#cfn-elasticache-serverlesscache-usergroupid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-elasticache-serverlesscache-syntax.yaml"></a>

```
Type: AWS::ElastiCache::ServerlessCache
Properties:
  [CacheUsageLimits](#cfn-elasticache-serverlesscache-cacheusagelimits): {{
    CacheUsageLimits}}
  [DailySnapshotTime](#cfn-elasticache-serverlesscache-dailysnapshottime): {{String}}
  [Description](#cfn-elasticache-serverlesscache-description): {{String}}
  [Endpoint](#cfn-elasticache-serverlesscache-endpoint): {{
    Endpoint}}
  [Engine](#cfn-elasticache-serverlesscache-engine): {{String}}
  [FinalSnapshotName](#cfn-elasticache-serverlesscache-finalsnapshotname): {{String}}
  [KmsKeyId](#cfn-elasticache-serverlesscache-kmskeyid): {{String}}
  [MajorEngineVersion](#cfn-elasticache-serverlesscache-majorengineversion): {{String}}
  [ReaderEndpoint](#cfn-elasticache-serverlesscache-readerendpoint): {{
    Endpoint}}
  [SecurityGroupIds](#cfn-elasticache-serverlesscache-securitygroupids): {{
    - String}}
  [ServerlessCacheName](#cfn-elasticache-serverlesscache-serverlesscachename): {{String}}
  [SnapshotArnsToRestore](#cfn-elasticache-serverlesscache-snapshotarnstorestore): {{
    - String}}
  [SnapshotRetentionLimit](#cfn-elasticache-serverlesscache-snapshotretentionlimit): {{Integer}}
  [SubnetIds](#cfn-elasticache-serverlesscache-subnetids): {{
    - String}}
  [Tags](#cfn-elasticache-serverlesscache-tags): {{
    - Tag}}
  [UserGroupId](#cfn-elasticache-serverlesscache-usergroupid): {{String}}
```

## Properties
<a name="aws-resource-elasticache-serverlesscache-properties"></a>

`CacheUsageLimits`  <a name="cfn-elasticache-serverlesscache-cacheusagelimits"></a>
The cache usage limit for the serverless cache.
*Required*: No
*Type*: [CacheUsageLimits](aws-properties-elasticache-serverlesscache-cacheusagelimits.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DailySnapshotTime`  <a name="cfn-elasticache-serverlesscache-dailysnapshottime"></a>
The daily time that a cache snapshot will be created. Default is NULL, i.e. snapshots will not be created at a specific time on a daily basis. Available for Valkey, Redis OSS and Serverless Memcached only.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-elasticache-serverlesscache-description"></a>
A description of the serverless cache.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-elasticache-serverlesscache-endpoint"></a>
Represents the information required for client programs to connect to a cache node. This value is read-only.
*Required*: No
*Type*: [Endpoint](aws-properties-elasticache-serverlesscache-endpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-elasticache-serverlesscache-engine"></a>
The engine the serverless cache is compatible with.
Allowed values: `valkey` \| `redis` \| `memcached`
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FinalSnapshotName`  <a name="cfn-elasticache-serverlesscache-finalsnapshotname"></a>
The name of the final snapshot taken of a cache before the cache is deleted.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-elasticache-serverlesscache-kmskeyid"></a>
The ID of the AWS Key Management Service (KMS) key that is used to encrypt data at rest in the serverless cache.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MajorEngineVersion`  <a name="cfn-elasticache-serverlesscache-majorengineversion"></a>
The version number of the engine the serverless cache is compatible with. Specify an integer (for example, `7`, `8`, or `9`), not a decimal value (for example, `8.0`).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReaderEndpoint`  <a name="cfn-elasticache-serverlesscache-readerendpoint"></a>
Represents the information required for client programs to connect to a cache node. This value is read-only.
*Required*: No
*Type*: [Endpoint](aws-properties-elasticache-serverlesscache-endpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-elasticache-serverlesscache-securitygroupids"></a>
The IDs of the EC2 security groups associated with the serverless cache.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerlessCacheName`  <a name="cfn-elasticache-serverlesscache-serverlesscachename"></a>
The unique identifier of the serverless cache. Maximum length is 40 characters.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotArnsToRestore`  <a name="cfn-elasticache-serverlesscache-snapshotarnstorestore"></a>
The ARN of the snapshot from which to restore data into the new cache.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotRetentionLimit`  <a name="cfn-elasticache-serverlesscache-snapshotretentionlimit"></a>
The number of days for which ElastiCache retains automatic snapshots before deleting them. Available for Valkey, Redis OSS and Serverless Memcached only. The maximum value allowed is 35 days.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-elasticache-serverlesscache-subnetids"></a>
If no subnet IDs are given and your VPC is in us-west-1, then ElastiCache will select 2 default subnets across AZs in your VPC. For all other Regions, if no subnet IDs are given then ElastiCache will select 3 default subnets across AZs in your default VPC.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-elasticache-serverlesscache-tags"></a>
A list of tags to be added to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticache-serverlesscache-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserGroupId`  <a name="cfn-elasticache-serverlesscache-usergroupid"></a>
The identifier of the user group associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elasticache-serverlesscache-return-values"></a>

### Ref
<a name="aws-resource-elasticache-serverlesscache-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-elasticache-serverlesscache-return-values-fn--getatt"></a>

####
<a name="aws-resource-elasticache-serverlesscache-return-values-fn--getatt-fn--getatt"></a>

`ARN`  <a name="ARN-fn::getatt"></a>
The Amazon Resource Name (ARN) of the serverless cache.

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
When the serverless cache was created.

`Endpoint.Address`  <a name="Endpoint.Address-fn::getatt"></a>
The DNS hostname of the cache node.

`Endpoint.Port`  <a name="Endpoint.Port-fn::getatt"></a>
The port number that the cache engine is listening on.

`FullEngineVersion`  <a name="FullEngineVersion-fn::getatt"></a>
The name and version number of the engine the serverless cache is compatible with.

`ReaderEndpoint.Address`  <a name="ReaderEndpoint.Address-fn::getatt"></a>
The port used by the reader endpoint.

`ReaderEndpoint.Port`  <a name="ReaderEndpoint.Port-fn::getatt"></a>
The port used by the endpoint.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the serverless cache. The allowed values are CREATING, AVAILABLE, DELETING, CREATE-FAILED and MODIFYING.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
