---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-metadatadestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket MetadataDestination
<a name="aws-properties-s3-bucket-metadatadestination"></a>

 The destination information for the S3 Metadata configuration.

## Syntax
<a name="aws-properties-s3-bucket-metadatadestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-metadatadestination-syntax.json"></a>

```
{
  "[TableBucketArn](#cfn-s3-bucket-metadatadestination-tablebucketarn)" : {{String}},
  "[TableBucketType](#cfn-s3-bucket-metadatadestination-tablebuckettype)" : {{String}},
  "[TableNamespace](#cfn-s3-bucket-metadatadestination-tablenamespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-metadatadestination-syntax.yaml"></a>

```
  [TableBucketArn](#cfn-s3-bucket-metadatadestination-tablebucketarn): {{String}}
  [TableBucketType](#cfn-s3-bucket-metadatadestination-tablebuckettype): {{String}}
  [TableNamespace](#cfn-s3-bucket-metadatadestination-tablenamespace): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-metadatadestination-properties"></a>

`TableBucketArn`  <a name="cfn-s3-bucket-metadatadestination-tablebucketarn"></a>
 The Amazon Resource Name (ARN) of the table bucket where the metadata configuration is stored.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableBucketType`  <a name="cfn-s3-bucket-metadatadestination-tablebuckettype"></a>
 The type of the table bucket where the metadata configuration is stored. The `aws` value indicates an AWS managed table bucket, and the `customer` value indicates a customer-managed table bucket. V2 metadata configurations are stored in AWS managed table buckets, and V1 metadata configurations are stored in customer-managed table buckets.
*Required*: Yes
*Type*: String
*Allowed values*: `aws | customer`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableNamespace`  <a name="cfn-s3-bucket-metadatadestination-tablenamespace"></a>
 The namespace in the table bucket where the metadata tables for a metadata configuration are stored.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
