---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-serverlesscache-datastorage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ServerlessCache DataStorage
<a name="aws-properties-elasticache-serverlesscache-datastorage"></a>

The data storage limit.

## Syntax
<a name="aws-properties-elasticache-serverlesscache-datastorage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-serverlesscache-datastorage-syntax.json"></a>

```
{
  "[Maximum](#cfn-elasticache-serverlesscache-datastorage-maximum)" : {{Integer}},
  "[Minimum](#cfn-elasticache-serverlesscache-datastorage-minimum)" : {{Integer}},
  "[Unit](#cfn-elasticache-serverlesscache-datastorage-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-serverlesscache-datastorage-syntax.yaml"></a>

```
  [Maximum](#cfn-elasticache-serverlesscache-datastorage-maximum): {{Integer}}
  [Minimum](#cfn-elasticache-serverlesscache-datastorage-minimum): {{Integer}}
  [Unit](#cfn-elasticache-serverlesscache-datastorage-unit): {{String}}
```

## Properties
<a name="aws-properties-elasticache-serverlesscache-datastorage-properties"></a>

`Maximum`  <a name="cfn-elasticache-serverlesscache-datastorage-maximum"></a>
The upper limit for data storage the cache is set to use.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Minimum`  <a name="cfn-elasticache-serverlesscache-datastorage-minimum"></a>
The lower limit for data storage the cache is set to use.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-elasticache-serverlesscache-datastorage-unit"></a>
The unit that the storage is measured in, in GB.
*Required*: Yes
*Type*: String
*Allowed values*: `GB`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
