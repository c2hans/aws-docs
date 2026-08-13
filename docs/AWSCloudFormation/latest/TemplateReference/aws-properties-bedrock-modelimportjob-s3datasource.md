---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-modelimportjob-s3datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ModelImportJob S3DataSource
<a name="aws-properties-bedrock-modelimportjob-s3datasource"></a>

The Amazon S3 data source of the model to import. For the [CreateCustomModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModel.html) API operation, you must specify the Amazon S3 URI for the Amazon-managed Amazon S3 bucket containing your model artifacts. SageMaker AI creates this bucket when you run your first SageMaker AI training job.

## Syntax
<a name="aws-properties-bedrock-modelimportjob-s3datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-modelimportjob-s3datasource-syntax.json"></a>

```
{
  "[S3Uri](#cfn-bedrock-modelimportjob-s3datasource-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-modelimportjob-s3datasource-syntax.yaml"></a>

```
  [S3Uri](#cfn-bedrock-modelimportjob-s3datasource-s3uri): {{String}}
```

## Properties
<a name="aws-properties-bedrock-modelimportjob-s3datasource-properties"></a>

`S3Uri`  <a name="cfn-bedrock-modelimportjob-s3datasource-s3uri"></a>
The URI of the Amazon S3 data source.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://[a-z0-9][-.a-z0-9]{1,61}[a-z0-9](?:/[-!_*'().a-z0-9A-Z]+(?:/[-!_*'().a-z0-9A-Z]+)*)?/?$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
