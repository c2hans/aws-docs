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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
