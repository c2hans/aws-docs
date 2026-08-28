---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile PardotConnectorProfileProperties
<a name="aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties"></a>

The connector-specific profile properties required when using Salesforce Pardot.

## Syntax
<a name="aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties-syntax.json"></a>

```
{
  "[BusinessUnitId](#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-businessunitid)" : {{String}},
  "[InstanceUrl](#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-instanceurl)" : {{String}},
  "[IsSandboxEnvironment](#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-issandboxenvironment)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties-syntax.yaml"></a>

```
  [BusinessUnitId](#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-businessunitid): {{String}}
  [InstanceUrl](#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-instanceurl): {{String}}
  [IsSandboxEnvironment](#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-issandboxenvironment): {{Boolean}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties-properties"></a>

`BusinessUnitId`  <a name="cfn-appflow-connectorprofile-pardotconnectorprofileproperties-businessunitid"></a>
The business unit id of Salesforce Pardot instance.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `18`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceUrl`  <a name="cfn-appflow-connectorprofile-pardotconnectorprofileproperties-instanceurl"></a>
The location of the Salesforce Pardot resource.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsSandboxEnvironment`  <a name="cfn-appflow-connectorprofile-pardotconnectorprofileproperties-issandboxenvironment"></a>
Indicates whether the connector profile applies to a sandbox or production environment.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
