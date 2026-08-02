---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-privateconnection-selfmanagedmode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::PrivateConnection SelfManagedMode
<a name="aws-properties-devopsagent-privateconnection-selfmanagedmode"></a>

<a name="aws-properties-devopsagent-privateconnection-selfmanagedmode-description"></a>The `SelfManagedMode` property type specifies Property description not available. for an [AWS::DevOpsAgent::PrivateConnection](aws-resource-devopsagent-privateconnection.md).

## Syntax
<a name="aws-properties-devopsagent-privateconnection-selfmanagedmode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-privateconnection-selfmanagedmode-syntax.json"></a>

```
{
  "[ResourceConfigurationId](#cfn-devopsagent-privateconnection-selfmanagedmode-resourceconfigurationid)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-privateconnection-selfmanagedmode-syntax.yaml"></a>

```
  [ResourceConfigurationId](#cfn-devopsagent-privateconnection-selfmanagedmode-resourceconfigurationid): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-privateconnection-selfmanagedmode-properties"></a>

`ResourceConfigurationId`  <a name="cfn-devopsagent-privateconnection-selfmanagedmode-resourceconfigurationid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
