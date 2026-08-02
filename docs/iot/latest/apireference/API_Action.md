---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_Action.html
---

# Action
<a name="API_Action"></a>

Describes the actions associated with a rule.

## Contents
<a name="API_Action_Contents"></a>

 ** cloudwatchAlarm **   <a name="iot-Type-Action-cloudwatchAlarm"></a>
Change the state of a CloudWatch alarm.
Type: [CloudwatchAlarmAction](API_CloudwatchAlarmAction.md) object
Required: No

 ** cloudwatchLogs **   <a name="iot-Type-Action-cloudwatchLogs"></a>
Send data to CloudWatch Logs.
Type: [CloudwatchLogsAction](API_CloudwatchLogsAction.md) object
Required: No

 ** cloudwatchMetric **   <a name="iot-Type-Action-cloudwatchMetric"></a>
Capture a CloudWatch metric.
Type: [CloudwatchMetricAction](API_CloudwatchMetricAction.md) object
Required: No

 ** dynamoDB **   <a name="iot-Type-Action-dynamoDB"></a>
Write to a DynamoDB table.
Type: [DynamoDBAction](API_DynamoDBAction.md) object
Required: No

 ** dynamoDBv2 **   <a name="iot-Type-Action-dynamoDBv2"></a>
Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
Type: [DynamoDBv2Action](API_DynamoDBv2Action.md) object
Required: No

 ** elasticsearch **   <a name="iot-Type-Action-elasticsearch"></a>
Write data to an Amazon OpenSearch Service domain.
The `Elasticsearch` action can only be used by existing rule actions. To create a new rule action or to update an existing rule action, use the `OpenSearch` rule action instead. For more information, see [OpenSearchAction](https://docs.aws.amazon.com/iot/latest/apireference/API_OpenSearchAction.html).
Type: [ElasticsearchAction](API_ElasticsearchAction.md) object
Required: No

 ** firehose **   <a name="iot-Type-Action-firehose"></a>
Write to an Amazon Kinesis Firehose stream.
Type: [FirehoseAction](API_FirehoseAction.md) object
Required: No

 ** http **   <a name="iot-Type-Action-http"></a>
Send data to an HTTPS endpoint.
Type: [HttpAction](API_HttpAction.md) object
Required: No

 ** iotAnalytics **   <a name="iot-Type-Action-iotAnalytics"></a>
Sends message data to an AWS IoT Analytics channel.
Type: [IotAnalyticsAction](API_IotAnalyticsAction.md) object
Required: No

 ** iotEvents **   <a name="iot-Type-Action-iotEvents"></a>
Sends an input to an AWS IoT Events detector.
Type: [IotEventsAction](API_IotEventsAction.md) object
Required: No

 ** iotSiteWise **   <a name="iot-Type-Action-iotSiteWise"></a>
Sends data from the MQTT message that triggered the rule to AWS IoT SiteWise asset properties.
Type: [IotSiteWiseAction](API_IotSiteWiseAction.md) object
Required: No

 ** kafka **   <a name="iot-Type-Action-kafka"></a>
Send messages to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) or self-managed Apache Kafka cluster.
Type: [KafkaAction](API_KafkaAction.md) object
Required: No

 ** kinesis **   <a name="iot-Type-Action-kinesis"></a>
Write data to an Amazon Kinesis stream.
Type: [KinesisAction](API_KinesisAction.md) object
Required: No

 ** lambda **   <a name="iot-Type-Action-lambda"></a>
Invoke a Lambda function.
Type: [LambdaAction](API_LambdaAction.md) object
Required: No

 ** location **   <a name="iot-Type-Action-location"></a>
The Amazon Location Service rule action sends device location updates from an MQTT message to an Amazon Location tracker resource.
Type: [LocationAction](API_LocationAction.md) object
Required: No

 ** openSearch **   <a name="iot-Type-Action-openSearch"></a>
Write data to an Amazon OpenSearch Service domain.
Type: [OpenSearchAction](API_OpenSearchAction.md) object
Required: No

 ** republish **   <a name="iot-Type-Action-republish"></a>
Publish to another MQTT topic.
Type: [RepublishAction](API_RepublishAction.md) object
Required: No

 ** s3 **   <a name="iot-Type-Action-s3"></a>
Write to an Amazon S3 bucket.
Type: [S3Action](API_S3Action.md) object
Required: No

 ** salesforce **   <a name="iot-Type-Action-salesforce"></a>
Send a message to a Salesforce IoT Cloud Input Stream.
Type: [SalesforceAction](API_SalesforceAction.md) object
Required: No

 ** sns **   <a name="iot-Type-Action-sns"></a>
Publish to an Amazon SNS topic.
Type: [SnsAction](API_SnsAction.md) object
Required: No

 ** sqs **   <a name="iot-Type-Action-sqs"></a>
Publish to an Amazon SQS queue.
Type: [SqsAction](API_SqsAction.md) object
Required: No

 ** stepFunctions **   <a name="iot-Type-Action-stepFunctions"></a>
Starts execution of a Step Functions state machine.
Type: [StepFunctionsAction](API_StepFunctionsAction.md) object
Required: No

 ** timestream **   <a name="iot-Type-Action-timestream"></a>
The Timestream rule action writes attributes (measures) from an MQTT message into an Amazon Timestream table. For more information, see the [Timestream](https://docs.aws.amazon.com/iot/latest/developerguide/timestream-rule-action.html) topic rule action documentation.
Type: [TimestreamAction](API_TimestreamAction.md) object
Required: No

## See Also
<a name="API_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/Action)
