---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-multiregionaccesspoint-region.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::MultiRegionAccessPoint Region
<a name="aws-properties-s3-multiregionaccesspoint-region"></a>

A bucket associated with a specific Region when creating Multi-Region Access Points.

## Syntax
<a name="aws-properties-s3-multiregionaccesspoint-region-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-multiregionaccesspoint-region-syntax.json"></a>

```
{
  "[Bucket](#cfn-s3-multiregionaccesspoint-region-bucket)" : {{String}},
  "[BucketAccountId](#cfn-s3-multiregionaccesspoint-region-bucketaccountid)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-multiregionaccesspoint-region-syntax.yaml"></a>

```
  [Bucket](#cfn-s3-multiregionaccesspoint-region-bucket): {{String}}
  [BucketAccountId](#cfn-s3-multiregionaccesspoint-region-bucketaccountid): {{String}}
```

## Properties
<a name="aws-properties-s3-multiregionaccesspoint-region-properties"></a>

`Bucket`  <a name="cfn-s3-multiregionaccesspoint-region-bucket"></a>
The name of the associated bucket for the Region.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][a-z0-9//.//-]*[a-z0-9]$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BucketAccountId`  <a name="cfn-s3-multiregionaccesspoint-region-bucketaccountid"></a>
The AWS account ID that owns the Amazon S3 bucket that's associated with this Multi-Region Access Point.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
