---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-eventbridge.html
---

# Amazon EventBridge connector
<a name="connector-eventbridge"></a>

The Amazon EventBridge connector publishes events to a custom EventBridge event bus when asset lifecycle events occur. Use this connector to fan out resource events to multiple downstream consumers through EventBridge rules — notifying external systems, triggering workflows in other AWS accounts, or feeding event-driven architectures.

EventBridge is a publish-only connector type. It sends events outward from SDMA but does not derive content or serve resources inward. This is intentional — EventBridge is a publish bus with no natural inbound read path.

Step type: `eventBridgePutEvents`

Filters, `output` blocks, and `${…​}` variables work the same way for every connector type. For more information, see [Trigger filters](connector-configuration.md#trigger-filters), [Output routing](connector-configuration.md#output-routing), and [Variable substitution](connector-configuration.md#variable-substitution).

## Roles
<a name="eventbridge-roles"></a>

| Role | Description |
| --- | --- |
| Publisher | Sends structured events to an EventBridge event bus when asset lifecycle events occur. The event detail contains the mapped asset metadata. |
| Step type | Participates in multi-step triggers alongside other step types. An `eventBridgePutEvents` step can appear as the final step in a workflow — for example, after writing metadata to S3 and invoking a Lambda function. |

## Prerequisites
<a name="eventbridge-prerequisites"></a>

1. Create or identify the target EventBridge custom event bus.

1. Create an IAM role:
   +  **Role name** must start with `SpatialDataManagementContentPublisher-`.
   +  **Trust policy** must allow the SDMA connector invocation Lambda to assume it:

     ```
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Principal": {
             "AWS": [
               "<connector-invocation-role-arn>",
               "<async-connector-invocation-role-arn>"
             ]
           },
           "Action": "sts:AssumeRole"
         }
       ]
     }
     ```

     Replace `<connector-invocation-role-arn>` and `<async-connector-invocation-role-arn>` with the execution role ARNs of the connector invocation Lambda functions in your SDMA deployment.

     If you have AWS CLI access, you can find these values by running:

     ```
     aws lambda get-function \
       --function-name SpatialDataManagement-ConnectorInvocationFunction \
       --query 'Configuration.Role' --output text

     aws lambda get-function \
       --function-name SpatialDataManagement-ConnectorInvocationAsyncFunction \
       --query 'Configuration.Role' --output text
     ```

     Alternatively, in the AWS Lambda console, open the [SpatialDataManagement-ConnectorInvocationFunction](https://console.aws.amazon.com/lambda/home#/functions/SpatialDataManagement-ConnectorInvocationFunction) and [SpatialDataManagement-ConnectorInvocationAsyncFunction](https://console.aws.amazon.com/lambda/home#/functions/SpatialDataManagement-ConnectorInvocationAsyncFunction) functions and find the role name for each under **Configuration** > **Permissions**. Use these names to construct the full ARNs (for example, `arn:aws:iam::<account-id>:role/<connector-invocation-role-name>`).
   +  **Permissions policy** must grant `events:PutEvents` on the target event bus:

     ```
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": "events:PutEvents",
           "Resource": "arn:aws:events:<region>:<account-id>:event-bus/<event-bus-name>"
         }
       ]
     }
     ```

## Using EventBridge as a publisher
<a name="eventbridge-as-publisher"></a>

### Example – publish asset events to an event bus
<a name="_example-publish-asset-events-to-an-event-bus"></a>

```
{
  "securityConfig": {
    "type": "AssumeRole",
    "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-EventBridge"
  },
  "eventBridgeConfig": {
    "eventBusArn": "arn:aws:events:<region>:<account-id>:event-bus/<event-bus-name>",
    "source": "sdma.connectors",
    "detailType": "AssetLifecycleEvent"
  },
  "defaultStepConfig": {
    "stepType": "eventBridgePutEvents"
  },
  "fieldMappings": [
    { "source": "asset.assetId", "target": "assetId" },
    { "source": "asset.assetName", "target": "assetName" },
    { "source": "project.projectId", "target": "projectId" }
  ],
  "triggers": [
    {
      "description": "Publish asset lifecycle events",
      "resources": ["asset"],
      "events": ["create", "update", "delete"],
      "steps": [{}]
    }
  ]
}
```

Downstream consumers create EventBridge rules that match on `source` and `detailType` to route events to AWS Step Functions state machines, Amazon SQS queues, AWS Lambda functions, or other targets.

## Using EventBridge as a step type in multi-step triggers
<a name="eventbridge-as-step-type"></a>

The `eventBridgePutEvents` step type can appear in multi-step triggers. A common pattern is to write metadata to S3, invoke a Lambda function, and then publish a notification event:

```
"steps": [
  {
    "stepType": "s3PutObject",
    "s3Config": { "objectKey": "assets/${asset.assetId}.json" }
  },
  {
    "stepType": "lambdaInvoke",
    "lambdaConfig": {
      "functionArn": "arn:aws:lambda:<region>:<account-id>:function:post-process"
    }
  },
  {
    "stepType": "eventBridgePutEvents",
    "eventBridgeConfig": {
      "eventBusArn": "arn:aws:events:<region>:<account-id>:event-bus/notifications",
      "source": "sdma.connectors",
      "detailType": "AssetPublished"
    }
  }
]
```

## Configuration fields
<a name="eventbridge-config-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `eventBridgeConfig.eventBusArn`  | Yes | ARN of the target EventBridge custom event bus. |
|  `eventBridgeConfig.source`  | Yes | Event source string. Use a descriptive namespace (for example, `sdma.connectors`). |
|  `eventBridgeConfig.detailType`  | Yes | Event detail type. Downstream rules match on this value. |
|  `securityConfig`  | Yes | Connector-level authentication configuration, a sibling of `eventBridgeConfig`. Must use `AssumeRole` type. |
|  `payload.fields`  | No | Array of field names to include in the event detail. If omitted, all mapped fields are included. |
