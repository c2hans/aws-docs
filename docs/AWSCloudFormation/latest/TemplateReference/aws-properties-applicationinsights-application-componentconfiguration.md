---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationinsights-application-componentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationInsights::Application ComponentConfiguration
<a name="aws-properties-applicationinsights-application-componentconfiguration"></a>

The `AWS::ApplicationInsights::Application ComponentConfiguration` property type defines the configuration settings of the component.

## Syntax
<a name="aws-properties-applicationinsights-application-componentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationinsights-application-componentconfiguration-syntax.json"></a>

```
{
  "[ConfigurationDetails](#cfn-applicationinsights-application-componentconfiguration-configurationdetails)" : {{ConfigurationDetails}},
  "[SubComponentTypeConfigurations](#cfn-applicationinsights-application-componentconfiguration-subcomponenttypeconfigurations)" : {{[ SubComponentTypeConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-applicationinsights-application-componentconfiguration-syntax.yaml"></a>

```
  [ConfigurationDetails](#cfn-applicationinsights-application-componentconfiguration-configurationdetails): {{
    ConfigurationDetails}}
  [SubComponentTypeConfigurations](#cfn-applicationinsights-application-componentconfiguration-subcomponenttypeconfigurations): {{
    - SubComponentTypeConfiguration}}
```

## Properties
<a name="aws-properties-applicationinsights-application-componentconfiguration-properties"></a>

`ConfigurationDetails`  <a name="cfn-applicationinsights-application-componentconfiguration-configurationdetails"></a>
The configuration settings.
*Required*: No
*Type*: [ConfigurationDetails](aws-properties-applicationinsights-application-configurationdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubComponentTypeConfigurations`  <a name="cfn-applicationinsights-application-componentconfiguration-subcomponenttypeconfigurations"></a>
Sub-component configurations of the component.
*Required*: No
*Type*: Array of [SubComponentTypeConfiguration](aws-properties-applicationinsights-application-subcomponenttypeconfiguration.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
