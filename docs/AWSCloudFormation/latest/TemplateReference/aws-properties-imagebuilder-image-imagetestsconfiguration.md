---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-image-imagetestsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Image ImageTestsConfiguration
<a name="aws-properties-imagebuilder-image-imagetestsconfiguration"></a>

Configure image tests for your pipeline build. Tests run after building the image, to verify that the AMI or container image is valid before distributing it.

## Syntax
<a name="aws-properties-imagebuilder-image-imagetestsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-image-imagetestsconfiguration-syntax.json"></a>

```
{
  "[ImageTestsEnabled](#cfn-imagebuilder-image-imagetestsconfiguration-imagetestsenabled)" : {{Boolean}},
  "[TimeoutMinutes](#cfn-imagebuilder-image-imagetestsconfiguration-timeoutminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-imagebuilder-image-imagetestsconfiguration-syntax.yaml"></a>

```
  [ImageTestsEnabled](#cfn-imagebuilder-image-imagetestsconfiguration-imagetestsenabled): {{Boolean}}
  [TimeoutMinutes](#cfn-imagebuilder-image-imagetestsconfiguration-timeoutminutes): {{Integer}}
```

## Properties
<a name="aws-properties-imagebuilder-image-imagetestsconfiguration-properties"></a>

`ImageTestsEnabled`  <a name="cfn-imagebuilder-image-imagetestsconfiguration-imagetestsenabled"></a>
Determines if tests should run after building the image. Image Builder defaults to enable tests to run following the image build, before image distribution.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimeoutMinutes`  <a name="cfn-imagebuilder-image-imagetestsconfiguration-timeoutminutes"></a>
The maximum time in minutes that tests are permitted to run.
The timeout property is not currently active. This value is ignored.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `1440`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
