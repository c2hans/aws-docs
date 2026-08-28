---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-prefixlevel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens PrefixLevel
<a name="aws-properties-s3-storagelens-prefixlevel"></a>

This resource contains the details of the prefix-level of the Amazon S3 Storage Lens.

## Syntax
<a name="aws-properties-s3-storagelens-prefixlevel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-prefixlevel-syntax.json"></a>

```
{
  "[StorageMetrics](#cfn-s3-storagelens-prefixlevel-storagemetrics)" : {{PrefixLevelStorageMetrics}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-prefixlevel-syntax.yaml"></a>

```
  [StorageMetrics](#cfn-s3-storagelens-prefixlevel-storagemetrics): {{
    PrefixLevelStorageMetrics}}
```

## Properties
<a name="aws-properties-s3-storagelens-prefixlevel-properties"></a>

`StorageMetrics`  <a name="cfn-s3-storagelens-prefixlevel-storagemetrics"></a>
A property for the prefix-level storage metrics for Amazon S3 Storage Lens.
*Required*: Yes
*Type*: [PrefixLevelStorageMetrics](aws-properties-s3-storagelens-prefixlevelstoragemetrics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
