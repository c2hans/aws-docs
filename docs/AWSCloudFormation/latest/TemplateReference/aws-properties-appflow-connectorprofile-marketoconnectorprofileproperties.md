---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile MarketoConnectorProfileProperties
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties"></a>

 The connector-specific profile properties required when using Marketo.

## Syntax
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties-syntax.json"></a>

```
{
  "[InstanceUrl](#cfn-appflow-connectorprofile-marketoconnectorprofileproperties-instanceurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties-syntax.yaml"></a>

```
  [InstanceUrl](#cfn-appflow-connectorprofile-marketoconnectorprofileproperties-instanceurl): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties-properties"></a>

`InstanceUrl`  <a name="cfn-appflow-connectorprofile-marketoconnectorprofileproperties-instanceurl"></a>
 The location of the Marketo resource.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties--seealso"></a>
+ [MarketoConnectorProfileProperties](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_MarketoConnectorProfileProperties.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
