---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-serverlesscache-cacheusagelimits.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ServerlessCache CacheUsageLimits
<a name="aws-properties-elasticache-serverlesscache-cacheusagelimits"></a>

The usage limits for storage and ElastiCache Processing Units for the cache.

## Syntax
<a name="aws-properties-elasticache-serverlesscache-cacheusagelimits-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-serverlesscache-cacheusagelimits-syntax.json"></a>

```
{
  "[DataStorage](#cfn-elasticache-serverlesscache-cacheusagelimits-datastorage)" : {{DataStorage}},
  "[ECPUPerSecond](#cfn-elasticache-serverlesscache-cacheusagelimits-ecpupersecond)" : {{ECPUPerSecond}}
}
```

### YAML
<a name="aws-properties-elasticache-serverlesscache-cacheusagelimits-syntax.yaml"></a>

```
  [DataStorage](#cfn-elasticache-serverlesscache-cacheusagelimits-datastorage): {{
    DataStorage}}
  [ECPUPerSecond](#cfn-elasticache-serverlesscache-cacheusagelimits-ecpupersecond): {{
    ECPUPerSecond}}
```

## Properties
<a name="aws-properties-elasticache-serverlesscache-cacheusagelimits-properties"></a>

`DataStorage`  <a name="cfn-elasticache-serverlesscache-cacheusagelimits-datastorage"></a>
 The maximum data storage limit in the cache, expressed in Gigabytes.
*Required*: No
*Type*: [DataStorage](aws-properties-elasticache-serverlesscache-datastorage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ECPUPerSecond`  <a name="cfn-elasticache-serverlesscache-cacheusagelimits-ecpupersecond"></a>
The number of ElastiCache Processing Units (ECPU) the cache can consume per second.
*Required*: No
*Type*: [ECPUPerSecond](aws-properties-elasticache-serverlesscache-ecpupersecond.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
