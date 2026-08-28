---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-privateconnection-connectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::PrivateConnection ConnectionConfiguration
<a name="aws-properties-devopsagent-privateconnection-connectionconfiguration"></a>

The connection configuration for the private connection.

## Syntax
<a name="aws-properties-devopsagent-privateconnection-connectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-privateconnection-connectionconfiguration-syntax.json"></a>

```
{
  "[SelfManaged](#cfn-devopsagent-privateconnection-connectionconfiguration-selfmanaged)" : {{SelfManagedMode}},
  "[ServiceManaged](#cfn-devopsagent-privateconnection-connectionconfiguration-servicemanaged)" : {{ServiceManagedMode}}
}
```

### YAML
<a name="aws-properties-devopsagent-privateconnection-connectionconfiguration-syntax.yaml"></a>

```
  [SelfManaged](#cfn-devopsagent-privateconnection-connectionconfiguration-selfmanaged): {{
    SelfManagedMode}}
  [ServiceManaged](#cfn-devopsagent-privateconnection-connectionconfiguration-servicemanaged): {{
    ServiceManagedMode}}
```

## Properties
<a name="aws-properties-devopsagent-privateconnection-connectionconfiguration-properties"></a>

`SelfManaged`  <a name="cfn-devopsagent-privateconnection-connectionconfiguration-selfmanaged"></a>
Self-managed private connection configuration.
*Required*: No
*Type*: [SelfManagedMode](aws-properties-devopsagent-privateconnection-selfmanagedmode.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceManaged`  <a name="cfn-devopsagent-privateconnection-connectionconfiguration-servicemanaged"></a>
Service-managed private connection configuration.
*Required*: No
*Type*: [ServiceManagedMode](aws-properties-devopsagent-privateconnection-servicemanagedmode.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
