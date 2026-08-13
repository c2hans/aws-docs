---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-modelimportjob-modeldatasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ModelImportJob ModelDataSource
<a name="aws-properties-bedrock-modelimportjob-modeldatasource"></a>

The data source of the model to import.

## Syntax
<a name="aws-properties-bedrock-modelimportjob-modeldatasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-modelimportjob-modeldatasource-syntax.json"></a>

```
{
  "[S3DataSource](#cfn-bedrock-modelimportjob-modeldatasource-s3datasource)" : {{S3DataSource}}
}
```

### YAML
<a name="aws-properties-bedrock-modelimportjob-modeldatasource-syntax.yaml"></a>

```
  [S3DataSource](#cfn-bedrock-modelimportjob-modeldatasource-s3datasource): {{
    S3DataSource}}
```

## Properties
<a name="aws-properties-bedrock-modelimportjob-modeldatasource-properties"></a>

`S3DataSource`  <a name="cfn-bedrock-modelimportjob-modeldatasource-s3datasource"></a>
The Amazon S3 data source of the model to import.
*Required*: Yes
*Type*: [S3DataSource](aws-properties-bedrock-modelimportjob-s3datasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
