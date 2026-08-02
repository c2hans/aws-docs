---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScalingPolicy.html
---

# ScalingPolicy
<a name="API_ScalingPolicy"></a>

Represents a scaling policy to use with Application Auto Scaling.

For more information about configuring scaling policies for a specific service, see [AWS services that you can use with Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/integrated-services-list.html) in the *Application Auto Scaling User Guide*.

## Contents
<a name="API_ScalingPolicy_Contents"></a>

 ** CreationTime **   <a name="autoscaling-Type-ScalingPolicy-CreationTime"></a>
The Unix timestamp for when the scaling policy was created.
Type: Timestamp
Required: Yes

 ** PolicyARN **   <a name="autoscaling-Type-ScalingPolicy-PolicyARN"></a>
The Amazon Resource Name (ARN) of the scaling policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** PolicyName **   <a name="autoscaling-Type-ScalingPolicy-PolicyName"></a>
The name of the scaling policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\p{Print}+`
Required: Yes

 ** PolicyType **   <a name="autoscaling-Type-ScalingPolicy-PolicyType"></a>
The scaling policy type.
The following policy types are supported:
 `TargetTrackingScaling`—Not supported for Amazon EMR
 `StepScaling`—Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.
 `PredictiveScaling`—Only supported for Amazon ECS
Type: String
Valid Values: `StepScaling | TargetTrackingScaling | PredictiveScaling`
Required: Yes

 ** ResourceId **   <a name="autoscaling-Type-ScalingPolicy-ResourceId"></a>
The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.
+ ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/my-cluster/my-service`.
+ Spot Fleet - The resource type is `spot-fleet-request` and the unique identifier is the Spot Fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.
+ EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.
+ AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.
+ DynamoDB table - The resource type is `table` and the unique identifier is the table name. Example: `table/my-table`.
+ DynamoDB global secondary index - The resource type is `index` and the unique identifier is the index name. Example: `table/my-table/index/my-table-index`.
+ Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.
+ SageMaker endpoint variant - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.
+ Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our [GitHub repository](https://github.com/aws/aws-auto-scaling-custom-resource).
+ Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: `arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`.
+ Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: `arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`.
+ Lambda provisioned concurrency - The resource type is `function` and the unique identifier is the function name with a function version or alias name suffix that is not `$LATEST`. Example: `function:my-function:prod` or `function:my-function:1`.
+ Amazon Keyspaces table - The resource type is `table` and the unique identifier is the table name. Example: `keyspace/mykeyspace/table/mytable`.
+ Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: `arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`.
+ Amazon ElastiCache replication group - The resource type is `replication-group` and the unique identifier is the replication group name. Example: `replication-group/mycluster`.
+ Amazon ElastiCache cache cluster - The resource type is `cache-cluster` and the unique identifier is the cache cluster name. Example: `cache-cluster/mycluster`.
+ Neptune cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:mycluster`.
+ SageMaker serverless endpoint - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.
+ SageMaker inference component - The resource type is `inference-component` and the unique identifier is the resource ID. Example: `inference-component/my-inference-component`.
+ Pool of WorkSpaces - The resource type is `workspacespool` and the unique identifier is the pool ID. Example: `workspacespool/wspool-123456`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** ScalableDimension **   <a name="autoscaling-Type-ScalingPolicy-ScalableDimension"></a>
The scalable dimension. This string consists of the service namespace, resource type, and scaling property.
+  `ecs:service:DesiredCount` - The task count of an ECS service.
+  `elasticmapreduce:instancegroup:InstanceCount` - The instance count of an EMR Instance Group.
+  `ec2:spot-fleet-request:TargetCapacity` - The target capacity of a Spot Fleet.
+  `appstream:fleet:DesiredCapacity` - The capacity of an AppStream 2.0 fleet.
+  `dynamodb:table:ReadCapacityUnits` - The provisioned read capacity for a DynamoDB table.
+  `dynamodb:table:WriteCapacityUnits` - The provisioned write capacity for a DynamoDB table.
+  `dynamodb:index:ReadCapacityUnits` - The provisioned read capacity for a DynamoDB global secondary index.
+  `dynamodb:index:WriteCapacityUnits` - The provisioned write capacity for a DynamoDB global secondary index.
+  `rds:cluster:ReadReplicaCount` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
+  `sagemaker:variant:DesiredInstanceCount` - The number of EC2 instances for a SageMaker model endpoint variant.
+  `custom-resource:ResourceType:Property` - The scalable dimension for a custom resource provided by your own application or service.
+  `comprehend:document-classifier-endpoint:DesiredInferenceUnits` - The number of inference units for an Amazon Comprehend document classification endpoint.
+  `comprehend:entity-recognizer-endpoint:DesiredInferenceUnits` - The number of inference units for an Amazon Comprehend entity recognizer endpoint.
+  `lambda:function:ProvisionedConcurrency` - The provisioned concurrency for a Lambda function.
+  `cassandra:table:ReadCapacityUnits` - The provisioned read capacity for an Amazon Keyspaces table.
+  `cassandra:table:WriteCapacityUnits` - The provisioned write capacity for an Amazon Keyspaces table.
+  `kafka:broker-storage:VolumeSize` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.
+  `elasticache:cache-cluster:Nodes` - The number of nodes for an Amazon ElastiCache cache cluster.
+  `elasticache:replication-group:NodeGroups` - The number of node groups for an Amazon ElastiCache replication group.
+  `elasticache:replication-group:Replicas` - The number of replicas per node group for an Amazon ElastiCache replication group.
+  `neptune:cluster:ReadReplicaCount` - The count of read replicas in an Amazon Neptune DB cluster.
+  `sagemaker:variant:DesiredProvisionedConcurrency` - The provisioned concurrency for a SageMaker serverless endpoint.
+  `sagemaker:inference-component:DesiredCopyCount` - The number of copies across an endpoint for a SageMaker inference component.
+  `workspaces:workspacespool:DesiredUserSessions` - The number of user sessions for the WorkSpaces in the pool.
Type: String
Valid Values: `ecs:service:DesiredCount | ec2:spot-fleet-request:TargetCapacity | elasticmapreduce:instancegroup:InstanceCount | appstream:fleet:DesiredCapacity | dynamodb:table:ReadCapacityUnits | dynamodb:table:WriteCapacityUnits | dynamodb:index:ReadCapacityUnits | dynamodb:index:WriteCapacityUnits | rds:cluster:ReadReplicaCount | sagemaker:variant:DesiredInstanceCount | custom-resource:ResourceType:Property | comprehend:document-classifier-endpoint:DesiredInferenceUnits | comprehend:entity-recognizer-endpoint:DesiredInferenceUnits | lambda:function:ProvisionedConcurrency | cassandra:table:ReadCapacityUnits | cassandra:table:WriteCapacityUnits | kafka:broker-storage:VolumeSize | elasticache:cache-cluster:Nodes | elasticache:replication-group:NodeGroups | elasticache:replication-group:Replicas | neptune:cluster:ReadReplicaCount | sagemaker:variant:DesiredProvisionedConcurrency | sagemaker:inference-component:DesiredCopyCount | workspaces:workspacespool:DesiredUserSessions`
Required: Yes

 ** ServiceNamespace **   <a name="autoscaling-Type-ScalingPolicy-ServiceNamespace"></a>
The namespace of the AWS service that provides the resource, or a `custom-resource`.
Type: String
Valid Values: `ecs | elasticmapreduce | ec2 | appstream | dynamodb | rds | sagemaker | custom-resource | comprehend | lambda | cassandra | kafka | elasticache | neptune | workspaces`
Required: Yes

 ** Alarms **   <a name="autoscaling-Type-ScalingPolicy-Alarms"></a>
The CloudWatch alarms associated with the scaling policy.
Type: Array of [Alarm](API_Alarm.md) objects
Required: No

 ** PredictiveScalingPolicyConfiguration **   <a name="autoscaling-Type-ScalingPolicy-PredictiveScalingPolicyConfiguration"></a>
 The predictive scaling policy configuration.
Type: [PredictiveScalingPolicyConfiguration](API_PredictiveScalingPolicyConfiguration.md) object
Required: No

 ** StepScalingPolicyConfiguration **   <a name="autoscaling-Type-ScalingPolicy-StepScalingPolicyConfiguration"></a>
A step scaling policy.
Type: [StepScalingPolicyConfiguration](API_StepScalingPolicyConfiguration.md) object
Required: No

 ** TargetTrackingScalingPolicyConfiguration **   <a name="autoscaling-Type-ScalingPolicy-TargetTrackingScalingPolicyConfiguration"></a>
A target tracking scaling policy.
Type: [TargetTrackingScalingPolicyConfiguration](API_TargetTrackingScalingPolicyConfiguration.md) object
Required: No

## See Also
<a name="API_ScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/ScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/ScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/ScalingPolicy)
