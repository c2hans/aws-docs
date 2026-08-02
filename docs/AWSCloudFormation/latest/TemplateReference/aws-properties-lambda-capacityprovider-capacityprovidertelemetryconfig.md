---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-capacityprovider-capacityprovidertelemetryconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::CapacityProvider CapacityProviderTelemetryConfig
<a name="aws-properties-lambda-capacityprovider-capacityprovidertelemetryconfig"></a>

Configuration that specifies the telemetry collection for the capacity provider.

## Syntax
<a name="aws-properties-lambda-capacityprovider-capacityprovidertelemetryconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-capacityprovider-capacityprovidertelemetryconfig-syntax.json"></a>

```
{
  "[LoggingConfig](#cfn-lambda-capacityprovider-capacityprovidertelemetryconfig-loggingconfig)" : {{CapacityProviderLoggingConfig}}
}
```

### YAML
<a name="aws-properties-lambda-capacityprovider-capacityprovidertelemetryconfig-syntax.yaml"></a>

```
  [LoggingConfig](#cfn-lambda-capacityprovider-capacityprovidertelemetryconfig-loggingconfig): {{
    CapacityProviderLoggingConfig}}
```

## Properties
<a name="aws-properties-lambda-capacityprovider-capacityprovidertelemetryconfig-properties"></a>

`LoggingConfig`  <a name="cfn-lambda-capacityprovider-capacityprovidertelemetryconfig-loggingconfig"></a>
The capacity provider's Amazon CloudWatch Logs configuration settings.
*Required*: No
*Type*: [CapacityProviderLoggingConfig](aws-properties-lambda-capacityprovider-capacityproviderloggingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
