---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_sqs_code_examples.html
---

# Amazon SQS examples using SDK for Rust
<a name="rust_sqs_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with Amazon SQS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)
+ [Serverless examples](#serverless_examples)

## Actions
<a name="actions"></a>

### `ListQueues`
<a name="sqs_ListQueues_rust_topic"></a>

The following code example shows how to use `ListQueues`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/sqs#code-examples).
Retrieve the first Amazon SQS queue listed in the Region.

```
async fn find_first_queue(client: &Client) -> Result<String, Error> {
    let queues = client.list_queues().send().await?;
    let queue_urls = queues.queue_urls();
    Ok(queue_urls
        .first()
        .expect("No queues in this account and Region. Create a queue to proceed.")
        .to_string())
}
```
+  For API details, see [ListQueues](https://docs.rs/aws-sdk-sqs/latest/aws_sdk_sqs/client/struct.Client.html#method.list_queues) in *AWS SDK for Rust API reference*.

### `ReceiveMessage`
<a name="sqs_ReceiveMessage_rust_topic"></a>

The following code example shows how to use `ReceiveMessage`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/sqs#code-examples).

```
async fn receive(client: &Client, queue_url: &String) -> Result<(), Error> {
    let rcv_message_output = client.receive_message().queue_url(queue_url).send().await?;

    println!("Messages from queue with url: {}", queue_url);

    for message in rcv_message_output.messages.unwrap_or_default() {
        println!("Got the message: {:#?}", message);
    }

    Ok(())
}
```
+  For API details, see [ReceiveMessage](https://docs.rs/aws-sdk-sqs/latest/aws_sdk_sqs/client/struct.Client.html#method.receive_message) in *AWS SDK for Rust API reference*.

### `SendMessage`
<a name="sqs_SendMessage_rust_topic"></a>

The following code example shows how to use `SendMessage`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/sqs#code-examples).

```
async fn send(client: &Client, queue_url: &String, message: &SQSMessage) -> Result<(), Error> {
    println!("Sending message to queue with URL: {}", queue_url);

    let rsp = client
        .send_message()
        .queue_url(queue_url)
        .message_body(&message.body)
        // If the queue is FIFO, you need to set .message_deduplication_id
        // and message_group_id or configure the queue for ContentBasedDeduplication.
        .send()
        .await?;

    println!("Send message to the queue: {:#?}", rsp);

    Ok(())
}
```
+  For API details, see [SendMessage](https://docs.rs/aws-sdk-sqs/latest/aws_sdk_sqs/client/struct.Client.html#method.send_message) in *AWS SDK for Rust API reference*.

## Serverless examples
<a name="serverless_examples"></a>

### Invoke a Lambda function from an Amazon SQS trigger
<a name="serverless_SQS_Lambda_rust_topic"></a>

The following code example shows how to implement a Lambda function that receives an event triggered by receiving messages from an SQS queue. The function retrieves the messages from the event parameter and logs the content of each message.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-sqs-to-lambda) repository.
Consuming an SQS event with Lambda using Rust.

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
use aws_lambda_events::event::sqs::SqsEvent;
use lambda_runtime::{run, service_fn, Error, LambdaEvent};

async fn function_handler(event: LambdaEvent<SqsEvent>) -> Result<(), Error> {
    event.payload.records.iter().for_each(|record| {
        // process the record
        tracing::info!("Message body: {}", record.body.as_deref().unwrap_or_default())
    });

    Ok(())
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_max_level(tracing::Level::INFO)
        // disable printing the name of the module in every log line.
        .with_target(false)
        // disabling time is handy because CloudWatch will add the ingestion time.
        .without_time()
        .init();

    run(service_fn(function_handler)).await
}
```

### Reporting batch item failures for Lambda functions with an Amazon SQS trigger
<a name="serverless_SQS_Lambda_batch_item_failures_rust_topic"></a>

The following code example shows how to implement partial batch response for Lambda functions that receive events from an SQS queue. The function reports the batch item failures in the response, signaling to Lambda to retry those messages later.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/lambda-function-sqs-report-batch-item-failures) repository.
Reporting SQS batch item failures with Lambda using Rust.

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
use aws_lambda_events::{
    event::sqs::{SqsBatchResponse, SqsEvent},
    sqs::{BatchItemFailure, SqsMessage},
};
use lambda_runtime::{run, service_fn, Error, LambdaEvent};

async fn process_record(_: &SqsMessage) -> Result<(), Error> {
    Err(Error::from("Error processing message"))
}

async fn function_handler(event: LambdaEvent<SqsEvent>) -> Result<SqsBatchResponse, Error> {
    let mut batch_item_failures = Vec::new();
    for record in event.payload.records {
        match process_record(&record).await {
            Ok(_) => (),
            Err(_) => batch_item_failures.push(BatchItemFailure {
                item_identifier: record.message_id.unwrap(),
            }),
        }
    }

    Ok(SqsBatchResponse {
        batch_item_failures,
    })
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    run(service_fn(function_handler)).await
}
```
