---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-accountlevel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens AccountLevel
<a name="aws-properties-s3-storagelens-accountlevel"></a>

This resource contains the details of the account-level metrics for Amazon S3 Storage Lens.

## Syntax
<a name="aws-properties-s3-storagelens-accountlevel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-accountlevel-syntax.json"></a>

```
{
  "[ActivityMetrics](#cfn-s3-storagelens-accountlevel-activitymetrics)" : {{ActivityMetrics}},
  "[AdvancedCostOptimizationMetrics](#cfn-s3-storagelens-accountlevel-advancedcostoptimizationmetrics)" : {{AdvancedCostOptimizationMetrics}},
  "[AdvancedDataProtectionMetrics](#cfn-s3-storagelens-accountlevel-advanceddataprotectionmetrics)" : {{AdvancedDataProtectionMetrics}},
  "[AdvancedPerformanceMetrics](#cfn-s3-storagelens-accountlevel-advancedperformancemetrics)" : {{AdvancedPerformanceMetrics}},
  "[BucketLevel](#cfn-s3-storagelens-accountlevel-bucketlevel)" : {{BucketLevel}},
  "[DetailedStatusCodesMetrics](#cfn-s3-storagelens-accountlevel-detailedstatuscodesmetrics)" : {{DetailedStatusCodesMetrics}},
  "[StorageLensGroupLevel](#cfn-s3-storagelens-accountlevel-storagelensgrouplevel)" : {{StorageLensGroupLevel}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-accountlevel-syntax.yaml"></a>

```
  [ActivityMetrics](#cfn-s3-storagelens-accountlevel-activitymetrics): {{
    ActivityMetrics}}
  [AdvancedCostOptimizationMetrics](#cfn-s3-storagelens-accountlevel-advancedcostoptimizationmetrics): {{
    AdvancedCostOptimizationMetrics}}
  [AdvancedDataProtectionMetrics](#cfn-s3-storagelens-accountlevel-advanceddataprotectionmetrics): {{
    AdvancedDataProtectionMetrics}}
  [AdvancedPerformanceMetrics](#cfn-s3-storagelens-accountlevel-advancedperformancemetrics): {{
    AdvancedPerformanceMetrics}}
  [BucketLevel](#cfn-s3-storagelens-accountlevel-bucketlevel): {{
    BucketLevel}}
  [DetailedStatusCodesMetrics](#cfn-s3-storagelens-accountlevel-detailedstatuscodesmetrics): {{
    DetailedStatusCodesMetrics}}
  [StorageLensGroupLevel](#cfn-s3-storagelens-accountlevel-storagelensgrouplevel): {{
    StorageLensGroupLevel}}
```

## Properties
<a name="aws-properties-s3-storagelens-accountlevel-properties"></a>

`ActivityMetrics`  <a name="cfn-s3-storagelens-accountlevel-activitymetrics"></a>
This property contains the details of account-level activity metrics for S3 Storage Lens.
*Required*: No
*Type*: [ActivityMetrics](aws-properties-s3-storagelens-activitymetrics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdvancedCostOptimizationMetrics`  <a name="cfn-s3-storagelens-accountlevel-advancedcostoptimizationmetrics"></a>
This property contains the details of account-level advanced cost optimization metrics for S3 Storage Lens.
*Required*: No
*Type*: [AdvancedCostOptimizationMetrics](aws-properties-s3-storagelens-advancedcostoptimizationmetrics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdvancedDataProtectionMetrics`  <a name="cfn-s3-storagelens-accountlevel-advanceddataprotectionmetrics"></a>
This property contains the details of account-level advanced data protection metrics for S3 Storage Lens.
*Required*: No
*Type*: [AdvancedDataProtectionMetrics](aws-properties-s3-storagelens-advanceddataprotectionmetrics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdvancedPerformanceMetrics`  <a name="cfn-s3-storagelens-accountlevel-advancedperformancemetrics"></a>
This property contains the account-level details for S3 Storage Lens advanced performance metrics.
*Required*: No
*Type*: [AdvancedPerformanceMetrics](aws-properties-s3-storagelens-advancedperformancemetrics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketLevel`  <a name="cfn-s3-storagelens-accountlevel-bucketlevel"></a>
This property contains the details of the account-level bucket-level configurations for Amazon S3 Storage Lens. To enable bucket-level configurations, make sure to also set the same metrics at the account level.
*Required*: Yes
*Type*: [BucketLevel](aws-properties-s3-storagelens-bucketlevel.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetailedStatusCodesMetrics`  <a name="cfn-s3-storagelens-accountlevel-detailedstatuscodesmetrics"></a>
This property contains the details of account-level detailed status code metrics for S3 Storage Lens.
*Required*: No
*Type*: [DetailedStatusCodesMetrics](aws-properties-s3-storagelens-detailedstatuscodesmetrics.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageLensGroupLevel`  <a name="cfn-s3-storagelens-accountlevel-storagelensgrouplevel"></a>
This property determines the scope of Storage Lens group data that is displayed in the Storage Lens dashboard.
*Required*: No
*Type*: [StorageLensGroupLevel](aws-properties-s3-storagelens-storagelensgrouplevel.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
