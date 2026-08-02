---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-serverlesscache-ecpupersecond.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ServerlessCache ECPUPerSecond
<a name="aws-properties-elasticache-serverlesscache-ecpupersecond"></a>

The configuration for the number of ElastiCache Processing Units (ECPU) the cache can consume per second.

## Syntax
<a name="aws-properties-elasticache-serverlesscache-ecpupersecond-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-serverlesscache-ecpupersecond-syntax.json"></a>

```
{
  "[Maximum](#cfn-elasticache-serverlesscache-ecpupersecond-maximum)" : {{Integer}},
  "[Minimum](#cfn-elasticache-serverlesscache-ecpupersecond-minimum)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-elasticache-serverlesscache-ecpupersecond-syntax.yaml"></a>

```
  [Maximum](#cfn-elasticache-serverlesscache-ecpupersecond-maximum): {{Integer}}
  [Minimum](#cfn-elasticache-serverlesscache-ecpupersecond-minimum): {{Integer}}
```

## Properties
<a name="aws-properties-elasticache-serverlesscache-ecpupersecond-properties"></a>

`Maximum`  <a name="cfn-elasticache-serverlesscache-ecpupersecond-maximum"></a>
The configuration for the maximum number of ECPUs the cache can consume per second.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Minimum`  <a name="cfn-elasticache-serverlesscache-ecpupersecond-minimum"></a>
The configuration for the minimum number of ECPUs the cache should be able consume per second.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
