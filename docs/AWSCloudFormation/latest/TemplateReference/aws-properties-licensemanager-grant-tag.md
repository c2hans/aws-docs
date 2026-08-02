---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-grant-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::Grant Tag
<a name="aws-properties-licensemanager-grant-tag"></a>

Details about the tags for a resource. For more information about tagging support in License Manager, see the [TagResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html) operation.

## Syntax
<a name="aws-properties-licensemanager-grant-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-grant-tag-syntax.json"></a>

```
{
  "[Key](#cfn-licensemanager-grant-tag-key)" : {{String}},
  "[Value](#cfn-licensemanager-grant-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-licensemanager-grant-tag-syntax.yaml"></a>

```
  [Key](#cfn-licensemanager-grant-tag-key): {{String}}
  [Value](#cfn-licensemanager-grant-tag-value): {{String}}
```

## Properties
<a name="aws-properties-licensemanager-grant-tag-properties"></a>

`Key`  <a name="cfn-licensemanager-grant-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-licensemanager-grant-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
