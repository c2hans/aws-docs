---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-collection-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Collection Tag
<a name="aws-properties-opensearchserverless-collection-tag"></a>

A map of key-value pairs associated to an OpenSearch Serverless resource.

## Syntax
<a name="aws-properties-opensearchserverless-collection-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-collection-tag-syntax.json"></a>

```
{
  "[Key](#cfn-opensearchserverless-collection-tag-key)" : {{String}},
  "[Value](#cfn-opensearchserverless-collection-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-collection-tag-syntax.yaml"></a>

```
  [Key](#cfn-opensearchserverless-collection-tag-key): {{String}}
  [Value](#cfn-opensearchserverless-collection-tag-value): {{String}}
```

## Properties
<a name="aws-properties-opensearchserverless-collection-tag-properties"></a>

`Key`  <a name="cfn-opensearchserverless-collection-tag-key"></a>
The key to use in the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-opensearchserverless-collection-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
