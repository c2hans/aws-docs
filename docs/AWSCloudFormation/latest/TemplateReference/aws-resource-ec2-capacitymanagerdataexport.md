---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-capacitymanagerdataexport.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::CapacityManagerDataExport
<a name="aws-resource-ec2-capacitymanagerdataexport"></a>

 Creates a new data export configuration for EC2 Capacity Manager. This allows you to automatically export capacity usage data to an S3 bucket on a scheduled basis. The exported data includes metrics for On-Demand, Spot, and Capacity Reservations usage across your organization.

## Syntax
<a name="aws-resource-ec2-capacitymanagerdataexport-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-capacitymanagerdataexport-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::CapacityManagerDataExport",
  "Properties" : {
      "[OutputFormat](#cfn-ec2-capacitymanagerdataexport-outputformat)" : {{String}},
      "[S3BucketName](#cfn-ec2-capacitymanagerdataexport-s3bucketname)" : {{String}},
      "[S3BucketPrefix](#cfn-ec2-capacitymanagerdataexport-s3bucketprefix)" : {{String}},
      "[Schedule](#cfn-ec2-capacitymanagerdataexport-schedule)" : {{String}},
      "[Tags](#cfn-ec2-capacitymanagerdataexport-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-capacitymanagerdataexport-syntax.yaml"></a>

```
Type: AWS::EC2::CapacityManagerDataExport
Properties:
  [OutputFormat](#cfn-ec2-capacitymanagerdataexport-outputformat): {{String}}
  [S3BucketName](#cfn-ec2-capacitymanagerdataexport-s3bucketname): {{String}}
  [S3BucketPrefix](#cfn-ec2-capacitymanagerdataexport-s3bucketprefix): {{String}}
  [Schedule](#cfn-ec2-capacitymanagerdataexport-schedule): {{String}}
  [Tags](#cfn-ec2-capacitymanagerdataexport-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-capacitymanagerdataexport-properties"></a>

`OutputFormat`  <a name="cfn-ec2-capacitymanagerdataexport-outputformat"></a>
 The file format of the exported data.
*Required*: Yes
*Type*: String
*Allowed values*: `csv | parquet`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3BucketName`  <a name="cfn-ec2-capacitymanagerdataexport-s3bucketname"></a>
 The name of the S3 bucket where export files are delivered.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3BucketPrefix`  <a name="cfn-ec2-capacitymanagerdataexport-s3bucketprefix"></a>
 The S3 key prefix used for organizing export files within the bucket.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Schedule`  <a name="cfn-ec2-capacitymanagerdataexport-schedule"></a>
 The frequency at which data exports are generated.
*Required*: Yes
*Type*: String
*Allowed values*: `hourly`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-capacitymanagerdataexport-tags"></a>
 The tags associated with the data export configuration.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-capacitymanagerdataexport-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-capacitymanagerdataexport-return-values"></a>

### Ref
<a name="aws-resource-ec2-capacitymanagerdataexport-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the export ID, such as `cmde-0f3f217ee9a5baead`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-capacitymanagerdataexport-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-capacitymanagerdataexport-return-values-fn--getatt-fn--getatt"></a>

`CapacityManagerDataExportId`  <a name="CapacityManagerDataExportId-fn::getatt"></a>
 The unique identifier for the data export configuration.
