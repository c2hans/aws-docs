---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-s3reportoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service S3ReportOutputConfiguration
<a name="aws-properties-resiliencehubv2-service-s3reportoutputconfiguration"></a>

S3 configuration for report output.

## Syntax
<a name="aws-properties-resiliencehubv2-service-s3reportoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-s3reportoutputconfiguration-syntax.json"></a>

```
{
  "[BucketOwner](#cfn-resiliencehubv2-service-s3reportoutputconfiguration-bucketowner)" : {{String}},
  "[BucketPath](#cfn-resiliencehubv2-service-s3reportoutputconfiguration-bucketpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-s3reportoutputconfiguration-syntax.yaml"></a>

```
  [BucketOwner](#cfn-resiliencehubv2-service-s3reportoutputconfiguration-bucketowner): {{String}}
  [BucketPath](#cfn-resiliencehubv2-service-s3reportoutputconfiguration-bucketpath): {{String}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-s3reportoutputconfiguration-properties"></a>

`BucketOwner`  <a name="cfn-resiliencehubv2-service-s3reportoutputconfiguration-bucketowner"></a>
Account ID of the bucket owner for cross-account access verification.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketPath`  <a name="cfn-resiliencehubv2-service-s3reportoutputconfiguration-bucketpath"></a>
S3 bucket path where reports will be written (e.g., my-bucket/ngrh-reports/).
*Required*: Yes
*Type*: String
*Pattern*: `^(s3://)?[a-z0-9][a-z0-9.-]{1,61}[a-z0-9](/.*)?$`
*Minimum*: `3`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
