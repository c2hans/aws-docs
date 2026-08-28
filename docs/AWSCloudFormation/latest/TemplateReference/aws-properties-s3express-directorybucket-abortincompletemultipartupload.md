---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-directorybucket-abortincompletemultipartupload.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::DirectoryBucket AbortIncompleteMultipartUpload
<a name="aws-properties-s3express-directorybucket-abortincompletemultipartupload"></a>

Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload. For more information, see [ Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config) in the *Amazon S3 User Guide*.

## Syntax
<a name="aws-properties-s3express-directorybucket-abortincompletemultipartupload-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-directorybucket-abortincompletemultipartupload-syntax.json"></a>

```
{
  "[DaysAfterInitiation](#cfn-s3express-directorybucket-abortincompletemultipartupload-daysafterinitiation)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3express-directorybucket-abortincompletemultipartupload-syntax.yaml"></a>

```
  [DaysAfterInitiation](#cfn-s3express-directorybucket-abortincompletemultipartupload-daysafterinitiation): {{Integer}}
```

## Properties
<a name="aws-properties-s3express-directorybucket-abortincompletemultipartupload-properties"></a>

`DaysAfterInitiation`  <a name="cfn-s3express-directorybucket-abortincompletemultipartupload-daysafterinitiation"></a>
Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
