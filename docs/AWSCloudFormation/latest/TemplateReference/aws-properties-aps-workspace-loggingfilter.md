---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-workspace-loggingfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Workspace LoggingFilter
<a name="aws-properties-aps-workspace-loggingfilter"></a>

Filtering criteria that determine which queries are logged.

## Syntax
<a name="aws-properties-aps-workspace-loggingfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-workspace-loggingfilter-syntax.json"></a>

```
{
  "[QspThreshold](#cfn-aps-workspace-loggingfilter-qspthreshold)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-aps-workspace-loggingfilter-syntax.yaml"></a>

```
  [QspThreshold](#cfn-aps-workspace-loggingfilter-qspthreshold): {{Integer}}
```

## Properties
<a name="aws-properties-aps-workspace-loggingfilter-properties"></a>

`QspThreshold`  <a name="cfn-aps-workspace-loggingfilter-qspthreshold"></a>
The Query Samples Processed (QSP) threshold above which queries will be logged. Queries processing more samples than this threshold will be captured in logs.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
