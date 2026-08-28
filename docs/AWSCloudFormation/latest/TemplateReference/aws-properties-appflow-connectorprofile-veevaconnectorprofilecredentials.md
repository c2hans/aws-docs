---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile VeevaConnectorProfileCredentials
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials"></a>

 The connector-specific profile credentials required when using Veeva.

## Syntax
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials-syntax.json"></a>

```
{
  "[Password](#cfn-appflow-connectorprofile-veevaconnectorprofilecredentials-password)" : {{String}},
  "[Username](#cfn-appflow-connectorprofile-veevaconnectorprofilecredentials-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials-syntax.yaml"></a>

```
  [Password](#cfn-appflow-connectorprofile-veevaconnectorprofilecredentials-password): {{String}}
  [Username](#cfn-appflow-connectorprofile-veevaconnectorprofilecredentials-username): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials-properties"></a>

`Password`  <a name="cfn-appflow-connectorprofile-veevaconnectorprofilecredentials-password"></a>
 The password that corresponds to the user name.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-appflow-connectorprofile-veevaconnectorprofilecredentials-username"></a>
 The name of the user.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials--seealso"></a>
+ [VeevaConnectorProfileCredentials](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_VeevaConnectorProfileCredentials.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
