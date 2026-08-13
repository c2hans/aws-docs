---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-codegenjob-reactstartcodegenjobdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::CodegenJob ReactStartCodegenJobData
<a name="aws-properties-amplifyuibuilder-codegenjob-reactstartcodegenjobdata"></a>

Describes the code generation job configuration for a React project.

## Syntax
<a name="aws-properties-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-syntax.json"></a>

```
{
  "[ApiConfiguration](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-apiconfiguration)" : {{ApiConfiguration}},
  "[InlineSourceMap](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-inlinesourcemap)" : {{Boolean}},
  "[Module](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-module)" : {{String}},
  "[RenderTypeDeclarations](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-rendertypedeclarations)" : {{Boolean}},
  "[Script](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-script)" : {{String}},
  "[Target](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-target)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-syntax.yaml"></a>

```
  [ApiConfiguration](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-apiconfiguration): {{
    ApiConfiguration}}
  [InlineSourceMap](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-inlinesourcemap): {{Boolean}}
  [Module](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-module): {{String}}
  [RenderTypeDeclarations](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-rendertypedeclarations): {{Boolean}}
  [Script](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-script): {{String}}
  [Target](#cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-target): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-properties"></a>

`ApiConfiguration`  <a name="cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-apiconfiguration"></a>
The API configuration for the code generation job.
*Required*: No
*Type*: [ApiConfiguration](aws-properties-amplifyuibuilder-codegenjob-apiconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InlineSourceMap`  <a name="cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-inlinesourcemap"></a>
Specifies whether the code generation job should render inline source maps.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Module`  <a name="cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-module"></a>
The JavaScript module type.
*Required*: No
*Type*: String
*Allowed values*: `es2020 | esnext`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RenderTypeDeclarations`  <a name="cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-rendertypedeclarations"></a>
Specifies whether the code generation job should render type declaration files.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Script`  <a name="cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-script"></a>
The file type to use for a JavaScript project.
*Required*: No
*Type*: String
*Allowed values*: `jsx | tsx | js`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Target`  <a name="cfn-amplifyuibuilder-codegenjob-reactstartcodegenjobdata-target"></a>
The ECMAScript specification to use.
*Required*: No
*Type*: String
*Allowed values*: `es2015 | es2020`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
