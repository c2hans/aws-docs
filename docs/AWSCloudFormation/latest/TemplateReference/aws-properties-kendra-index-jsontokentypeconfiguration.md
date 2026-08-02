---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-index-jsontokentypeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::Index JsonTokenTypeConfiguration
<a name="aws-properties-kendra-index-jsontokentypeconfiguration"></a>

Provides the configuration information for the JSON token type.

## Syntax
<a name="aws-properties-kendra-index-jsontokentypeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-index-jsontokentypeconfiguration-syntax.json"></a>

```
{
  "[GroupAttributeField](#cfn-kendra-index-jsontokentypeconfiguration-groupattributefield)" : {{String}},
  "[UserNameAttributeField](#cfn-kendra-index-jsontokentypeconfiguration-usernameattributefield)" : {{String}}
}
```

### YAML
<a name="aws-properties-kendra-index-jsontokentypeconfiguration-syntax.yaml"></a>

```
  [GroupAttributeField](#cfn-kendra-index-jsontokentypeconfiguration-groupattributefield): {{String}}
  [UserNameAttributeField](#cfn-kendra-index-jsontokentypeconfiguration-usernameattributefield): {{String}}
```

## Properties
<a name="aws-properties-kendra-index-jsontokentypeconfiguration-properties"></a>

`GroupAttributeField`  <a name="cfn-kendra-index-jsontokentypeconfiguration-groupattributefield"></a>
The group attribute field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserNameAttributeField`  <a name="cfn-kendra-index-jsontokentypeconfiguration-usernameattributefield"></a>
The user name attribute field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
