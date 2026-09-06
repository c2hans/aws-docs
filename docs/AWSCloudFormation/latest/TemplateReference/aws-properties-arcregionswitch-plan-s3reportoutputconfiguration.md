---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-s3reportoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan S3ReportOutputConfiguration
<a name="aws-properties-arcregionswitch-plan-s3reportoutputconfiguration"></a>

Configuration for delivering generated reports to an Amazon S3 bucket.

## Syntax
<a name="aws-properties-arcregionswitch-plan-s3reportoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-s3reportoutputconfiguration-syntax.json"></a>

```
{
  "[BucketOwner](#cfn-arcregionswitch-plan-s3reportoutputconfiguration-bucketowner)" : {{String}},
  "[BucketPath](#cfn-arcregionswitch-plan-s3reportoutputconfiguration-bucketpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-s3reportoutputconfiguration-syntax.yaml"></a>

```
  [BucketOwner](#cfn-arcregionswitch-plan-s3reportoutputconfiguration-bucketowner): {{String}}
  [BucketPath](#cfn-arcregionswitch-plan-s3reportoutputconfiguration-bucketpath): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-s3reportoutputconfiguration-properties"></a>

`BucketOwner`  <a name="cfn-arcregionswitch-plan-s3reportoutputconfiguration-bucketowner"></a>
The AWS account ID that owns the S3 bucket. Required to ensure the bucket is still owned by the same expected owner at generation time.
*Required*: No
*Type*: String
*Pattern*: `^\d{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketPath`  <a name="cfn-arcregionswitch-plan-s3reportoutputconfiguration-bucketpath"></a>
The S3 bucket name and optional prefix where reports are stored. Format: bucket-name or bucket-name/prefix.
*Required*: No
*Type*: String
*Pattern*: `^(?:s3://)?[a-z0-9][a-z0-9-]{1,61}[a-z0-9](?:/[^/ ][^/]*)*/?$`
*Minimum*: `3`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
