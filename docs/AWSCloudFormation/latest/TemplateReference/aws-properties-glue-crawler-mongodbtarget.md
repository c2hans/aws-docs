---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-crawler-mongodbtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Crawler MongoDBTarget
<a name="aws-properties-glue-crawler-mongodbtarget"></a>

Specifies an Amazon DocumentDB or MongoDB data store to crawl.

## Syntax
<a name="aws-properties-glue-crawler-mongodbtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-crawler-mongodbtarget-syntax.json"></a>

```
{
  "[ConnectionName](#cfn-glue-crawler-mongodbtarget-connectionname)" : {{String}},
  "[Path](#cfn-glue-crawler-mongodbtarget-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-crawler-mongodbtarget-syntax.yaml"></a>

```
  [ConnectionName](#cfn-glue-crawler-mongodbtarget-connectionname): {{String}}
  [Path](#cfn-glue-crawler-mongodbtarget-path): {{String}}
```

## Properties
<a name="aws-properties-glue-crawler-mongodbtarget-properties"></a>

`ConnectionName`  <a name="cfn-glue-crawler-mongodbtarget-connectionname"></a>
The name of the connection to use to connect to the Amazon DocumentDB or MongoDB target.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-glue-crawler-mongodbtarget-path"></a>
The path of the Amazon DocumentDB or MongoDB target (database/collection).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
