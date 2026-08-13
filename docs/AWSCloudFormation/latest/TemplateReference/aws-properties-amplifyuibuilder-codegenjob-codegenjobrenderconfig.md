---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-codegenjob-codegenjobrenderconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::CodegenJob CodegenJobRenderConfig
<a name="aws-properties-amplifyuibuilder-codegenjob-codegenjobrenderconfig"></a>

Describes the configuration information for rendering the UI component associated with the code generation job.

## Syntax
<a name="aws-properties-amplifyuibuilder-codegenjob-codegenjobrenderconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-codegenjob-codegenjobrenderconfig-syntax.json"></a>

```
{
  "[React](#cfn-amplifyuibuilder-codegenjob-codegenjobrenderconfig-react)" : {{ReactStartCodegenJobData}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-codegenjob-codegenjobrenderconfig-syntax.yaml"></a>

```
  [React](#cfn-amplifyuibuilder-codegenjob-codegenjobrenderconfig-react): {{
    ReactStartCodegenJobData}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-codegenjob-codegenjobrenderconfig-properties"></a>

`React`  <a name="cfn-amplifyuibuilder-codegenjob-codegenjobrenderconfig-react"></a>
The name of the `ReactStartCodegenJobData` object.
*Required*: Yes
*Type*: [ReactStartCodegenJobData](aws-properties-amplifyuibuilder-codegenjob-reactstartcodegenjobdata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
