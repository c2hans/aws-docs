---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-s3tablesparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource S3TablesParameters
<a name="aws-properties-quicksight-datasource-s3tablesparameters"></a>

The parameters for S3 Tables.

## Syntax
<a name="aws-properties-quicksight-datasource-s3tablesparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-s3tablesparameters-syntax.json"></a>

```
{
  "[TableBucketArn](#cfn-quicksight-datasource-s3tablesparameters-tablebucketarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-s3tablesparameters-syntax.yaml"></a>

```
  [TableBucketArn](#cfn-quicksight-datasource-s3tablesparameters-tablebucketarn): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-s3tablesparameters-properties"></a>

`TableBucketArn`  <a name="cfn-quicksight-datasource-s3tablesparameters-tablebucketarn"></a>
The Amazon Resource Name (ARN) of the S3 Tables bucket.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-zA-Z0-9-_]{3,63})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
