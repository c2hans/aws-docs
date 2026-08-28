---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpointemail-configurationset-deliveryoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PinpointEmail::ConfigurationSet DeliveryOptions
<a name="aws-properties-pinpointemail-configurationset-deliveryoptions"></a>

Used to associate a configuration set with a dedicated IP pool.

## Syntax
<a name="aws-properties-pinpointemail-configurationset-deliveryoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpointemail-configurationset-deliveryoptions-syntax.json"></a>

```
{
  "[SendingPoolName](#cfn-pinpointemail-configurationset-deliveryoptions-sendingpoolname)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpointemail-configurationset-deliveryoptions-syntax.yaml"></a>

```
  [SendingPoolName](#cfn-pinpointemail-configurationset-deliveryoptions-sendingpoolname): {{String}}
```

## Properties
<a name="aws-properties-pinpointemail-configurationset-deliveryoptions-properties"></a>

`SendingPoolName`  <a name="cfn-pinpointemail-configurationset-deliveryoptions-sendingpoolname"></a>
The name of the dedicated IP pool that you want to associate with the configuration set.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
