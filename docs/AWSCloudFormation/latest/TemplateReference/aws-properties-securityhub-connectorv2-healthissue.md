---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-connectorv2-healthissue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConnectorV2 HealthIssue
<a name="aws-properties-securityhub-connectorv2-healthissue"></a>

Represents a specific health issue detected for a connector.

## Syntax
<a name="aws-properties-securityhub-connectorv2-healthissue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-connectorv2-healthissue-syntax.json"></a>

```
{
  "[Code](#cfn-securityhub-connectorv2-healthissue-code)" : {{String}},
  "[Message](#cfn-securityhub-connectorv2-healthissue-message)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-connectorv2-healthissue-syntax.yaml"></a>

```
  [Code](#cfn-securityhub-connectorv2-healthissue-code): {{String}}
  [Message](#cfn-securityhub-connectorv2-healthissue-message): {{String}}
```

## Properties
<a name="aws-properties-securityhub-connectorv2-healthissue-properties"></a>

`Code`  <a name="cfn-securityhub-connectorv2-healthissue-code"></a>
The error code that identifies the type of health issue.
*Required*: Yes
*Type*: String
*Allowed values*: `AUTHENTICATION_FAILURE | STREAM_AUTHORIZATION_FAILURE | DISCOVERY_FAILURE | STREAM_LIMIT_EXCEEDED | STREAM_DISCONNECTED | RECORDING_FAILURE | NO_HEALTH_DATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Message`  <a name="cfn-securityhub-connectorv2-healthissue-message"></a>
A human-readable message that describes the health issue.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
