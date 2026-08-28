---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/channel-namespace-handlers.html
---

# Process real-time events with AWS AppSync event handlers
<a name="channel-namespace-handlers"></a>

**Topics**
+ [Overview](#event-handlers-overview)
+ [onPublish handler](#event-handler-onpublish)
+ [onSubscribe handler](#event-handler-onsubscribe)
+ [Error handling](#error-handling)

## Overview
<a name="event-handlers-overview"></a>

AWS AppSync Event handlers let you run custom business logic on real-time events.

These JavaScript functions:
+ Run on the AWS AppSync runtime
+ Process published events
+ Authorize subscription requests

This topic covers *simple* event handlers without data source integration. For information about integrating with data sources like DynamoDB tables and Lambda functions, see the following topics:
+ [Data source integrations](https://docs.aws.amazon.com/appsync/latest/eventapi/data-source-integrations.html)
+ [Direct Lambda integrations](https://docs.aws.amazon.com/appsync/latest/eventapi/direct-lambda-integrations.html)

**Note**
Event handlers run after the incoming request is authorized through your configured authorization mode.

## onPublish handler
<a name="event-handler-onpublish"></a>

Use the `onPublish` handler to process and filter events before they reach subscribers. This handler runs each time an event is published to a channel.

The handler uses this signature:

```
function onPublish(context: Context): OutgoingEvent[] | null
```

```
type Context = {
  events: IncomingEvent[];  // Array of events to process
  channel: string;          // Channel the events were published to
  identity: Identity;       // Information about the publisher
  info: {
    channel: {
      path: string;        // Full channel path
      segments: string[];  // Path segments
    }
  }
  channelNamespace: {
    name: string
  }
  operation: 'SUBSCRIBE' | 'PUBLISH'
}
```

The handler receives a context object with:
+ `events` - Array of events to process
+ `channel` - Target channel name
+ `identity` - Publisher information

For more information on the context object reference, see the [Context Reference guide](context-reference.md).

### Common onPublish tasks
<a name="common-onpublish-tasks"></a>

#### Forward all events
<a name="forward-events"></a>

The default API behavior for the `onPublish` handler *forwards all received events*. The onPublish function needs a context object as a parameter.

```
export function onPublish(ctx) {
  return ctx.events
}
```

#### Filter specific events
<a name="filter-events"></a>

Filter out events and return only those matching specific criteria. In the following example, the handler filters the events and only forwards those that have *odds greater than 0.5*.

```
export function onPublish(ctx) {
  return ctx.events.filter((event) => event.payload.odds > 0.5)
}
```

#### Transform events
<a name="transform-events"></a>

Transform events by mapping them to a new shape. In the following example, the handler below formats each event to include a *timestamp* and changes the message to upper case format.

```
import { util } from '@aws-appsync/utils'

export function onPublish(ctx) {
  return ctx.events.map(event => ({
    id: event.id,
    payload: {
      ...event.payload,
      message: event.payload.message.toUpperCase(),
      timestamp: util.time.nowISO8601()
    }
  }))
}
```

### Important rules for onPublish
<a name="onpublish-rules"></a>
+ Avoid duplicate event IDs
+ Events with an `error` property won't broadcast
+ `Null` values in the returned array are ignored
+ Returns an array of events or null
+ Match each returned event ID to an incoming event
+ Using an unknown event ID will result in an error

## onSubscribe handler
<a name="event-handler-onsubscribe"></a>

Use the `onSubscribe` handler to authorize and process subscription requests before allowing channel subscriptions. The handler in the following example runs when the client subscribes.

The handler uses this signature:

```
function onSubscribe(context: Context): void
```

For more information on the context object reference, see [the Context Reference Guide](https://docs.aws.amazon.com/appsync/latest/eventapi/context-reference.html).

### Examples
<a name="onsubscribe-examples"></a>

**Example Logging a subscription request**  <a name="logging-subscription"></a>
In the following example, a Amazon Cognito user pool authorization is used and the `onSubscribe` handler logs a message when an admin user subscribes to a channel.

```
export function onSubscribe(ctx) {
  if (ctx.identity.groups.includes('admin')) {
    console.log(`Admin ${ctx.identity.sub} subscribed to ${ctx.channel}`)
  }
}
```

**Example Reject a request**  <a name="reject-subscription"></a>
In the following example, a subscription request is rejected by calling `util.unauthorized()`. The `onSubscribe` handler restricts the Amazon Cognito user pool's authenticated users to their own channel. Clients can only subscribe to channels that match the pattern `/messages/inbox/[username]`.

```
export function onSubscribe(ctx) {
  const requested = ctx.info.channel.path
  const allowed = `/messages/inbox/${ctx.identity.username}`

  if (requested !== allowed) {
    util.unauthorized()
  }
}
```

## Error handling
<a name="error-handling"></a>

Use error handling to manage invalid requests and provide meaningful feedback to users. This toipic explains how to implement error handling for both *HTTP endpoints* and *WebSocket connections*. To reject requests and return errors to publishers or subscribers, use the `utility.error` function. When the publishing is done using the HTTP endpoint, it returns an HTTP `403` response.

**Note**
When publishing is done over an HTTP endpoint, it returns an HTTP `403` response.
When publishing over WebSocket, it returns a `publish_error` message with the provided message.

### Examples
<a name="error-handling-examples"></a>

The following examples demonstrates how to return an error message.

**Example Validating required message properties**  <a name="validate-properties"></a>

```
export function onPublish(ctx) {
  return ctx.events.map(event => {
    if (!event.payload.message) {
      event.error = "Message required"
    }
    return event
  })
}
```

**Example Rejecting entire requests**  <a name="reject-requests"></a>

```
export function onPublish(ctx) {
  util.error("Operation not allowed")
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
