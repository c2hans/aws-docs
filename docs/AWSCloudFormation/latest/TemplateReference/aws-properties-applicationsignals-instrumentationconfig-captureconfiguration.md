---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-instrumentationconfig-captureconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::InstrumentationConfig CaptureConfiguration
<a name="aws-properties-applicationsignals-instrumentationconfig-captureconfiguration"></a>

A union that defines what data to capture when the instrumentation point is hit. Specify `CodeCapture` for code-level capture settings.

## Syntax
<a name="aws-properties-applicationsignals-instrumentationconfig-captureconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-instrumentationconfig-captureconfiguration-syntax.json"></a>

```
{
  "[CodeCapture](#cfn-applicationsignals-instrumentationconfig-captureconfiguration-codecapture)" : {{CodeCaptureConfiguration}}
}
```

### YAML
<a name="aws-properties-applicationsignals-instrumentationconfig-captureconfiguration-syntax.yaml"></a>

```
  [CodeCapture](#cfn-applicationsignals-instrumentationconfig-captureconfiguration-codecapture): {{
    CodeCaptureConfiguration}}
```

## Properties
<a name="aws-properties-applicationsignals-instrumentationconfig-captureconfiguration-properties"></a>

`CodeCapture`  <a name="cfn-applicationsignals-instrumentationconfig-captureconfiguration-codecapture"></a>
Capture settings for code-level instrumentation, including arguments, return values, stack traces, local variables, and safety limits.
*Required*: Yes
*Type*: [CodeCaptureConfiguration](aws-properties-applicationsignals-instrumentationconfig-codecaptureconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
