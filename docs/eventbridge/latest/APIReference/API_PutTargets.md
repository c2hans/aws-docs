---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutTargets.html
---

# PutTargets
<a name="API_PutTargets"></a>

Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule.

Targets are the resources that are invoked when a rule is triggered.

The maximum number of entries per request is 10.

**Note**
Each rule can have up to five (5) targets associated with it at one time.

For a list of services you can configure as targets for events, see [EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) in the * *Amazon EventBridge User Guide* *.

Creating rules with built-in targets is supported only in the AWS Management Console. The built-in targets are:
+  `Amazon EBS CreateSnapshot API call`
+  `Amazon EC2 RebootInstances API call`
+  `Amazon EC2 StopInstances API call`
+  `Amazon EC2 TerminateInstances API call`

For some target types, `PutTargets` provides target-specific parameters. If the target is a Kinesis data stream, you can optionally specify which shard the event goes to by using the `KinesisParameters` argument. To invoke a command on multiple EC2 instances with one rule, you can use the `RunCommandParameters` field.

To be able to make API calls against the resources that you own, Amazon EventBridge needs the appropriate permissions:
+ For AWS Lambda and Amazon SNS resources, EventBridge relies on resource-based policies.
+ For EC2 instances, Kinesis Data Streams, AWS Step Functions state machines and API Gateway APIs, EventBridge relies on IAM roles that you specify in the `RoleARN` argument in `PutTargets`.

For more information, see [Authentication and Access Control](https://docs.aws.amazon.com/eventbridge/latest/userguide/auth-and-access-control-eventbridge.html) in the * *Amazon EventBridge User Guide* *.

If another AWS account is in the same region and has granted you permission (using `PutPermission`), you can send events to that account. Set that account's event bus as a target of the rules in your account. To send the matched events to the other account, specify that account's event bus as the `Arn` value when you run `PutTargets`. If your account sends events to another account, your account is charged for each sent event. Each event sent to another account is charged as a custom event. The account receiving the event is not charged. For more information, see [Amazon EventBridge Pricing](http://aws.amazon.com/eventbridge/pricing/).

**Note**
 `Input`, `InputPath`, and `InputTransformer` are not available with `PutTarget` if the target is an event bus of a different AWS account.

If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a `RoleArn` with proper permissions in the `Target` structure. For more information, see [Sending and Receiving Events Between AWS Accounts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html) in the *Amazon EventBridge User Guide*.

**Note**
If you have an IAM role on a cross-account event bus target, a `PutTargets` call without a role on the same target (same `Id` and `Arn`) will not remove the role.

For more information about enabling cross-account events, see [PutPermission](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPermission.html).

 **Input**, **InputPath**, and **InputTransformer** are mutually exclusive and optional parameters of a target. When a rule is triggered due to a matched event:
+ If none of the following arguments are specified for a target, then the entire event is passed to the target in JSON format (unless the target is Amazon EC2 Run Command or Amazon ECS task, in which case nothing from the event is passed to the target).
+ If **Input** is specified in the form of valid JSON, then the matched event is overridden with this constant.
+ If **InputPath** is specified in the form of JSONPath (for example, `$.detail`), then only the part of the event specified in the path is passed to the target (for example, only the detail part of the event is passed).
+ If **InputTransformer** is specified, then one or more specified JSONPaths are extracted from the event and used as values in a template that you specify as the input to the target.

When you specify `InputPath` or `InputTransformer`, you must use JSON dot notation, not bracket notation.

When you add targets to a rule and the associated rule triggers soon after, new or updated targets might not be immediately invoked. Allow a short period of time for changes to take effect.

This action can partially fail if too many requests are made at the same time. If that happens, `FailedEntryCount` is non-zero in the response and each entry in `FailedEntries` provides the ID of the failed target and the error code.

## Request Syntax
<a name="API_PutTargets_RequestSyntax"></a>

```
{
   "EventBusName": "{{string}}",
   "Rule": "{{string}}",
   "Targets": [
      {
         "AppSyncParameters": {
            "GraphQLOperation": "{{string}}"
         },
         "Arn": "{{string}}",
         "BatchParameters": {
            "ArrayProperties": {
               "Size": {{number}}
            },
            "JobDefinition": "{{string}}",
            "JobName": "{{string}}",
            "RetryStrategy": {
               "Attempts": {{number}}
            }
         },
         "DeadLetterConfig": {
            "Arn": "{{string}}"
         },
         "EcsParameters": {
            "CapacityProviderStrategy": [
               {
                  "base": {{number}},
                  "capacityProvider": "{{string}}",
                  "weight": {{number}}
               }
            ],
            "EnableECSManagedTags": {{boolean}},
            "EnableExecuteCommand": {{boolean}},
            "Group": "{{string}}",
            "LaunchType": "{{string}}",
            "NetworkConfiguration": {
               "awsvpcConfiguration": {
                  "AssignPublicIp": "{{string}}",
                  "SecurityGroups": [ "{{string}}" ],
                  "Subnets": [ "{{string}}" ]
               }
            },
            "PlacementConstraints": [
               {
                  "expression": "{{string}}",
                  "type": "{{string}}"
               }
            ],
            "PlacementStrategy": [
               {
                  "field": "{{string}}",
                  "type": "{{string}}"
               }
            ],
            "PlatformVersion": "{{string}}",
            "PropagateTags": "{{string}}",
            "ReferenceId": "{{string}}",
            "Tags": [
               {
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "TaskCount": {{number}},
            "TaskDefinitionArn": "{{string}}"
         },
         "HttpParameters": {
            "HeaderParameters": {
               "{{string}}" : "{{string}}"
            },
            "PathParameterValues": [ "{{string}}" ],
            "QueryStringParameters": {
               "{{string}}" : "{{string}}"
            }
         },
         "Id": "{{string}}",
         "Input": "{{string}}",
         "InputPath": "{{string}}",
         "InputTransformer": {
            "InputPathsMap": {
               "{{string}}" : "{{string}}"
            },
            "InputTemplate": "{{string}}"
         },
         "KinesisParameters": {
            "PartitionKeyPath": "{{string}}"
         },
         "RedshiftDataParameters": {
            "Database": "{{string}}",
            "DbUser": "{{string}}",
            "SecretManagerArn": "{{string}}",
            "Sql": "{{string}}",
            "Sqls": [ "{{string}}" ],
            "StatementName": "{{string}}",
            "WithEvent": {{boolean}}
         },
         "RetryPolicy": {
            "MaximumEventAgeInSeconds": {{number}},
            "MaximumRetryAttempts": {{number}}
         },
         "RoleArn": "{{string}}",
         "RunCommandParameters": {
            "RunCommandTargets": [
               {
                  "Key": "{{string}}",
                  "Values": [ "{{string}}" ]
               }
            ]
         },
         "SageMakerPipelineParameters": {
            "PipelineParameterList": [
               {
                  "Name": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         },
         "SqsParameters": {
            "MessageGroupId": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_PutTargets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventBusName](#API_PutTargets_RequestSyntax) **   <a name="eventbridge-PutTargets-request-EventBusName"></a>
The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(arn:aws[\w-]*:events:[a-z]+-[a-z]+-[\w-]+:[0-9]{12}:event-bus\/)?[/\.\-_A-Za-z0-9]+`
Required: No

 ** [Rule](#API_PutTargets_RequestSyntax) **   <a name="eventbridge-PutTargets-request-Rule"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

 ** [Targets](#API_PutTargets_RequestSyntax) **   <a name="eventbridge-PutTargets-request-Targets"></a>
The targets to update or add to the rule.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_PutTargets_ResponseSyntax"></a>

```
{
   "FailedEntries": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "TargetId": "string"
      }
   ],
   "FailedEntryCount": number
}
```

## Response Elements
<a name="API_PutTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedEntries](#API_PutTargets_ResponseSyntax) **   <a name="eventbridge-PutTargets-response-FailedEntries"></a>
The failed target entries.
Type: Array of [PutTargetsResultEntry](API_PutTargetsResultEntry.md) objects

 ** [FailedEntryCount](#API_PutTargets_ResponseSyntax) **   <a name="eventbridge-PutTargets-response-FailedEntryCount"></a>
The number of failed entries.
Type: Integer

## Errors
<a name="API_PutTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** LimitExceededException **
The request failed because it attempted to create resource beyond the allowed service quota.
HTTP Status Code: 400

 ** ManagedRuleException **
This rule was created by an AWS service on behalf of your account. It is managed by that service. If you see this error in response to `DeleteRule` or `RemoveTargets`, you can use the `Force` parameter in those calls to delete the rule or remove targets from the rule. You cannot modify these managed rules by using `DisableRule`, `EnableRule`, `PutTargets`, `PutRule`, `TagResource`, or `UntagResource`.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## Examples
<a name="API_PutTargets_Examples"></a>

### Adds a target to a Lambda function with the ID "MyTargetId" to the rule named "test"
<a name="API_PutTargets_Example_1"></a>

The following is an example of a PutTargets request.

#### Sample Request
<a name="API_PutTargets_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
    "Rule": "test",
    "Targets": [
        {
            "Id": "MyTargetId",
            "Arn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction"
        }
    ]
}
```

#### Sample Response
<a name="API_PutTargets_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
    "FailedEntries": [],
    "FailedEntryCount": 0
}
```

### Use Input Transformer to extract data from an event and input that data to the target
<a name="API_PutTargets_Example_2"></a>

This example extracts the instance and state from an event, puts them into a simple text template, and passes this data to a Lambda function called `MyFunction`.

**Note**
If your are using `InputTransformer` with CloudWatch Logs as a target, the `Template` must be `{"timestamp":<timestamp>,"message":<version-id>}`.

#### Sample Request
<a name="API_PutTargets_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
    "Rule": "testrule",
    "Targets": [
        {
            "Id": "MyTargetId",
            "Arn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "InputTransformer":
              {
                "InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},
                "InputTemplate": "<instance> is in state <status>"
              }
        }
    ]
}
```

### Example
<a name="API_PutTargets_Example_3"></a>

Here is another sample request using `InputTransformer`. The input to the Lambda function is in JSON format, with an array substituted. Below that sample request are examples of an event and the resulting output to the target, using this sample request.

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
    "Rule": "testrule",
    "Targets": [
        {
            "Id": "MyTargetId",
            "Arn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction"
            "InputTransformer":
              {
                "InputPathsMap": {"commandsToRun": "$.detail.commands"},
                "InputTemplate": "{\"commands\": <commandsToRun>}"
              }
        }
    ]
}
```

```
               Incoming event:

{
    "Time": 1225864800,
    "Source": "foo",
    "Resources": ["foo", "foo"],
    "DetailType": "foo",
    "Detail": {
        "commands": ["ls -lrt", "echo HelloWorld!"]
    }
}
```

```
               Output sent to the target:

{
    "commands" : ["ls -lrt", "echo HelloWorld!"]
}
```

### Sends a command to a list of EC2 instances specified by InstanceIds, using Amazon EC2 Run Command
<a name="API_PutTargets_Example_4"></a>

This example illustrates one usage of PutTargets.

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
    "Rule": "testrule",
    "Targets": [
        {
            "Id": "id123456789",
            "Arn": "arn:aws:ssm:us-east-1:12345679012:document/RestartLinuxService",
            "RoleArn": "arn:aws:iam::123456789012:role/MyRoleToAccessEC2"
            "RunCommandParameters": {
                 "RunCommandTargets": [
                    {
                        "Key":"InstanceIds",
                        "Values":["i-123456789012", "i-098765432109"]
                    }
                                       ]
    }

    ]
}
```

### Sends a batch job command to an job queue
<a name="API_PutTargets_Example_5"></a>

When the target is an AWS Batch job queue, the `Arn` field specifies the ARN of the job queue, while `JobDefinition` specifies the ARN of the job definition.

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
   "Rule":"batch-job-rule",
   "Targets":[
      {
         "Id":"id123456789",
         "Arn":"arn:aws:batch:us-west-2:012345678910:job-queue/default",
         "BatchParameters":{
            "ArrayProperties":{
               "Size":25
            },
            "JobDefinition":"arn:aws:batch:us-west-2:012345678910:job-definition/nvidia-smi:1",
            "JobName":"unique-job-name",
            "RetryStrategy":{
               "Attempts":5
            }
         }
      }
   ]
}
```

### Uses KinesisParameters to control the shard assignment
<a name="API_PutTargets_Example_6"></a>

In this example, `KinesisParameters` is used to specify that events related to status changes are sent to a shard specific to the affected instance ID.

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
    "Rule": "StatusChangeRule",
    "Targets": [
           {
        "Id" : "1",
        "Arn": "arn:aws:kinesis:us-east-1:123456789012:function:stream/mystream",
        "KinesisParameters":{
             "PartitionKeyPath":"$.detail.instance-id"}'
    }
]
}
```

### Adds an Amazon Data Firehose data delivery stream as a target
<a name="API_PutTargets_Example_7"></a>

This example sets a Kinesis data delivery stream named `target-stream-name` as a target.

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
    "Rule": "FirehoseExample",
    "Targets": [
           {
        "RoleArn": "arn:aws:iam::123456789012:role/MyRoleToAccessKinesis"
        "Id" : "FirehoseStream",
        "Arn": "arn:aws:firehose:us-east-1:123456789012:deliverystream/target-stream-name",
    }
]
}
```

### Adds a Step Functions state machine as a target
<a name="API_PutTargets_Example_8"></a>

This example targets a state machine called "HelloWorld", and sends the input constant "Hello World\!" to that target.

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
    "Rule": "testrule",
    "Targets": [
           {
        "RoleArn": "arn:aws:iam::123456789012:role/MyRoleToAccessStepFunctions"
        "Arn":"arn:aws:states:us-east-1:123456789012:stateMachine:HelloWorld",
        "Input":"HelloWorld!"
    }
]
}
```

### Adds a target that creates three Amazon ECS tasks based on a task definition
<a name="API_PutTargets_Example_9"></a>

This example uses Amazon ECS as the target. You must have already created the task definition and cluster in Amazon ECS.

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
    "Rule": "test",
    "Targets": [
        {
            "Id": "Target1",
            "RoleArn": "arn:aws:iam::123456789012:role/MyRoleToAccessECS"
            "Arn": "arn:aws:ecs:us-east-1:123456789012:cluster/example-cluster",
            "ECSParameters": {
                  "TaskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:task-definition/example",
                  "TaskCount": 3
             }
         }
    ]
}
```

### Specifying two targets with one command
<a name="API_PutTargets_Example_10"></a>

This example sets two simple targets with one command. In this example, both targets are AWS Lambda functions, but the two targets could be different AWS services as well.

#### Sample Request
<a name="API_PutTargets_Example_10_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
    "Rule": "test",
    "Targets": [
        {
            "Id": "MyTargetId",
            "Arn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction"
        }
        {
            "Id": "MyTargetId2",
            "Arn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction2"
        }
    ]
}
```

### Specifying another account as a target
<a name="API_PutTargets_Example_11"></a>

This example shows cross-account event delivery. The target being added is the event bus of a separate AWS account, which has the AWS account ID of `444455556666`.

**Note**
 `Input`, `InputPath`, and `InputTransformer` are not available with `PutTarget` if the target is an event bus of a different AWS account.

#### Sample Request
<a name="API_PutTargets_Example_11_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
    "Rule": "producer-rule",
    "Targets": [
        {
            "Id": "CrossAccountTargetId",
            "Arn": "arn:aws:events:us-east-1:444455556666:event-bus/default"
        }
   ]
}
```

### Adds a API Gateway API as a target
<a name="API_PutTargets_Example_12"></a>

This example targets an API Gateway API with static and dynamic HTTP parameters.

**Note**
 HTTP parameters with static values are passed through to API Gateway as-is. If you provide a JSON Path (prefixed with "$."), it will be dynamically replaced at runtime with a value from the event payload (before input transformation).

#### Sample Request
<a name="API_PutTargets_Example_12_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutTargets

{
 "Rule": "test",
 "Targets":
  [
    {
     "Id": "testTargetId",
     "Arn": "arn:aws:execute-api:us-east-1:444455556666:py1kl011je/testStage/POST/path1/*/path2/*",
     "RoleArn": "arn:aws:iam::415653183693:role/APIGatewayPOC",
     "HttpParameters":
      {
       "PathParameterValues": ["pp1Val", "pp2Val"],
       "HeaderParameters": {"hp1": "hp1Val", "hp2": "$.detail.header"},
       "QueryStringParameters": {"qsp1": "qsp1Val", "qsp2": "$.source"}
      }
    }
  ]
}
```

## See Also
<a name="API_PutTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/PutTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/PutTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/PutTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/PutTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/PutTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/PutTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/PutTargets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/PutTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/PutTargets)
