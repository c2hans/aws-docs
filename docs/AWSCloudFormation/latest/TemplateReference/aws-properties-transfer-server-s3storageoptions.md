---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-server-s3storageoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Server S3StorageOptions
<a name="aws-properties-transfer-server-s3storageoptions"></a>

The Amazon S3 storage options that are configured for your server.

## Syntax
<a name="aws-properties-transfer-server-s3storageoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-server-s3storageoptions-syntax.json"></a>

```
{
  "[DirectoryListingOptimization](#cfn-transfer-server-s3storageoptions-directorylistingoptimization)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-server-s3storageoptions-syntax.yaml"></a>

```
  [DirectoryListingOptimization](#cfn-transfer-server-s3storageoptions-directorylistingoptimization): {{String}}
```

## Properties
<a name="aws-properties-transfer-server-s3storageoptions-properties"></a>

`DirectoryListingOptimization`  <a name="cfn-transfer-server-s3storageoptions-directorylistingoptimization"></a>
Specifies whether or not performance for your Amazon S3 directories is optimized.
+ If using the console, this is enabled by default.
+ If using the API or CLI, this is disabled by default.
By default, home directory mappings have a `TYPE` of `DIRECTORY`. If you enable this option, you would then need to explicitly set the `HomeDirectoryMapEntry``Type` to `FILE` if you want a mapping to have a file target.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
