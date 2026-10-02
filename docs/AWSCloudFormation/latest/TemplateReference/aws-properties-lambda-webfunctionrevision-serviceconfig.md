---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-serviceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionRevision ServiceConfig
<a name="aws-properties-lambda-webfunctionrevision-serviceconfig"></a>

<a name="aws-properties-lambda-webfunctionrevision-serviceconfig-description"></a>The `ServiceConfig` property type specifies Property description not available. for an [AWS::Lambda::WebFunctionRevision](aws-resource-lambda-webfunctionrevision.md).

## Syntax
<a name="aws-properties-lambda-webfunctionrevision-serviceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunctionrevision-serviceconfig-syntax.json"></a>

```
{
  "[EnvironmentVariables](#cfn-lambda-webfunctionrevision-serviceconfig-environmentvariables)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ExecutionRoleArn](#cfn-lambda-webfunctionrevision-serviceconfig-executionrolearn)" : {{String}},
  "[MaxConcurrencyPerEnvironment](#cfn-lambda-webfunctionrevision-serviceconfig-maxconcurrencyperenvironment)" : {{Integer}},
  "[TelemetryConfig](#cfn-lambda-webfunctionrevision-serviceconfig-telemetryconfig)" : {{TelemetryConfig}},
  "[TimeoutSeconds](#cfn-lambda-webfunctionrevision-serviceconfig-timeoutseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-webfunctionrevision-serviceconfig-syntax.yaml"></a>

```
  [EnvironmentVariables](#cfn-lambda-webfunctionrevision-serviceconfig-environmentvariables): {{
    {{Key}}: {{Value}}}}
  [ExecutionRoleArn](#cfn-lambda-webfunctionrevision-serviceconfig-executionrolearn): {{String}}
  [MaxConcurrencyPerEnvironment](#cfn-lambda-webfunctionrevision-serviceconfig-maxconcurrencyperenvironment): {{Integer}}
  [TelemetryConfig](#cfn-lambda-webfunctionrevision-serviceconfig-telemetryconfig): {{
    TelemetryConfig}}
  [TimeoutSeconds](#cfn-lambda-webfunctionrevision-serviceconfig-timeoutseconds): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-webfunctionrevision-serviceconfig-properties"></a>

`EnvironmentVariables`  <a name="cfn-lambda-webfunctionrevision-serviceconfig-environmentvariables"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z]([a-zA-Z0-9_])*$`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRoleArn`  <a name="cfn-lambda-webfunctionrevision-serviceconfig-executionrolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-z-]*){1}:iam::[0-9]{12}:role/.*$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxConcurrencyPerEnvironment`  <a name="cfn-lambda-webfunctionrevision-serviceconfig-maxconcurrencyperenvironment"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TelemetryConfig`  <a name="cfn-lambda-webfunctionrevision-serviceconfig-telemetryconfig"></a>
Property description not available.
*Required*: No
*Type*: [TelemetryConfig](aws-properties-lambda-webfunctionrevision-telemetryconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimeoutSeconds`  <a name="cfn-lambda-webfunctionrevision-serviceconfig-timeoutseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `3`
*Maximum*: `900`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
