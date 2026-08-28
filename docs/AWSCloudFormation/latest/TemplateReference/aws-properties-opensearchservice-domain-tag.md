---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain Tag
<a name="aws-properties-opensearchservice-domain-tag"></a>

A tag (key-value pair) for an Amazon OpenSearch Service resource.

## Syntax
<a name="aws-properties-opensearchservice-domain-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-tag-syntax.json"></a>

```
{
  "[Key](#cfn-opensearchservice-domain-tag-key)" : {{String}},
  "[Value](#cfn-opensearchservice-domain-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-tag-syntax.yaml"></a>

```
  [Key](#cfn-opensearchservice-domain-tag-key): {{String}}
  [Value](#cfn-opensearchservice-domain-tag-value): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-tag-properties"></a>

`Key`  <a name="cfn-opensearchservice-domain-tag-key"></a>
The tag key. Tag keys must be unique for the domain to which they are attached.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-opensearchservice-domain-tag-value"></a>
The value assigned to the corresponding tag key. Tag values can be null and don't have to be unique in a tag set. For example, you can have a key value pair in a tag set of `project : Trinity` and `cost-center : Trinity`
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
