---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-crawler-icebergtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Crawler IcebergTarget
<a name="aws-properties-glue-crawler-icebergtarget"></a>

Specifies Apache Iceberg data store targets.

## Syntax
<a name="aws-properties-glue-crawler-icebergtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-crawler-icebergtarget-syntax.json"></a>

```
{
  "[ConnectionName](#cfn-glue-crawler-icebergtarget-connectionname)" : {{String}},
  "[Exclusions](#cfn-glue-crawler-icebergtarget-exclusions)" : {{[ String, ... ]}},
  "[MaximumTraversalDepth](#cfn-glue-crawler-icebergtarget-maximumtraversaldepth)" : {{Integer}},
  "[Paths](#cfn-glue-crawler-icebergtarget-paths)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-crawler-icebergtarget-syntax.yaml"></a>

```
  [ConnectionName](#cfn-glue-crawler-icebergtarget-connectionname): {{String}}
  [Exclusions](#cfn-glue-crawler-icebergtarget-exclusions): {{
    - String}}
  [MaximumTraversalDepth](#cfn-glue-crawler-icebergtarget-maximumtraversaldepth): {{Integer}}
  [Paths](#cfn-glue-crawler-icebergtarget-paths): {{
    - String}}
```

## Properties
<a name="aws-properties-glue-crawler-icebergtarget-properties"></a>

`ConnectionName`  <a name="cfn-glue-crawler-icebergtarget-connectionname"></a>
The name of the connection to use to connect to the Iceberg target.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Exclusions`  <a name="cfn-glue-crawler-icebergtarget-exclusions"></a>
A list of global patterns used to exclude from the crawl.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumTraversalDepth`  <a name="cfn-glue-crawler-icebergtarget-maximumtraversaldepth"></a>
The maximum depth of Amazon S3 paths that the crawler can traverse to discover the Iceberg metadata folder in your Amazon S3 path. Used to limit the crawler run time.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Paths`  <a name="cfn-glue-crawler-icebergtarget-paths"></a>
One or more Amazon S3 paths that contains Iceberg metadata folders as s3://bucket/prefix .
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
