---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-multiregionaccesspoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::MultiRegionAccessPoint
<a name="aws-resource-s3-multiregionaccesspoint"></a>

The `AWS::S3::MultiRegionAccessPoint` resource creates an Amazon S3 Multi-Region Access Point. To learn more about Multi-Region Access Points, see [ Multi-Region Access Points in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html) in the in the *Amazon S3 User Guide*.

## Syntax
<a name="aws-resource-s3-multiregionaccesspoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3-multiregionaccesspoint-syntax.json"></a>

```
{
  "Type" : "AWS::S3::MultiRegionAccessPoint",
  "Properties" : {
      "[Name](#cfn-s3-multiregionaccesspoint-name)" : {{String}},
      "[PublicAccessBlockConfiguration](#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration)" : {{PublicAccessBlockConfiguration}},
      "[Regions](#cfn-s3-multiregionaccesspoint-regions)" : {{[ Region, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-s3-multiregionaccesspoint-syntax.yaml"></a>

```
Type: AWS::S3::MultiRegionAccessPoint
Properties:
  [Name](#cfn-s3-multiregionaccesspoint-name): {{String}}
  [PublicAccessBlockConfiguration](#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration): {{
    PublicAccessBlockConfiguration}}
  [Regions](#cfn-s3-multiregionaccesspoint-regions): {{
    - Region}}
```

## Properties
<a name="aws-resource-s3-multiregionaccesspoint-properties"></a>

`Name`  <a name="cfn-s3-multiregionaccesspoint-name"></a>
The name of the Multi-Region Access Point.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9][-a-z0-9]{1,48}[a-z0-9]$`
*Minimum*: `3`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PublicAccessBlockConfiguration`  <a name="cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration"></a>
The PublicAccessBlock configuration that you want to apply to this Multi-Region Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers an object public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status) in the *Amazon S3 User Guide*.
*Required*: No
*Type*: [PublicAccessBlockConfiguration](aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Regions`  <a name="cfn-s3-multiregionaccesspoint-regions"></a>
A collection of the Regions and buckets associated with the Multi-Region Access Point.
*Required*: Yes
*Type*: Array of [Region](aws-properties-s3-multiregionaccesspoint-region.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3-multiregionaccesspoint-return-values"></a>

### Ref
<a name="aws-resource-s3-multiregionaccesspoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the Multi-Region Access Point.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3-multiregionaccesspoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3-multiregionaccesspoint-return-values-fn--getatt-fn--getatt"></a>

`Alias`  <a name="Alias-fn::getatt"></a>
The alias for the Multi-Region Access Point. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see [Managing Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming) in the *Amazon S3 User Guide*.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the Multi-Region Access Point is created.

## Examples
<a name="aws-resource-s3-multiregionaccesspoint--examples"></a>

You can use AWSCloudFormation to create a Multi-Region Access Point. When you create the Multi-Region Access Point, you must provide all the S3 buckets that it supports. Be aware that you can't add any S3 buckets to the Multi-Region Access Point after it's been created.

### Multi-Region Access Point with two Regions
<a name="aws-resource-s3-multiregionaccesspoint--examples--Multi-Region_Access_Point_with_two_Regions"></a>

The following template can be used to create a Multi-Region Access Point (with two Regions) through AWS CloudFormation.

#### JSON
<a name="aws-resource-s3-multiregionaccesspoint--examples--Multi-Region_Access_Point_with_two_Regions--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "DOC-EXAMPLE-MULTI-REGION-ACCESS-POINT": {
          "Type" : "AWS::S3::MultiRegionAccessPoint",
          "Properties" : {
            "PublicAccessBlockConfiguration" : {
              "BlockPublicAcls" : "True",
              "BlockPublicPolicy" : "True",
              "IgnorePublicAcls" : "True",
              "RestrictPublicBuckets" : "True"
            },
            "Regions" : [ {"Bucket":"DOC-EXAMPLE-BUCKET1"}, {"Bucket": "DOC-EXAMPLE-BUCKET2"} ]
        }
      }
    }
}
```

#### YAML
<a name="aws-resource-s3-multiregionaccesspoint--examples--Multi-Region_Access_Point_with_two_Regions--yaml"></a>

```
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  DOC-EXAMPLE-MULTI-REGION-ACCESS-POINT:
    Type: AWS::S3::MultiRegionAccessPoint
    Properties:
      PublicAccessBlockConfiguration:
        BlockPublicAcls: "True"
        BlockPublicPolicy: "True"
        IgnorePublicAcls: "True"
        RestrictPublicBuckets: "True"
      Regions:
        - Bucket: DOC-EXAMPLE-BUCKET1
        - Bucket: DOC-EXAMPLE-BUCKET2
```
