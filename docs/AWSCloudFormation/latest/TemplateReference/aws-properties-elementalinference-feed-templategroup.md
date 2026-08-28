---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elementalinference-feed-templategroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElementalInference::Feed TemplateGroup
<a name="aws-properties-elementalinference-feed-templategroup"></a>

<a name="aws-properties-elementalinference-feed-templategroup-description"></a>The `TemplateGroup` property type specifies Property description not available. for an [AWS::ElementalInference::Feed](aws-resource-elementalinference-feed.md).

## Syntax
<a name="aws-properties-elementalinference-feed-templategroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elementalinference-feed-templategroup-syntax.json"></a>

```
{
  "[Name](#cfn-elementalinference-feed-templategroup-name)" : {{String}},
  "[TemplateUris](#cfn-elementalinference-feed-templategroup-templateuris)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-elementalinference-feed-templategroup-syntax.yaml"></a>

```
  [Name](#cfn-elementalinference-feed-templategroup-name): {{String}}
  [TemplateUris](#cfn-elementalinference-feed-templategroup-templateuris): {{
    - String}}
```

## Properties
<a name="aws-properties-elementalinference-feed-templategroup-properties"></a>

`Name`  <a name="cfn-elementalinference-feed-templategroup-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateUris`  <a name="cfn-elementalinference-feed-templategroup-templateuris"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `10 | 1`
*Maximum*: `255 | 2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
