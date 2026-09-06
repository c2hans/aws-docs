---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-s3outputformatconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow S3OutputFormatConfig
<a name="aws-properties-appflow-flow-s3outputformatconfig"></a>

 The configuration that determines how Amazon AppFlow should format the flow output data when Amazon S3 is used as the destination.

## Syntax
<a name="aws-properties-appflow-flow-s3outputformatconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-s3outputformatconfig-syntax.json"></a>

```
{
  "[AggregationConfig](#cfn-appflow-flow-s3outputformatconfig-aggregationconfig)" : {{AggregationConfig}},
  "[FileType](#cfn-appflow-flow-s3outputformatconfig-filetype)" : {{String}},
  "[PrefixConfig](#cfn-appflow-flow-s3outputformatconfig-prefixconfig)" : {{PrefixConfig}},
  "[PreserveSourceDataTyping](#cfn-appflow-flow-s3outputformatconfig-preservesourcedatatyping)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-appflow-flow-s3outputformatconfig-syntax.yaml"></a>

```
  [AggregationConfig](#cfn-appflow-flow-s3outputformatconfig-aggregationconfig): {{
    AggregationConfig}}
  [FileType](#cfn-appflow-flow-s3outputformatconfig-filetype): {{String}}
  [PrefixConfig](#cfn-appflow-flow-s3outputformatconfig-prefixconfig): {{
    PrefixConfig}}
  [PreserveSourceDataTyping](#cfn-appflow-flow-s3outputformatconfig-preservesourcedatatyping): {{Boolean}}
```

## Properties
<a name="aws-properties-appflow-flow-s3outputformatconfig-properties"></a>

`AggregationConfig`  <a name="cfn-appflow-flow-s3outputformatconfig-aggregationconfig"></a>
 The aggregation settings that you can use to customize the output format of your flow data.
*Required*: No
*Type*: [AggregationConfig](aws-properties-appflow-flow-aggregationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FileType`  <a name="cfn-appflow-flow-s3outputformatconfig-filetype"></a>
 Indicates the file type that Amazon AppFlow places in the Amazon S3 bucket.
*Required*: No
*Type*: String
*Allowed values*: `CSV | JSON | PARQUET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrefixConfig`  <a name="cfn-appflow-flow-s3outputformatconfig-prefixconfig"></a>
 Determines the prefix that Amazon AppFlow applies to the folder name in the Amazon S3 bucket. You can name folders according to the flow frequency and date.
*Required*: No
*Type*: [PrefixConfig](aws-properties-appflow-flow-prefixconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreserveSourceDataTyping`  <a name="cfn-appflow-flow-s3outputformatconfig-preservesourcedatatyping"></a>
If your file output format is Parquet, use this parameter to set whether Amazon AppFlow preserves the data types in your source data when it writes the output to Amazon S3.
+ `true`: Amazon AppFlow preserves the data types when it writes to Amazon S3. For example, an integer or `1` in your source data is still an integer in your output.
+ `false`: Amazon AppFlow converts all of the source data into strings when it writes to Amazon S3. For example, an integer of `1` in your source data becomes the string `"1"` in the output.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-flow-s3outputformatconfig--seealso"></a>
+ [S3OutputFormatConfig](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_S3OutputFormatConfig.html) in the *Amazon AppFlow API Reference*.
