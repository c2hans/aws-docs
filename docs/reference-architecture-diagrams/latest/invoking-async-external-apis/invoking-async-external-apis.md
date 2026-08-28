---
source_url: https://docs.aws.amazon.com/reference-architecture-diagrams/latest/invoking-async-external-apis/invoking-async-external-apis.html
---

# Invoking Asynchronous External APIs
<a name="invoking-async-external-apis"></a>

Publication date: **January 30, 2023 ([Diagram history](#diagram-history))**

This architecture shows how to call third-party services that implement the service callback pattern to process long-running jobs. You build an orchestration with [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) to manage request lifecycles, throttle calls to the external service according to the maximum-requests-per-second (RPS) contract, and pause request workflows until you receive a callback notification.

## Invoking Asynchronous External APIs
<a name="diagram1"></a>

![Architecture diagram showing asynchronous external API invocation using AWS Step Functions, Amazon Simple Queue Service, AWS Lambda, Amazon API Gateway, and Amazon DynamoDB.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/invoking-async-external-apis/images/invoking-async-external-apis.png)

The following steps describe the architecture:

1. Set up Step Functions to handle the lifecycle of long-running requests to a third-party service. Add a request step that pauses the workflow, waiting for a task token to continue. Set a timeout to fail the workflow if a callback is not received.

1. Send the task token and request payload to an [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) queue. Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to monitor the queue length and consider adjusting the contract if length grows beyond limits.

1. Use [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) to poll Amazon SQS and trigger an express Step Functions workflow. Control the invocation rate using polling batch size, reserved concurrency, and maximum concurrency.

1. Add a dynamic delay inside Lambda controlled by AWS AppConfig if the system needs a lower invocation rate to comply with the contracted RPS.

1. Step Functions invokes an [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) HTTP proxy API configured with a rate limit to comply with the contracted RPS.

1. Invoke the external third-party asynchronous service API sending the payload consumed from the requests queue, and receive the job ID. Send failed requests to the dead letter queue (DLQ) using Amazon SQS.

1. Store the workflow's task token and the received job ID in a token store implemented with [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html).

1. When the external service completes, receive the completed job ID in a callback webhook endpoint implemented with API Gateway.

1. Transform external callbacks with API Gateway mapping templates, add the payload and job ID to an Amazon SQS queue, and respond immediately to the caller.

1. Use Lambda to poll the callback Amazon SQS queue, query the token store, and use the token to unblock the waiting workflow. Store failed messages in a callback DLQ.

1. On the workflow, pass the job ID to the next step and invoke a Step Functions processor to fetch results from the external third-party results store by job ID. Process the external service's results.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date |
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | January 30, 2023 |

**Note**
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Reference Architecture Diagrams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query reference-architecture-diagrams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
