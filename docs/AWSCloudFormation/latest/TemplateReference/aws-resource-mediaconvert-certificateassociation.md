---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconvert-certificateassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConvert::CertificateAssociation
<a name="aws-resource-mediaconvert-certificateassociation"></a>

<a name="aws-resource-mediaconvert-certificateassociation-description"></a>The `AWS::MediaConvert::CertificateAssociation` resource Property description not available. for MediaConvert.

## Syntax
<a name="aws-resource-mediaconvert-certificateassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconvert-certificateassociation-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConvert::CertificateAssociation",
  "Properties" : {
      "[Arn](#cfn-mediaconvert-certificateassociation-arn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-mediaconvert-certificateassociation-syntax.yaml"></a>

```
Type: AWS::MediaConvert::CertificateAssociation
Properties:
  [Arn](#cfn-mediaconvert-certificateassociation-arn): {{String}}
```

## Properties
<a name="aws-resource-mediaconvert-certificateassociation-properties"></a>

`Arn`  <a name="cfn-mediaconvert-certificateassociation-arn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z]+)*:acm:[a-z0-9-]+:[0-9]{12}:certificate/[a-f0-9-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-mediaconvert-certificateassociation-return-values"></a>

### Ref
<a name="aws-resource-mediaconvert-certificateassociation-return-values-ref"></a>
