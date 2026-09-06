---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/best-practices-for-using-mqtt-topics-in-the-aws-iot-rules-engine.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Best practices for using MQTT topics in the AWS IoT Rules Engine
<a name="best-practices-for-using-mqtt-topics-in-the-aws-iot-rules-engine"></a>

 The [AWS IoT Rules Engine](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) enables you to define how messages sent to AWS IoT Core can interact with AWS services. An AWS IoT rule consists of a SQL SELECT statement, a topic filter, and a rule action.

The SQL SELECT statement can extract data from incoming MQTT messages. The topic filter of an AWS IoT rule specifies which MQTT topics invoke an AWS IoT Rule Action.

 The rules engine plays a pivotal role in intelligently directing messages to other AWS services or republishing to devices. AWS IoT rules support use cases, such as gathering operational metrics, data enrichment, data aggregation of device telemetry for analytics purpose, and for troubleshooting errors.

## Rules Engine integration with telemetry topics
<a name="rules-engine-integration-with-telemetry-topics"></a>

 We recommend using a topic structure for telemetry similar to the following:

```
 dt/<application-prefix>/<context>/<thing-name>/<dt-type>
```

 The second field in the MQTT topic telemetry pattern defined as `application-prefix` represents an immutable, natural bifurcation between your devices in a fleet. A common attribute for the application is the device hardware version or the name of the IoT application. Using the telemetry MQTT structure, you can create an IoT rule to capture all telemetry associated with a specific application version:

```
{
    "sql":"SELECT *, topic(2) as applicationVersion, topic(3) as
contextIdentifier FROM 'dt/#'",
    "awsIoTSqlVersion":"2016-03-23",
    "ruleDisabled":false,
    "actions":[{
    ...
    }]
}
```

 Because the MQTT topic structure mirrors a hierarchy, this rule can select different parts of the MQTT topic hierarchy and inject it into the new payload. These attributes provide further context as messages are processed and stored in other AWS services.

## Rules Engine integration with command topics
<a name="rules-engine-integration-with-command-topics"></a>

 The Rules Engine can be used to capture insight into the success or failure of commands, regardless of whether the commands are sent using the AWS IoT Device Shadow service, AWS IoT Jobs, or by using an MQTT command topic.

### Tracking success of commands
<a name="tracking-success-of-commands"></a>

 The AWS IoT Rules Engine can be used to track the success rates of individual commands. The IoT rule extracts payload information, such as the session identifier; generates additional metadata in the rule select statement, such as creating a time to live; and temporarily stores the new message payload into a data store, such as [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).

The rule that follows mirrors a common implementation of this use case for an AWS customer. The IoT rule stores each session as an individual DynamoDB record and because the WHERE clause identifies this as an incoming command, the rule adds a literal value named `status` that marks the command as `In progress`.

```
{
"sql": "SELECT sessionId AS token,timestamp()/1000 as ttl, topicId AS responseTopic, clientId AS requestorID, action.type AS commandType, 'In PRogress' AS status FROM 'cmd/series100/#' WHERE topic(5) == 'credentials'”
 "actions": [{
      "dynamoDBv2": {
          "roleArn": "arn:aws:iam::12345678:role/service-role/dynamoDBrole",
       "putItem":{
       	"tableName": "command sessions table"
                 }
             }
       }]
```

 As command messages are published to the topic matching the rule, the preceding rule maintains a record of all in-transit commands.

 By following the MQTT topic best practices, the response topic includes overlapping information as the command itself (for example, the original session ID and the response topic used by the smart lock).

As an added capability, the cloud application may have a second IoT rule that uses the session ID to update the status of a specific command using information from the response metadata.

 Refer to the following example:

```
{
      "sql": "SELECT sessionId AS token,timestamp()/1000 as ttl, topic() AS responseTopic, clientId AS requestorID, res.code AS response.code, 'Complete' AS status FROM 'cmd/series100/#' WHERE topic(5) == 'res'”
        "actions": [{
            "dynamoDBv2": {
                "roleArn": "arn:aws:iam::12345678:role/service-role/dynamoDBrole",
            "putItem":{
       	        "tableName": "command sessions table"
                      }
                  }
            }]
```

## Aligning Rules Engine capabilities with MQTT topics
<a name="aligning-rules-engine-capabilities-with-mqtt-topics"></a>

 As you define your use of the IoT rules, review the following recommendations as you relate to MQTT topics and the AWS IoT Rules Engine:
+  Use the [topic(Decimal)](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-functions.html#iot-function-topic) rule function to augment your MQTT messages with contextual information contained in your MQTT topics.
+  Use the [timestamp()](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-functions.html#iot-function-timestamp) rule function to include a timestamp that correlates the time that a message reached AWS IoT Core.
+  If your commands are in JSON, reference any contextual payload metadata, such as session ID, in the [SELECT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-select.html) and [WHERE](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-where.html) clause of the rules engine. The additional payload information can be used to determine if and when a rule should initiate.
+  Use [Substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) in your AWS IoT actions to express variables as part of the AWS IoT Rule action that is initiated. Substitution expressions make it easier to scale and dynamically route to downstream IoT Rule actions.
+  To track the completion of a command or request, use the AWS IoT Rules Engine to store the data and status in a service, such as DynamoDB. As messages are processed, data can be automatically expired from DynamoDB using a TTL field. In cases where commands are sent at a high throughput rate, you can leverage the AWS IoT Rules Engine with Amazon Kinesis to buffer data before DynamoDB storage.
+  Use the AWS IoT Rules WHERE clause to filter messages that do not apply to an AWS IoT Action. The WHERE clause can be used with the JSON payload or Rules Engine functions, such as [get\_thing\_shadow(thingName, roleARN)](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-functions.html#iot-sql-function-get-thing-shadow) or [aws\_lambda(functionArn, inputJson)](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-functions.html#iot-func-aws-lambda).
+  After AWS IoT Core receives a message, use AWS services like Amazon Kinesis or Amazon SQS to buffer the message payload along with the MQTT topic the message was published to. Once messages are buffered, you can run your own logic on [AWS Lambda](https://aws.amazon.com/lambda/) or [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) to map fields from the payload or the topic and enrich the payload with additional metadata related to the individual devices, the type of device, or the device group. The `topic(decimal)` rule function can be used to enrich the payload with the entire topic when using `topic()`. If you want to enrich the payload with an serial number that is part of the MQTT topic shown below then you would use `topic(4)`.

  ```
  dt/customer435/hub/745384327
  ```
