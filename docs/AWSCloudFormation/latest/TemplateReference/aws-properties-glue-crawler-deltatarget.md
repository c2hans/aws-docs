---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-crawler-deltatarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Crawler DeltaTarget
<a name="aws-properties-glue-crawler-deltatarget"></a>

Specifies a Delta data store to crawl one or more Delta tables.

## Syntax
<a name="aws-properties-glue-crawler-deltatarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-crawler-deltatarget-syntax.json"></a>

```
{
  "[ConnectionName](#cfn-glue-crawler-deltatarget-connectionname)" : {{String}},
  "[CreateNativeDeltaTable](#cfn-glue-crawler-deltatarget-createnativedeltatable)" : {{Boolean}},
  "[DeltaTables](#cfn-glue-crawler-deltatarget-deltatables)" : {{[ String, ... ]}},
  "[WriteManifest](#cfn-glue-crawler-deltatarget-writemanifest)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-glue-crawler-deltatarget-syntax.yaml"></a>

```
  [ConnectionName](#cfn-glue-crawler-deltatarget-connectionname): {{String}}
  [CreateNativeDeltaTable](#cfn-glue-crawler-deltatarget-createnativedeltatable): {{Boolean}}
  [DeltaTables](#cfn-glue-crawler-deltatarget-deltatables): {{
    - String}}
  [WriteManifest](#cfn-glue-crawler-deltatarget-writemanifest): {{Boolean}}
```

## Properties
<a name="aws-properties-glue-crawler-deltatarget-properties"></a>

`ConnectionName`  <a name="cfn-glue-crawler-deltatarget-connectionname"></a>
The name of the connection to use to connect to the Delta table target.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateNativeDeltaTable`  <a name="cfn-glue-crawler-deltatarget-createnativedeltatable"></a>
Specifies whether the crawler will create native tables, to allow integration with query engines that support querying of the Delta transaction log directly.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeltaTables`  <a name="cfn-glue-crawler-deltatarget-deltatables"></a>
A list of the Amazon S3 paths to the Delta tables.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WriteManifest`  <a name="cfn-glue-crawler-deltatarget-writemanifest"></a>
Specifies whether to write the manifest files to the Delta table path.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
