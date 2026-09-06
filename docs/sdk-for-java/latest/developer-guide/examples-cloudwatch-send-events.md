---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-cloudwatch-send-events.html
---

# Use Amazon CloudWatch Events
<a name="examples-cloudwatch-send-events"></a>

 CloudWatch Events delivers a near real-time stream of system events that describe changes in AWS resources to Amazon EC2 instances, Lambda functions, Kinesis streams, Amazon ECS tasks, Step Functions state machines, Amazon SNS topics, Amazon SQS queues, or built-in targets. You can match events and route them to one or more target functions or streams by using simple rules.

Amazon EventBridge is the [evolution](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cwe-now-eb.html) of CloudWatch Events. Both services use the same API, so you can continue using the [CloudWatch Events client](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudwatch/CloudWatchClient.html) provided by the SDK or migrate to the SDK for Java's [EventBridge client](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/eventbridge/EventBridgeClient.html) for CloudWatch Events functionality. CloudWatch Events [User Guide documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/index.html) and [API reference](https://docs.aws.amazon.com/eventbridge/latest/APIReference/index.html) are now available through the EventBridge documentation sites.

## Add events
<a name="add-events"></a>

To add custom CloudWatch events, call the `CloudWatchEventsClient’s` `putEvents` method with a [`PutEventsRequest`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudwatchevents/model/PutEventsRequest.html) object that contains one or more [`PutEventsRequestEntry`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudwatchevents/model/PutEventsRequestEntry.html) objects that provide details about each event. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.

**Note**
You can specify a maximum of 10 events per call to `putEvents`.

 **Imports**

```
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import software.amazon.awssdk.services.cloudwatchevents.CloudWatchEventsClient;
import software.amazon.awssdk.services.cloudwatchevents.model.PutEventsRequest;
import software.amazon.awssdk.services.cloudwatchevents.model.PutEventsRequestEntry;
```

 **Code**

```
    public static void putCWEvents(CloudWatchEventsClient cwe, String resourceArn ) {

        try {

            final String EVENT_DETAILS =
                "{ \"key1\": \"value1\", \"key2\": \"value2\" }";

            PutEventsRequestEntry requestEntry = PutEventsRequestEntry.builder()
                    .detail(EVENT_DETAILS)
                    .detailType("sampleSubmitted")
                    .resources(resourceArn)
                    .source("aws-sdk-java-cloudwatch-example")
                    .build();

            PutEventsRequest request = PutEventsRequest.builder()
                    .entries(requestEntry)
                    .build();

            cwe.putEvents(request);
            System.out.println("Successfully put CloudWatch event");

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/0b1785e42949ebf959eaa0f0da4dc2a48f92ea25/javav2/example_code/cloudwatch/src/main/java/com/example/cloudwatch/PutEvents.java) on GitHub.

## Add rules
<a name="add-rules"></a>

To create or update a rule, call the `CloudWatchEventsClient’s` `putRule` method with a [`PutRuleRequest`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudwatchevents/model/PutRuleRequest.html) with the name of the rule and optional parameters such as the [event pattern](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html), IAM role to associate with the rule, and a [scheduling expression](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html) that describes how often the rule is run.

 **Imports**

```
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import software.amazon.awssdk.services.cloudwatchevents.CloudWatchEventsClient;
import software.amazon.awssdk.services.cloudwatchevents.model.PutRuleRequest;
import software.amazon.awssdk.services.cloudwatchevents.model.PutRuleResponse;
import software.amazon.awssdk.services.cloudwatchevents.model.RuleState;
```

 **Code**

```
    public static void putCWRule(CloudWatchEventsClient cwe, String ruleName, String roleArn) {

        try {
            PutRuleRequest request = PutRuleRequest.builder()
                .name(ruleName)
                .roleArn(roleArn)
                .scheduleExpression("rate(5 minutes)")
                .state(RuleState.ENABLED)
                .build();

            PutRuleResponse response = cwe.putRule(request);
            System.out.printf(
                    "Successfully created CloudWatch events rule %s with arn %s",
                    roleArn, response.ruleArn());
        } catch (
            CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/0b1785e42949ebf959eaa0f0da4dc2a48f92ea25/javav2/example_code/cloudwatch/src/main/java/com/example/cloudwatch/PutRule.java) on GitHub.

## Add targets
<a name="add-targets"></a>

Targets are the resources that are invoked when a rule is triggered. Example targets include Amazon EC2 instances, Lambda functions, Kinesis streams, Amazon ECS tasks, Step Functions state machines, and built-in targets.

To add a target to a rule, call the `CloudWatchEventsClient’s` `putTargets` method with a [`PutTargetsRequest`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cloudwatchevents/model/PutTargetsRequest.html) containing the rule to update and a list of targets to add to the rule.

 **Imports**

```
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import software.amazon.awssdk.services.cloudwatchevents.CloudWatchEventsClient;
import software.amazon.awssdk.services.cloudwatchevents.model.PutTargetsRequest;
import software.amazon.awssdk.services.cloudwatchevents.model.PutTargetsResponse;
import software.amazon.awssdk.services.cloudwatchevents.model.Target;
```

 **Code**

```
    public static void putCWTargets(CloudWatchEventsClient cwe, String ruleName, String functionArn, String targetId ) {

        try {
            Target target = Target.builder()
                .arn(functionArn)
                .id(targetId)
                .build();

            PutTargetsRequest request = PutTargetsRequest.builder()
                .targets(target)
                .rule(ruleName)
                .build();

            PutTargetsResponse response = cwe.putTargets(request);
            System.out.printf(
                "Successfully created CloudWatch events target for rule %s",
                ruleName);
        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/0b1785e42949ebf959eaa0f0da4dc2a48f92ea25/javav2/example_code/cloudwatch/src/main/java/com/example/cloudwatch/PutTargets.java) on GitHub.

## More information
<a name="more-information"></a>
+  [Adding Events with PutEvents](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-putevents.html) in the Amazon EventBridge User Guide
+  [Schedule Expressions for Rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html#eb-create-scheduled-rule-schedule) in the Amazon EventBridge User Guide
+  [Event Types for CloudWatch Events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html) in the Amazon EventBridge User Guide
+  [Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the Amazon EventBridge User Guide
+  [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html) in the Amazon EventBridge API Reference
+  [PutTargets](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutTargets.html) in the Amazon EventBridge API Reference
+  [PutRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutRule.html) in the Amazon EventBridge API Reference
