---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeregisterScalableTarget.html
---

# DeregisterScalableTarget
<a name="API_DeregisterScalableTarget"></a>

Deregisters an Application Auto Scaling scalable target when you have finished using it. To see which resources have been registered, use [DescribeScalableTargets](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html).

**Note**
Deregistering a scalable target deletes the scaling policies and the scheduled actions that are associated with it.

## Request Syntax
<a name="API_DeregisterScalableTarget_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "ScalableDimension": "{{string}}",
   "ServiceNamespace": "{{string}}"
}
```

## Request Parameters
<a name="API_DeregisterScalableTarget_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceId](#API_DeregisterScalableTarget_RequestSyntax) **   <a name="autoscaling-DeregisterScalableTarget-request-ResourceId"></a>
The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.
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

 ** [ScalableDimension](#API_DeregisterScalableTarget_RequestSyntax) **   <a name="autoscaling-DeregisterScalableTarget-request-ScalableDimension"></a>
The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.
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

 ** [ServiceNamespace](#API_DeregisterScalableTarget_RequestSyntax) **   <a name="autoscaling-DeregisterScalableTarget-request-ServiceNamespace"></a>
The namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use `custom-resource` instead.
Type: String
Valid Values: `ecs | elasticmapreduce | ec2 | appstream | dynamodb | rds | sagemaker | custom-resource | comprehend | lambda | cassandra | kafka | elasticache | neptune | workspaces`
Required: Yes

## Response Elements
<a name="API_DeregisterScalableTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeregisterScalableTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentUpdateException **
Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.
HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an internal error.
HTTP Status Code: 400

 ** ObjectNotFoundException **
The specified object could not be found. For any operation that depends on the existence of a scalable target, this exception is thrown if the scalable target with the specified service namespace, resource ID, and scalable dimension does not exist. For any operation that deletes or deregisters a resource, this exception is thrown if the resource cannot be found.
HTTP Status Code: 400

 ** ValidationException **
An exception was thrown for a validation issue. Review the available parameters for the API request.
HTTP Status Code: 400

## Examples
<a name="API_DeregisterScalableTarget_Examples"></a>

If you plan to create requests manually, you must replace the Authorization header contents in the examples (`AUTHPARAMS`) with a signature. For more information, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the *IAM User Guide*. If you plan to use the [AWS CLI](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/), these tools sign the requests for you.

### Example
<a name="API_DeregisterScalableTarget_Example_1"></a>

The following example deregisters a scalable target for an Amazon ECS service called `web-app` that is running in the `default` cluster.

#### Sample Request
<a name="API_DeregisterScalableTarget_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: application-autoscaling.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
X-Amz-Target: AnyScaleFrontendService.DeregisterScalableTarget
X-Amz-Date: 20190506T210150Z
User-Agent: aws-cli/1.10.23 Python/2.7.11 Darwin/15.4.0 botocore/1.4.8
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "ResourceId": "service/my-cluster/my-service",
    "ServiceNamespace": "ecs",
    "ScalableDimension": "ecs:service:DesiredCount"
}
```

## See Also
<a name="API_DeregisterScalableTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-autoscaling-2016-02-06/DeregisterScalableTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-autoscaling-2016-02-06/DeregisterScalableTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/DeregisterScalableTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-autoscaling-2016-02-06/DeregisterScalableTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/DeregisterScalableTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-autoscaling-2016-02-06/DeregisterScalableTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-autoscaling-2016-02-06/DeregisterScalableTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-autoscaling-2016-02-06/DeregisterScalableTarget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-autoscaling-2016-02-06/DeregisterScalableTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/DeregisterScalableTarget)
