---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::DocumentClassifier DocumentClassifierOutputDataConfig
<a name="aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig"></a>

Provide the location for output data from a custom classifier job. This field is mandatory if you are training a native document model.

## Syntax
<a name="aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-comprehend-documentclassifier-documentclassifieroutputdataconfig-kmskeyid)" : {{String}},
  "[S3Uri](#cfn-comprehend-documentclassifier-documentclassifieroutputdataconfig-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-comprehend-documentclassifier-documentclassifieroutputdataconfig-kmskeyid): {{String}}
  [S3Uri](#cfn-comprehend-documentclassifier-documentclassifieroutputdataconfig-s3uri): {{String}}
```

## Properties
<a name="aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig-properties"></a>

`KmsKeyId`  <a name="cfn-comprehend-documentclassifier-documentclassifieroutputdataconfig-kmskeyid"></a>
ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job. The KmsKeyId can be one of the following formats:
+ KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
+ KMS Key Alias: `"alias/ExampleAlias"`
+ ARN of a KMS Key Alias: `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-comprehend-documentclassifier-documentclassifieroutputdataconfig-s3uri"></a>
When you use the `OutputDataConfig` object while creating a custom classifier, you specify the Amazon S3 location where you want to write the confusion matrix and other output files. The URI must be in the same Region as the API endpoint that you are calling. The location is used as the prefix for the actual location of this output file.
When the custom classifier job is finished, the service creates the output file in a directory specific to the job. The `S3Uri` field contains the location of the output file, called `output.tar.gz`. It is a compressed archive that contains the confusion matrix.
*Required*: No
*Type*: String
*Pattern*: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
