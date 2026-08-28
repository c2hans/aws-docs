---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-cloudconnector-configurationtargets.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::CloudConnector ConfigurationTargets
<a name="aws-properties-ssm-cloudconnector-configurationtargets"></a>

The target resources in the third-party cloud environment.

## Syntax
<a name="aws-properties-ssm-cloudconnector-configurationtargets-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-cloudconnector-configurationtargets-syntax.json"></a>

```
{
  "[Subscriptions](#cfn-ssm-cloudconnector-configurationtargets-subscriptions)" : {{[ AzureSubscription, ... ]}}
}
```

### YAML
<a name="aws-properties-ssm-cloudconnector-configurationtargets-syntax.yaml"></a>

```
  [Subscriptions](#cfn-ssm-cloudconnector-configurationtargets-subscriptions): {{
    - AzureSubscription}}
```

## Properties
<a name="aws-properties-ssm-cloudconnector-configurationtargets-properties"></a>

`Subscriptions`  <a name="cfn-ssm-cloudconnector-configurationtargets-subscriptions"></a>
A list of Azure subscriptions to target.
*Required*: Yes
*Type*: Array of [AzureSubscription](aws-properties-ssm-cloudconnector-azuresubscription.md)
*Minimum*: `1`
*Maximum*: `75`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
