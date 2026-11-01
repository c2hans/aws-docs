---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_eventbridge_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# EventBridge examples using AWS CLI
<a name="cli_2_eventbridge_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with EventBridge.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `delete-rule`
<a name="eventbridge_DeleteRule_cli_2_topic"></a>

The following code example shows how to use `delete-rule`.

**AWS CLI**
**To delete a CloudWatch Events rule**
The following `delete-rule` example deletes the rule named `EC2InstanceStateChanges`.

```
aws events delete-rule \
    --name {{"EC2InstanceStateChanges"}}
```
This command produces no output.
For more information, see [Disabling or deleting a rule in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-delete-rule.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [DeleteRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-rule.html) in *AWS CLI Command Reference*.

### `describe-rule`
<a name="eventbridge_DescribeRule_cli_2_topic"></a>

The following code example shows how to use `describe-rule`.

**AWS CLI**
**To display information about a CloudWatch Events rule**
The following `describe-rule` example displays information about the rule named `DailyLambdaFunction`.

```
aws events describe-rule \
    --name {{"DailyLambdaFunction"}}
```
Output:

```
{
    "Name": "DailyLambdaFunction",
    "Arn": "arn:aws:events:us-west-2:123456789012:rule/DailyLambdaFunction",
    "ScheduleExpression": "cron(0 9 * * ? *)",
    "State": "ENABLED",
    "EventBusName": "default",
    "CreatedBy": "123456789012"
}
```
For more information, see [Rules in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [DescribeRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-rule.html) in *AWS CLI Command Reference*.

### `disable-rule`
<a name="eventbridge_DisableRule_cli_2_topic"></a>

The following code example shows how to use `disable-rule`.

**AWS CLI**
**To disable a CloudWatch Events rule**
The following `disable-rule` example disables the rule named `DailyLambdaFunction`. The rule is not deleted.

```
aws events disable-rule \
    --name {{"DailyLambdaFunction"}}
```
This command produces no output.
For more information, see [Disabling or deleting a rule in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-delete-rule.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [DisableRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/disable-rule.html) in *AWS CLI Command Reference*.

### `enable-rule`
<a name="eventbridge_EnableRule_cli_2_topic"></a>

The following code example shows how to use `enable-rule`.

**AWS CLI**
**To enable a CloudWatch Events rule**
The following `enable-rule` example enables the rule named `DailyLambdaFunction`, which had been previously disabled.

```
aws events enable-rule \
    --name {{"DailyLambdaFunction"}}
```
This command produces no output.
For more information, see [Rules in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [EnableRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/enable-rule.html) in *AWS CLI Command Reference*.

### `list-rule-names-by-target`
<a name="eventbridge_ListRuleNamesByTarget_cli_2_topic"></a>

The following code example shows how to use `list-rule-names-by-target`.

**AWS CLI**
**To display all the rules that have a specified target**
The following `list-rule-names-by-target` example displays all rules that have the Lambda function named `MyFunctionName` as the target.

```
aws events list-rule-names-by-target \
    --target-arn {{"arn:aws:lambda:us-west-2:123456789012:function:MyFunctionName"}}
```
Output:

```
{
    "RuleNames": [
        "DailyLambdaFunction"
    ]
}
```
For more information, see [Event bus targets in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [ListRuleNamesByTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-rule-names-by-target.html) in *AWS CLI Command Reference*.

### `list-rules`
<a name="eventbridge_ListRules_cli_2_topic"></a>

The following code example shows how to use `list-rules`.

**AWS CLI**
**Example 1: To display a list of all CloudWatch Events rules**
The following `list-rules` example displays all CloudWatch Events rules in the region.

```
aws events list-rules
```
Output:

```
{
    "Rules": [
        {
            "Name": "DailyLambdaFunction",
            "Arn": "arn:aws:events:us-west-2:123456789012:rule/DailyLambdaFunction",
            "State": "ENABLED",
            "ScheduleExpression": "cron(0 9 * * ? *)",
            "EventBusName": "default"
        },
        {
            "Name": "EC2InstanceStateChanges",
            "Arn": "arn:aws:events:us-west-2:123456789012:rule/EC2InstanceStateChanges",
            "EventPattern": "{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EC2 Instance State-change Notification\"]}",
            "State": "ENABLED",
            "RoleArn": "arn:aws:iam::123456789012:role/MyRoleForThisRule",
            "EventBusName": "default"
        }
    ]
}
```
**Example 2: To display a list of CloudWatch Events rules beginning with a certain string**
The following `list-rules` example displays all CloudWatch Events rules in the region that have a name starting with `Daily`.

```
aws events list-rules \
    --name-prefix {{"Daily"}}
```
Output:

```
{
    "Rules": [
        {
            "Name": "DailyLambdaFunction",
            "Arn": "arn:aws:events:us-west-2:123456789012:rule/DailyLambdaFunction",
            "State": "ENABLED",
            "ScheduleExpression": "cron(0 9 * * ? *)",
            "EventBusName": "default"
        }
    ]
}
```
For more information, see [Rules in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [ListRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-rules.html) in *AWS CLI Command Reference*.

### `list-targets-by-rule`
<a name="eventbridge_ListTargetsByRule_cli_2_topic"></a>

The following code example shows how to use `list-targets-by-rule`.

**AWS CLI**
**To display all the targets for a CloudWatch Events rule**
The following `list-targets-by-rule` example displays all the targets of the rule named `DailyLambdaFunction`.

```
aws events list-targets-by-rule \
    --rule {{"DailyLambdaFunction"}}
```
Output:

```
{
    "Targets": [
        {
            "Id": "1",
            "Arn": "arn:aws:lambda:us-west-2:123456789012:function:MyFunctionName"
        }
    ]
}
```
For more information, see [Event bus targets in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [ListTargetsByRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-targets-by-rule.html) in *AWS CLI Command Reference*.

### `put-events`
<a name="eventbridge_PutEvents_cli_2_topic"></a>

The following code example shows how to use `put-events`.

**AWS CLI**
**To send a custom event to CloudWatch Events**
The following `put-events` example sends a custom event to CloudWatch Events. The event is contained within the `putevents.json` file.

```
aws events put-events \
    --entries {{file://putevents.json}}
```
Contents of `putevents.json`:

```
[
    {
        "Source": "com.mycompany.myapp",
        "Detail": "{ \"key1\": \"value1\", \"key2\": \"value2\" }",
        "Resources": [
            "resource1",
            "resource2"
        ],
        "DetailType": "myDetailType"
    },
    {
        "Source": "com.mycompany.myapp",
        "Detail": "{ \"key1\": \"value3\", \"key2\": \"value4\" }",
        "Resources": [
            "resource1",
            "resource2"
        ],
        "DetailType": "myDetailType"
    }
]
```
Output:

```
{
    "FailedEntryCount": 0,
    "Entries": [
        {
            "EventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        },
        {
            "EventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
    ]
}
```
For more information, see [Sending events with PutEvents in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-putevents.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [PutEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-events.html) in *AWS CLI Command Reference*.

### `put-rule`
<a name="eventbridge_PutRule_cli_2_topic"></a>

The following code example shows how to use `put-rule`.

**AWS CLI**
**To create CloudWatch Events rules**
The following `put-rule` example creates a rule that triggers every day at 9:00am (UTC). If you use `put-targets` to add a Lambda function as a target of this rule, you could run the Lambda function every day at the specified time.

```
aws events put-rule \
    --name {{"DailyLambdaFunction"}} \
    --schedule-expression {{"cron(0 9 * * ? *)"}}
```
Output:

```
{
    "RuleArn": "arn:aws:events:us-west-2:123456789012:rule/DailyLambdaFunction"
}
```
The following `put-rule` example creates a rule that triggers when any EC2 instance in the region changes state.

```
aws events put-rule \
    --name {{"EC2InstanceStateChanges"}} \
    --event-pattern "{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EC2 Instance State-change Notification\"]}" \
    --role-arn {{"arn:aws:iam::123456789012:role/MyRoleForThisRule"}}
```
Output:

```
{
    "RuleArn": "arn:aws:events:us-west-2:123456789012:rule/EC2InstanceStateChanges"
}
```
The following `put-rule` example creates a rule that triggers when any EC2 instance in the region is stopped or terminated.

```
aws events put-rule \
    --name {{"EC2InstanceStateChangeStopOrTerminate"}} \
    --event-pattern "{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EC2 Instance State-change Notification\"],\"detail\":{\"state\":[\"stopped\",\"terminated\"]}}" \
    --role-arn {{"arn:aws:iam::123456789012:role/MyRoleForThisRule"}}
```
Output:

```
{
    "RuleArn": "arn:aws:events:us-west-2:123456789012:rule/EC2InstanceStateChangeStopOrTerminate"
}
```
For more information, see [Rules in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [PutRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-rule.html) in *AWS CLI Command Reference*.

### `put-targets`
<a name="eventbridge_PutTargets_cli_2_topic"></a>

The following code example shows how to use `put-targets`.

**AWS CLI**
**To add targets for CloudWatch Events rules**
The following `put-targets` example adds a Lambda function as the target of a rule.

```
aws events put-targets \
    --rule {{DailyLambdaFunction}} \
    --targets "Id"="1","Arn"="arn:aws:lambda:us-west-2:123456789012:function:MyFunctionName"
```
Output:

```
{
    "FailedEntryCount": 0,
    "FailedEntries": []
}
```
The following `put-targets` example sets an Amazon Kinesis stream as the target, so that events caught by this rule are relayed to the stream.

```
aws events put-targets \
    --rule {{EC2InstanceStateChanges}} \
    --targets "Id"="1","Arn"="arn:aws:kinesis:us-west-2:123456789012:stream/MyStream","RoleArn"="arn:aws:iam::123456789012:role/MyRoleForThisRule"
```
Output:

```
{
    "FailedEntryCount": 0,
    "FailedEntries": []
}
```
The following `put-targets` example sets two Amazon Kinesis streams as targets for one rule.

```
aws events put-targets \
    --rule {{DailyLambdaFunction}} \
    --targets "Id"="Target1","Arn"="arn:aws:kinesis:us-west-2:123456789012:stream/MyStream1","RoleArn"="arn:aws:iam::123456789012:role/ MyRoleToAccessLambda" "Id"="Target2"," Arn"="arn:aws:kinesis:us-west-2:123456789012:stream/MyStream2","RoleArn"="arn:aws:iam::123456789012:role/MyRoleToAccessLambda"
```
Output:

```
{
    "FailedEntryCount": 0,
    "FailedEntries": []
}
```
For more information, see [Event bus targets in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [PutTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-targets.html) in *AWS CLI Command Reference*.

### `remove-targets`
<a name="eventbridge_RemoveTargets_cli_2_topic"></a>

The following code example shows how to use `remove-targets`.

**AWS CLI**
**To remove a target for an event**
The following `remove-targets` example removes the Amazon Kinesis stream named `MyStream1` from being a target of the rule `DailyLambdaFunction`. When `DailyLambdaFunction` was created, this stream was set as a target with an ID of `Target1`.

```
aws events remove-targets \
    --rule {{"DailyLambdaFunction"}} \
    --ids {{"Target1"}}
```
Output:

```
{
    "FailedEntryCount": 0,
    "FailedEntries": []
}
```
For more information, see [Event bus targets in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [RemoveTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/remove-targets.html) in *AWS CLI Command Reference*.

### `test-event-pattern`
<a name="eventbridge_TestEventPattern_cli_2_topic"></a>

The following code example shows how to use `test-event-pattern`.

**AWS CLI**
**To check whether an event pattern matches a specified event**
The following `test-event-pattern` example tests whether the pattern `source:com.mycompany.myapp` matches the specified event. In this example, the output would be `true`.

```
aws events test-event-pattern \
    --event-pattern "{\"source\":[\"com.mycompany.myapp\"]}" \
    --event "{\"id\":\"1\",\"source\":\"com.mycompany.myapp\",\"detail-type\":\"myDetailType\",\"account\":\"123456789012\",\"region\":\"us-west-2\",\"time\":\"2017-04-11T20:11:04Z\"}"
```
Output:

```
{
    "Result": true
}
```
For more information, see [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide*.
+  For API details, see [TestEventPattern](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/test-event-pattern.html) in *AWS CLI Command Reference*.
