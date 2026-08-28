---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filesystem-readcacheconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileSystem ReadCacheConfiguration
<a name="aws-properties-fsx-filesystem-readcacheconfiguration"></a>

 The configuration for the optional provisioned SSD read cache on Amazon FSx for OpenZFS file systems that use the Intelligent-Tiering storage class.

## Syntax
<a name="aws-properties-fsx-filesystem-readcacheconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filesystem-readcacheconfiguration-syntax.json"></a>

```
{
  "[SizeGiB](#cfn-fsx-filesystem-readcacheconfiguration-sizegib)" : {{Integer}},
  "[SizingMode](#cfn-fsx-filesystem-readcacheconfiguration-sizingmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-filesystem-readcacheconfiguration-syntax.yaml"></a>

```
  [SizeGiB](#cfn-fsx-filesystem-readcacheconfiguration-sizegib): {{Integer}}
  [SizingMode](#cfn-fsx-filesystem-readcacheconfiguration-sizingmode): {{String}}
```

## Properties
<a name="aws-properties-fsx-filesystem-readcacheconfiguration-properties"></a>

`SizeGiB`  <a name="cfn-fsx-filesystem-readcacheconfiguration-sizegib"></a>
 Required if `SizingMode` is set to `USER_PROVISIONED`. Specifies the size of the file system's SSD read cache, in gibibytes (GiB).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizingMode`  <a name="cfn-fsx-filesystem-readcacheconfiguration-sizingmode"></a>
 Specifies how the provisioned SSD read cache is sized, as follows:
+ Set to `NO_CACHE` if you do not want to use an SSD read cache with your Intelligent-Tiering file system.
+ Set to `USER_PROVISIONED` to specify the exact size of your SSD read cache.
+ Set to `PROPORTIONAL_TO_THROUGHPUT_CAPACITY` to have your SSD read cache automatically sized based on your throughput capacity.
*Required*: No
*Type*: String
*Allowed values*: `NO_CACHE | USER_PROVISIONED | PROPORTIONAL_TO_THROUGHPUT_CAPACITY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
