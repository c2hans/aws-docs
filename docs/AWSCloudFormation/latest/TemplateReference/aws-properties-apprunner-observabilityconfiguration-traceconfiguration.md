---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-observabilityconfiguration-traceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::ObservabilityConfiguration TraceConfiguration
<a name="aws-properties-apprunner-observabilityconfiguration-traceconfiguration"></a>

Describes the configuration of the tracing feature within an AWS App Runner observability configuration.

## Syntax
<a name="aws-properties-apprunner-observabilityconfiguration-traceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-observabilityconfiguration-traceconfiguration-syntax.json"></a>

```
{
  "[Vendor](#cfn-apprunner-observabilityconfiguration-traceconfiguration-vendor)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-observabilityconfiguration-traceconfiguration-syntax.yaml"></a>

```
  [Vendor](#cfn-apprunner-observabilityconfiguration-traceconfiguration-vendor): {{String}}
```

## Properties
<a name="aws-properties-apprunner-observabilityconfiguration-traceconfiguration-properties"></a>

`Vendor`  <a name="cfn-apprunner-observabilityconfiguration-traceconfiguration-vendor"></a>
The implementation provider chosen for tracing App Runner services.
*Required*: Yes
*Type*: String
*Allowed values*: `AWSXRAY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
