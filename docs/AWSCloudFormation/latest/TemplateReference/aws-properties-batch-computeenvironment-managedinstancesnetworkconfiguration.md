---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-managedinstancesnetworkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment ManagedInstancesNetworkConfiguration
<a name="aws-properties-batch-computeenvironment-managedinstancesnetworkconfiguration"></a>

<a name="aws-properties-batch-computeenvironment-managedinstancesnetworkconfiguration-description"></a>The `ManagedInstancesNetworkConfiguration` property type specifies Property description not available. for an [AWS::Batch::ComputeEnvironment](aws-resource-batch-computeenvironment.md).

## Syntax
<a name="aws-properties-batch-computeenvironment-managedinstancesnetworkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-managedinstancesnetworkconfiguration-syntax.json"></a>

```
{
  "[SecurityGroups](#cfn-batch-computeenvironment-managedinstancesnetworkconfiguration-securitygroups)" : {{[ String, ... ]}},
  "[Subnets](#cfn-batch-computeenvironment-managedinstancesnetworkconfiguration-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-managedinstancesnetworkconfiguration-syntax.yaml"></a>

```
  [SecurityGroups](#cfn-batch-computeenvironment-managedinstancesnetworkconfiguration-securitygroups): {{
    - String}}
  [Subnets](#cfn-batch-computeenvironment-managedinstancesnetworkconfiguration-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-managedinstancesnetworkconfiguration-properties"></a>

`SecurityGroups`  <a name="cfn-batch-computeenvironment-managedinstancesnetworkconfiguration-securitygroups"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-batch-computeenvironment-managedinstancesnetworkconfiguration-subnets"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
