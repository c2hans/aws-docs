---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-allimagebuildversions-imagetestsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::AllImageBuildVersions ImageTestsConfiguration
<a name="aws-properties-imagebuilder-allimagebuildversions-imagetestsconfiguration"></a>

Configure image tests for your pipeline build. Tests run after building the image, to verify that the AMI or container image is valid before distributing it.

## Syntax
<a name="aws-properties-imagebuilder-allimagebuildversions-imagetestsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-allimagebuildversions-imagetestsconfiguration-syntax.json"></a>

```
{
  "[ImageTestsEnabled](#cfn-imagebuilder-allimagebuildversions-imagetestsconfiguration-imagetestsenabled)" : {{Boolean}},
  "[TimeoutMinutes](#cfn-imagebuilder-allimagebuildversions-imagetestsconfiguration-timeoutminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-imagebuilder-allimagebuildversions-imagetestsconfiguration-syntax.yaml"></a>

```
  [ImageTestsEnabled](#cfn-imagebuilder-allimagebuildversions-imagetestsconfiguration-imagetestsenabled): {{Boolean}}
  [TimeoutMinutes](#cfn-imagebuilder-allimagebuildversions-imagetestsconfiguration-timeoutminutes): {{Integer}}
```

## Properties
<a name="aws-properties-imagebuilder-allimagebuildversions-imagetestsconfiguration-properties"></a>

`ImageTestsEnabled`  <a name="cfn-imagebuilder-allimagebuildversions-imagetestsconfiguration-imagetestsenabled"></a>
Determines if tests should run after building the image. Image Builder defaults to enable tests to run following the image build, before image distribution.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-imagebuilder-allimagebuildversions-imagetestsconfiguration-timeoutminutes"></a>
The maximum time in minutes that tests are permitted to run.
The timeout property is not currently active. This value is ignored.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `1440`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
