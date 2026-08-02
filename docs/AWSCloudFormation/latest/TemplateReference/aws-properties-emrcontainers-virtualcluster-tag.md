---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-virtualcluster-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::VirtualCluster Tag
<a name="aws-properties-emrcontainers-virtualcluster-tag"></a>

A map of key-value pairs.

## Syntax
<a name="aws-properties-emrcontainers-virtualcluster-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-virtualcluster-tag-syntax.json"></a>

```
{
  "[Key](#cfn-emrcontainers-virtualcluster-tag-key)" : {{String}},
  "[Value](#cfn-emrcontainers-virtualcluster-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-virtualcluster-tag-syntax.yaml"></a>

```
  [Key](#cfn-emrcontainers-virtualcluster-tag-key): {{String}}
  [Value](#cfn-emrcontainers-virtualcluster-tag-value): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-virtualcluster-tag-properties"></a>

`Key`  <a name="cfn-emrcontainers-virtualcluster-tag-key"></a>
The key to use in the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-emrcontainers-virtualcluster-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
