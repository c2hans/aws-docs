---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-s3accesspointattachment-s3accesspoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::S3AccessPointAttachment S3AccessPoint
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspoint"></a>

Describes the S3 access point configuration of the S3 access point attachment.

## Syntax
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspoint-syntax.json"></a>

```
{
  "[Alias](#cfn-fsx-s3accesspointattachment-s3accesspoint-alias)" : {{String}},
  "[Policy](#cfn-fsx-s3accesspointattachment-s3accesspoint-policy)" : {{Json}},
  "[ResourceARN](#cfn-fsx-s3accesspointattachment-s3accesspoint-resourcearn)" : {{String}},
  "[VpcConfiguration](#cfn-fsx-s3accesspointattachment-s3accesspoint-vpcconfiguration)" : {{S3AccessPointVpcConfiguration}}
}
```

### YAML
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspoint-syntax.yaml"></a>

```
  [Alias](#cfn-fsx-s3accesspointattachment-s3accesspoint-alias): {{String}}
  [Policy](#cfn-fsx-s3accesspointattachment-s3accesspoint-policy): {{Json}}
  [ResourceARN](#cfn-fsx-s3accesspointattachment-s3accesspoint-resourcearn): {{String}}
  [VpcConfiguration](#cfn-fsx-s3accesspointattachment-s3accesspoint-vpcconfiguration): {{
    S3AccessPointVpcConfiguration}}
```

## Properties
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspoint-properties"></a>

`Alias`  <a name="cfn-fsx-s3accesspointattachment-s3accesspoint-alias"></a>
The S3 access point's alias.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-z\\-]{1,63}`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policy`  <a name="cfn-fsx-s3accesspointattachment-s3accesspoint-policy"></a>
The S3 access point's policy.
*Required*: No
*Type*: Json
*Minimum*: `1`
*Maximum*: `200000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceARN`  <a name="cfn-fsx-s3accesspointattachment-s3accesspoint-resourcearn"></a>
The S3 access point's ARN.
*Required*: No
*Type*: String
*Pattern*: `^arn:[^:]{1,63}:[^:]{0,63}:[^:]{0,63}:(?:|\d{12}):[^/].{0,1023}$`
*Minimum*: `8`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfiguration`  <a name="cfn-fsx-s3accesspointattachment-s3accesspoint-vpcconfiguration"></a>
The S3 access point's virtual private cloud (VPC) configuration.
*Required*: No
*Type*: [S3AccessPointVpcConfiguration](aws-properties-fsx-s3accesspointattachment-s3accesspointvpcconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
