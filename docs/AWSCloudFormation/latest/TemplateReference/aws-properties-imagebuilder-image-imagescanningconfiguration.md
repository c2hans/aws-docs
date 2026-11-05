---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-image-imagescanningconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Image ImageScanningConfiguration
<a name="aws-properties-imagebuilder-image-imagescanningconfiguration"></a>

Contains settings for Image Builder image resource and container image scans.

## Syntax
<a name="aws-properties-imagebuilder-image-imagescanningconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-image-imagescanningconfiguration-syntax.json"></a>

```
{
  "[EcrConfiguration](#cfn-imagebuilder-image-imagescanningconfiguration-ecrconfiguration)" : {{EcrConfiguration}},
  "[ImageScanningEnabled](#cfn-imagebuilder-image-imagescanningconfiguration-imagescanningenabled)" : {{Boolean}},
  "[ImageScanningTypes](#cfn-imagebuilder-image-imagescanningconfiguration-imagescanningtypes)" : {{[ String, ... ]}},
  "[ScanResultCondition](#cfn-imagebuilder-image-imagescanningconfiguration-scanresultcondition)" : {{ScanResultCondition}}
}
```

### YAML
<a name="aws-properties-imagebuilder-image-imagescanningconfiguration-syntax.yaml"></a>

```
  [EcrConfiguration](#cfn-imagebuilder-image-imagescanningconfiguration-ecrconfiguration): {{
    EcrConfiguration}}
  [ImageScanningEnabled](#cfn-imagebuilder-image-imagescanningconfiguration-imagescanningenabled): {{Boolean}}
  [ImageScanningTypes](#cfn-imagebuilder-image-imagescanningconfiguration-imagescanningtypes): {{
    - String}}
  [ScanResultCondition](#cfn-imagebuilder-image-imagescanningconfiguration-scanresultcondition): {{
    ScanResultCondition}}
```

## Properties
<a name="aws-properties-imagebuilder-image-imagescanningconfiguration-properties"></a>

`EcrConfiguration`  <a name="cfn-imagebuilder-image-imagescanningconfiguration-ecrconfiguration"></a>
Contains Amazon ECR settings for vulnerability scans.
*Required*: No
*Type*: [EcrConfiguration](aws-properties-imagebuilder-image-ecrconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageScanningEnabled`  <a name="cfn-imagebuilder-image-imagescanningconfiguration-imagescanningenabled"></a>
Specifies whether Amazon Inspector scans for vulnerabilities when you create a new image, and whether Image Builder saves the findings. Amazon Inspector must be enabled in the account. Image tests must also be enabled. For AMI output, Amazon Inspector scans the test instance. For container output, Amazon Inspector scans the container image that Image Builder pushes to the Amazon ECR repository from your `ecrConfiguration` settings.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageScanningTypes`  <a name="cfn-imagebuilder-image-imagescanningconfiguration-imagescanningtypes"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Allowed values*: `TEST_INSTANCE_CVE | ON_DEMAND_AMI_CVE`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScanResultCondition`  <a name="cfn-imagebuilder-image-imagescanningconfiguration-scanresultcondition"></a>
Property description not available.
*Required*: No
*Type*: [ScanResultCondition](aws-properties-imagebuilder-image-scanresultcondition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
