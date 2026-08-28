---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3-event-notification.html
---

# Changes in the S3 Event Notifications API from version 1 to version 2
<a name="migration-s3-event-notification"></a>

This topic details the changes in the S3 Event Notifications API from version 1.x (v1) to version 2 .x (v2) of the AWS SDK for Java.

## High-level changes
<a name="migration-s3-event-notification-hl"></a>

### Structural changes
<a name="migration-s3-event-notification-hl-struct"></a>

V1 uses static inner classes for `EventNotificationRecord` types and their attributes, whereas v2 uses separate public classes for `EventNotificationRecord` types.

### Naming convention changes
<a name="migration-s3-event-notification-hl-naming"></a>

In v1, attribute class names include the suffix *Entity*, whereas v2 omits this suffix for simpler naming: for example, *eventData* instead of *eventDataEntity*.

## Changes in dependencies, packages and class names
<a name="migration-s3-event-notification-deps"></a>

In v1, S3 Event Notification API classes are transitively imported with along with the S3 module (artifactId `aws-java-sdk-s3`). However, in v2, you need to add a dependency on the `s3-event-notifications` artifact.

| Change | v1 | v2 |
| --- | --- | --- |
|  <br />Maven dependencies |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>com.amazonaws</groupId><br />            <artifactId>aws-java-sdk-bom</artifactId><br />            <version>{{1.X.X}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>com.amazonaws</groupId><br />        <artifactId>aws-java-sdk-s3</artifactId><br />    </dependency><br /></dependencies></pre>  |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>{{2.X.X1}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>s3-event-notifications</artifactId><br />    </dependency><br /></dependencies></pre>  |
| Package name | com.amazonaws.services.s3.event | software.amazon.awssdk.eventnotifications.s3.model |
| Class names | [S3EventNotification](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.html)<br />[S3EventNotification.S3EventNotificationRecord](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.S3EventNotificationRecord.html)<br />[ S3EventNotification.GlacierEventDataEntity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.GlacierEventDataEntity.html)<br />[S3EventNotification.IntelligentTieringEventDataEntity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.IntelligentTieringEventDataEntity.html)<br />[S3EventNotification.LifecycleEventDataEntity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.LifecycleEventDataEntity.html)<br />[S3EventNotification.ReplicationEventDataEntity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.ReplicationEventDataEntity.html)<br />[S3EventNotification.RequestParametersEntity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.RequestParametersEntity.html)<br />[S3EventNotification.ResponseElementsEntity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.ResponseElementsEntity.html)<br />[S3EventNotification.RestoreEventDataEntity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.RestoreEventDataEntity.html)<br />[S3EventNotification.S3BucketEntity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.S3BucketEntity.html)<br />[ S3EventNotification.S3Entity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.S3Entity.html)<br />[S3EventNotification.S3ObjectEntity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.S3ObjectEntity.html)<br />[S3EventNotification.TransitionEventDataEntity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.TransitionEventDataEntity.html)<br />[S3EventNotification.UserIdentityEntity](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/event/S3EventNotification.UserIdentityEntity.html) |  [S3EventNotification](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/S3EventNotification.html)<br />[S3EventNotificationRecord](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/S3EventNotificationRecord.html)<br />[GlacierEventData](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/GlacierEventData.html)<br />[IntelligentTieringEventData](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/IntelligentTieringEventData.html)<br />[LifecycleEventData](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/LifecycleEventData.html)<br />[ReplicationEventData](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/ReplicationEventData.html)<br />[RequestParameters](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/RequestParameters.html)<br />[ResponseElements](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/ResponseElements.html)<br />[RestoreEventData](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/RestoreEventData.html)<br />[S3Bucket](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/S3Bucket.html)<br />[S3](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/S3.html)<br />[S3Object](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/S3Object.html)<br />[TransitionEventData](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/TransitionEventData.html)<br />[UserIdentity](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/eventnotifications/s3/model/UserIdentity.html) |

1 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

## API changes
<a name="migration-s3-event-notification-API-changes"></a>

### JSON to `S3EventNotification` and reverse
<a name="migration-s3-event-notification-API-changes-conv"></a>

| Use case | v1 | v2 |
| --- | --- | --- |
| Create S3EventNotification from JSON String |  <pre>S3EventNotification notification = <br />        S3EventNotification.parseJson(message.body());</pre>  |  <pre>S3EventNotification notification = <br />        S3EventNotification.fromJson(message.body());</pre>  |
| Convert S3EventNotification to JSON String |  <pre>String json = notification.toJson();</pre>  |  <pre>String json = notification.toJson();</pre>  |

### Access attributes of `S3EventNotification`
<a name="migration-s3-event-notification-API-changes-attr"></a>

| Use case | v1 | v2 |
| --- | --- | --- |
| Retrieve records from a notification |  <pre>List<S3EventNotification.S3EventNotificationRecord> records = <br />        notifcation.getRecords();</pre>  |  <pre>List<S3EventNotificationRecord> records = <br />        notification.getRecords();</pre>  |
| Retrieve a record from a list of records |  <pre>S3EventNotification.S3EventNotificationRecord record = <br />        records.stream().findAny().get();</pre>  |  <pre>S3EventNotificationRecord record = <br />        records.stream().findAny().get();</pre>  |
| Retrieve Glacier event data |  <pre>S3EventNotification.GlacierEventDataEntity glacierEventData =<br />        record.getGlacierEventData();</pre>  |  <pre>GlacierEventData glacierEventData = <br />        record.getGlacierEventData();</pre>  |
| Retrieve restore event data from a Glacier event |  <pre>S3EventNotification.RestoreEventDataEntity restoreEventData = <br />        glacierEventData.getRestoreEventDataEntity();</pre>  |  <pre>RestoreEventData restoreEventData = <br />        glacierEventData.getRestoreEventData();</pre>  |
| Retrieve request parameters |  <pre>S3EventNotification.RequestParametersEntity requestParameters = <br />        record.getRequestParameters();</pre>  |  <pre>RequestParameters requestParameters = <br />        record.getRequestParameters();</pre>  |
| Retrieve Intelligent Tiering event data |  <pre>S3EventNotification.IntelligentTieringEventDataEntity tieringEventData = <br />        record.getIntelligentTieringEventData();</pre>  |  <pre>IntelligentTieringEventData intelligentTieringEventData = <br />        record.getIntelligentTieringEventData();</pre>  |
| Retrieve lifecyle event data |  <pre>S3EventNotification.LifecycleEventDataEntity lifecycleEventData = <br />        record.getLifecycleEventData();</pre>  |  <pre>LifecycleEventData lifecycleEventData = <br />        record.getLifecycleEventData();</pre>  |
| Retrieve event name as enum |  <pre>S3Event eventNameAsEnum = record.getEventNameAsEnum();</pre>  |  <pre>//getEventNameAsEnum does not exist; use 'getEventName()'<br />String eventName = record.getEventName();</pre>  |
| Retrieve replication event data |  <pre>S3EventNotification.ReplicationEventDataEntity replicationEntity = <br />        record.getReplicationEventDataEntity();</pre>  |  <pre>ReplicationEventData replicationEventData = <br />        record.getReplicationEventData();</pre>  |
| Retrieve S3 bucket and object information |  <pre>S3EventNotification.S3Entity s3 = record.getS3();</pre>  |  <pre>S3 s3 = record.getS3();</pre>  |
| Retrieve user identity information |  <pre>S3EventNotification.UserIdentityEntity userIdentity = <br />        record.getUserIdentity();</pre>  |  <pre>UserIdentity userIdentity = <br />        record.getUserIdentity();</pre>  |
| Retrieve response elements |  <pre>S3EventNotification.ResponseElementsEntity responseElements = <br />        record.getResponseElements();</pre>  |  <pre>ResponseElements responseElements = <br />        record.getResponseElements();</pre>  |

## Migrate the `aws-lambda-java-events` library version
<a name="migration-s3-events-notification-lambda-lib"></a>

If you use [aws-lambda-java-events](https://github.com/aws/aws-lambda-java-libs/tree/main/aws-lambda-java-events) to work with S3 notification events within a Lambda function, we recommend that you upgrade to the latest 3.x.x version. Recent versions eliminate all dependencies on AWS SDK for Java 1.x from the S3 event notification API.

For more information about the differences in handling S3 event notifications between the `aws-lambda-java-events` library and the SDK for Java 2.x, see [Process S3 Events in Lambda with Java Libraries: AWS SDK for Java 2.x and `aws-lambda-java-events`](examples-s3-event-notifications.md#s3-event-notif-processing-options).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
