---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/bb-realtime-async.html
---

# Realtime and async

This section covers AWS CDK Blocks for realtime communication and background processing.

## Choosing a realtime or async Block
<a name="_choosing_a_realtime_or_async_block"></a>

| Block | Best for | Avoid when |
| --- | --- | --- |
|  `Realtime`  | Live updates, chat, notifications, collaborative features via WebSocket | Your use case is request/response only (no persistent connections needed) |
|  `AsyncJob`  | Long-running background tasks, event-driven processing, queue-based workloads | The task completes in under a few seconds (handle it synchronously) |
|  `CronJob`  | Scheduled recurring tasks, periodic cleanup, report generation | You need immediate execution triggered by an event (use AsyncJob) |

## Realtime
<a name="bb-realtime"></a>

Typed WebSocket pub/sub channels. Define each namespace with a schema for type-safe message broadcasting. Any Standard Schema library works, such as Zod. Publish messages from the server and subscribe from the client. Each namespace can have multiple channels for topic-based routing.

Locally, Realtime uses an in-process EventEmitter with a local WebSocket server. On AWS, it provisions one shared API Gateway WebSocket API for the app, with a DynamoDB table for connection management. Best for live updates, chat, notifications, and collaborative features.

For more information, see [bb-realtime on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-realtime).

## AsyncJob
<a name="bb-async-job"></a>

Background job processing. Submit work that runs asynchronously outside the request lifecycle. Define a handler function that processes each job payload. By default, jobs are fire-and-forget from the caller’s perspective, with automatic retries on failure. Set `trackStatus: true` to record each job’s state (`queued`, `processing`, `complete`, or `failed`) and read it with `getStatus()` or `waitUntilComplete()`. A job is `failed` when the handler throws on its last attempt. Status tracking adds a DynamoDB table.

Locally, AsyncJob executes handlers in-process. On AWS, it provisions an SQS queue with a Lambda consumer, or a container consumer when you assign it to a container `Compute`. Each job gets 3 delivery attempts (`maxRetries`) before it moves to a dead-letter queue that keeps messages for 14 days. The consumer receives up to 10 jobs per batch (`batchSize`) and waits up to 5 seconds to fill a batch (`maxBatchingWindowSeconds`). The queue’s visibility timeout is the 15-minute handler timeout plus the batching window, so 905 seconds by default. Best for tasks that don’t need an immediate response: sending emails, processing uploads, generating reports.

For more information, see [bb-async-job on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-async-job).

## CronJob
<a name="bb-cron-job"></a>

Scheduled task execution. Define a handler function and a cron expression or rate schedule. The handler runs automatically at the specified interval. Cron expressions use UTC unless you set `timezone` to an IANA time zone name, such as `America/Los_Angeles`. Set `enabled: false` to create the schedule turned off. Use `input` to pass the same typed payload to the handler on every run.

Locally, CronJob executes on schedule using Node.js timers. On AWS, it provisions an Amazon EventBridge Scheduler schedule that invokes a Lambda function. Best for periodic maintenance, batch processing, cleanup jobs, and report generation.

For more information, see [bb-cron-job on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-cron-job).
