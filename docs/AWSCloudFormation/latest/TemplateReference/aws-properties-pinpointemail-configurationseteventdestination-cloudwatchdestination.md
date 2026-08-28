---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PinpointEmail::ConfigurationSetEventDestination CloudWatchDestination
<a name="aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination"></a>

An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.

## Syntax
<a name="aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination-syntax.json"></a>

```
{
  "[DimensionConfigurations](#cfn-pinpointemail-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations)" : {{[ DimensionConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination-syntax.yaml"></a>

```
  [DimensionConfigurations](#cfn-pinpointemail-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations): {{
    - DimensionConfiguration}}
```

## Properties
<a name="aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination-properties"></a>

`DimensionConfigurations`  <a name="cfn-pinpointemail-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations"></a>
An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.
*Required*: No
*Type*: Array of [DimensionConfiguration](aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
