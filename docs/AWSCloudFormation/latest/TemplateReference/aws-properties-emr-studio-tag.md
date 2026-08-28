---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-studio-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Studio Tag
<a name="aws-properties-emr-studio-tag"></a>

A key-value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html).

## Syntax
<a name="aws-properties-emr-studio-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-studio-tag-syntax.json"></a>

```
{
  "[Key](#cfn-emr-studio-tag-key)" : {{String}},
  "[Value](#cfn-emr-studio-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-studio-tag-syntax.yaml"></a>

```
  [Key](#cfn-emr-studio-tag-key): {{String}}
  [Value](#cfn-emr-studio-tag-value): {{String}}
```

## Properties
<a name="aws-properties-emr-studio-tag-properties"></a>

`Key`  <a name="cfn-emr-studio-tag-key"></a>
A user-defined key, which is the minimum required information for a valid tag. For more information, see [Tag](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html).
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-emr-studio-tag-value"></a>
A user-defined value, which is optional in a tag. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html).
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z+-=._:/]+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
