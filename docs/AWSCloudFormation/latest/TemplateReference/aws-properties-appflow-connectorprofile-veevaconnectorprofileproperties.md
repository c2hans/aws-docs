---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile VeevaConnectorProfileProperties
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties"></a>

 The connector-specific profile properties required when using Veeva.

## Syntax
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties-syntax.json"></a>

```
{
  "[InstanceUrl](#cfn-appflow-connectorprofile-veevaconnectorprofileproperties-instanceurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties-syntax.yaml"></a>

```
  [InstanceUrl](#cfn-appflow-connectorprofile-veevaconnectorprofileproperties-instanceurl): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties-properties"></a>

`InstanceUrl`  <a name="cfn-appflow-connectorprofile-veevaconnectorprofileproperties-instanceurl"></a>
 The location of the Veeva resource.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties--seealso"></a>
+ [VeevaConnectorProfileProperties](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_VeevaConnectorProfileProperties.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
