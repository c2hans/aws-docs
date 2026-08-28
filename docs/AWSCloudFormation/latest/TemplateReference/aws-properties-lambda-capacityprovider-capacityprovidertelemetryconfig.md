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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
