---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datasync-locations3.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationS3
<a name="aws-resource-datasync-locations3"></a>

The `AWS::DataSync::LocationS3` resource specifies an endpoint for an Amazon S3 bucket.

For more information, see the [https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html).

## Syntax
<a name="aws-resource-datasync-locations3-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datasync-locations3-syntax.json"></a>

```
{
  "Type" : "AWS::DataSync::LocationS3",
  "Properties" : {
      "[S3BucketArn](#cfn-datasync-locations3-s3bucketarn)" : {{String}},
      "[S3Config](#cfn-datasync-locations3-s3config)" : {{S3Config}},
      "[S3StorageClass](#cfn-datasync-locations3-s3storageclass)" : {{String}},
      "[Subdirectory](#cfn-datasync-locations3-subdirectory)" : {{String}},
      "[Tags](#cfn-datasync-locations3-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datasync-locations3-syntax.yaml"></a>

```
Type: AWS::DataSync::LocationS3
Properties:
  [S3BucketArn](#cfn-datasync-locations3-s3bucketarn): {{String}}
  [S3Config](#cfn-datasync-locations3-s3config): {{
    S3Config}}
  [S3StorageClass](#cfn-datasync-locations3-s3storageclass): {{String}}
  [Subdirectory](#cfn-datasync-locations3-subdirectory): {{String}}
  [Tags](#cfn-datasync-locations3-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-datasync-locations3-properties"></a>

`S3BucketArn`  <a name="cfn-datasync-locations3-s3bucketarn"></a>
The ARN of the Amazon S3 bucket.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3:[a-z\-0-9]*:[0-9]*:.*$`
*Maximum*: `156`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Config`  <a name="cfn-datasync-locations3-s3config"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used to access an Amazon S3 bucket.
For detailed information about using such a role, see [Creating a Location for Amazon S3](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html#create-s3-location) in the *AWS DataSync User Guide*.
*Required*: Yes
*Type*: [S3Config](aws-properties-datasync-locations3-s3config.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3StorageClass`  <a name="cfn-datasync-locations3-s3storageclass"></a>
The Amazon S3 storage class that you want to store your files in when this location is used as a task destination. For buckets in AWS Regions, the storage class defaults to S3 Standard.
For more information about S3 storage classes, see [Amazon S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/). Some storage classes have behaviors that can affect your S3 storage costs. For detailed information, see [Considerations When Working with Amazon S3 Storage Classes in DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes).
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | GLACIER_INSTANT_RETRIEVAL | DEEP_ARCHIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subdirectory`  <a name="cfn-datasync-locations3-subdirectory"></a>
Specifies a prefix in the S3 bucket that DataSync reads from or writes to (depending on whether the bucket is a source or destination location).
DataSync can't transfer objects with a prefix that begins with a slash (`/`) or includes `//`, `/./`, or `/../` patterns. For example:
+  `/photos`
+  `photos//2006/January`
+  `photos/./2006/February`
+  `photos/../2006/March`
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}\p{C}]*$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-datasync-locations3-tags"></a>
Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your transfer location.
*Required*: No
*Type*: Array of [Tag](aws-properties-datasync-locations3-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datasync-locations3-return-values"></a>

### Ref
<a name="aws-resource-datasync-locations3-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the location resource Amazon Resource Name (ARN). For example:

 `arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50s3`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datasync-locations3-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datasync-locations3-return-values-fn--getatt-fn--getatt"></a>

`LocationArn`  <a name="LocationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the specified Amazon S3 location.

`LocationUri`  <a name="LocationUri-fn::getatt"></a>
The URI of the specified Amazon S3 location.

## Examples
<a name="aws-resource-datasync-locations3--examples"></a>

### Create an Amazon S3 location for DataSync
<a name="aws-resource-datasync-locations3--examples--Create_an_Amazon_S3_location_for_DataSync"></a>

The following example specifies an S3 location for DataSync. In this example, the S3 location uses the bucket specified by the Amazon Resource Name (ARN) `arn:aws:s3:::amzn-s3-demo-bucket`. The access role is specified by the ARN `arn:aws:iam::111222333444:role/amzn-s3-demo-bucket-access-role`. The example uses the S3 Standard storage class and refers to the subdirectory `/MyFolder`.

AWS Security Token Service (AWS STS) must be activated in your account and Region for DataSync to assume the IAM role. For more information about temporary security credentials, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the * IAM User Guide *.

#### JSON
<a name="aws-resource-datasync-locations3--examples--Create_an_Amazon_S3_location_for_DataSync--json"></a>

```
{
"AWSTemplateFormatVersion": "2010-09-09",
"Description": "Specifies an S3 location for DataSync",
"Resources":
  {
    "LocationS3": {
      "Type": "AWS::DataSync::LocationS3",
      "Properties": {
        "S3BucketArn": "arn:aws:s3:::amzn-s3-demo-bucket",
        "S3Config": {
          "BucketAccessRoleArn": "arn:aws:iam::111222333444:role/amzn-s3-demo-bucket-access-role"
        },
      "S3StorageClass": "STANDARD",
      "Subdirectory": "/MyFolder"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-datasync-locations3--examples--Create_an_Amazon_S3_location_for_DataSync--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Specifies an S3 location for DataSync
Resources:
  LocationS3:
    Type: AWS::DataSync::LocationS3
    Properties:
      S3BucketArn: arn:aws:s3:::amzn-s3-demo-bucket
      S3Config:
        BucketAccessRoleArn: arn:aws:iam::111222333444:role/amzn-s3-demo-bucket-access-role
      S3StorageClass: STANDARD
      Subdirectory: /MyFolder
```
