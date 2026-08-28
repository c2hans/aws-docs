---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-multiplex-multiplexmediaconnectoutputdestinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Multiplex MultiplexMediaConnectOutputDestinationSettings
<a name="aws-properties-medialive-multiplex-multiplexmediaconnectoutputdestinationsettings"></a>

Multiplex MediaConnect output destination settings.

## Syntax
<a name="aws-properties-medialive-multiplex-multiplexmediaconnectoutputdestinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-multiplex-multiplexmediaconnectoutputdestinationsettings-syntax.json"></a>

```
{
  "[EntitlementArn](#cfn-medialive-multiplex-multiplexmediaconnectoutputdestinationsettings-entitlementarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-multiplex-multiplexmediaconnectoutputdestinationsettings-syntax.yaml"></a>

```
  [EntitlementArn](#cfn-medialive-multiplex-multiplexmediaconnectoutputdestinationsettings-entitlementarn): {{String}}
```

## Properties
<a name="aws-properties-medialive-multiplex-multiplexmediaconnectoutputdestinationsettings-properties"></a>

`EntitlementArn`  <a name="cfn-medialive-multiplex-multiplexmediaconnectoutputdestinationsettings-entitlementarn"></a>
The MediaConnect entitlement ARN available as a Flow source.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
