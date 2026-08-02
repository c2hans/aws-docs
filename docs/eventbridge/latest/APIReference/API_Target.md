---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Target.html
---

# Target
<a name="API_Target"></a>

Targets are the resources to be invoked when a rule is triggered. For a complete list of services and resources that can be set as a target, see [PutTargets](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutTargets.html).

If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a `RoleArn` with proper permissions in the `Target` structure. For more information, see [Sending and Receiving Events Between AWS Accounts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html) in the *Amazon EventBridge User Guide*.

## Contents
<a name="API_Target_Contents"></a>

 ** Arn **   <a name="eventbridge-Type-Target-Arn"></a>
The Amazon Resource Name (ARN) of the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: Yes

 ** Id **   <a name="eventbridge-Type-Target-Id"></a>
The ID of the target within the specified rule. Use this ID to reference the target when updating the rule. We recommend using a memorable and unique string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

 ** AppSyncParameters **   <a name="eventbridge-Type-Target-AppSyncParameters"></a>
Contains the GraphQL operation to be parsed and executed, if the event target is an AWS AppSync API.
Type: [AppSyncParameters](API_AppSyncParameters.md) object
Required: No

 ** BatchParameters **   <a name="eventbridge-Type-Target-BatchParameters"></a>
If the event target is an AWS Batch job, this contains the job definition, job name, and other parameters. For more information, see [Jobs](https://docs.aws.amazon.com/batch/latest/userguide/jobs.html) in the * AWS Batch User Guide*.
Type: [BatchParameters](API_BatchParameters.md) object
Required: No

 ** DeadLetterConfig **   <a name="eventbridge-Type-Target-DeadLetterConfig"></a>
The `DeadLetterConfig` that defines the target queue to send dead-letter queue events to.
Type: [DeadLetterConfig](API_DeadLetterConfig.md) object
Required: No

 ** EcsParameters **   <a name="eventbridge-Type-Target-EcsParameters"></a>
Contains the Amazon ECS task definition and task count to be used, if the event target is an Amazon ECS task. For more information about Amazon ECS tasks, see [Task Definitions ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html) in the *Amazon EC2 Container Service Developer Guide*.
Type: [EcsParameters](API_EcsParameters.md) object
Required: No

 ** HttpParameters **   <a name="eventbridge-Type-Target-HttpParameters"></a>
Contains the HTTP parameters to use when the target is a API Gateway endpoint or EventBridge ApiDestination.
If you specify an API Gateway API or EventBridge ApiDestination as a target, you can use this parameter to specify headers, path parameters, and query string keys/values as part of your target invoking request. If you're using ApiDestinations, the corresponding Connection can also have these values configured. In case of any conflicting keys, values from the Connection take precedence.
Type: [HttpParameters](API_HttpParameters.md) object
Required: No

 ** Input **   <a name="eventbridge-Type-Target-Input"></a>
Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see [The JavaScript Object Notation (JSON) Data Interchange Format](http://www.rfc-editor.org/rfc/rfc7159.txt).
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** InputPath **   <a name="eventbridge-Type-Target-InputPath"></a>
The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You may use JSON dot notation or bracket notation. For more information about JSON paths, see [JSONPath](http://goessner.net/articles/JsonPath/).
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** InputTransformer **   <a name="eventbridge-Type-Target-InputTransformer"></a>
Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that data to send customized input to the target.
Type: [InputTransformer](API_InputTransformer.md) object
Required: No

 ** KinesisParameters **   <a name="eventbridge-Type-Target-KinesisParameters"></a>
The custom parameter you can use to control the shard assignment, when the target is a Kinesis data stream. If you do not include this parameter, the default is to use the `eventId` as the partition key.
Type: [KinesisParameters](API_KinesisParameters.md) object
Required: No

 ** RedshiftDataParameters **   <a name="eventbridge-Type-Target-RedshiftDataParameters"></a>
Contains the Amazon Redshift Data API parameters to use when the target is a Amazon Redshift cluster.
If you specify a Amazon Redshift Cluster as a Target, you can use this to specify parameters to invoke the Amazon Redshift Data API ExecuteStatement based on EventBridge events.
Type: [RedshiftDataParameters](API_RedshiftDataParameters.md) object
Required: No

 ** RetryPolicy **   <a name="eventbridge-Type-Target-RetryPolicy"></a>
The retry policy configuration to use for the dead-letter queue.
Type: [RetryPolicy](API_RetryPolicy.md) object
Required: No

 ** RoleArn **   <a name="eventbridge-Type-Target-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** RunCommandParameters **   <a name="eventbridge-Type-Target-RunCommandParameters"></a>
Parameters used when you are using the rule to invoke Amazon EC2 Run Command.
Type: [RunCommandParameters](API_RunCommandParameters.md) object
Required: No

 ** SageMakerPipelineParameters **   <a name="eventbridge-Type-Target-SageMakerPipelineParameters"></a>
Contains the SageMaker AI Model Building Pipeline parameters to start execution of a SageMaker AI Model Building Pipeline.
If you specify a SageMaker AI Model Building Pipeline as a target, you can use this to specify parameters to start a pipeline execution based on EventBridge events.
Type: [SageMakerPipelineParameters](API_SageMakerPipelineParameters.md) object
Required: No

 ** SqsParameters **   <a name="eventbridge-Type-Target-SqsParameters"></a>
Contains the message group ID to use when the target is an Amazon SQS fair or FIFO queue.
If you specify a fair or FIFO queue as a target, the queue must have content-based deduplication enabled.
Type: [SqsParameters](API_SqsParameters.md) object
Required: No

## See Also
<a name="API_Target_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/Target)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/Target)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/Target)
