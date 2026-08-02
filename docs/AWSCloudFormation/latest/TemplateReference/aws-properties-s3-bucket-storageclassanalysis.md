---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-storageclassanalysis.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket StorageClassAnalysis
<a name="aws-properties-s3-bucket-storageclassanalysis"></a>

Specifies data related to access patterns to be collected and made available to analyze the tradeoffs between different storage classes for an Amazon S3 bucket.

## Syntax
<a name="aws-properties-s3-bucket-storageclassanalysis-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-storageclassanalysis-syntax.json"></a>

```
{
  "[DataExport](#cfn-s3-bucket-storageclassanalysis-dataexport)" : {{DataExport}}
}
```

### YAML
<a name="aws-properties-s3-bucket-storageclassanalysis-syntax.yaml"></a>

```
  [DataExport](#cfn-s3-bucket-storageclassanalysis-dataexport): {{
    DataExport}}
```

## Properties
<a name="aws-properties-s3-bucket-storageclassanalysis-properties"></a>

`DataExport`  <a name="cfn-s3-bucket-storageclassanalysis-dataexport"></a>
Specifies how data related to the storage class analysis for an Amazon S3 bucket should be exported.
*Required*: No
*Type*: [DataExport](aws-properties-s3-bucket-dataexport.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-s3-bucket-storageclassanalysis--seealso"></a>
+ AWS::S3::Bucket [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#aws-properties-s3-bucket--examples)
