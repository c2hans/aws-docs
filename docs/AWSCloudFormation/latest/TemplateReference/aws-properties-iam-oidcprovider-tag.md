---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iam-oidcprovider-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IAM::OIDCProvider Tag
<a name="aws-properties-iam-oidcprovider-tag"></a>

A structure that represents user-provided metadata that can be associated with an IAM resource. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

## Syntax
<a name="aws-properties-iam-oidcprovider-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iam-oidcprovider-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iam-oidcprovider-tag-key)" : {{String}},
  "[Value](#cfn-iam-oidcprovider-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iam-oidcprovider-tag-syntax.yaml"></a>

```
  [Key](#cfn-iam-oidcprovider-tag-key): {{String}}
  [Value](#cfn-iam-oidcprovider-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iam-oidcprovider-tag-properties"></a>

`Key`  <a name="cfn-iam-oidcprovider-tag-key"></a>
The key name that can be used to look up or retrieve the associated value. For example, `Department` or `Cost Center` are common choices.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iam-oidcprovider-tag-value"></a>
The value associated with this tag. For example, tags with a key name of `Department` could have values such as `Human Resources`, `Accounting`, and `Support`. Tags with a key name of `Cost Center` might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
