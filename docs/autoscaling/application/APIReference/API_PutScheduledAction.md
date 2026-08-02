---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScheduledAction.html
---

# PutScheduledAction
<a name="API_PutScheduledAction"></a>

Creates or updates a scheduled action for an Application Auto Scaling scalable target.

Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scheduled action applies to the scalable target identified by those three attributes. You cannot create a scheduled action until you have registered the resource as a scalable target.

When you specify start and end times with a recurring schedule using a cron expression or rates, they form the boundaries for when the recurring action starts and stops.

To update a scheduled action, specify the parameters that you want to change. If you don't specify start and end times, the old values are deleted.

For more information, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html) in the *Application Auto Scaling User Guide*.

**Note**
If a scalable target is deregistered, the scalable target is no longer available to run scheduled actions. Any scheduled actions that were specified for the scalable target are deleted.

## Request Syntax
<a name="API_PutScheduledAction_RequestSyntax"></a>

```
{
   "EndTime": {{number}},
   "ResourceId": "{{string}}",
   "ScalableDimension": "{{string}}",
   "ScalableTargetAction": {
      "MaxCapacity": {{number}},
      "MinCapacity": {{number}}
   },
   "Schedule": "{{string}}",
   "ScheduledActionName": "{{string}}",
   "ServiceNamespace": "{{string}}",
   "StartTime": {{number}},
   "Timezone": "{{string}}"
}
```

## Request Parameters
<a name="API_PutScheduledAction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndTime](#API_PutScheduledAction_RequestSyntax) **   <a name="autoscaling-PutScheduledAction-request-EndTime"></a>
The date and time for the recurring schedule to end, in UTC.
Type: Timestamp
Required: No

 ** [ResourceId](#API_PutScheduledAction_RequestSyntax) **   <a name="autoscaling-PutScheduledAction-request-ResourceId"></a>
The identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier.
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

 ** [ScalableDimension](#API_PutScheduledAction_RequestSyntax) **   <a name="autoscaling-PutScheduledAction-request-ScalableDimension"></a>
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

 ** [ScalableTargetAction](#API_PutScheduledAction_RequestSyntax) **   <a name="autoscaling-PutScheduledAction-request-ScalableTargetAction"></a>
The new minimum and maximum capacity. You can set both values or just one. At the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity.
Type: [ScalableTargetAction](API_ScalableTargetAction.md) object
Required: No

 ** [Schedule](#API_PutScheduledAction_RequestSyntax) **   <a name="autoscaling-PutScheduledAction-request-Schedule"></a>
The schedule for this action. The following formats are supported:
+ At expressions - "`at(yyyy-mm-ddThh:mm:ss)`"
+ Rate expressions - "`rate(value unit)`"
+ Cron expressions - "`cron(fields)`"
At expressions are useful for one-time schedules. Cron expressions are useful for scheduled actions that run periodically at a specified date and time, and rate expressions are useful for scheduled actions that run at a regular interval.
At and cron expressions use Universal Coordinated Time (UTC) by default.
The cron format consists of six fields separated by white spaces: [Minutes] [Hours] [Day\_of\_Month] [Month] [Day\_of\_Week] [Year].
For rate expressions, *value* is a positive integer and *unit* is `minute` \| `minutes` \| `hour` \| `hours` \| `day` \| `days`.
For more information, see [Schedule recurring scaling actions using cron expressions](https://docs.aws.amazon.com/autoscaling/application/userguide/scheduled-scaling-using-cron-expressions.html) in the *Application Auto Scaling User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [ScheduledActionName](#API_PutScheduledAction_RequestSyntax) **   <a name="autoscaling-PutScheduledAction-request-ScheduledActionName"></a>
The name of the scheduled action. This name must be unique among all other scheduled actions on the specified scalable target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(?!((^[ ]+.*)|(.*([\u0000-\u001f]|[\u007f-\u009f]|[:/|])+.*)|(.*[ ]+$))).+`
Required: Yes

 ** [ServiceNamespace](#API_PutScheduledAction_RequestSyntax) **   <a name="autoscaling-PutScheduledAction-request-ServiceNamespace"></a>
The namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use `custom-resource` instead.
Type: String
Valid Values: `ecs | elasticmapreduce | ec2 | appstream | dynamodb | rds | sagemaker | custom-resource | comprehend | lambda | cassandra | kafka | elasticache | neptune | workspaces`
Required: Yes

 ** [StartTime](#API_PutScheduledAction_RequestSyntax) **   <a name="autoscaling-PutScheduledAction-request-StartTime"></a>
The date and time for this scheduled action to start, in UTC.
Type: Timestamp
Required: No

 ** [Timezone](#API_PutScheduledAction_RequestSyntax) **   <a name="autoscaling-PutScheduledAction-request-Timezone"></a>
Specifies the time zone used when setting a scheduled action by using an at or cron expression. If a time zone is not provided, UTC is used by default.
Valid values are the canonical names of the IANA time zones supported by Joda-Time (such as `Etc/GMT+9` or `Pacific/Tahiti`). For more information, see [https://www.joda.org/joda-time/timezones.html](https://www.joda.org/joda-time/timezones.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Response Elements
<a name="API_PutScheduledAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutScheduledAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentUpdateException **
Concurrent updates caused an exception, for example, if you request an update to an Application Auto Scaling resource that already has a pending update.
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
<a name="API_PutScheduledAction_Examples"></a>

If you plan to create requests manually, you must replace the Authorization header contents in the examples (`AUTHPARAMS`) with a signature. For more information, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the *IAM User Guide*. If you plan to use the [AWS CLI](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/), these tools sign the requests for you.

### Example of a scheduled action
<a name="API_PutScheduledAction_Example_1"></a>

This example adds a scheduled action to a DynamoDB table called `TestTable` to scale out on a recurring schedule. On the specified schedule (every day at 12:15pm UTC), if the current capacity is below the value specified for `MinCapacity`, Application Auto Scaling scales out to the value specified by `MinCapacity`.

#### Sample Request
<a name="API_PutScheduledAction_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: application-autoscaling.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
X-Amz-Target: AnyScaleFrontendService.PutScheduledAction
X-Amz-Date: 20190506T191138Z
User-Agent: aws-cli/1.10.23 Python/2.7.11 Darwin/15.4.0 botocore/1.4.8
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "ScheduledActionName": "my-recurring-action",
    "Schedule": "cron(15 12 * * ? *)",
    "ScalableTargetAction": {
        "MinCapacity": 6
    },
    "ServiceNamespace": "dynamodb",
    "ScalableDimension": "dynamodb:table:WriteCapacityUnits",
    "ResourceId": "table/TestTable"
}
```

## See Also
<a name="API_PutScheduledAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-autoscaling-2016-02-06/PutScheduledAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-autoscaling-2016-02-06/PutScheduledAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/PutScheduledAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-autoscaling-2016-02-06/PutScheduledAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/PutScheduledAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-autoscaling-2016-02-06/PutScheduledAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-autoscaling-2016-02-06/PutScheduledAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-autoscaling-2016-02-06/PutScheduledAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-autoscaling-2016-02-06/PutScheduledAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/PutScheduledAction)
