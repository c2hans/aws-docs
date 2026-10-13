---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-buildconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionRevision BuildConfig
<a name="aws-properties-lambda-webfunctionrevision-buildconfig"></a>

The build configuration for a web function revision, including code location and runtime settings.

## Syntax
<a name="aws-properties-lambda-webfunctionrevision-buildconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunctionrevision-buildconfig-syntax.json"></a>

```
{
  "[CodeConfig](#cfn-lambda-webfunctionrevision-buildconfig-codeconfig)" : {{CodeConfig}},
  "[RuntimeConfig](#cfn-lambda-webfunctionrevision-buildconfig-runtimeconfig)" : {{RuntimeConfig}}
}
```

### YAML
<a name="aws-properties-lambda-webfunctionrevision-buildconfig-syntax.yaml"></a>

```
  [CodeConfig](#cfn-lambda-webfunctionrevision-buildconfig-codeconfig): {{
    CodeConfig}}
  [RuntimeConfig](#cfn-lambda-webfunctionrevision-buildconfig-runtimeconfig): {{
    RuntimeConfig}}
```

## Properties
<a name="aws-properties-lambda-webfunctionrevision-buildconfig-properties"></a>

`CodeConfig`  <a name="cfn-lambda-webfunctionrevision-buildconfig-codeconfig"></a>
The code configuration specifying where the deployment artifact is stored.
*Required*: Yes
*Type*: [CodeConfig](aws-properties-lambda-webfunctionrevision-codeconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RuntimeConfig`  <a name="cfn-lambda-webfunctionrevision-buildconfig-runtimeconfig"></a>
The runtime configuration for the revision.
*Required*: Yes
*Type*: [RuntimeConfig](aws-properties-lambda-webfunctionrevision-runtimeconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
