---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-bucketsandregions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens BucketsAndRegions
<a name="aws-properties-s3-storagelens-bucketsandregions"></a>

This resource contains the details of the buckets and Regions for the Amazon S3 Storage Lens configuration.

## Syntax
<a name="aws-properties-s3-storagelens-bucketsandregions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-bucketsandregions-syntax.json"></a>

```
{
  "[Buckets](#cfn-s3-storagelens-bucketsandregions-buckets)" : {{[ String, ... ]}},
  "[Regions](#cfn-s3-storagelens-bucketsandregions-regions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-bucketsandregions-syntax.yaml"></a>

```
  [Buckets](#cfn-s3-storagelens-bucketsandregions-buckets): {{
    - String}}
  [Regions](#cfn-s3-storagelens-bucketsandregions-regions): {{
    - String}}
```

## Properties
<a name="aws-properties-s3-storagelens-bucketsandregions-properties"></a>

`Buckets`  <a name="cfn-s3-storagelens-bucketsandregions-buckets"></a>
This property contains the details of the buckets for the Amazon S3 Storage Lens configuration. This should be the bucket Amazon Resource Name(ARN). For valid values, see [Buckets ARN format here](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Include.html#API_control_Include_Contents) in the *Amazon S3 API Reference*.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regions`  <a name="cfn-s3-storagelens-bucketsandregions-regions"></a>
This property contains the details of the Regions for the S3 Storage Lens configuration.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
