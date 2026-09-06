---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccesstrustprovider-ssespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessTrustProvider SseSpecification
<a name="aws-properties-ec2-verifiedaccesstrustprovider-ssespecification"></a>

AWS Verified Access provides server side encryption by default to data at rest using AWS-owned KMS keys. You also have the option of using customer managed KMS keys, which can be specified using the options below.

## Syntax
<a name="aws-properties-ec2-verifiedaccesstrustprovider-ssespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccesstrustprovider-ssespecification-syntax.json"></a>

```
{
  "[CustomerManagedKeyEnabled](#cfn-ec2-verifiedaccesstrustprovider-ssespecification-customermanagedkeyenabled)" : {{Boolean}},
  "[KmsKeyArn](#cfn-ec2-verifiedaccesstrustprovider-ssespecification-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccesstrustprovider-ssespecification-syntax.yaml"></a>

```
  [CustomerManagedKeyEnabled](#cfn-ec2-verifiedaccesstrustprovider-ssespecification-customermanagedkeyenabled): {{Boolean}}
  [KmsKeyArn](#cfn-ec2-verifiedaccesstrustprovider-ssespecification-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccesstrustprovider-ssespecification-properties"></a>

`CustomerManagedKeyEnabled`  <a name="cfn-ec2-verifiedaccesstrustprovider-ssespecification-customermanagedkeyenabled"></a>
 Enable or disable the use of customer managed KMS keys for server side encryption.
Valid values: `True` \| `False`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-ec2-verifiedaccesstrustprovider-ssespecification-kmskeyarn"></a>
 The ARN of the KMS key.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
