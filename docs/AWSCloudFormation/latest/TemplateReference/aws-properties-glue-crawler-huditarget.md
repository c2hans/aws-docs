---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-crawler-huditarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Crawler HudiTarget
<a name="aws-properties-glue-crawler-huditarget"></a>

Specifies an Apache Hudi data source.

## Syntax
<a name="aws-properties-glue-crawler-huditarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-crawler-huditarget-syntax.json"></a>

```
{
  "[ConnectionName](#cfn-glue-crawler-huditarget-connectionname)" : {{String}},
  "[Exclusions](#cfn-glue-crawler-huditarget-exclusions)" : {{[ String, ... ]}},
  "[MaximumTraversalDepth](#cfn-glue-crawler-huditarget-maximumtraversaldepth)" : {{Integer}},
  "[Paths](#cfn-glue-crawler-huditarget-paths)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-crawler-huditarget-syntax.yaml"></a>

```
  [ConnectionName](#cfn-glue-crawler-huditarget-connectionname): {{String}}
  [Exclusions](#cfn-glue-crawler-huditarget-exclusions): {{
    - String}}
  [MaximumTraversalDepth](#cfn-glue-crawler-huditarget-maximumtraversaldepth): {{Integer}}
  [Paths](#cfn-glue-crawler-huditarget-paths): {{
    - String}}
```

## Properties
<a name="aws-properties-glue-crawler-huditarget-properties"></a>

`ConnectionName`  <a name="cfn-glue-crawler-huditarget-connectionname"></a>
The name of the connection to use to connect to the Hudi target. If your Hudi files are stored in buckets that require VPC authorization, you can set their connection properties here.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Exclusions`  <a name="cfn-glue-crawler-huditarget-exclusions"></a>
A list of glob patterns used to exclude from the crawl. For more information, see [Catalog Tables with a Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumTraversalDepth`  <a name="cfn-glue-crawler-huditarget-maximumtraversaldepth"></a>
The maximum depth of Amazon S3 paths that the crawler can traverse to discover the Hudi metadata folder in your Amazon S3 path. Used to limit the crawler run time.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Paths`  <a name="cfn-glue-crawler-huditarget-paths"></a>
An array of Amazon S3 location strings for Hudi, each indicating the root folder with which the metadata files for a Hudi table resides. The Hudi folder may be located in a child folder of the root folder.
The crawler will scan all folders underneath a path for a Hudi folder.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
