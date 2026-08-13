---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-managedinstancesprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment ManagedInstancesProvider
<a name="aws-properties-batch-computeenvironment-managedinstancesprovider"></a>

<a name="aws-properties-batch-computeenvironment-managedinstancesprovider-description"></a>The `ManagedInstancesProvider` property type specifies Property description not available. for an [AWS::Batch::ComputeEnvironment](aws-resource-batch-computeenvironment.md).

## Syntax
<a name="aws-properties-batch-computeenvironment-managedinstancesprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-managedinstancesprovider-syntax.json"></a>

```
{
  "[InfrastructureOptimization](#cfn-batch-computeenvironment-managedinstancesprovider-infrastructureoptimization)" : {{InfrastructureOptimization}},
  "[InfrastructureRoleArn](#cfn-batch-computeenvironment-managedinstancesprovider-infrastructurerolearn)" : {{String}},
  "[InstanceLaunchTemplate](#cfn-batch-computeenvironment-managedinstancesprovider-instancelaunchtemplate)" : {{InstanceLaunchTemplate}},
  "[PropagateTags](#cfn-batch-computeenvironment-managedinstancesprovider-propagatetags)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-managedinstancesprovider-syntax.yaml"></a>

```
  [InfrastructureOptimization](#cfn-batch-computeenvironment-managedinstancesprovider-infrastructureoptimization): {{
    InfrastructureOptimization}}
  [InfrastructureRoleArn](#cfn-batch-computeenvironment-managedinstancesprovider-infrastructurerolearn): {{String}}
  [InstanceLaunchTemplate](#cfn-batch-computeenvironment-managedinstancesprovider-instancelaunchtemplate): {{
    InstanceLaunchTemplate}}
  [PropagateTags](#cfn-batch-computeenvironment-managedinstancesprovider-propagatetags): {{String}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-managedinstancesprovider-properties"></a>

`InfrastructureOptimization`  <a name="cfn-batch-computeenvironment-managedinstancesprovider-infrastructureoptimization"></a>
Property description not available.
*Required*: No
*Type*: [InfrastructureOptimization](aws-properties-batch-computeenvironment-infrastructureoptimization.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InfrastructureRoleArn`  <a name="cfn-batch-computeenvironment-managedinstancesprovider-infrastructurerolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceLaunchTemplate`  <a name="cfn-batch-computeenvironment-managedinstancesprovider-instancelaunchtemplate"></a>
Property description not available.
*Required*: Yes
*Type*: [InstanceLaunchTemplate](aws-properties-batch-computeenvironment-instancelaunchtemplate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropagateTags`  <a name="cfn-batch-computeenvironment-managedinstancesprovider-propagatetags"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `CAPACITY_PROVIDER | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
