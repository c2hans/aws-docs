---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ExecutionBlockConfiguration.html
---

# ExecutionBlockConfiguration
<a name="API_ExecutionBlockConfiguration"></a>

Execution block configurations for a workflow in a Region switch plan. An execution block represents a specific type of action to perform during a Region switch.

## Contents
<a name="API_ExecutionBlockConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** arcRoutingControlConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-arcRoutingControlConfig"></a>
An ARC routing control execution block.
Type: [ArcRoutingControlConfiguration](API_ArcRoutingControlConfiguration.md) object
Required: No

 ** auroraProvisionedScalingConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-auroraProvisionedScalingConfig"></a>
An Aurora provisioned cluster scaling execution block.
Type: [AuroraProvisionedScalingConfiguration](API_AuroraProvisionedScalingConfiguration.md) object
Required: No

 ** auroraServerlessScalingConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-auroraServerlessScalingConfig"></a>
An Aurora Serverless scaling execution block.
Type: [AuroraServerlessScalingConfiguration](API_AuroraServerlessScalingConfiguration.md) object
Required: No

 ** customActionLambdaConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-customActionLambdaConfig"></a>
An AWS Lambda execution block.
Type: [CustomActionLambdaConfiguration](API_CustomActionLambdaConfiguration.md) object
Required: No

 ** documentDbConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-documentDbConfig"></a>
Configuration for Amazon DocumentDB global clusters used in a Region switch plan.
Type: [DocumentDbConfiguration](API_DocumentDbConfiguration.md) object
Required: No

 ** ec2AsgCapacityIncreaseConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-ec2AsgCapacityIncreaseConfig"></a>
An EC2 Auto Scaling group execution block.
Type: [Ec2AsgCapacityIncreaseConfiguration](API_Ec2AsgCapacityIncreaseConfiguration.md) object
Required: No

 ** ecsCapacityIncreaseConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-ecsCapacityIncreaseConfig"></a>
The capacity increase specified for the configuration.
Type: [EcsCapacityIncreaseConfiguration](API_EcsCapacityIncreaseConfiguration.md) object
Required: No

 ** eksResourceScalingConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-eksResourceScalingConfig"></a>
An AWS EKS resource scaling execution block.
Type: [EksResourceScalingConfiguration](API_EksResourceScalingConfiguration.md) object
Required: No

 ** executionApprovalConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-executionApprovalConfig"></a>
A manual approval execution block.
Type: [ExecutionApprovalConfiguration](API_ExecutionApprovalConfiguration.md) object
Required: No

 ** globalAuroraConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-globalAuroraConfig"></a>
An Aurora Global Database execution block.
Type: [GlobalAuroraConfiguration](API_GlobalAuroraConfiguration.md) object
Required: No

 ** lambdaEventSourceMappingConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-lambdaEventSourceMappingConfig"></a>
A Lambda event source mapping execution block.
Type: [LambdaEventSourceMappingConfiguration](API_LambdaEventSourceMappingConfiguration.md) object
Required: No

 ** neptuneGlobalDatabaseConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-neptuneGlobalDatabaseConfig"></a>
A Neptune global database execution block.
Type: [NeptuneGlobalDatabaseConfiguration](API_NeptuneGlobalDatabaseConfiguration.md) object
Required: No

 ** parallelConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-parallelConfig"></a>
A parallel configuration execution block.
Type: [ParallelExecutionBlockConfiguration](API_ParallelExecutionBlockConfiguration.md) object
Required: No

 ** rdsCreateCrossRegionReadReplicaConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-rdsCreateCrossRegionReadReplicaConfig"></a>
An Amazon RDS create cross-Region replica execution block.
Type: [RdsCreateCrossRegionReplicaConfiguration](API_RdsCreateCrossRegionReplicaConfiguration.md) object
Required: No

 ** rdsPromoteReadReplicaConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-rdsPromoteReadReplicaConfig"></a>
An Amazon RDS promote read replica execution block.
Type: [RdsPromoteReadReplicaConfiguration](API_RdsPromoteReadReplicaConfiguration.md) object
Required: No

 ** regionSwitchPlanConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-regionSwitchPlanConfig"></a>
A Region switch plan execution block.
Type: [RegionSwitchPlanConfiguration](API_RegionSwitchPlanConfiguration.md) object
Required: No

 ** route53HealthCheckConfig **   <a name="regionswitch-Type-ExecutionBlockConfiguration-route53HealthCheckConfig"></a>
The Amazon Route 53 health check configuration.
Type: [Route53HealthCheckConfiguration](API_Route53HealthCheckConfiguration.md) object
Required: No

## See Also
<a name="API_ExecutionBlockConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ExecutionBlockConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ExecutionBlockConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ExecutionBlockConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
