---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ServerlessCacheSnapshot ServerlessCacheConfiguration
<a name="aws-properties-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration"></a>

The configuration settings for a specific serverless cache.

## Syntax
<a name="aws-properties-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-syntax.json"></a>

```
{
  "[Engine](#cfn-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-engine)" : {{String}},
  "[MajorEngineVersion](#cfn-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-majorengineversion)" : {{String}},
  "[ServerlessCacheName](#cfn-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-serverlesscachename)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-syntax.yaml"></a>

```
  [Engine](#cfn-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-engine): {{String}}
  [MajorEngineVersion](#cfn-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-majorengineversion): {{String}}
  [ServerlessCacheName](#cfn-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-serverlesscachename): {{String}}
```

## Properties
<a name="aws-properties-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-properties"></a>

`Engine`  <a name="cfn-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-engine"></a>
The engine that the serverless cache is configured with.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MajorEngineVersion`  <a name="cfn-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-majorengineversion"></a>
The engine version number that the serverless cache is configured with.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerlessCacheName`  <a name="cfn-elasticache-serverlesscachesnapshot-serverlesscacheconfiguration-serverlesscachename"></a>
The identifier of a serverless cache.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
