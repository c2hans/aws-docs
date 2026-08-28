---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-connector-connectorhealth.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Connector ConnectorHealth
<a name="aws-properties-inspectorv2-connector-connectorhealth"></a>

<a name="aws-properties-inspectorv2-connector-connectorhealth-description"></a>The `ConnectorHealth` property type specifies Property description not available. for an [AWS::InspectorV2::Connector](aws-resource-inspectorv2-connector.md).

## Syntax
<a name="aws-properties-inspectorv2-connector-connectorhealth-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-connector-connectorhealth-syntax.json"></a>

```
{
  "[ConnectorStatus](#cfn-inspectorv2-connector-connectorhealth-connectorstatus)" : {{String}},
  "[LastCheckedAt](#cfn-inspectorv2-connector-connectorhealth-lastcheckedat)" : {{String}},
  "[Message](#cfn-inspectorv2-connector-connectorhealth-message)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspectorv2-connector-connectorhealth-syntax.yaml"></a>

```
  [ConnectorStatus](#cfn-inspectorv2-connector-connectorhealth-connectorstatus): {{String}}
  [LastCheckedAt](#cfn-inspectorv2-connector-connectorhealth-lastcheckedat): {{String}}
  [Message](#cfn-inspectorv2-connector-connectorhealth-message): {{String}}
```

## Properties
<a name="aws-properties-inspectorv2-connector-connectorhealth-properties"></a>

`ConnectorStatus`  <a name="cfn-inspectorv2-connector-connectorhealth-connectorstatus"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `CONNECTED | DEGRADED | FAILED_TO_CONNECT | PENDING_AUTHORIZATION | PENDING_CONFIGURATION | UNKNOWN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastCheckedAt`  <a name="cfn-inspectorv2-connector-connectorhealth-lastcheckedat"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Message`  <a name="cfn-inspectorv2-connector-connectorhealth-message"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
