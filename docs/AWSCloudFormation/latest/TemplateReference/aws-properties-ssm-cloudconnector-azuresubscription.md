---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-cloudconnector-azuresubscription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::CloudConnector AzureSubscription
<a name="aws-properties-ssm-cloudconnector-azuresubscription"></a>

Information about an Azure subscription targeted by the cloud connector.

## Syntax
<a name="aws-properties-ssm-cloudconnector-azuresubscription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-cloudconnector-azuresubscription-syntax.json"></a>

```
{
  "[DisplayName](#cfn-ssm-cloudconnector-azuresubscription-displayname)" : {{String}},
  "[Id](#cfn-ssm-cloudconnector-azuresubscription-id)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssm-cloudconnector-azuresubscription-syntax.yaml"></a>

```
  [DisplayName](#cfn-ssm-cloudconnector-azuresubscription-displayname): {{String}}
  [Id](#cfn-ssm-cloudconnector-azuresubscription-id): {{String}}
```

## Properties
<a name="aws-properties-ssm-cloudconnector-azuresubscription-properties"></a>

`DisplayName`  <a name="cfn-ssm-cloudconnector-azuresubscription-displayname"></a>
The display name of the Azure subscription.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-ssm-cloudconnector-azuresubscription-id"></a>
The ID of the Azure subscription.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
