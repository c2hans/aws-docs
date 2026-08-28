---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-association-s3outputlocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::Association S3OutputLocation
<a name="aws-properties-ssm-association-s3outputlocation"></a>

`S3OutputLocation` is a property of the [AWS::SSM::Association](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html) resource that specifies an Amazon S3 bucket where you want to store the results of this association request.

## Syntax
<a name="aws-properties-ssm-association-s3outputlocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-association-s3outputlocation-syntax.json"></a>

```
{
  "[OutputS3BucketName](#cfn-ssm-association-s3outputlocation-outputs3bucketname)" : {{String}},
  "[OutputS3KeyPrefix](#cfn-ssm-association-s3outputlocation-outputs3keyprefix)" : {{String}},
  "[OutputS3Region](#cfn-ssm-association-s3outputlocation-outputs3region)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssm-association-s3outputlocation-syntax.yaml"></a>

```
  [OutputS3BucketName](#cfn-ssm-association-s3outputlocation-outputs3bucketname): {{String}}
  [OutputS3KeyPrefix](#cfn-ssm-association-s3outputlocation-outputs3keyprefix): {{String}}
  [OutputS3Region](#cfn-ssm-association-s3outputlocation-outputs3region): {{String}}
```

## Properties
<a name="aws-properties-ssm-association-s3outputlocation-properties"></a>

`OutputS3BucketName`  <a name="cfn-ssm-association-s3outputlocation-outputs3bucketname"></a>
The name of the S3 bucket.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputS3KeyPrefix`  <a name="cfn-ssm-association-s3outputlocation-outputs3keyprefix"></a>
The S3 bucket subfolder.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputS3Region`  <a name="cfn-ssm-association-s3outputlocation-outputs3region"></a>
The AWS Region of the S3 bucket.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
