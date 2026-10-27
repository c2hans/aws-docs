---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-domainaccessgrantfororganization-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::DomainAccessGrantForOrganization Tag
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-tag"></a>

A key-value pair associated with a CloudWatch resource.

## Syntax
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cloudwatch-domainaccessgrantfororganization-tag-key)" : {{String}},
  "[Value](#cfn-cloudwatch-domainaccessgrantfororganization-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-tag-syntax.yaml"></a>

```
  [Key](#cfn-cloudwatch-domainaccessgrantfororganization-tag-key): {{String}}
  [Value](#cfn-cloudwatch-domainaccessgrantfororganization-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-tag-properties"></a>

`Key`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-tag-key"></a>
A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-tag-value"></a>
The value for the specified tag key.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
