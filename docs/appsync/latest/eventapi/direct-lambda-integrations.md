---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/direct-lambda-integrations.html
---

# Direct data source integrations using Lambda
<a name="direct-lambda-integrations"></a>

AWS AppSync lets you integrate Lambda functions directly with your channel namespace without writing additional handler code. Both *publish* and *subscribe* operations are supported through `Request`/`Response` mode and `event` mode.

**Note**
Configuring your direct Lambda integration in `event` mode triggers your Lambda aysncronously and does not wait for a reply. The result of the invocation does not impact the rest of the `onPublish` or `onSubscribe` handling.

## How it works
<a name="how-it-works"></a>

Your Lambda function receives a context object containing event information. The function then passes a context object containing information for the events. The Lambda function can perform the following operations.
+ Filter and transform events for broadcasting
+ Return error messages for failed processing
+ Handle both publish and subscribe operations

**Example Setting a Lambda configuration of a channel namespace in AWS CloudFormation**
Set up a direct Lambda integration, configure `handlerConfigs` on your [channel namespace](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-channelnamespace.html) using AWS CloudFormation.

```
{
  "Type" : "AWS::AppSync::ChannelNamespace",
  "Properties" : {
    "ApiId" : "api-id-123",
    "Name" : "lambda-direct-ns",
    "HandlerConfigs" : {
      "OnPublish": {
        "Behavior": "DIRECT",
        "Integration": {
          "DataSourceName": "LAMBDA_FUNCTION_DS",
          "LambdaConfig": {
            "InvokeType": "REQUEST_RESPONSE"
          }
        }
      }
    }
  }
}
```

**Example Setting a Lambda configuration of a channel namespace in the AWS Cloud Development Kit (AWS CDK)**

```
api.addChannelNamespace('lambda-direct-ns', {
  publishHandlerConfig: {
    dataSource: lambdaDataSource,
    direct: true,
  },
});
```
With this configuration, you do not need to provide code for your channel namespace. Your Lambda function will be called for every `onPublish` event.

**Example `onPublish` response format**  <a name="onpublish-response"></a>
`onPublish` handlers that are configured with the `REQUEST_RESPONSE` invocation type must return a response payload with the following structure.

```
type LambdaAppSyncEventResponse = {
  events?: OutgoingEvent[], // array of outgoing events to broadcast
  error?: string //Optional error message if processing fails
}
```

**Note**
If you use `EVENT` as the invocation type, your Lambda function is trigged asynchronously and AWS AppSync does not wait for a response. AWS AppSync broadcasts the events as usual.
If you include an error message in the response when logging is enabled, AWS AppSync Events logs the error message but doesn't return it to the publisher.

**Example onSubscribe response format**  <a name="onsubscribe-response"></a>
For `onSubscribe` handlers configured with `REQUEST_RESPONSE` invocation type, your Lambda function must return one of the following.
+ A payload containing an error message
+ `null` to indicate a successful subscription

```
type LambdaAppSyncEventResponse = {
  error: string // Error message if subscription fails
} | null
```

## Best practices
<a name="best-practices"></a>

We recommend the following best practices for using direct Lambda integrations.
+ Enable logging to track error messages.
+ Ensure your Lambda function handles both success and error cases.
+ Test your integration with various payload scenarios.

## Powertools for Lambda
<a name="powertools"></a>

You can utilize the following Powertools for Lambda to efficiently write your Lambda function handlers the following languages.
+ [TypeScript/Node.js ](https://docs.powertools.aws.dev/lambda/typescript/latest/features/event-handler/appsync-events/)
+ [Python](https://docs.powertools.aws.dev/lambda/python/latest/core/event_handler/appsync_events/)
+ [.NET ](https://docs.powertools.aws.dev/lambda/dotnet/core/event_handler/appsync_events/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
