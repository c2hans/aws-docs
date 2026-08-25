---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3-event-notifications.html
---

# Work with S3 Event Notifications
<a name="examples-s3-event-notifications"></a>

To help you monitor activity in your buckets, Amazon S3 can send notifications when certain events happen. The Amazon S3 User Guide provides information on the [notifications that a bucket can send out](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html#notification-how-to-overview).

You can set up a bucket to send events to four possible destinations using the SDK for Java:
+ Amazon Simple Notification Service topics
+ Amazon Simple Queue Service queues
+ AWS Lambda functions
+ Amazon EventBridge

When you setup up a bucket to send events to EventBridge, you have the ability to configure an EventBridge rule to fanout the same event to multiple destinations. When you configure your bucket to send directly to one of the first three destinations, only one destination type can be specified for each event.

In the next section, you'll see how to configure a bucket using the SDK for Java to send S3 Event Notifications in two ways: directly to an Amazon SQS queue and to EventBridge.

The last section shows you how to use the S3 Event Notifications API to work with notifications in an object-oriented way.

## Configure a bucket to send directly to a destination
<a name="s3-event-conf-bucket-direct"></a>

The following example configures a bucket to send notifications when *object create* events or *object tagging* events occur against a bucket.

```
static void processS3Events(String bucketName, String queueArn) {
    // Configure the bucket to send Object Created and Object Tagging notifications to an existing SQS queue.
    s3Client.putBucketNotificationConfiguration(b -> b
            .notificationConfiguration(ncb -> ncb
                    .queueConfigurations(qcb -> qcb
                            .events(Event.S3_OBJECT_CREATED, Event.S3_OBJECT_TAGGING)
                            .queueArn(queueArn)))
                    .bucket(bucketName)
    );
}
```

The code shown above sets up one queue to receive two types of events. Conveniently, the `queueConfigurations` method allows you to set multiple queue destinations if needed. Also, in the `notificationConfiguration` method you can set additional destinations, such as one or more Amazon SNS topics or one or more Lambda functions. The following snippet shows an example with two queues and three types of destinations.

```
s3Client.putBucketNotificationConfiguration(b -> b
                .notificationConfiguration(ncb -> ncb
                        .queueConfigurations(qcb -> qcb
                                .events(Event.S3_OBJECT_CREATED, Event.S3_OBJECT_TAGGING)
                                .queueArn(queueArn),
                                qcb2 -> qcb2.{{<...>}})
                        .topicConfigurations(tcb -> tcb.{{<...>}})
                        .lambdaFunctionConfigurations(lfcb -> lfcb.{{<...>}}))
                        .bucket(bucketName)
        );
```

The Code Examples GitHub repository contains the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/ProcessS3EventNotification.java) to send S3 event notifications directly to a queue.

## Configure a bucket to send to EventBridge
<a name="s3-event-conf-bucket-eventbridge"></a>

The following example configures a bucket to send notifications to EventBridge.

```
public static String setBucketNotificationToEventBridge(String bucketName) {
    // Enable bucket to emit S3 Event notifications to EventBridge.
    s3Client.putBucketNotificationConfiguration(b -> b
            .bucket(bucketName)
            .notificationConfiguration(b1 -> b1
                    .eventBridgeConfiguration(SdkBuilder::build))
    .build());
```

When you configure a bucket to send events to EventBridge, you simply indicate the EventBridge destination, not the types of events nor the ultimate destination that EventBridge will dispatch to. You configure the ultimate targets and event types by using the Java SDK's EventBridge client.

The following code shows how to configure EventBridge to fan out *object created* events to a topic and a queue.

```
   public static String configureEventBridge(String topicArn, String queueArn) {
        try {
            // Create an EventBridge rule to route Object Created notifications.
            PutRuleRequest putRuleRequest = PutRuleRequest.builder()
                    .name(RULE_NAME)
                    .eventPattern("""
                            {
                              "source": ["aws.s3"],
                              "detail-type": ["Object Created"],
                              "detail": {
                                "bucket": {
                                  "name": ["%s"]
                                }
                              }
                            }
                            """.formatted(bucketName))
                    .build();

            // Add the rule to the default event bus.
            PutRuleResponse putRuleResponse = eventBridgeClient.putRule(putRuleRequest)
                    .whenComplete((r, t) -> {
                        if (t != null) {
                            logger.error("Error creating event bus rule: " + t.getMessage(), t);
                            throw new RuntimeException(t.getCause().getMessage(), t);
                        }
                        logger.info("Event bus rule creation request sent successfully. ARN is: {}", r.ruleArn());
                    }).join();

            // Add the existing SNS topic and SQS queue as targets to the rule.
            eventBridgeClient.putTargets(b -> b
                    .eventBusName("default")
                    .rule(RULE_NAME)
                    .targets(List.of (
                            Target.builder()
                                    .arn(queueArn)
                                    .id("Queue")
                                    .build(),
                            Target.builder()
                                    .arn(topicArn)
                                    .id("Topic")
                                    .build())
                            )
                    ).join();
            return putRuleResponse.ruleArn();
        } catch (S3Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return null;
    }
```

To work with EventBridge in your Java code, add a dependency on the `eventbridge` artifact to your Maven `pom.xml` file.

```
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>eventbridge</artifactId>
</dependency>
```

The Code Examples GitHub repository contains the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/PutBucketS3EventNotificationEventBridge.java) to send S3 event notifications to EventBridge and then to a topic and queue.

## Use the S3 Event Notifications API to process events
<a name="s3-event-notification-read"></a>

After a destination receives S3 notification events, you can process them in an object-oriented way by using the S3 Event Notifications API. You can use the S3 Event Notifications API to work with event notifications that are dispatched directly to a target (as shown in the [first example](#s3-event-conf-bucket-direct)), but not with notifications routed through EventBridge. S3 event notifications sent by buckets to EventBridge contain a [different structure](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ev-events.html#ev-events-list) that the S3 Event Notifications API does not currently handle.

### Add dependency
<a name="s3-event-notifications-dep"></a>

The S3 Event Notifications API was released with version 2.25.11 of the SDK for Java 2.x.

To use the S3 Event Notifications API, add the required dependency element to your Maven `pom.xml` as shown in the following snippet.

```
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>bom</artifactId>
            <version>{{2.X.X1}}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>s3-event-notifications</artifactId>
    </dependency>
</dependencies>
```

1 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

### Use the `S3EventNotification` class
<a name="s3-event-notifications-use"></a>

#### Create an `S3EventNotification` instance from a JSON string
<a name="s3-event-notifications-use-from-json"></a>

To convert a JSON string into an `S3EventNotification` object, use the static methods of the `S3EventNotification` class as shown in the following example.

```
import software.amazon.awssdk.eventnotifications.s3.model.S3EventNotification
import software.amazon.awssdk.eventnotifications.s3.model.S3EventNotificationRecord
import software.amazon.awssdk.services.sqs.model.Message;

public class S3EventNotificationExample {
    ...

    void receiveMessage(Message message) {
       // Message received from SQSClient.
       String sqsEventBody = message.body();
       S3EventNotification s3EventNotification = S3EventNotification.fromJson(sqsEventBody);

       // Use getRecords() to access all the records in the notification.
       List<S3EventNotificationRecord> records = s3EventNotification.getRecords();

        S3EventNotificationRecord record = records.stream().findFirst();
        // Use getters on the record to access individual attributes.
        String awsRegion = record.getAwsRegion();
        String eventName = record.getEventName();
        String eventSource = record.getEventSource();
    }
}
```

In this example, the `fromJson` method converts the JSON string into an `S3EventNotification` object. Missing fields in the JSON string will result in `null` values in the corresponding Java object fields and any extra fields in the JSON will be ignored.

Other APIs for an event notification record can be found in API reference for `[S3EventNotificationRecord](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/S3EventNotificationRecord.html)`.

#### Convert an `S3EventNotification` instance to a JSON string
<a name="s3-event-notifications-use-to-json"></a>

Use the `toJson` (or `toJsonPretty`) method to convert an `S3EventNotification` object into a JSON string as shown in the following example.

```
import software.amazon.awssdk.eventnotifications.s3.model.S3EventNotification

public class S3EventNotificationExample {
    ...

    void toJsonString(S3EventNotification event) {

        String json = event.toJson();
        String jsonPretty = event.toJsonPretty();

        System.out.println("JSON: " + json);
        System.out.println("Pretty JSON: " + jsonPretty);
    }
}
```

Fields for `GlacierEventData`, `ReplicationEventData`, `IntelligentTieringEventData`, and `LifecycleEventData` are excluded from the JSON if they are `null`. Other `null` fields will be serialized as `null`.

The following shows example output of the `toJsonPretty` method for an S3 object tagging event.

```
{
  "Records" : [ {
    "eventVersion" : "2.3",
    "eventSource" : "aws:s3",
    "awsRegion" : "us-east-1",
    "eventTime" : "2024-07-19T20:09:18.551Z",
    "eventName" : "ObjectTagging:Put",
    "userIdentity" : {
      "principalId" : "AWS:XXXXXXXXXXX"
    },
    "requestParameters" : {
      "sourceIPAddress" : "XXX.XX.XX.XX"
    },
    "responseElements" : {
      "x-amz-request-id" : "XXXXXXXXXXXX",
      "x-amz-id-2" : "XXXXXXXXXXXXX"
    },
    "s3" : {
      "s3SchemaVersion" : "1.0",
      "configurationId" : "XXXXXXXXXXXXX",
      "bucket" : {
        "name" : "amzn-s3-demo-bucket",
        "ownerIdentity" : {
          "principalId" : "XXXXXXXXXXX"
        },
        "arn" : "arn:aws:s3:::XXXXXXXXXX"
      },
      "object" : {
        "key" : "akey",
        "size" : null,
        "eTag" : "XXXXXXXXXX",
        "versionId" : null,
        "sequencer" : null
      }
    }
  } ]
}
```

A [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/75c3daadf750406156fc87fa30ee499a206b4a36/javav2/example_code/s3/src/main/java/com/example/s3/ProcessS3EventNotification.java#L117) is available in GitHub that shows how to use the API to work with notifications received by an Amazon SQS queue.

## Process S3 Events in Lambda with Java Libraries: AWS SDK for Java 2.x and `aws-lambda-java-events`
<a name="s3-event-notif-processing-options"></a>

Instead of using the SDK for Java 2.x to process Amazon S3 event notifications in a Lambda function, you can use the `[aws-lambda-java-events](https://github.com/aws/aws-lambda-java-libs/tree/main/aws-lambda-java-events)` library at version 3.x.x. AWS maintains the `aws-lambda-java-events` library independently, and it has its own dependency requirements. The `aws-lambda-java-events` library works only with S3 events in Lambda functions, whereas the SDK for Java 2.x works with S3 events in Lambda functions, Amazon SNS, and Amazon SQS.

Both approaches model the JSON event notification payload in an object-oriented way with similar APIs. The following table shows the notable differences between using the two approaches.

|  | AWS SDK for Java | aws-lambda-java-events library |
| --- | --- | --- |
| Package naming | `software.amazon.awssdk.eventnotifications.s3.model.S3EventNotification` | com.amazonaws.services.lambda.runtime.events.models.s3.S3EventNotification |
| RequestHandler parameter | Write your Lambda function's `RequestHandler` implementation to receive a JSON String:<pre>import com.amazonaws.services.lambda.runtime.Context;<br />import com.amazonaws.services.lambda.runtime.RequestHandler;<br />import software.amazon.awssdk.eventnotifications.s3.model.S3EventNotification;<br /><br />public class Handler implements RequestHandler<String, String> {<br /><br />    @Override<br />        public String handleRequest(String jsonS3Event, Context context) {<br />            S3EventNotification s3Event = S3EventNotification<br />                                             .fromJson(jsonS3Event);<br />            // Work with the s3Event object.        <br />            ...<br />    }<br />}</pre> | Write your Lambda function's RequestHandler implementation to receive an S3Event object:<pre>import com.amazonaws.services.lambda.runtime.Context;<br />import com.amazonaws.services.lambda.runtime.RequestHandler;<br />import com.amazonaws.services.lambda.runtime.events.S3Event;<br /><br />public class Handler implements RequestHandler<S3Event, String> {<br /><br />    @Override<br />        public String handleRequest(S3Event s3event, Context context) {<br />            // Work with the s3Event object.        <br />            ...<br />    }<br />}</pre> |
| Maven dependencies |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>2.X.X</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>s3-event-notifications</artifactId><br />    </dependency><br />    <!-- Add other SDK dependencies that you need. --><br /></dependencies></pre>  |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>2.X.X</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <!-- The following two dependencies are for the <br />         aws-lambda-java-events library. --><br />    <dependency><br />        <groupId>com.amazonaws</groupId><br />        <artifactId>aws-lambda-java-core</artifactId><br />        <version>1.2.3</version>     <br />    </dependency><br />    <dependency><br />        <groupId>com.amazonaws</groupId><br />        <artifactId>aws-lambda-java-events</artifactId><br />        <version>3.15.0</version><br />    </dependency><br />    <!-- Add other SDK dependencies that you need. --><br /></dependencies></pre>  |
