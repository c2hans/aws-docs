---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-executionblockconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan ExecutionBlockConfiguration
<a name="aws-properties-arcregionswitch-plan-executionblockconfiguration"></a>

Execution block configurations for a workflow in a Region switch plan. An execution block represents a specific type of action to perform during a Region switch.

## Syntax
<a name="aws-properties-arcregionswitch-plan-executionblockconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-executionblockconfiguration-syntax.json"></a>

```
{
  "[ArcRoutingControlConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-arcroutingcontrolconfig)" : {{ArcRoutingControlConfiguration}},
  "[AuroraProvisionedScalingConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-auroraprovisionedscalingconfig)" : {{AuroraProvisionedScalingConfiguration}},
  "[AuroraServerlessScalingConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-auroraserverlessscalingconfig)" : {{AuroraServerlessScalingConfiguration}},
  "[CustomActionLambdaConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-customactionlambdaconfig)" : {{CustomActionLambdaConfiguration}},
  "[DocumentDbConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-documentdbconfig)" : {{DocumentDbConfiguration}},
  "[Ec2AsgCapacityIncreaseConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-ec2asgcapacityincreaseconfig)" : {{Ec2AsgCapacityIncreaseConfiguration}},
  "[EcsCapacityIncreaseConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-ecscapacityincreaseconfig)" : {{EcsCapacityIncreaseConfiguration}},
  "[EksResourceScalingConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-eksresourcescalingconfig)" : {{EksResourceScalingConfiguration}},
  "[ExecutionApprovalConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-executionapprovalconfig)" : {{ExecutionApprovalConfiguration}},
  "[GlobalAuroraConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-globalauroraconfig)" : {{GlobalAuroraConfiguration}},
  "[LambdaEventSourceMappingConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-lambdaeventsourcemappingconfig)" : {{LambdaEventSourceMappingConfiguration}},
  "[NeptuneGlobalDatabaseConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-neptuneglobaldatabaseconfig)" : {{NeptuneGlobalDatabaseConfiguration}},
  "[ParallelConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-parallelconfig)" : {{ParallelExecutionBlockConfiguration}},
  "[RdsCreateCrossRegionReadReplicaConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-rdscreatecrossregionreadreplicaconfig)" : {{RdsCreateCrossRegionReplicaConfiguration}},
  "[RdsPromoteReadReplicaConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-rdspromotereadreplicaconfig)" : {{RdsPromoteReadReplicaConfiguration}},
  "[RegionSwitchPlanConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-regionswitchplanconfig)" : {{RegionSwitchPlanConfiguration}},
  "[Route53HealthCheckConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-route53healthcheckconfig)" : {{Route53HealthCheckConfiguration}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-executionblockconfiguration-syntax.yaml"></a>

```
  [ArcRoutingControlConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-arcroutingcontrolconfig): {{
    ArcRoutingControlConfiguration}}
  [AuroraProvisionedScalingConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-auroraprovisionedscalingconfig): {{
    AuroraProvisionedScalingConfiguration}}
  [AuroraServerlessScalingConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-auroraserverlessscalingconfig): {{
    AuroraServerlessScalingConfiguration}}
  [CustomActionLambdaConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-customactionlambdaconfig): {{
    CustomActionLambdaConfiguration}}
  [DocumentDbConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-documentdbconfig): {{
    DocumentDbConfiguration}}
  [Ec2AsgCapacityIncreaseConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-ec2asgcapacityincreaseconfig): {{
    Ec2AsgCapacityIncreaseConfiguration}}
  [EcsCapacityIncreaseConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-ecscapacityincreaseconfig): {{
    EcsCapacityIncreaseConfiguration}}
  [EksResourceScalingConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-eksresourcescalingconfig): {{
    EksResourceScalingConfiguration}}
  [ExecutionApprovalConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-executionapprovalconfig): {{
    ExecutionApprovalConfiguration}}
  [GlobalAuroraConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-globalauroraconfig): {{
    GlobalAuroraConfiguration}}
  [LambdaEventSourceMappingConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-lambdaeventsourcemappingconfig): {{
    LambdaEventSourceMappingConfiguration}}
  [NeptuneGlobalDatabaseConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-neptuneglobaldatabaseconfig): {{
    NeptuneGlobalDatabaseConfiguration}}
  [ParallelConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-parallelconfig): {{
    ParallelExecutionBlockConfiguration}}
  [RdsCreateCrossRegionReadReplicaConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-rdscreatecrossregionreadreplicaconfig): {{
    RdsCreateCrossRegionReplicaConfiguration}}
  [RdsPromoteReadReplicaConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-rdspromotereadreplicaconfig): {{
    RdsPromoteReadReplicaConfiguration}}
  [RegionSwitchPlanConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-regionswitchplanconfig): {{
    RegionSwitchPlanConfiguration}}
  [Route53HealthCheckConfig](#cfn-arcregionswitch-plan-executionblockconfiguration-route53healthcheckconfig): {{
    Route53HealthCheckConfiguration}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-executionblockconfiguration-properties"></a>

`ArcRoutingControlConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-arcroutingcontrolconfig"></a>
An ARC routing control execution block.
*Required*: No
*Type*: [ArcRoutingControlConfiguration](aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuroraProvisionedScalingConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-auroraprovisionedscalingconfig"></a>
An Aurora provisioned cluster scaling execution block.
*Required*: No
*Type*: [AuroraProvisionedScalingConfiguration](aws-properties-arcregionswitch-plan-auroraprovisionedscalingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuroraServerlessScalingConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-auroraserverlessscalingconfig"></a>
An Aurora Serverless scaling execution block.
*Required*: No
*Type*: [AuroraServerlessScalingConfiguration](aws-properties-arcregionswitch-plan-auroraserverlessscalingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomActionLambdaConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-customactionlambdaconfig"></a>
An AWS Lambda execution block.
*Required*: No
*Type*: [CustomActionLambdaConfiguration](aws-properties-arcregionswitch-plan-customactionlambdaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentDbConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-documentdbconfig"></a>
Property description not available.
*Required*: No
*Type*: [DocumentDbConfiguration](aws-properties-arcregionswitch-plan-documentdbconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ec2AsgCapacityIncreaseConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-ec2asgcapacityincreaseconfig"></a>
An EC2 Auto Scaling group execution block.
*Required*: No
*Type*: [Ec2AsgCapacityIncreaseConfiguration](aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EcsCapacityIncreaseConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-ecscapacityincreaseconfig"></a>
The capacity increase specified for the configuration.
*Required*: No
*Type*: [EcsCapacityIncreaseConfiguration](aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EksResourceScalingConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-eksresourcescalingconfig"></a>
An AWS EKS resource scaling execution block.
*Required*: No
*Type*: [EksResourceScalingConfiguration](aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionApprovalConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-executionapprovalconfig"></a>
A manual approval execution block.
*Required*: No
*Type*: [ExecutionApprovalConfiguration](aws-properties-arcregionswitch-plan-executionapprovalconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalAuroraConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-globalauroraconfig"></a>
An Aurora Global Database execution block.
*Required*: No
*Type*: [GlobalAuroraConfiguration](aws-properties-arcregionswitch-plan-globalauroraconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaEventSourceMappingConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-lambdaeventsourcemappingconfig"></a>
A Lambda event source mapping execution block.
*Required*: No
*Type*: [LambdaEventSourceMappingConfiguration](aws-properties-arcregionswitch-plan-lambdaeventsourcemappingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NeptuneGlobalDatabaseConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-neptuneglobaldatabaseconfig"></a>
A Neptune global database execution block.
*Required*: No
*Type*: [NeptuneGlobalDatabaseConfiguration](aws-properties-arcregionswitch-plan-neptuneglobaldatabaseconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParallelConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-parallelconfig"></a>
A parallel configuration execution block.
*Required*: No
*Type*: [ParallelExecutionBlockConfiguration](aws-properties-arcregionswitch-plan-parallelexecutionblockconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RdsCreateCrossRegionReadReplicaConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-rdscreatecrossregionreadreplicaconfig"></a>
An Amazon RDS create cross-Region replica execution block.
*Required*: No
*Type*: [RdsCreateCrossRegionReplicaConfiguration](aws-properties-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RdsPromoteReadReplicaConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-rdspromotereadreplicaconfig"></a>
An Amazon RDS promote read replica execution block.
*Required*: No
*Type*: [RdsPromoteReadReplicaConfiguration](aws-properties-arcregionswitch-plan-rdspromotereadreplicaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionSwitchPlanConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-regionswitchplanconfig"></a>
A Region switch plan execution block.
*Required*: No
*Type*: [RegionSwitchPlanConfiguration](aws-properties-arcregionswitch-plan-regionswitchplanconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Route53HealthCheckConfig`  <a name="cfn-arcregionswitch-plan-executionblockconfiguration-route53healthcheckconfig"></a>
The Amazon Route 53 health check configuration.
*Required*: No
*Type*: [Route53HealthCheckConfiguration](aws-properties-arcregionswitch-plan-route53healthcheckconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
