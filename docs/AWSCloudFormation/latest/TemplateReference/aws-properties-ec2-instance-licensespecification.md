---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-licensespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance LicenseSpecification
<a name="aws-properties-ec2-instance-licensespecification"></a>

Specifies the license configuration to use.

`LicenseSpecification` is a property of the [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource.

## Syntax
<a name="aws-properties-ec2-instance-licensespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-licensespecification-syntax.json"></a>

```
{
  "[LicenseConfigurationArn](#cfn-ec2-instance-licensespecification-licenseconfigurationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instance-licensespecification-syntax.yaml"></a>

```
  [LicenseConfigurationArn](#cfn-ec2-instance-licensespecification-licenseconfigurationarn): {{String}}
```

## Properties
<a name="aws-properties-ec2-instance-licensespecification-properties"></a>

`LicenseConfigurationArn`  <a name="cfn-ec2-instance-licensespecification-licenseconfigurationarn"></a>
The Amazon Resource Name (ARN) of the license configuration.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
