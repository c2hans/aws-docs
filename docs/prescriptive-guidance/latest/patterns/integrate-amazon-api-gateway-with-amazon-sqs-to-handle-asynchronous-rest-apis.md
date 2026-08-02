---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html
---

# Integrate Amazon API Gateway with Amazon SQS to handle asynchronous REST APIs
<a name="integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis"></a>

*Natalia Colantonio Favero and Gustavo Martim, Amazon Web Services*

## Summary
<a name="integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis-summary"></a>

When you deploy REST APIs, sometimes you need to expose a message queue that client applications can publish. For example, you might have problems with the latency of third-party APIs and delays in responses, or you might want to avoid the response time of database queries or avoid scaling the server when there are a large number of concurrent APIs. In these scenarios, the client applications that publish to the queue only need to know that the API received the data—not what happens after the data was received.

This pattern creates a REST API endpoint by using [Amazon API Gateway](https://aws.amazon.com/api-gateway/) to send a message to [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/). It creates an easy-to-implement integration between the two services that avoids direct access to the SQS queue.

## Prerequisites and limitations
<a name="integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis-prereqs"></a>
+ An [active AWS account](https://portal.aws.amazon.com/billing/signup/iam)

## Architecture
<a name="integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis-architecture"></a>

![Architecture for integrating API Gateway with Amazon SQS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/70984dee-e49f-4446-9d52-49ce826c3909/images/737ba0b2-da8f-4478-8c54-0a4835fd69f9.png)

The diagram illustrates these steps:

1. Request a POST REST API endpoint by using a tool such as Postman, another API, or other technologies.

1. API Gateway posts a message, which is received on the request's body, on the queue.

1. Amazon SQS receives the message and sends an answer to API Gateway with a success or failure code.

## Tools
<a name="integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis-tools"></a>
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) helps you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) provides a secure, durable, and available hosted queue that helps you integrate and decouple distributed software systems and components.

## Epics
<a name="integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis-epics"></a>

### Create an SQS queue
<a name="create-an-sqs-queue"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a queue. | To create an SQS queue that receives the messages from the REST API:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html) | App developer |

### Provide access to Amazon SQS
<a name="provide-access-to-sqs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM role. | This IAM role gives API Gateway resources full access to Amazon SQS.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html) | App developer, AWS administrator |

### Create a REST API
<a name="create-a-rest-api"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a REST API. | This is the REST API that HTTP requests are sent to.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html) | App developer |
| Connect API Gateway to Amazon SQS. | This step enables the message to flow from inside the HTTP request’s body to Amazon SQS.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html) | App developer |

### Test the REST API
<a name="test-the-rest-api"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the REST API. | Run a test to check for missing configuration:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html) | App developer |
| Change the API integration to forward the request properly to Amazon SQS. | Complete the configuration to fix the integration error:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html) | App developer |
| Test and validate the message in Amazon SQS. | Run a test to confirm that the test completed successfully:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html) | App developer |
| Test API Gateway with a special character. | Run a test that includes special characters (such as &) that aren't acceptable in a message:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html)<br />This is because special characters aren't supported by default in the message body. In the next step, you'll configure API Gateway to support special characters. For more information about content type conversions, see the [API Gateway documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-workflow.html). | App developer |
| Change the API configuration to support special characters. | Adjust the configuration to accept special characters in the message:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html)<br />The new message should include the special character. | App developer |

### Deploy the REST API
<a name="deploy-the-rest-api"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the API. |  <br />To deploy the REST API:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html) | App developer |
| Test with an external tool. | Run a test with an external tool to confirm that the message is received successfully:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis.html) | App developer |

### Clean Up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the API. | On the [API Gateway console](https://console.aws.amazon.com/apigateway/), choose the API you created, and then choose **Delete**. | App developer |
| Delete the IAM role. | On the [IAM console](https://console.aws.amazon.com/iam/), in the **Roles** pane, select **AWSGatewayRoleForSQS**, and then choose **Delete**. | App developer |
| Delete the SQS queue. | On the [Amazon SQS console](https://console.aws.amazon.com/sqs/), in the **Queues** pane, choose the SQS queue you created, and then choose **Delete**. | App developer |

## Related resources
<a name="integrate-amazon-api-gateway-with-amazon-sqs-to-handle-asynchronous-rest-apis-resources"></a>
+ [SQS-SendMessage](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html#SQS-SendMessage) (API Gateway documentation)
+ [Content type conversions in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-workflow.html) (API Gateway documentation)
+ [$util variables](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#util-template-reference) (API Gateway documentation)
+ [How do I integrate an API Gateway REST API with Amazon SQS and resolve common errors?](https://repost.aws/knowledge-center/api-gateway-rest-api-sqs-errors) (AWS re:Post article)
