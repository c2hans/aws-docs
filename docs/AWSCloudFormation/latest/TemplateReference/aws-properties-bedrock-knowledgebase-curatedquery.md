---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-curatedquery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase CuratedQuery
<a name="aws-properties-bedrock-knowledgebase-curatedquery"></a>

Contains configurations for a query, each of which defines information about example queries to help the query engine generate appropriate SQL queries.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-curatedquery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-curatedquery-syntax.json"></a>

```
{
  "[NaturalLanguage](#cfn-bedrock-knowledgebase-curatedquery-naturallanguage)" : {{String}},
  "[Sql](#cfn-bedrock-knowledgebase-curatedquery-sql)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-curatedquery-syntax.yaml"></a>

```
  [NaturalLanguage](#cfn-bedrock-knowledgebase-curatedquery-naturallanguage): {{String}}
  [Sql](#cfn-bedrock-knowledgebase-curatedquery-sql): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-curatedquery-properties"></a>

`NaturalLanguage`  <a name="cfn-bedrock-knowledgebase-curatedquery-naturallanguage"></a>
An example natural language query.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sql`  <a name="cfn-bedrock-knowledgebase-curatedquery-sql"></a>
The SQL equivalent of the natural language query.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
