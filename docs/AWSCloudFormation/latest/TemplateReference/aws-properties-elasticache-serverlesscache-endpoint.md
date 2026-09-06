---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-serverlesscache-endpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ServerlessCache Endpoint
<a name="aws-properties-elasticache-serverlesscache-endpoint"></a>

Represents the information required for client programs to connect to a cache node. This value is read-only.

## Syntax
<a name="aws-properties-elasticache-serverlesscache-endpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-serverlesscache-endpoint-syntax.json"></a>

```
{
  "[Address](#cfn-elasticache-serverlesscache-endpoint-address)" : {{String}},
  "[Port](#cfn-elasticache-serverlesscache-endpoint-port)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-serverlesscache-endpoint-syntax.yaml"></a>

```
  [Address](#cfn-elasticache-serverlesscache-endpoint-address): {{String}}
  [Port](#cfn-elasticache-serverlesscache-endpoint-port): {{String}}
```

## Properties
<a name="aws-properties-elasticache-serverlesscache-endpoint-properties"></a>

`Address`  <a name="cfn-elasticache-serverlesscache-endpoint-address"></a>
The DNS hostname of the cache node.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-elasticache-serverlesscache-endpoint-port"></a>
The port number that the cache engine is listening on.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
