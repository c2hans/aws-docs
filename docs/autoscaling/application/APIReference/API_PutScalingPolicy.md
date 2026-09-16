---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html
---

# PutScalingPolicy
<a name="API_PutScalingPolicy"></a>

Creates or updates a scaling policy for an Application Auto Scaling scalable target.

Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scaling policy applies to the scalable target identified by those three attributes. You cannot create a scaling policy until you have registered the resource as a scalable target.

Multiple scaling policies can be in force at the same time for the same scalable target. You can have one or more target tracking scaling policies, one or more step scaling policies, or both. However, there is a chance that multiple policies could conflict, instructing the scalable target to scale out or in at the same time. Application Auto Scaling gives precedence to the policy that provides the largest capacity for both scale out and scale in. For example, if one policy increases capacity by 3, another policy increases capacity by 200 percent, and the current capacity is 10, Application Auto Scaling uses the policy with the highest calculated capacity (200% of 10 = 20) and scales out to 30.

We recommend caution, however, when using target tracking scaling policies with step scaling policies because conflicts between these policies can cause undesirable behavior. For example, if the step scaling policy initiates a scale-in activity before the target tracking policy is ready to scale in, the scale-in activity will not be blocked. After the scale-in activity completes, the target tracking policy could instruct the scalable target to scale out again.

For more information, see [Target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html), [Step scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html), and [Predictive scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/aas-create-predictive-scaling-policy.html) in the *Application Auto Scaling User Guide*.

**Note**
If a scalable target is deregistered, the scalable target is no longer available to use scaling policies. Any scaling policies that were specified for the scalable target are deleted.

## Request Syntax
<a name="API_PutScalingPolicy_RequestSyntax"></a>

```
{
   "PolicyName": "{{string}}",
   "PolicyType": "{{string}}",
   "PredictiveScalingPolicyConfiguration": {
      "MaxCapacityBreachBehavior": "{{string}}",
      "MaxCapacityBuffer": {{number}},
      "MetricSpecifications": [
         {
            "CustomizedCapacityMetricSpecification": {
               "MetricDataQueries": [
                  {
                     "Expression": "{{string}}",
                     "Id": "{{string}}",
                     "Label": "{{string}}",
                     "MetricStat": {
                        "Metric": {
                           "Dimensions": [
                              {
                                 "Name": "{{string}}",
                                 "Value": "{{string}}"
                              }
                           ],
                           "MetricName": "{{string}}",
                           "Namespace": "{{string}}"
                        },
                        "Stat": "{{string}}",
                        "Unit": "{{string}}"
                     },
                     "ReturnData": {{boolean}}
                  }
               ]
            },
            "CustomizedLoadMetricSpecification": {
               "MetricDataQueries": [
                  {
                     "Expression": "{{string}}",
                     "Id": "{{string}}",
                     "Label": "{{string}}",
                     "MetricStat": {
                        "Metric": {
                           "Dimensions": [
                              {
                                 "Name": "{{string}}",
                                 "Value": "{{string}}"
                              }
                           ],
                           "MetricName": "{{string}}",
                           "Namespace": "{{string}}"
                        },
                        "Stat": "{{string}}",
                        "Unit": "{{string}}"
                     },
                     "ReturnData": {{boolean}}
                  }
               ]
            },
            "CustomizedScalingMetricSpecification": {
               "MetricDataQueries": [
                  {
                     "Expression": "{{string}}",
                     "Id": "{{string}}",
                     "Label": "{{string}}",
                     "MetricStat": {
                        "Metric": {
                           "Dimensions": [
                              {
                                 "Name": "{{string}}",
                                 "Value": "{{string}}"
                              }
                           ],
                           "MetricName": "{{string}}",
                           "Namespace": "{{string}}"
                        },
                        "Stat": "{{string}}",
                        "Unit": "{{string}}"
                     },
                     "ReturnData": {{boolean}}
                  }
               ]
            },
            "PredefinedLoadMetricSpecification": {
               "PredefinedMetricType": "{{string}}",
               "ResourceLabel": "{{string}}"
            },
            "PredefinedMetricPairSpecification": {
               "PredefinedMetricType": "{{string}}",
               "ResourceLabel": "{{string}}"
            },
            "PredefinedScalingMetricSpecification": {
               "PredefinedMetricType": "{{string}}",
               "ResourceLabel": "{{string}}"
            },
            "TargetValue": {{number}}
         }
      ],
      "Mode": "{{string}}",
      "SchedulingBufferTime": {{number}}
   },
   "ResourceId": "{{string}}",
   "ScalableDimension": "{{string}}",
   "ServiceNamespace": "{{string}}",
   "StepScalingPolicyConfiguration": {
      "AdjustmentType": "{{string}}",
      "Cooldown": {{number}},
      "MetricAggregationType": "{{string}}",
      "MinAdjustmentMagnitude": {{number}},
      "StepAdjustments": [
         {
            "MetricIntervalLowerBound": {{number}},
            "MetricIntervalUpperBound": {{number}},
            "ScalingAdjustment": {{number}}
         }
      ]
   },
   "TargetTrackingScalingPolicyConfiguration": {
      "CustomizedMetricSpecification": {
         "Dimensions": [
            {
               "Name": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "MetricName": "{{string}}",
         "Metrics": [
            {
               "Expression": "{{string}}",
               "Id": "{{string}}",
               "Label": "{{string}}",
               "MetricStat": {
                  "Metric": {
                     "Dimensions": [
                        {
                           "Name": "{{string}}",
                           "Value": "{{string}}"
                        }
                     ],
                     "MetricName": "{{string}}",
                     "Namespace": "{{string}}"
                  },
                  "Stat": "{{string}}",
                  "Unit": "{{string}}"
               },
               "ReturnData": {{boolean}}
            }
         ],
         "Namespace": "{{string}}",
         "Statistic": "{{string}}",
         "Unit": "{{string}}"
      },
      "DisableScaleIn": {{boolean}},
      "PredefinedMetricSpecification": {
         "PredefinedMetricType": "{{string}}",
         "ResourceLabel": "{{string}}"
      },
      "ScaleInCooldown": {{number}},
      "ScaleOutCooldown": {{number}},
      "TargetValue": {{number}}
   }
}
```

## Request Parameters
<a name="API_PutScalingPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PolicyName](#API_PutScalingPolicy_RequestSyntax) **   <a name="autoscaling-PutScalingPolicy-request-PolicyName"></a>
The name of the scaling policy.
You cannot change the name of a scaling policy, but you can delete the original scaling policy and create a new scaling policy with the same settings and a different name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\p{Print}+`
Required: Yes

 ** [PolicyType](#API_PutScalingPolicy_RequestSyntax) **   <a name="autoscaling-PutScalingPolicy-request-PolicyType"></a>
The scaling policy type. This parameter is required if you are creating a scaling policy.
The following policy types are supported:
 `TargetTrackingScaling`—Not supported for Amazon EMR.
 `StepScaling`—Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.
 `PredictiveScaling`—Only supported for Amazon ECS.
For more information, see [Target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html), [Step scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html), and [Predictive scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/aas-create-predictive-scaling-policy.html) in the *Application Auto Scaling User Guide*.
Type: String
Valid Values: `StepScaling | TargetTrackingScaling | PredictiveScaling`
Required: No

 ** [PredictiveScalingPolicyConfiguration](#API_PutScalingPolicy_RequestSyntax) **   <a name="autoscaling-PutScalingPolicy-request-PredictiveScalingPolicyConfiguration"></a>
 The configuration of the predictive scaling policy.
Type: [PredictiveScalingPolicyConfiguration](API_PredictiveScalingPolicyConfiguration.md) object
Required: No

 ** [ResourceId](#API_PutScalingPolicy_RequestSyntax) **   <a name="autoscaling-PutScalingPolicy-request-ResourceId"></a>
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

 ** [ScalableDimension](#API_PutScalingPolicy_RequestSyntax) **   <a name="autoscaling-PutScalingPolicy-request-ScalableDimension"></a>
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

 ** [ServiceNamespace](#API_PutScalingPolicy_RequestSyntax) **   <a name="autoscaling-PutScalingPolicy-request-ServiceNamespace"></a>
The namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use `custom-resource` instead.
Type: String
Valid Values: `ecs | elasticmapreduce | ec2 | appstream | dynamodb | rds | sagemaker | custom-resource | comprehend | lambda | cassandra | kafka | elasticache | neptune | workspaces`
Required: Yes

 ** [StepScalingPolicyConfiguration](#API_PutScalingPolicy_RequestSyntax) **   <a name="autoscaling-PutScalingPolicy-request-StepScalingPolicyConfiguration"></a>
A step scaling policy.
This parameter is required if you are creating a policy and the policy type is `StepScaling`.
Type: [StepScalingPolicyConfiguration](API_StepScalingPolicyConfiguration.md) object
Required: No

 ** [TargetTrackingScalingPolicyConfiguration](#API_PutScalingPolicy_RequestSyntax) **   <a name="autoscaling-PutScalingPolicy-request-TargetTrackingScalingPolicyConfiguration"></a>
A target tracking scaling policy. Includes support for predefined or customized metrics.
This parameter is required if you are creating a policy and the policy type is `TargetTrackingScaling`.
Type: [TargetTrackingScalingPolicyConfiguration](API_TargetTrackingScalingPolicyConfiguration.md) object
Required: No

## Response Syntax
<a name="API_PutScalingPolicy_ResponseSyntax"></a>

```
{
   "Alarms": [
      {
         "AlarmARN": "string",
         "AlarmName": "string"
      }
   ],
   "PolicyARN": "string"
}
```

## Response Elements
<a name="API_PutScalingPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Alarms](#API_PutScalingPolicy_ResponseSyntax) **   <a name="autoscaling-PutScalingPolicy-response-Alarms"></a>
The CloudWatch alarms created for the target tracking scaling policy.
Type: Array of [Alarm](API_Alarm.md) objects

 ** [PolicyARN](#API_PutScalingPolicy_ResponseSyntax) **   <a name="autoscaling-PutScalingPolicy-response-PolicyARN"></a>
The Amazon Resource Name (ARN) of the resulting scaling policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_PutScalingPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentUpdateException **
Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.
HTTP Status Code: 400

 ** FailedResourceAccessException **
Failed access to resources caused an exception. This exception is thrown when Application Auto Scaling is unable to retrieve the alarms associated with a scaling policy due to a client error, for example, if the role ARN specified for a scalable target does not have permission to call the CloudWatch [DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) on your behalf.
HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an internal error.
HTTP Status Code: 400

 ** LimitExceededException **
A per-account resource limit is exceeded. For more information, see [Application Auto Scaling service quotas](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-limits.html).
HTTP Status Code: 400

 ** ObjectNotFoundException **
The specified object could not be found. For any operation that depends on the existence of a scalable target, this exception is thrown if the scalable target with the specified service namespace, resource ID, and scalable dimension does not exist. For any operation that deletes or deregisters a resource, this exception is thrown if the resource cannot be found.
HTTP Status Code: 400

 ** ValidationException **
An exception was thrown for a validation issue. Review the available parameters for the API request.
HTTP Status Code: 400

## Examples
<a name="API_PutScalingPolicy_Examples"></a>

If you plan to create requests manually, you must replace the Authorization header contents in the examples (`AUTHPARAMS`) with a signature. For more information, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the *IAM User Guide*. If you plan to use the [AWS CLI](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/), these tools sign the requests for you.

### Example of a target tracking scaling policy
<a name="API_PutScalingPolicy_Example_1"></a>

The following example applies a target tracking scaling policy to an Amazon ECS service called `web-app` in the `default` cluster. The policy keeps the average CPU utilization of the service at 75 percent, with scale-out and scale-in cooldown periods of 60 seconds. The output contains the ARNs and names of the two CloudWatch alarms created on your behalf.

#### Sample Request
<a name="API_PutScalingPolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: application-autoscaling.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
X-Amz-Target: AnyScaleFrontendService.PutScalingPolicy
X-Amz-Date: 20190506T191044Z
User-Agent: aws-cli/1.10.23 Python/2.7.11 Darwin/15.4.0 botocore/1.4.8
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "PolicyName": "cpu75-target-tracking-scaling-policy",
    "PolicyType": "TargetTrackingScaling",
    "TargetTrackingScalingPolicyConfiguration": {
        "TargetValue": 75.0,
        "PredefinedMetricSpecification": {
            "PredefinedMetricType": "ECSServiceAverageCPUUtilization"
        },
        "ScaleOutCooldown": 60,
        "ScaleInCooldown": 60
    },
    "ServiceNamespace": "ecs",
    "ScalableDimension": "ecs:service:DesiredCount",
    "ResourceId": "service/my-cluster/my-service"
}
```

#### Sample Response
<a name="API_PutScalingPolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: [request-id]
Content-Type: application/x-amz-json-1.1
Content-Length: 314
Date: Fri, 06 May 2019 19:10:44 GMT

{
    "PolicyARN": "arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/ecs/service/my-cluster/my-service:policyName/cpu75-target-tracking-scaling-policy",
    "Alarms": [
        {
            "AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:TargetTracking-service/my-cluster/my-service-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca",
            "AlarmName": "TargetTracking-service/my-cluster/my-service-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca"
        },
        {
            "AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:TargetTracking-service/my-cluster/my-service-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d",
            "AlarmName": "TargetTracking-service/my-cluster/my-service-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d"
        }
    ]
}
```

### Example of a step scaling policy for scale out
<a name="API_PutScalingPolicy_Example_2"></a>

The following example applies a step scaling policy to an Amazon ECS service called `web-app` in the `default` cluster. The policy increases the desired count of the service by 200%, with a cooldown period of 60 seconds. The output includes the ARN for the policy, which you use to create the CloudWatch alarm.

#### Sample Request
<a name="API_PutScalingPolicy_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: application-autoscaling.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
X-Amz-Target: AnyScaleFrontendService.PutScalingPolicy
X-Amz-Date: 20190506T191138Z
User-Agent: aws-cli/1.10.23 Python/2.7.11 Darwin/15.4.0 botocore/1.4.8
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "PolicyName": "my-scale-out-policy",
    "PolicyType": "StepScaling",
    "StepScalingPolicyConfiguration": {
        "AdjustmentType": "PercentChangeInCapacity",
        "Cooldown": 60,
        "MetricAggregationType": "Average",
        "StepAdjustments": [
            {
                "ScalingAdjustment": 200,
                "MetricIntervalLowerBound": 0
            }
        ]
    },
    "ServiceNamespace": "ecs",
    "ScalableDimension": "ecs:service:DesiredCount",
    "ResourceId": "service/my-cluster/my-service"
}
```

#### Sample Response
<a name="API_PutScalingPolicy_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: [request-id]
Content-Type: application/x-amz-json-1.1
Content-Length: 175
Date: Fri, 06 May 2019 19:11:38 GMT

{
    "PolicyARN": "arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy:ac542982-cbeb-4294-891c-a5a941dfa787:resource/ecs/service/my-cluster/my-service:policyName/my-scale-out-policy"
}
```

### Example of a step scaling policy for scale in
<a name="API_PutScalingPolicy_Example_3"></a>

The following example applies a step scaling policy to the same Amazon ECS service as in the preceding example. The policy has two step adjustments that decrease the desired count of the service by 25% or 50%, depending on the size of the alarm breach, with a cooldown period of 120 seconds. The output includes the ARN for the policy, which you use to create the CloudWatch alarm.

#### Sample Request
<a name="API_PutScalingPolicy_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: application-autoscaling.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
X-Amz-Target: AnyScaleFrontendService.PutScalingPolicy
X-Amz-Date: 20190506T191152Z
User-Agent: aws-cli/1.10.23 Python/2.7.11 Darwin/15.4.0 botocore/1.4.8
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "PolicyName": "my-scale-in-policy",
    "PolicyType": "StepScaling",
    "StepScalingPolicyConfiguration": {
        "AdjustmentType": "PercentChangeInCapacity",
        "Cooldown": 120,
        "MetricAggregationType": "Average",
        "MinAdjustmentMagnitude": 1,
        "StepAdjustments": [
            {
                "ScalingAdjustment": -25,
                "MetricIntervalLowerBound": -15,
                "MetricIntervalUpperBound": 0
             },
            {
                "ScalingAdjustment": -50,
                "MetricIntervalUpperBound": -15
            }
        ]
    },
    "ServiceNamespace": "ecs",
    "ScalableDimension": "ecs:service:DesiredCount",
    "ResourceId": "service/my-cluster/my-service"
}
```

#### Sample Response
<a name="API_PutScalingPolicy_Example_3_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: [request-id]
Content-Type: application/x-amz-json-1.1
Content-Length: 174
Date: Fri, 06 May 2019 19:11:52 GMT

{
    "PolicyARN": "arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/ecs/service/my-cluster/my-service:policyName/my-scale-in-policy"
}
```

## See Also
<a name="API_PutScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-autoscaling-2016-02-06/PutScalingPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-autoscaling-2016-02-06/PutScalingPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/PutScalingPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-autoscaling-2016-02-06/PutScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/PutScalingPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-autoscaling-2016-02-06/PutScalingPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-autoscaling-2016-02-06/PutScalingPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-autoscaling-2016-02-06/PutScalingPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-autoscaling-2016-02-06/PutScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/PutScalingPolicy)
