---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-ulimit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition Ulimit
<a name="aws-properties-batch-jobdefinition-ulimit"></a>

The `ulimit` settings to pass to the container. For more information, see [Ulimit](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html).

**Note**
This object isn't applicable to jobs that are running on Fargate resources.

## Syntax
<a name="aws-properties-batch-jobdefinition-ulimit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-ulimit-syntax.json"></a>

```
{
  "[HardLimit](#cfn-batch-jobdefinition-ulimit-hardlimit)" : {{Integer}},
  "[Name](#cfn-batch-jobdefinition-ulimit-name)" : {{String}},
  "[SoftLimit](#cfn-batch-jobdefinition-ulimit-softlimit)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-ulimit-syntax.yaml"></a>

```
  [HardLimit](#cfn-batch-jobdefinition-ulimit-hardlimit): {{Integer}}
  [Name](#cfn-batch-jobdefinition-ulimit-name): {{String}}
  [SoftLimit](#cfn-batch-jobdefinition-ulimit-softlimit): {{Integer}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-ulimit-properties"></a>

`HardLimit`  <a name="cfn-batch-jobdefinition-ulimit-hardlimit"></a>
The hard limit for the `ulimit` type.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-batch-jobdefinition-ulimit-name"></a>
The `type` of the `ulimit`. Valid values are: `core` \| `cpu` \| `data` \| `fsize` \| `locks` \| `memlock` \| `msgqueue` \| `nice` \| `nofile` \| `nproc` \| `rss` \| `rtprio` \| `rttime` \| `sigpending` \| `stack`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SoftLimit`  <a name="cfn-batch-jobdefinition-ulimit-softlimit"></a>
The soft limit for the `ulimit` type.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
