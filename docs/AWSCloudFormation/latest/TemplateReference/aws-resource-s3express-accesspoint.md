---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3express-accesspoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::AccessPoint
<a name="aws-resource-s3express-accesspoint"></a>

Access points simplify managing data access at scale for shared datasets in Amazon S3. Access points are unique hostnames you create to enforce distinct permissions and network controls for all requests made through an access point. You can create hundreds of access points per bucket, each with a distinct name and permissions customized for each application. Each access point works in conjunction with the bucket policy that is attached to the underlying bucket. For more information, see [Managing access to shared datasets in directory buckets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html).

## Syntax
<a name="aws-resource-s3express-accesspoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3express-accesspoint-syntax.json"></a>

```
{
  "Type" : "AWS::S3Express::AccessPoint",
  "Properties" : {
      "[Bucket](#cfn-s3express-accesspoint-bucket)" : {{String}},
      "[BucketAccountId](#cfn-s3express-accesspoint-bucketaccountid)" : {{String}},
      "[Name](#cfn-s3express-accesspoint-name)" : {{String}},
      "[Policy](#cfn-s3express-accesspoint-policy)" : {{Json}},
      "[PublicAccessBlockConfiguration](#cfn-s3express-accesspoint-publicaccessblockconfiguration)" : {{PublicAccessBlockConfiguration}},
      "[Scope](#cfn-s3express-accesspoint-scope)" : {{Scope}},
      "[Tags](#cfn-s3express-accesspoint-tags)" : {{[ Tag, ... ]}},
      "[VpcConfiguration](#cfn-s3express-accesspoint-vpcconfiguration)" : {{VpcConfiguration}}
    }
}
```

### YAML
<a name="aws-resource-s3express-accesspoint-syntax.yaml"></a>

```
Type: AWS::S3Express::AccessPoint
Properties:
  [Bucket](#cfn-s3express-accesspoint-bucket): {{String}}
  [BucketAccountId](#cfn-s3express-accesspoint-bucketaccountid): {{String}}
  [Name](#cfn-s3express-accesspoint-name): {{String}}
  [Policy](#cfn-s3express-accesspoint-policy): {{Json}}
  [PublicAccessBlockConfiguration](#cfn-s3express-accesspoint-publicaccessblockconfiguration): {{
    PublicAccessBlockConfiguration}}
  [Scope](#cfn-s3express-accesspoint-scope): {{
    Scope}}
  [Tags](#cfn-s3express-accesspoint-tags): {{
    - Tag}}
  [VpcConfiguration](#cfn-s3express-accesspoint-vpcconfiguration): {{
    VpcConfiguration}}
```

## Properties
<a name="aws-resource-s3express-accesspoint-properties"></a>

`Bucket`  <a name="cfn-s3express-accesspoint-bucket"></a>
The name of the bucket that you want to associate the access point with.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BucketAccountId`  <a name="cfn-s3express-accesspoint-bucketaccountid"></a>
The AWS account ID that owns the bucket associated with this access point.
*Required*: No
*Type*: String
*Pattern*: `^\d{12}$`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-s3express-accesspoint-name"></a>
An access point name consists of a base name you provide, followed by the zoneID (AWS Local Zone) followed by the prefix `--xa-s3`. For example, accesspointname--zoneID--xa-s3.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`
*Minimum*: `3`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policy`  <a name="cfn-s3express-accesspoint-policy"></a>
The access point policy associated with the specified access point.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublicAccessBlockConfiguration`  <a name="cfn-s3express-accesspoint-publicaccessblockconfiguration"></a>
Public access is blocked by default to access points for directory buckets.
*Required*: No
*Type*: [PublicAccessBlockConfiguration](aws-properties-s3express-accesspoint-publicaccessblockconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-s3express-accesspoint-scope"></a>
You can use the access point scope to restrict access to specific prefixes, API operations, or a combination of both.
For more information, see [Manage the scope of your access points for directory buckets.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-manage-scope.html)
*Required*: No
*Type*: [Scope](aws-properties-s3express-accesspoint-scope.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-s3express-accesspoint-tags"></a>
An array of tags that you can apply to access points. Tags are key-value pairs of metadata used to categorize your access points and control access. For more information, see [Using tags for attribute-based access control (ABAC)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#using-tags-for-abac).
*Required*: No
*Type*: Array of [Tag](aws-properties-s3express-accesspoint-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfiguration`  <a name="cfn-s3express-accesspoint-vpcconfiguration"></a>
If you include this field, Amazon S3 restricts access to this access point to requests from the specified virtual private cloud (VPC).
*Required*: No
*Type*: [VpcConfiguration](aws-properties-s3express-accesspoint-vpcconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3express-accesspoint-return-values"></a>

### Ref
<a name="aws-resource-s3express-accesspoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-s3express-accesspoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-s3express-accesspoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the access point.

`NetworkOrigin`  <a name="NetworkOrigin-fn::getatt"></a>
The network configuration of the access point.
