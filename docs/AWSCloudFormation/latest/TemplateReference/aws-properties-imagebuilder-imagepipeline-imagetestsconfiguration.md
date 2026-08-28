---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImagePipeline ImageTestsConfiguration
<a name="aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration"></a>

Configure image tests for your pipeline build. Tests run after building the image, to verify that the AMI or container image is valid before distributing it.

## Syntax
<a name="aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration-syntax.json"></a>

```
{
  "[ImageTestsEnabled](#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-imagetestsenabled)" : {{Boolean}},
  "[TimeoutMinutes](#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-timeoutminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration-syntax.yaml"></a>

```
  [ImageTestsEnabled](#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-imagetestsenabled): {{Boolean}}
  [TimeoutMinutes](#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-timeoutminutes): {{Integer}}
```

## Properties
<a name="aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration-properties"></a>

`ImageTestsEnabled`  <a name="cfn-imagebuilder-imagepipeline-imagetestsconfiguration-imagetestsenabled"></a>
Determines if tests should run after building the image. Image Builder defaults to enable tests to run following the image build, before image distribution.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-imagebuilder-imagepipeline-imagetestsconfiguration-timeoutminutes"></a>
The maximum time in minutes that tests are permitted to run.
The timeout property is not currently active. This value is ignored.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `1440`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
