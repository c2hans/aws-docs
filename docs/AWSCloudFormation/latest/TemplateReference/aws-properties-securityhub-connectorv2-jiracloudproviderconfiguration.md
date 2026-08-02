---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-connectorv2-jiracloudproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConnectorV2 JiraCloudProviderConfiguration
<a name="aws-properties-securityhub-connectorv2-jiracloudproviderconfiguration"></a>

The initial configuration settings required to establish an integration between Security Hub and Jira Cloud.

## Syntax
<a name="aws-properties-securityhub-connectorv2-jiracloudproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-connectorv2-jiracloudproviderconfiguration-syntax.json"></a>

```
{
  "[ProjectKey](#cfn-securityhub-connectorv2-jiracloudproviderconfiguration-projectkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-connectorv2-jiracloudproviderconfiguration-syntax.yaml"></a>

```
  [ProjectKey](#cfn-securityhub-connectorv2-jiracloudproviderconfiguration-projectkey): {{String}}
```

## Properties
<a name="aws-properties-securityhub-connectorv2-jiracloudproviderconfiguration-properties"></a>

`ProjectKey`  <a name="cfn-securityhub-connectorv2-jiracloudproviderconfiguration-projectkey"></a>
The project key for a JiraCloud instance.
*Required*: Yes
*Type*: String
*Minimum*: `2`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
