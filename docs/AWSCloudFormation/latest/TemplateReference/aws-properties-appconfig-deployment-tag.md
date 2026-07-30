---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-deployment-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::Deployment Tag
<a name="aws-properties-appconfig-deployment-tag"></a>

Metadata to assign to the deployment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

## Syntax
<a name="aws-properties-appconfig-deployment-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appconfig-deployment-tag-syntax.json"></a>

```
{
  "[Key](#cfn-appconfig-deployment-tag-key)" : {{String}},
  "[Value](#cfn-appconfig-deployment-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appconfig-deployment-tag-syntax.yaml"></a>

```
  [Key](#cfn-appconfig-deployment-tag-key): {{String}}
  [Value](#cfn-appconfig-deployment-tag-value): {{String}}
```

## Properties
<a name="aws-properties-appconfig-deployment-tag-properties"></a>

`Key`  <a name="cfn-appconfig-deployment-tag-key"></a>
The tag key.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-appconfig-deployment-tag-value"></a>
An optional tag value.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
