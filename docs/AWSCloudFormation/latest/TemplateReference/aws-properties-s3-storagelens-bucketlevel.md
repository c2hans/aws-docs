---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-bucketlevel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens BucketLevel
<a name="aws-properties-s3-storagelens-bucketlevel"></a>

A property for the bucket-level storage metrics for Amazon S3 Storage Lens.

## Syntax
<a name="aws-properties-s3-storagelens-bucketlevel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-bucketlevel-syntax.json"></a>

```
{
  "[ActivityMetrics](#cfn-s3-storagelens-bucketlevel-activitymetrics)" : {{ActivityMetrics}},
  "[AdvancedCostOptimizationMetrics](#cfn-s3-storagelens-bucketlevel-advancedcostoptimizationmetrics)" : {{AdvancedCostOptimizationMetrics}},
  "[AdvancedDataProtectionMetrics](#cfn-s3-storagelens-bucketlevel-advanceddataprotectionmetrics)" : {{AdvancedDataProtectionMetrics}},
  "[AdvancedPerformanceMetrics](#cfn-s3-storagelens-bucketlevel-advancedperformancemetrics)" : {{AdvancedPerformanceMetrics}},
  "[DetailedStatusCodesMetrics](#cfn-s3-storagelens-bucketlevel-detailedstatuscodesmetrics)" : {{DetailedStatusCodesMetrics}},
  "[PrefixLevel](#cfn-s3-storagelens-bucketlevel-prefixlevel)" : {{PrefixLevel}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-bucketlevel-syntax.yaml"></a>

```
  [ActivityMetrics](#cfn-s3-storagelens-bucketlevel-activitymetrics): {{
    ActivityMetrics}}
  [AdvancedCostOptimizationMetrics](#cfn-s3-storagelens-bucketlevel-advancedcostoptimizationmetrics): {{
    AdvancedCostOptimizationMetrics}}
  [AdvancedDataProtectionMetrics](#cfn-s3-storagelens-bucketlevel-advanceddataprotectionmetrics): {{
    AdvancedDataProtectionMetrics}}
  [AdvancedPerformanceMetrics](#cfn-s3-storagelens-bucketlevel-advancedperformancemetrics): {{
    AdvancedPerformanceMetrics}}
  [DetailedStatusCodesMetrics](#cfn-s3-storagelens-bucketlevel-detailedstatuscodesmetrics): {{
    DetailedStatusCodesMetrics}}
  [PrefixLevel](#cfn-s3-storagelens-bucketlevel-prefixlevel): {{
    PrefixLevel}}
```

## Properties
<a name="aws-properties-s3-storagelens-bucketlevel-properties"></a>

`ActivityMetrics`  <a name="cfn-s3-storagelens-bucketlevel-activitymetrics"></a>
A property for bucket-level activity metrics for S3 Storage Lens.
*Required*: No
*Type*: [ActivityMetrics](aws-properties-s3-storagelens-activitymetrics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdvancedCostOptimizationMetrics`  <a name="cfn-s3-storagelens-bucketlevel-advancedcostoptimizationmetrics"></a>
A property for bucket-level advanced cost optimization metrics for S3 Storage Lens.
*Required*: No
*Type*: [AdvancedCostOptimizationMetrics](aws-properties-s3-storagelens-advancedcostoptimizationmetrics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdvancedDataProtectionMetrics`  <a name="cfn-s3-storagelens-bucketlevel-advanceddataprotectionmetrics"></a>
A property for bucket-level advanced data protection metrics for S3 Storage Lens.
*Required*: No
*Type*: [AdvancedDataProtectionMetrics](aws-properties-s3-storagelens-advanceddataprotectionmetrics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdvancedPerformanceMetrics`  <a name="cfn-s3-storagelens-bucketlevel-advancedperformancemetrics"></a>
A property for bucket-level advanced performance metrics for S3 Storage Lens.
*Required*: No
*Type*: [AdvancedPerformanceMetrics](aws-properties-s3-storagelens-advancedperformancemetrics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetailedStatusCodesMetrics`  <a name="cfn-s3-storagelens-bucketlevel-detailedstatuscodesmetrics"></a>
A property for bucket-level detailed status code metrics for S3 Storage Lens.
*Required*: No
*Type*: [DetailedStatusCodesMetrics](aws-properties-s3-storagelens-detailedstatuscodesmetrics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrefixLevel`  <a name="cfn-s3-storagelens-bucketlevel-prefixlevel"></a>
A property for bucket-level prefix-level storage metrics for S3 Storage Lens.
*Required*: No
*Type*: [PrefixLevel](aws-properties-s3-storagelens-prefixlevel.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
