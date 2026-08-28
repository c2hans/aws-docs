---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-environmentproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application EnvironmentProperties
<a name="aws-properties-kinesisanalyticsv2-application-environmentproperties"></a>

Describes execution properties for a Managed Service for Apache Flink application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-environmentproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-environmentproperties-syntax.json"></a>

```
{
  "[PropertyGroups](#cfn-kinesisanalyticsv2-application-environmentproperties-propertygroups)" : {{[ PropertyGroup, ... ]}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-environmentproperties-syntax.yaml"></a>

```
  [PropertyGroups](#cfn-kinesisanalyticsv2-application-environmentproperties-propertygroups): {{
    - PropertyGroup}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-environmentproperties-properties"></a>

`PropertyGroups`  <a name="cfn-kinesisanalyticsv2-application-environmentproperties-propertygroups"></a>
Describes the execution property groups.
*Required*: No
*Type*: Array of [PropertyGroup](aws-properties-kinesisanalyticsv2-application-propertygroup.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-application-environmentproperties--seealso"></a>
+ [EnvironmentProperties](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_EnvironmentProperties.html) in the *Amazon Kinesis Data Analytics API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
