---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-privateconnection-selfmanagedmode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::PrivateConnection SelfManagedMode
<a name="aws-properties-devopsagent-privateconnection-selfmanagedmode"></a>

Configuration for a private connection that uses an existing Amazon VPC Lattice resource configuration that you manage.

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
The Amazon Resource Name (ARN) of the Amazon VPC Lattice resource configuration that points to the target service.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
