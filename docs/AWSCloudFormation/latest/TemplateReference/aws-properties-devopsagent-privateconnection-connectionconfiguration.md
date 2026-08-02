---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-privateconnection-connectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::PrivateConnection ConnectionConfiguration
<a name="aws-properties-devopsagent-privateconnection-connectionconfiguration"></a>

<a name="aws-properties-devopsagent-privateconnection-connectionconfiguration-description"></a>The `ConnectionConfiguration` property type specifies Property description not available. for an [AWS::DevOpsAgent::PrivateConnection](aws-resource-devopsagent-privateconnection.md).

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
Property description not available.
*Required*: No
*Type*: [SelfManagedMode](aws-properties-devopsagent-privateconnection-selfmanagedmode.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceManaged`  <a name="cfn-devopsagent-privateconnection-connectionconfiguration-servicemanaged"></a>
Property description not available.
*Required*: No
*Type*: [ServiceManagedMode](aws-properties-devopsagent-privateconnection-servicemanagedmode.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
