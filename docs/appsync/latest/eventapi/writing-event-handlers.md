---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/writing-event-handlers.html
---

# Writing event handlers
<a name="writing-event-handlers"></a>

A handler is defined by a single function that doesn't interact with a data source, or is defined by an object that implements a request and a response function to interact with one of your data sources. When working with a Lambda function data source, AWS AppSync Events supports a `DIRECT` integration that allows you to interact with your Lambda function without writing any handler code.

You provide your code for the handlers using the namespace's code property. Essentially, you use a "single file" to define all your handlers. In your code file, you identify your handler definitions by exporting a function or object named onPublish or onSubscribe.

## Handler with no data source integration
<a name="no-datasource-handler"></a>

You can define a handler with no data source integration. In this case, the handler is defined as a single function. In the following example, the onPublish handler shows the default behavior when no handler is defined. It simply forwards the list of events.

```
export function onPublish(ctx) {
  return ctx.events
}
```

As an alternate example, this definition returns an empty list, which means that no event will be broadcast to the subscribers.

```
export const onPublish = (ctx) => ([])
```

In this example, the handler only returns the list of published events, but adds the property `msg` to the payload.

```
export function onPublish(ctx) {
  return ctx.events.map(({id, payload}) => {
    return {id: payload: {...payload, msg: "Hello!"}}
  })
}
```

## Handler with a data source integration
<a name="with-datasource-handler"></a>

You can define a handler with a data source integration. In this case, you define an object that implements and `request` and a `response` function. The `request` function defines the payload that is sent to invoke the data source while the `response` function receives the result of that invocation. The list of events to broadcast is returned by the `response` function.

The following example defines an `onPublish` handler that saves all published events to a `messages_table` before forwarding them to be broadcast. The `onSubscribe` handler doesn't have a data source integration and is defined by a single function that simply logs a message.

```
import * as ddb from `@aws-appsync/utils/dynamodb`

const TABLE = 'messages_table'
export const onPublish = {
  request(ctx) {
    const channel = ctx.info.channel.path
    return ddb.batchPut({
      tables: {
        [TABLE]: ctx.events.map(({ id, payload }) => ({ channel, id, ...payload })),
      },
    })
  },
  response(ctx) {
    console.log(`Batch Put result:`, ctx.result.data[TABLE])
    return ctx.events
  },
}

export const onSubscribe = (ctx) => {
  console.debug(`Joined the chat: ${ctx.info.channel.path}`)
}
```

## Skipping the data source
<a name="skip-datasource"></a>

You might have situations where you need to skip the data source invocation at run time. You can do this by using the `runtime.earlyReturn` utility. `earlyReturn` immediately returns the provided payload and skips the response function.

```
import * as ddb from `@aws-appsync/utils/dynamodb`

const TABLE = 'messages_table'
export const onPublish = {
  request(ctx) {
    if (ctx.info.channel.segments.includes('private')) {
      // return early and do no execute the response.
      return runtime.earlyReturn(ctx.events)
    }
    const channel = ctx.info.channel.path
    return ddb.batchPut({
      tables: {
        [TABLE]: ctx.events.map(({ id, payload }) => ({ channel, id, ...payload })),
      },
    })
  },
  response(ctx) {
    return ctx.result.data[TABLE].map(({ id, ...payload }) => ({ id, payload }))
  },
}
```

## Returning an error
<a name="return-error"></a>

During the execution of an event handler, you might need to return an error back to the publisher or subscriber. Use the `util.error` function to do this. When publishing is done using the HTTP endpoint, this returns an HTTP 403 response. When publishing over WebSocket, this returns a `publish_error` message with the provided message. The following example demonstrates how to return an error message.

```
export function onPublish(ctx) {
  util.error("Not possible!")
  return ctx.events
}
```

## Unauthorizing a request
<a name="unauthorizing-request"></a>

Your event handlers are always called after AWS AppSync has authorized the requests. However, you can run additional business logic and unauthorize a request in your event handler using the `util.unauthorize` function. When publishing over HTTP, this returns an HTTP 401 response. Over WebSocket, this returns a `publish_error` message with an `UnauthorizedException` error type. When trying to connect over WebSocket, you get a `subscribe_error` with an `Unauthorized` error type.

```
export function onSubscribe(ctx) {
  if (somethingNotValid() === true) {
    util.unauthorized()
  }
}

function somethingNotValid() {
  // implement custom business logic
}
```

## Direct Lambda integration
<a name="direct-lambda-integration"></a>

AWS AppSync lets you integrate Lambda functions directly with your channel namespace without writing additional handler code. This integration supports both publish and subscribe operations through Request/Response mode.

**How it works**

When AWS AppSync calls your Lambda function, it passes a context object containing event information. Then, the Lambda function can perform the following operations:
+ Filter and transform events for broadcasting
+ Return error messages for failed processing
+ Handle both publish and subscribe operations

**Publish operation response format**

For `onPublish` handlers, your Lambda function must return a response payload with the following structure:

```
type LambdaAppSyncEventResponse = {
  /** Array of outgoing events to broadcast */
  events?: OutgoingEvent[],

  /** Optional error message if processing fails */
  error?: string
}
```

**Note**
If you include an error message in the response, AWS AppSync logs it (when logging is enabled) but doesn't return it to the publisher.

**Subscribe operation response**

For `onSubscribe` handlers, your Lambda function must return one of the following:
+ A payload containing an error message
+ `null` to indicate a successful subscription

```
type LambdaAppSyncEventResponse = {
  /** Error message if subscription fails */
  error: string
} | null
```

**Best practices**

We recommend the following best practices for direct Lambda integrations:
+ Enable logging to track error messages.
+ Ensure your Lambda function handles both success and error cases.
+ Test your integration with various payload scenarios.

**Utilizing Powertools for Lambda**

You can utilize Powertools for Lambda to efficiently write your Lambda function handlers. To learn more, see the following Powertools for AWS Lambda documentation resources:
+ TypeScript/Node.js — See [https://docs.powertools.aws.dev/lambda/typescript/latest/features/event-handler/appsync-events/](https://docs.powertools.aws.dev/lambda/typescript/latest/features/event-handler/appsync-events/) in the *Powertools for AWS Lambda (TypeScript)* documentation.
+ Python — See [https://docs.powertools.aws.dev/lambda/python/latest/core/event\_handler/appsync\_events/](https://docs.powertools.aws.dev/lambda/python/latest/core/event_handler/appsync_events/) in the *Powertools for AWS Lambda (Python)* documentation.
+ .NET — See [https://docs.powertools.aws.dev/lambda/dotnet/core/event\_handler/appsync\_events/](https://docs.powertools.aws.dev/lambda/dotnet/core/event_handler/appsync_events/) in the *Powertools for AWS Lambda (.NET) * documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
