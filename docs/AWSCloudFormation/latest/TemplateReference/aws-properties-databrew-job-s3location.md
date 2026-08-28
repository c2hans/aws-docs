---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-job-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Job S3Location
<a name="aws-properties-databrew-job-s3location"></a>

Represents an Amazon S3 location (bucket name, bucket owner, and object key) where DataBrew can read input data, or write output from a job.

## Syntax
<a name="aws-properties-databrew-job-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-job-s3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-databrew-job-s3location-bucket)" : {{String}},
  "[BucketOwner](#cfn-databrew-job-s3location-bucketowner)" : {{String}},
  "[Key](#cfn-databrew-job-s3location-key)" : {{String}}
}
```

### YAML
<a name="aws-properties-databrew-job-s3location-syntax.yaml"></a>

```
  [Bucket](#cfn-databrew-job-s3location-bucket): {{String}}
  [BucketOwner](#cfn-databrew-job-s3location-bucketowner): {{String}}
  [Key](#cfn-databrew-job-s3location-key): {{String}}
```

## Properties
<a name="aws-properties-databrew-job-s3location-properties"></a>

`Bucket`  <a name="cfn-databrew-job-s3location-bucket"></a>
The Amazon S3 bucket name.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketOwner`  <a name="cfn-databrew-job-s3location-bucketowner"></a>
The AWS account ID of the bucket owner.
*Required*: No
*Type*: String
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-databrew-job-s3location-key"></a>
The unique name of the object in the bucket.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1280`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
