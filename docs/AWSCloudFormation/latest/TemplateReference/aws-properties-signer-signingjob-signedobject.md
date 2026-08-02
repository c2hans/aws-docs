---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-signer-signingjob-signedobject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Signer::SigningJob SignedObject
<a name="aws-properties-signer-signingjob-signedobject"></a>

Points to an `S3SignedObject` object that contains information about your signed code image.

## Syntax
<a name="aws-properties-signer-signingjob-signedobject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-signer-signingjob-signedobject-syntax.json"></a>

```
{
  "[S3](#cfn-signer-signingjob-signedobject-s3)" : {{S3SignedObject}}
}
```

### YAML
<a name="aws-properties-signer-signingjob-signedobject-syntax.yaml"></a>

```
  [S3](#cfn-signer-signingjob-signedobject-s3): {{
    S3SignedObject}}
```

## Properties
<a name="aws-properties-signer-signingjob-signedobject-properties"></a>

`S3`  <a name="cfn-signer-signingjob-signedobject-s3"></a>
The `S3SignedObject`.
*Required*: No
*Type*: [S3SignedObject](aws-properties-signer-signingjob-s3signedobject.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
