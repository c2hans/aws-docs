---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-integrationresourceproperty-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::IntegrationResourceProperty Tag
<a name="aws-properties-glue-integrationresourceproperty-tag"></a>

The `Tag` object represents a label that you can assign to an AWS resource. Each tag consists of a key and an optional value, both of which you define.

## Syntax
<a name="aws-properties-glue-integrationresourceproperty-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-integrationresourceproperty-tag-syntax.json"></a>

```
{
  "[Key](#cfn-glue-integrationresourceproperty-tag-key)" : {{String}},
  "[Value](#cfn-glue-integrationresourceproperty-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-integrationresourceproperty-tag-syntax.yaml"></a>

```
  [Key](#cfn-glue-integrationresourceproperty-tag-key): {{String}}
  [Value](#cfn-glue-integrationresourceproperty-tag-value): {{String}}
```

## Properties
<a name="aws-properties-glue-integrationresourceproperty-tag-properties"></a>

`Key`  <a name="cfn-glue-integrationresourceproperty-tag-key"></a>
The tag key. The key is required when you create a tag on an object. The key is case-sensitive, and must not contain the prefix aws.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-glue-integrationresourceproperty-tag-value"></a>
The tag value. The value is optional when you create a tag on an object. The value is case-sensitive, and must not contain the prefix aws.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
