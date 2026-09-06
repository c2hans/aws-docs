---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-advancedperformancemetrics.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens AdvancedPerformanceMetrics
<a name="aws-properties-s3-storagelens-advancedperformancemetrics"></a>

 A property for S3 Storage Lens advanced performance metrics. Advanced performance metrics provide insights into application performance such as access patterns and network originality metrics.

## Syntax
<a name="aws-properties-s3-storagelens-advancedperformancemetrics-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-advancedperformancemetrics-syntax.json"></a>

```
{
  "[IsEnabled](#cfn-s3-storagelens-advancedperformancemetrics-isenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-advancedperformancemetrics-syntax.yaml"></a>

```
  [IsEnabled](#cfn-s3-storagelens-advancedperformancemetrics-isenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-s3-storagelens-advancedperformancemetrics-properties"></a>

`IsEnabled`  <a name="cfn-s3-storagelens-advancedperformancemetrics-isenabled"></a>
This property indicates whether the advanced performance metrics are enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
