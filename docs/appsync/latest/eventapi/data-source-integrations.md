---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/data-source-integrations.html
---

# Data source integrations for AWS AppSync events
<a name="data-source-integrations"></a>

With AWS AppSync Events, you can create event handlers that run custom business logic on AWS AppSync's JavaScript runtime. By configuring data source integrations, you can interact with external systems like Lambdafunctions, DynamoDB tables, or Amazon RDS Aurora databases.

**Topics**
+ [Overview](#overview)
+ [Handler structure](#handler-structure)
+ [Direct data source integrations using Lambda](direct-lambda-integrations.md)

## Overview
<a name="overview"></a>

You can integrate data sources in your channel namespaces to interact with DynamoDB tables and Lambda functions. Each integration requires implementing request and response functions. This topic explains how to configure and use data sources with event handlers.

For detailed information about data source configuration options, see [Working with data sources for AWS AppSync Event APIs](https://docs.aws.amazon.com/appsync/latest/eventapi/data-sources-chapter.html).

## Handler structure
<a name="handler-structure"></a>

A handler that interacts with a data source has the following two functions:
+ Request — Defines the payload sent to the data source
+ Response — Defines the payload sent to the data source

**Example Saving events to DynamoDB before broadcasting**
The following example defines an `onPublish` handler that saves all published events to a messages\_table in DynamoDB before forwarding them to be broadcast.

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
  }
}
```

**Note**
You must return the list of events you want broadcasted in the response function.

**Example Forward all events after accessing it from the data source**  <a name="forward-all-events"></a>

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
  response: (ctx) => ctx.events // forward all events
}
```

### onSubscribe handler
<a name="onsubscribe-handler"></a>

Use the onSubscribe handler to process subscription requests.

**Example Logging subscriptions to an RDS database**

```
import { insert, createPgStatement as pg } from '@aws-appsync/utils/rds'

export const onSubscribe = {
  request(ctx) {
    const values = {
      channel: ctx.info.channel.path,
      identity: ctx.identity
    }
    return pg(insert({table: 'subs', values}))
  },
  response(ctx) {} // Required empty function
}
```

**Note**
You must provide a response function, which can be empty if no other action is required.

**Example Granting access based on a channel path**

```
import { select, createPgtatement as pg, toJsonObject } from '@aws-appsync/utils/rds';

export const onSubscribe = {
  request(ctx) {
    const values = {
      channel: ctx.info.channel.path,
      identity: ctx.identity
    }
    return pg(insert({
      select: 'subs',
      where: { channel: { eq: 'ALLOWED' }}
    }))
  },
  response(ctx){
    const { error, result } = ctx;
    if (error) {
        return util.error('db error')
    }
    const res = toJsonObject(result)[1][0];
    if (!res.length) {
      // did not find the item, subscription is not authorized
      util.unauthorized()
    }
  }
}
```

**Example Skipping the data source**  <a name="skip-data-source"></a>
To skip the data source invocation at runtime use the `runtime.earlyReturn` utility. The `earlyReturn` operation returns the provided payload and skips the response function.

```
import * as ddb from `@aws-appsync/utils/dynamodb`

export const onPublish = {
  request(ctx) {
    if (ctx.info.channel.segments.includes('private')) {
      // return early and do no execute the response.
      return runtime.earlyReturn(ctx.events)
    }
    const channel = ctx.info.channel.path
    const event = ctx.events[0]
    const key = { channel, id: event.payload.id }
    return ddb.put({ key, item: event.payload })
  },
  response: (ctx) => ctx.events // forward all events
}
```
