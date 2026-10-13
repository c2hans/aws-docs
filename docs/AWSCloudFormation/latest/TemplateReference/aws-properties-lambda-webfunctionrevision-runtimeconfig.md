---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-runtimeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionRevision RuntimeConfig
<a name="aws-properties-lambda-webfunctionrevision-runtimeconfig"></a>

The runtime configuration for a web function revision.

## Syntax
<a name="aws-properties-lambda-webfunctionrevision-runtimeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunctionrevision-runtimeconfig-syntax.json"></a>

```
{
  "[Runtime](#cfn-lambda-webfunctionrevision-runtimeconfig-runtime)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-webfunctionrevision-runtimeconfig-syntax.yaml"></a>

```
  [Runtime](#cfn-lambda-webfunctionrevision-runtimeconfig-runtime): {{String}}
```

## Properties
<a name="aws-properties-lambda-webfunctionrevision-runtimeconfig-properties"></a>

`Runtime`  <a name="cfn-lambda-webfunctionrevision-runtimeconfig-runtime"></a>
The runtime identifier for the web function (for example, a Node.js runtime identifier).
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9]*[0-9]+(\.[a-z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
