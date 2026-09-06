---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mwaaserverless-workflow-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MWAAServerless::Workflow S3Location
<a name="aws-properties-mwaaserverless-workflow-s3location"></a>

Specifies the Amazon S3 location of a workflow definition file. This structure contains the bucket name, object key, and optional version ID for the workflow definition. Amazon Managed Workflows for Apache Airflow Serverless takes a snapshot of the definition file at the time of workflow creation or update, ensuring that the workflow behavior remains consistent even if the source file is modified. The definition must be a valid YAML file that uses supported AWS operators and Amazon Managed Workflows for Apache Airflow Serverless syntax.

## Syntax
<a name="aws-properties-mwaaserverless-workflow-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mwaaserverless-workflow-s3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-mwaaserverless-workflow-s3location-bucket)" : {{String}},
  "[ObjectKey](#cfn-mwaaserverless-workflow-s3location-objectkey)" : {{String}},
  "[VersionId](#cfn-mwaaserverless-workflow-s3location-versionid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mwaaserverless-workflow-s3location-syntax.yaml"></a>

```
  [Bucket](#cfn-mwaaserverless-workflow-s3location-bucket): {{String}}
  [ObjectKey](#cfn-mwaaserverless-workflow-s3location-objectkey): {{String}}
  [VersionId](#cfn-mwaaserverless-workflow-s3location-versionid): {{String}}
```

## Properties
<a name="aws-properties-mwaaserverless-workflow-s3location-properties"></a>

`Bucket`  <a name="cfn-mwaaserverless-workflow-s3location-bucket"></a>
The name of the Amazon S3 bucket that contains the workflow definition file.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectKey`  <a name="cfn-mwaaserverless-workflow-s3location-objectkey"></a>
The key (name) of the workflow definition file within the S3 bucket.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionId`  <a name="cfn-mwaaserverless-workflow-s3location-versionid"></a>
Optional. The version ID of the workflow definition file in Amazon S3. If not specified, the latest version is used.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
