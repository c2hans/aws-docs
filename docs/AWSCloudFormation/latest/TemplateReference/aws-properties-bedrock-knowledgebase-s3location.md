---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase S3Location
<a name="aws-properties-bedrock-knowledgebase-s3location"></a>

A storage location in an Amazon S3 bucket.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-s3location-syntax.json"></a>

```
{
  "[URI](#cfn-bedrock-knowledgebase-s3location-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-s3location-syntax.yaml"></a>

```
  [URI](#cfn-bedrock-knowledgebase-s3location-uri): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-s3location-properties"></a>

`URI`  <a name="cfn-bedrock-knowledgebase-s3location-uri"></a>
An object URI starting with `s3://`.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://.{1,128}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
