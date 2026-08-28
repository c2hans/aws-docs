---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile InforNexusConnectorProfileProperties
<a name="aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties"></a>

 The connector-specific profile properties required by Infor Nexus.

## Syntax
<a name="aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties-syntax.json"></a>

```
{
  "[InstanceUrl](#cfn-appflow-connectorprofile-infornexusconnectorprofileproperties-instanceurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties-syntax.yaml"></a>

```
  [InstanceUrl](#cfn-appflow-connectorprofile-infornexusconnectorprofileproperties-instanceurl): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties-properties"></a>

`InstanceUrl`  <a name="cfn-appflow-connectorprofile-infornexusconnectorprofileproperties-instanceurl"></a>
 The location of the Infor Nexus resource.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties--seealso"></a>
+ [InforNexusConnectorProfileProperties](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_InforNexusConnectorProfileProperties.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
