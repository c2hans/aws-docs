---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/faq.html
---

# FAQ
<a name="faq"></a>

## How can I combine different integration patterns?
<a name="faq1"></a>

In most situations you will want to combine integration patterns. For example, you can use AWS Step Functions to orchestrate a process that calls a remote service by using the claim check pattern. Or, you might have an orchestrated process that puts messages into queues, which, in turn, trigger choreographed services.

## What is the primary benefit of using a microservices architecture?
<a name="faq2"></a>

The main advantages include independent scaling of services, improved fault isolation, enhanced development speed through parallel team work, and the ability for continuous delivery and deployment (CI/CD).

## How can I implement error handling in these patterns?
<a name="faq3"></a>

You can implement error handling by using built-in mechanisms in AWS services. For example, AWS Lambda functions can be configured with retry logic, and Amazon SQS supports dead-letter queues for handling persistent failures. Additionally, Step Functions provides error handling and retry mechanisms at the workflow level.

## What are the benefits of using the claim check pattern in asynchronous communication?
<a name="faq4"></a>

The claim check pattern allows clients to receive an identifier upon request submission. This identifier can be used later to check the status and retrieve the result. This pattern benefits clients by providing a mechanism to poll for results without waiting synchronously. For more information, see the [Claim check](asynchronous.md#claim-check) section earlier in this guide.

## How does the callback pattern improve asynchronous communication in microservices?
<a name="faq5"></a>

The callback pattern improves asynchronous communication by allowing the client to provide a location for the service to contact upon completion of processing. This decouples the client from waiting for a response, and enables it to continue with other tasks. For more information, see the [Callback](asynchronous.md#callback) section earlier in this guide.

## Can I implement bidirectional communication in microservices by using the patterns described?
<a name="faq6"></a>

You can implement bidirectional communication by creating a stateful connection between a client and a service, so they can both send and process messages asynchronously. This requires the service to support an open connection for each client. For more information, see the [Bidirectional communication](asynchronous.md#bidirectional) section earlier in this guide.

## How can I optimize the use of Lambda functions in asynchronous communication patterns?
<a name="faq7"></a>

You can optimize Lambda functions by ensuring they are idempotent to handle potential message duplications, by using Amazon SQS features such as message groups for ordering, and by implementing long polling to reduce costs. Additionally, you can monitor execution metrics to identify optimization opportunities.

## What are the key differences between using Amazon SNS and EventBridge for the pub/sub pattern?
<a name="faq8"></a>

Amazon SNS sends a single message to all subscribers, which may include unnecessary data for some subscribers. Amazon EventBridge allows for more granular control by allowing you to have several rules that match a single event, with each rule triggering a different downstream service or action. For more information, see the [Amazon SNS](sns.md) and [Amazon EventBridge](eventbridge.md) sections earlier in this guide.
