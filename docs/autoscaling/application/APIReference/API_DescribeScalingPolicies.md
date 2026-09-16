---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalingPolicies.html
---

# DescribeScalingPolicies
<a name="API_DescribeScalingPolicies"></a>

Describes the Application Auto Scaling scaling policies for the specified service namespace.

You can filter the results using `ResourceId`, `ScalableDimension`, and `PolicyNames`.

For more information, see [Target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) and [Step scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) in the *Application Auto Scaling User Guide*.

## Request Syntax
<a name="API_DescribeScalingPolicies_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PolicyNames": [ "{{string}}" ],
   "ResourceId": "{{string}}",
   "ScalableDimension": "{{string}}",
   "ServiceNamespace": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeScalingPolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeScalingPolicies_RequestSyntax) **   <a name="autoscaling-DescribeScalingPolicies-request-MaxResults"></a>
The maximum number of scalable targets. This value can be between 1 and 10. The default value is 10.
If this parameter is used, the operation returns up to `MaxResults` results at a time, along with a `NextToken` value. To get the next set of results, include the `NextToken` value in a subsequent call. If this parameter is not used, the operation returns up to 10 results and a `NextToken` value, if applicable.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeScalingPolicies_RequestSyntax) **   <a name="autoscaling-DescribeScalingPolicies-request-NextToken"></a>
The token for the next set of results.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [PolicyNames](#API_DescribeScalingPolicies_RequestSyntax) **   <a name="autoscaling-DescribeScalingPolicies-request-PolicyNames"></a>
The names of the scaling policies to describe.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [ResourceId](#API_DescribeScalingPolicies_RequestSyntax) **   <a name="autoscaling-DescribeScalingPolicies-request-ResourceId"></a>
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
Required: No

 ** [ScalableDimension](#API_DescribeScalingPolicies_RequestSyntax) **   <a name="autoscaling-DescribeScalingPolicies-request-ScalableDimension"></a>
The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.
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
Required: No

 ** [ServiceNamespace](#API_DescribeScalingPolicies_RequestSyntax) **   <a name="autoscaling-DescribeScalingPolicies-request-ServiceNamespace"></a>
The namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use `custom-resource` instead.
Type: String
Valid Values: `ecs | elasticmapreduce | ec2 | appstream | dynamodb | rds | sagemaker | custom-resource | comprehend | lambda | cassandra | kafka | elasticache | neptune | workspaces`
Required: Yes

## Response Syntax
<a name="API_DescribeScalingPolicies_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ScalingPolicies": [
      {
         "Alarms": [
            {
               "AlarmARN": "string",
               "AlarmName": "string"
            }
         ],
         "CreationTime": number,
         "PolicyARN": "string",
         "PolicyName": "string",
         "PolicyType": "string",
         "PredictiveScalingPolicyConfiguration": {
            "MaxCapacityBreachBehavior": "string",
            "MaxCapacityBuffer": number,
            "MetricSpecifications": [
               {
                  "CustomizedCapacityMetricSpecification": {
                     "MetricDataQueries": [
                        {
                           "Expression": "string",
                           "Id": "string",
                           "Label": "string",
                           "MetricStat": {
                              "Metric": {
                                 "Dimensions": [
                                    {
                                       "Name": "string",
                                       "Value": "string"
                                    }
                                 ],
                                 "MetricName": "string",
                                 "Namespace": "string"
                              },
                              "Stat": "string",
                              "Unit": "string"
                           },
                           "ReturnData": boolean
                        }
                     ]
                  },
                  "CustomizedLoadMetricSpecification": {
                     "MetricDataQueries": [
                        {
                           "Expression": "string",
                           "Id": "string",
                           "Label": "string",
                           "MetricStat": {
                              "Metric": {
                                 "Dimensions": [
                                    {
                                       "Name": "string",
                                       "Value": "string"
                                    }
                                 ],
                                 "MetricName": "string",
                                 "Namespace": "string"
                              },
                              "Stat": "string",
                              "Unit": "string"
                           },
                           "ReturnData": boolean
                        }
                     ]
                  },
                  "CustomizedScalingMetricSpecification": {
                     "MetricDataQueries": [
                        {
                           "Expression": "string",
                           "Id": "string",
                           "Label": "string",
                           "MetricStat": {
                              "Metric": {
                                 "Dimensions": [
                                    {
                                       "Name": "string",
                                       "Value": "string"
                                    }
                                 ],
                                 "MetricName": "string",
                                 "Namespace": "string"
                              },
                              "Stat": "string",
                              "Unit": "string"
                           },
                           "ReturnData": boolean
                        }
                     ]
                  },
                  "PredefinedLoadMetricSpecification": {
                     "PredefinedMetricType": "string",
                     "ResourceLabel": "string"
                  },
                  "PredefinedMetricPairSpecification": {
                     "PredefinedMetricType": "string",
                     "ResourceLabel": "string"
                  },
                  "PredefinedScalingMetricSpecification": {
                     "PredefinedMetricType": "string",
                     "ResourceLabel": "string"
                  },
                  "TargetValue": number
               }
            ],
            "Mode": "string",
            "SchedulingBufferTime": number
         },
         "ResourceId": "string",
         "ScalableDimension": "string",
         "ServiceNamespace": "string",
         "StepScalingPolicyConfiguration": {
            "AdjustmentType": "string",
            "Cooldown": number,
            "MetricAggregationType": "string",
            "MinAdjustmentMagnitude": number,
            "StepAdjustments": [
               {
                  "MetricIntervalLowerBound": number,
                  "MetricIntervalUpperBound": number,
                  "ScalingAdjustment": number
               }
            ]
         },
         "TargetTrackingScalingPolicyConfiguration": {
            "CustomizedMetricSpecification": {
               "Dimensions": [
                  {
                     "Name": "string",
                     "Value": "string"
                  }
               ],
               "MetricName": "string",
               "Metrics": [
                  {
                     "Expression": "string",
                     "Id": "string",
                     "Label": "string",
                     "MetricStat": {
                        "Metric": {
                           "Dimensions": [
                              {
                                 "Name": "string",
                                 "Value": "string"
                              }
                           ],
                           "MetricName": "string",
                           "Namespace": "string"
                        },
                        "Stat": "string",
                        "Unit": "string"
                     },
                     "ReturnData": boolean
                  }
               ],
               "Namespace": "string",
               "Statistic": "string",
               "Unit": "string"
            },
            "DisableScaleIn": boolean,
            "PredefinedMetricSpecification": {
               "PredefinedMetricType": "string",
               "ResourceLabel": "string"
            },
            "ScaleInCooldown": number,
            "ScaleOutCooldown": number,
            "TargetValue": number
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeScalingPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeScalingPolicies_ResponseSyntax) **   <a name="autoscaling-DescribeScalingPolicies-response-NextToken"></a>
The token required to get the next set of results. This value is `null` if there are no more results to return.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 ** [ScalingPolicies](#API_DescribeScalingPolicies_ResponseSyntax) **   <a name="autoscaling-DescribeScalingPolicies-response-ScalingPolicies"></a>
Information about the scaling policies.
Type: Array of [ScalingPolicy](API_ScalingPolicy.md) objects

## Errors
<a name="API_DescribeScalingPolicies_Errors"></a>

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

 ** InvalidNextTokenException **
The next token supplied was invalid.
HTTP Status Code: 400

 ** ValidationException **
An exception was thrown for a validation issue. Review the available parameters for the API request.
HTTP Status Code: 400

## Examples
<a name="API_DescribeScalingPolicies_Examples"></a>

If you plan to create requests manually, you must replace the Authorization header contents in the examples (`AUTHPARAMS`) with a signature. For more information, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the *IAM User Guide*. If you plan to use the [AWS CLI](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/), these tools sign the requests for you.

### Example
<a name="API_DescribeScalingPolicies_Example_1"></a>

The following example describes the scaling policies for the `ecs` service namespace.

#### Sample Request
<a name="API_DescribeScalingPolicies_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: application-autoscaling.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
X-Amz-Target: AnyScaleFrontendService.DescribeScalingPolicies
X-Amz-Date: 20190506T194435Z
User-Agent: aws-cli/1.10.23 Python/2.7.11 Darwin/15.4.0 botocore/1.4.8
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "ServiceNamespace": "ecs"
}
```

#### Sample Response
<a name="API_DescribeScalingPolicies_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: [request-id]
Content-Type: application/x-amz-json-1.1
Content-Length: 1393
Date: Fri, 06 May 2019 19:44:35 GMT

{
    "ScalingPolicies": [
        {
            "Alarms": [
                {
                    "AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:step-scaling-alarmhigh-ecs:service/my-cluster/my-service",
                    "AlarmName": "Step-Scaling-AlarmHigh-ECS:service/my-cluster/my-service"
                }
            ],
            "CreationTime": 1462561899.23,
            "PolicyARN": "arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy:ac542982-cbeb-4294-891c-a5a941dfa787:resource/ecs/service/my-cluster/my-service:policyName/my-scale-out-policy",
            "PolicyName": "my-scale-out-policy",
            "PolicyType": "StepScaling",
            "ResourceId": "service/my-cluster/my-service",
            "ScalableDimension": "ecs:service:DesiredCount",
            "ServiceNamespace": "ecs",
            "StepScalingPolicyConfiguration": {
                "AdjustmentType": "PercentChangeInCapacity",
                "Cooldown": 60,
                "MetricAggregationType": "Average",
                "StepAdjustments": [
                    {
                        "MetricIntervalLowerBound": 0,
                        "ScalingAdjustment": 200
                    }
                ]
            }
        },
        {
            "Alarms": [
                {
                    "AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:step-scaling-alarmlow-ecs:service/my-cluster/my-service",
                    "AlarmName": "Step-Scaling-AlarmLow-ECS:service/my-cluster/my-service"
                }
            ],
            "CreationTime": 1462562575.099,
            "PolicyARN": "arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/ecs/service/my-cluster/my-service:policyName/my-scale-in-policy",
            "PolicyName": "my-scale-in-policy",
            "PolicyType": "StepScaling",
            "ResourceId": "service/my-cluster/my-service",
            "ScalableDimension": "ecs:service:DesiredCount",
            "ServiceNamespace": "ecs",
            "StepScalingPolicyConfiguration": {
                "AdjustmentType": "PercentChangeInCapacity",
                "Cooldown": 120,
                "MetricAggregationType": "Average",
                "MinAdjustmentMagnitude": 1,
                "StepAdjustments": [
                    {
                        "MetricIntervalLowerBound": -15,
                        "MetricIntervalUpperBound": 0
                        "ScalingAdjustment": -25,
                    },
                    {
                        "MetricIntervalUpperBound": -15,
                        "ScalingAdjustment": -50
                    }
                ]
            }
        }
    ]
}
```

## See Also
<a name="API_DescribeScalingPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-autoscaling-2016-02-06/DescribeScalingPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-autoscaling-2016-02-06/DescribeScalingPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/DescribeScalingPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-autoscaling-2016-02-06/DescribeScalingPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/DescribeScalingPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-autoscaling-2016-02-06/DescribeScalingPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-autoscaling-2016-02-06/DescribeScalingPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-autoscaling-2016-02-06/DescribeScalingPolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-autoscaling-2016-02-06/DescribeScalingPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/DescribeScalingPolicies)
