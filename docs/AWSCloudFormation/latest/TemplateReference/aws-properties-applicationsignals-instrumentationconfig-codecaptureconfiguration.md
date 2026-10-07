---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-instrumentationconfig-codecaptureconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::InstrumentationConfig CodeCaptureConfiguration
<a name="aws-properties-applicationsignals-instrumentationconfig-codecaptureconfiguration"></a>

Defines what data to capture for code-level instrumentation, including arguments, return values, stack traces, local variables, and safety limits.

## Syntax
<a name="aws-properties-applicationsignals-instrumentationconfig-codecaptureconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-instrumentationconfig-codecaptureconfiguration-syntax.json"></a>

```
{
  "[CaptureArguments](#cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturearguments)" : {{[ String, ... ]}},
  "[CaptureLimits](#cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturelimits)" : {{CaptureLimitsConfig}},
  "[CaptureLocals](#cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturelocals)" : {{[ String, ... ]}},
  "[CaptureReturn](#cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturereturn)" : {{Boolean}},
  "[CaptureStackTrace](#cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturestacktrace)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-applicationsignals-instrumentationconfig-codecaptureconfiguration-syntax.yaml"></a>

```
  [CaptureArguments](#cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturearguments): {{
    - String}}
  [CaptureLimits](#cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturelimits): {{
    CaptureLimitsConfig}}
  [CaptureLocals](#cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturelocals): {{
    - String}}
  [CaptureReturn](#cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturereturn): {{Boolean}}
  [CaptureStackTrace](#cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturestacktrace): {{Boolean}}
```

## Properties
<a name="aws-properties-applicationsignals-instrumentationconfig-codecaptureconfiguration-properties"></a>

`CaptureArguments`  <a name="cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturearguments"></a>
The function arguments to capture. Omit to capture defaults, use an empty list to capture none, use `["*"]` to capture all arguments, or specify argument names to capture selectively (up to 10 entries).
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `80 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CaptureLimits`  <a name="cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturelimits"></a>
Safety limits that bound what is captured, including hit counts, string length, collection depth, and stack trace size.
*Required*: Yes
*Type*: [CaptureLimitsConfig](aws-properties-applicationsignals-instrumentationconfig-capturelimitsconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CaptureLocals`  <a name="cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturelocals"></a>
The local variables to capture by name. Omit or pass an empty list to capture none. You can specify up to 20 names.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `80 | 20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CaptureReturn`  <a name="cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturereturn"></a>
Whether to capture the return value. Defaults to false.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CaptureStackTrace`  <a name="cfn-applicationsignals-instrumentationconfig-codecaptureconfiguration-capturestacktrace"></a>
Whether to capture a stack trace when the instrumentation point is hit. Defaults to true.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
