---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/security-iam-awsmanpol.html
---

# AWS managed policies for Application Auto Scaling
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: WorkSpaces Applications and CloudWatch
<a name="appstream-policy"></a>

**Policy name: [AWSApplicationAutoscalingAppStreamFleetPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingAppStreamFleetPolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_AppStreamFleet](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call Amazon AppStream and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on all related resources ("Resource": "\*"):
+ Action: `appstream:DescribeFleets`
+ Action: `appstream:UpdateFleet`
+ Action: `cloudwatch:DescribeAlarms`
+ Action: `cloudwatch:PutMetricAlarm`
+ Action: `cloudwatch:DeleteAlarms`

## AWS managed policy: Aurora and CloudWatch
<a name="aurora-policy"></a>

**Policy name: [AWSApplicationAutoscalingRDSClusterPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingRDSClusterPolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_RDSCluster](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call Aurora and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on all related resources ("Resource": "\*"):
+ Action: `rds:AddTagsToResource`
+ Action: `rds:CreateDBInstance`
+ Action: `rds:DeleteDBInstance`
+ Action: `rds:DescribeDBClusters`
+ Action: `rds:DescribeDBInstance`
+ Action: `cloudwatch:DescribeAlarms`
+ Action: `cloudwatch:PutMetricAlarm`
+ Action: `cloudwatch:DeleteAlarms`

## AWS managed policy: Amazon Comprehend and CloudWatch
<a name="comprehend-policy"></a>

**Policy name: [AWSApplicationAutoscalingComprehendEndpointPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingComprehendEndpointPolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_ComprehendEndpoint](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call Amazon Comprehend and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on all related resources ("Resource": "\*"):
+ Action: `comprehend:UpdateEndpoint`
+ Action: `comprehend:DescribeEndpoint`
+ Action: `cloudwatch:DescribeAlarms`
+ Action: `cloudwatch:PutMetricAlarm`
+ Action: `cloudwatch:DeleteAlarms`

## AWS managed policy: DynamoDB and CloudWatch
<a name="ddb-policy"></a>

**Policy name: [AWSApplicationAutoscalingDynamoDBTablePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingDynamoDBTablePolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_DynamoDBTable](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call DynamoDBand CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on all related resources ("Resource": "\*"):
+ Action: `dynamodb:DescribeTable`
+ Action: `dynamodb:UpdateTable`
+ Action: `cloudwatch:DescribeAlarms`
+ Action: `cloudwatch:PutMetricAlarm`
+ Action: `cloudwatch:DeleteAlarms`

## AWS managed policy: Amazon ECS and CloudWatch
<a name="ecs-policy"></a>

**Policy name: [AWSApplicationAutoscalingECSServicePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingECSServicePolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_ECSService](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call Amazon ECS and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on all related resources ("Resource": "\*"):
+ Action: `ecs:DescribeServices`
+ Action: `ecs:DescribeServiceRevisions`
+ Action: `ecs:UpdateService`
+ Action: `cloudwatch:PutMetricAlarm`
+ Action: `cloudwatch:DescribeAlarms`
+ Action: `cloudwatch:GetMetricData`
+ Action: `cloudwatch:DeleteAlarms`

## AWS managed policy: ElastiCache and CloudWatch
<a name="elasticache-policy"></a>

**Policy name: [AWSApplicationAutoscalingElastiCacheRGPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingElastiCacheRGPolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_ElastiCacheRG](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call ElastiCache and CloudWatch and perform scaling on your behalf. This service-linked role can be used for ElastiCache Memcached, Redis OSS, and Valkey.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on the specified resources:
+ Action: `elasticache:DescribeReplicationGroups` on all resources
+ Action: `elasticache:ModifyReplicationGroupShardConfiguration` on all resources
+ Action: `elasticache:IncreaseReplicaCount` on all resources
+ Action: `elasticache:DecreaseReplicaCount` on all resources
+ Action: `elasticache:DescribeCacheClusters` on all resources
+ Action: `elasticache:DescribeCacheParameters` on all resources
+ Action: `elasticache:ModifyCacheCluster` on all resources
+ Action: `cloudwatch:DescribeAlarms` on the resource `arn:aws:cloudwatch:*:*:alarm:*`
+ Action: `cloudwatch:PutMetricAlarm` on the resource `arn:aws:cloudwatch:*:*:alarm:TargetTracking*`
+ Action: `cloudwatch:DeleteAlarms` on the resource `arn:aws:cloudwatch:*:*:alarm:TargetTracking*`

## AWS managed policy: Amazon Keyspaces and CloudWatch
<a name="keyspaces-policy"></a>

**Policy name: [AWSApplicationAutoscalingCassandraTablePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingCassandraTablePolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_CassandraTable](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call Amazon Keyspaces and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on the specified resources:
+ Action: `cassandra:Select` on the following resources:
  + `arn:*:cassandra:*:*:/keyspace/system/table/*`
  + `arn:*:cassandra:*:*:/keyspace/system_schema/table/*`
  + `arn:*:cassandra:*:*:/keyspace/system_schema_mcs/table/*`
+ Action: `cassandra:Alter` on all resources
+ Action: `cloudwatch:DescribeAlarms` on all resources
+ Action: `cloudwatch:PutMetricAlarm` on all resources
+ Action: `cloudwatch:DeleteAlarms` on all resources

## AWS managed policy: Lambda and CloudWatch
<a name="lambda-policy"></a>

**Policy name: [AWSApplicationAutoscalingLambdaConcurrencyPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingLambdaConcurrencyPolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_LambdaConcurrency](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call Lambda and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on all related resources ("Resource": "\*"):
+ Action: `lambda:PutProvisionedConcurrencyConfig`
+ Action: `lambda:GetProvisionedConcurrencyConfig`
+ Action: `lambda:DeleteProvisionedConcurrencyConfig`
+ Action: `cloudwatch:DescribeAlarms`
+ Action: `cloudwatch:PutMetricAlarm`
+ Action: `cloudwatch:DeleteAlarms`

## AWS managed policy: Amazon MSK and CloudWatch
<a name="msk-policy"></a>

**Policy name: [AWSApplicationAutoscalingKafkaClusterPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingKafkaClusterPolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_KafkaCluster](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call Amazon MSK and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on all related resources ("Resource": "\*"):
+ Action: `kafka:DescribeCluster`
+ Action: `kafka:DescribeClusterOperation`
+ Action: `kafka:UpdateBrokerStorage`
+ Action: `cloudwatch:DescribeAlarms`
+ Action: `cloudwatch:PutMetricAlarm`
+ Action: `cloudwatch:DeleteAlarms`

## AWS managed policy: Neptune and CloudWatch
<a name="neptune-policy"></a>

**Policy name: [AWSApplicationAutoscalingNeptuneClusterPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingNeptuneClusterPolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_NeptuneCluster](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call Neptune and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on the specified resources:
+ Action: `rds:ListTagsForResource` on all resources
+ Action: `rds:DescribeDBInstances` on all resources
+ Action: `rds:DescribeDBClusters` on all resources
+ Action: `rds:DescribeDBClusterParameters` on all resources
+ Action: `cloudwatch:DescribeAlarms` on all resources
+ Action: `rds:AddTagsToResource` on resources with the prefix *autoscaled-reader* in the Amazon Neptune database engine (`"Condition":{"StringEquals":{"rds:DatabaseEngine":"neptune"}`)
+ Action: `rds:CreateDBInstance` on resources with the prefix *autoscaled-reader* in all DB clusters (`"Resource":"arn:*:rds:*:*:db:autoscaled-reader*", "arn:aws:rds:*:*:cluster:*"`) in the Amazon Neptune database engine (`"Condition":{"StringEquals":{"rds:DatabaseEngine":"neptune"}`)
+ Action: `rds:DeleteDBInstance` on the resource `arn:aws:rds:*:*:db:autoscaled-reader*`
+ Action: `cloudwatch:PutMetricAlarm` on the resource `arn:aws:cloudwatch:*:*:alarm:TargetTracking*`
+ Action: `cloudwatch:DeleteAlarms` on the resource `arn:aws:cloudwatch:*:*:alarm:TargetTracking*`

## AWS managed policy: SageMaker AI and CloudWatch
<a name="sagemaker-policy"></a>

**Policy name: [AWSApplicationAutoscalingSageMakerEndpointPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingSageMakerEndpointPolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_SageMakerEndpoint](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call SageMaker AI and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on the specified resources:
+ Action: `sagemaker:DescribeEndpoint` on all resources
+ Action: `sagemaker:DescribeEndpointConfig` on all resources
+ Action: `sagemaker:DescribeInferenceComponent` on all resources
+ Action: `sagemaker:UpdateEndpointWeightsAndCapacities` on all resources
+ Action: `sagemaker:UpdateInferenceComponentRuntimeConfig` on all resources
+ Action: `cloudwatch:DescribeAlarms` on all resources
+ Action: `cloudwatch:GetMetricData` on all resources
+ Action: `cloudwatch:PutMetricAlarm` on the resource `arn:aws:cloudwatch:*:*:alarm:TargetTracking*`
+ Action: `cloudwatch:DeleteAlarms` on the resource `arn:aws:cloudwatch:*:*:alarm:TargetTracking*`

## AWS managed policy: EC2 Spot Fleet and CloudWatch
<a name="spot-policy"></a>

**Policy name: [AWSApplicationAutoscalingEC2SpotFleetRequestPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingEC2SpotFleetRequestPolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_EC2SpotFleetRequest](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call Amazon EC2 and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on all related resources ("Resource": "\*"):
+ Action: `ec2:DescribeSpotFleetRequests`
+ Action: `ec2:ModifySpotFleetRequest`
+ Action: `cloudwatch:DescribeAlarms`
+ Action: `cloudwatch:PutMetricAlarm`
+ Action: `cloudwatch:DeleteAlarms`

## AWS managed policy: WorkSpaces and CloudWatch
<a name="workspaces-policy"></a>

**Policy name: [AWSApplicationAutoscalingWorkSpacesPoolPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingWorkSpacesPoolPolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_WorkSpacesPool](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call WorkSpaces and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on the specified resources:
+ Action: `workspaces:DescribeWorkspacesPools` on all resources from the same account as the SLR
+ Action: `workspaces:UpdateWorkspacesPool` on all resources from the same account as the SLR
+ Action: `cloudwatch:DescribeAlarms` on all alarms from the same account as the SLR
+ Action: `cloudwatch:PutMetricAlarm` on all alarms from the same account as the SLR, where the alarm name starts with TargetTracking
+ Action: `cloudwatch:DeleteAlarms` on all alarms from the same account as the SLR, where the alarm name starts with TargetTracking

## AWS managed policy: custom resources and CloudWatch
<a name="custom-resources-policy"></a>

**Policy name: [AWSApplicationAutoScalingCustomResourcePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoScalingCustomResourcePolicy.html)**
This policy is attached to the service-linked role named [AWSServiceRoleForApplicationAutoScaling\_CustomResource](application-auto-scaling-service-linked-roles.md) to allow Application Auto Scaling to call your custom resources that are available through API Gateway and CloudWatch and perform scaling on your behalf.

**Permission details**

The permissions policy allows Application Auto Scaling to complete the following actions on all related resources ("Resource": "\*"):
+ Action: `execute-api:Invoke`
+ Action: `cloudwatch:DescribeAlarms`
+ Action: `cloudwatch:PutMetricAlarm`
+ Action: `cloudwatch:DeleteAlarms`

## Application Auto Scaling updates to AWS managed policies
<a name="policy-updates"></a>

View details about updates to AWS managed policies for Application Auto Scaling since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Application Auto Scaling Document history page.

| Change | Description | Date |
| --- | --- | --- |
| [AWSApplicationAutoscalingECSServicePolicy](#ecs-policy) – Update an existing policy | Added permission to call the Amazon ECS `DescribeServiceRevisions` API action to verify service configuration for high-resolution scaling. | May 20, 2026 |
| [AWSApplicationAutoscalingElastiCacheRGPolicy](#elasticache-policy) – Update an existing policy | Added permission to call the ElastiCache `ModifyCacheCluster` API action to support Memcached automatic scaling. | April 10, 2025 |
| [AWSApplicationAutoscalingECSServicePolicy](#ecs-policy) – Update an existing policy | Added permission to call the CloudWatch `GetMetricData` API action to support predictive scaling. | November 21, 2024 |
| [AWSApplicationAutoscalingWorkSpacesPoolPolicy](#workspaces-policy) – New policy | Added a managed policy for Amazon WorkSpaces. This policy is attached to a [service-linked role](application-auto-scaling-service-linked-roles.md) that allows Application Auto Scaling to call WorkSpaces and CloudWatch and perform scaling on your behalf. | June 24, 2024 |
| [AWSApplicationAutoscalingSageMakerEndpointPolicy](#sagemaker-policy) – Update to an existing policy | Added permissions to call the SageMaker AI `DescribeInferenceComponent` and `UpdateInferenceComponentRuntimeConfig` API actions to support compatibility for the auto scaling of SageMaker AI resources for an upcoming integration. The policy also now restricts the CloudWatch `PutMetricAlarm` and `DeleteAlarms` API actions to CloudWatch alarms that are used with target tracking scaling policies. | November 13, 2023 |
| [AWSApplicationAutoscalingNeptuneClusterPolicy](#neptune-policy) – New policy | Added a managed policy for Neptune. This policy is attached to a [service-linked role](application-auto-scaling-service-linked-roles.md) that allows Application Auto Scaling to call Neptune and CloudWatch and perform scaling on your behalf. | October 6, 2021 |
| [AWSApplicationAutoscalingRDSClusterPolicy](#aurora-policy) – New policy | Added a managed policy for ElastiCache. This policy is attached to a [service-linked role](application-auto-scaling-service-linked-roles.md) that allows Application Auto Scaling to call ElastiCache and CloudWatch and perform scaling on your behalf. | August 19, 2021 |
| Application Auto Scaling started tracking changes | Application Auto Scaling started tracking changes for its AWS managed policies. | August 19, 2021 |
