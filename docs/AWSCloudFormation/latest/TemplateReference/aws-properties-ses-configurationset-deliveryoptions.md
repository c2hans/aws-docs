---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationset-deliveryoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSet DeliveryOptions
<a name="aws-properties-ses-configurationset-deliveryoptions"></a>

Specifies the name of the dedicated IP pool to associate with the configuration set and whether messages that use the configuration set are required to use Transport Layer Security (TLS).

## Syntax
<a name="aws-properties-ses-configurationset-deliveryoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationset-deliveryoptions-syntax.json"></a>

```
{
  "[MaxDeliverySeconds](#cfn-ses-configurationset-deliveryoptions-maxdeliveryseconds)" : {{Number}},
  "[SendingPoolName](#cfn-ses-configurationset-deliveryoptions-sendingpoolname)" : {{String}},
  "[TlsPolicy](#cfn-ses-configurationset-deliveryoptions-tlspolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-configurationset-deliveryoptions-syntax.yaml"></a>

```
  [MaxDeliverySeconds](#cfn-ses-configurationset-deliveryoptions-maxdeliveryseconds): {{Number}}
  [SendingPoolName](#cfn-ses-configurationset-deliveryoptions-sendingpoolname): {{String}}
  [TlsPolicy](#cfn-ses-configurationset-deliveryoptions-tlspolicy): {{String}}
```

## Properties
<a name="aws-properties-ses-configurationset-deliveryoptions-properties"></a>

`MaxDeliverySeconds`  <a name="cfn-ses-configurationset-deliveryoptions-maxdeliveryseconds"></a>
The name of the configuration set used when sent through a configuration set with archiving enabled.
*Required*: No
*Type*: Number
*Minimum*: `300`
*Maximum*: `50400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SendingPoolName`  <a name="cfn-ses-configurationset-deliveryoptions-sendingpoolname"></a>
The name of the dedicated IP pool to associate with the configuration set.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TlsPolicy`  <a name="cfn-ses-configurationset-deliveryoptions-tlspolicy"></a>
Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `REQUIRE`, messages are only delivered if a TLS connection can be established. If the value is `OPTIONAL`, messages can be delivered in plain text if a TLS connection can't be established.
Valid Values: `REQUIRE | OPTIONAL`
*Required*: No
*Type*: String
*Pattern*: `REQUIRE|OPTIONAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
