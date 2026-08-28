---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::SubscriptionDefinition SubscriptionDefinitionVersion
<a name="aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion"></a>

<a name="aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion-description"></a> A subscription definition version contains a list of [subscriptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html).

**Note**
After you create a subscription definition version that contains the subscriptions you want to deploy, you must add it to your group version. For more information, see [`AWS::Greengrass::Group`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html).

<a name="aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion-inheritance"></a> In an CloudFormation template, `SubscriptionDefinitionVersion` is the property type of the `InitialVersion` property in the [`AWS::Greengrass::SubscriptionDefinition`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html) resource.

## Syntax
<a name="aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion-syntax.json"></a>

```
{
  "[Subscriptions](#cfn-greengrass-subscriptiondefinition-subscriptiondefinitionversion-subscriptions)" : {{[ Subscription, ... ]}}
}
```

### YAML
<a name="aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion-syntax.yaml"></a>

```
  [Subscriptions](#cfn-greengrass-subscriptiondefinition-subscriptiondefinitionversion-subscriptions): {{
    - Subscription}}
```

## Properties
<a name="aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion-properties"></a>

`Subscriptions`  <a name="cfn-greengrass-subscriptiondefinition-subscriptiondefinitionversion-subscriptions"></a>
The subscriptions in this version.
*Required*: Yes
*Type*: Array of [Subscription](aws-properties-greengrass-subscriptiondefinition-subscription.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion--seealso"></a>
+ [SubscriptionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-subscriptiondefinitionversion.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
