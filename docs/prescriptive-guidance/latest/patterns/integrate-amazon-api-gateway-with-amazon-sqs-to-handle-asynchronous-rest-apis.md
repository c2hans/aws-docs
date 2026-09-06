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
| Create a queue. | To create an SQS queue that receives the messages from the REST API:1. Sign in to your [AWS account](https://portal.aws.amazon.com/billing/signup/iam).<br />2. Open the Amazon SQS console at [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/).<br />3. Choose **Create queue**.<br />4. On the **Create queue** page, choose the correct AWS Region from the **Region** dropdown list.<br />5. For **Type**, keep the default setting (**Standard**).<br />6. Enter a **Name** for your queue.<br />7. Keep the default values for all other settings.<br />8. Choose **Create queue**. | App developer |

### Provide access to Amazon SQS
<a name="provide-access-to-sqs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM role. | This IAM role gives API Gateway resources full access to Amazon SQS.1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).<br />2. In the navigation pane, choose **Roles**, **Create role**.<br />3. For **Trusted entity type**, choose **AWS service**.<br />4. For **Use case**, choose **API Gateway** from the dropdown list, and then choose **Next**, **Next**.<br />5. For **Role name**, enter **AWSGatewayRoleForSQS** and an optional description, and then choose **Create role**.<br />6. In the **Roles **pane, search for **AWSGatewayRoleForSQS**, and select its checkbox.<br />7. In the **Permissions policies** section, choose **Add permissions**,** Attach policies**.<br />8. Search for **AmazonSQSFullAccess **and select it.<br />9. Choose **Add permissions**.<br />10. In the **Summary **section of **AWSGatewayRoleForSQS**, copy the Amazon Resource Number (ARN). You will use this ID in a later step. | App developer, AWS administrator |

### Create a REST API
<a name="create-a-rest-api"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a REST API. | This is the REST API that HTTP requests are sent to.1. Open the API Gateway console at [https://console.aws.amazon.com/apigateway/](https://console.aws.amazon.com/apigateway/).<br />2. In the **REST API** section, choose **Build.**<br />3. For **API name**, enter a name and an optional description for your API, keep all other default settings, and then choose **Create API**. | App developer |
| Connect API Gateway to Amazon SQS. | This step enables the message to flow from inside the HTTP request’s body to Amazon SQS.1. On the [API Gateway console](https://console.aws.amazon.com/apigateway/), choose the API that you created.<br />2. On the **Resources **page, in the **Methods **section, choose **Create method**.<br />3. For **Method type**, choose **POST**. <br />4. For **Integration type**, choose **AWS service**.<br />5. For **AWS Region**, choose the Region where you created your SQS queue.<br />6. For **AWS service**, choose **Simple Queue Service (SQS)**.<br />7. For HTTP method, choose **POST**.<br />8. For **Action type**, choose **Use path override**.<br />9. For **Path override**, enter **<AWS account ID>/<name of SQS queue>**.<br />10. For **Execution role**, paste the ARN of the role that you created earlier.<br />11. Choose **Create method**. | App developer |

### Test the REST API
<a name="test-the-rest-api"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the REST API. | Run a test to check for missing configuration:1. On the [API Gateway console](https://console.aws.amazon.com/apigateway/), choose the REST API that you created.<br />2. In the **Resources **pane, choose the **POST **method.<br />3. Choose the **Test** tab. (Use the right arrow if the tab isn't displayed.)<br />4. For **Request body**, paste the following JSON code:<pre>{<br />     "message": "lorem ipsum"<br />}</pre><br />5. Choose** Test**.<br />You will receive an error that's similar to the following:<pre><UnknownOperationException/></pre> | App developer |
| Change the API integration to forward the request properly to Amazon SQS. | Complete the configuration to fix the integration error:1. On the [API Gateway console](https://console.aws.amazon.com/apigateway/), choose the API you created, and then choose **POST**.<br />2. The **Method Execution** section shows the visual mapping between API Gateway and Amazon SQS. From this section, choose **Integration request**, and then choose **Edit**.<br />3. Expand the **HTTP headers** section, and then choose the **Add request header** parameter.For **Name**, specify **Content-Type**.For **Mapped from**, enter** 'application/x-www-form-urlencoded'**. Make sure to include the single quotation marks.Select the **Caching** checkbox.<br />4. Expand the **Mapping templates** section.Choose **Add mapping template**.For **Content type**, enter **application/json**.For **Template body**, paste this code:<pre>Action=SendMessage&MessageBody=$input.body</pre>Choose **Save**. | App developer |
| Test and validate the message in Amazon SQS. | Run a test to confirm that the test completed successfully:1. On the [API Gateway console](https://console.aws.amazon.com/apigateway/), choose the REST API you created.<br />2. In the **Resources** pane, choose the **POST** method.<br />3. Choose the **Test** tab. (Use the right arrow if the tab isn't displayed.)<br />4. For **Request body**, paste the following JSON code:<pre>{<br />     "message": "lorem ipsum"<br />}</pre><br />5. Choose** Test**.<br />6. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/).<br />7. In the navigation pane, choose **Queues**, and then choose your queue.<br />8. Choose **Send and receive messages**.<br />9. Choose **Poll for messages**.<br />10. Choose **Message**. It should display the following:<pre>Body { "message": "lorem ipsum" }</pre> | App developer |
| Test API Gateway with a special character. | Run a test that includes special characters (such as &) that aren't acceptable in a message:1. On the [API Gateway console](https://console.aws.amazon.com/apigateway/), choose your API.<br />2. Repeat the test from the earlier step by using the following JSON code:<pre>{<br />     "message": "lorem ipsum &"<br />}</pre><br />3. Choose** Test**.<br />You will receive an error such as the following:<pre>{<br />  "Error": {<br />    "Code": "AccessDenied",<br />    "Message": "Access to the resource https://sqs.us-east-2.amazonaws.com/976166761794/Apg2 is denied.",<br />    "Type": "Sender"<br />  },<br />  "RequestId": "e83c9c67-bcf6-5e9a-91e9-c737094b17ab"<br />}</pre><br />This is because special characters aren't supported by default in the message body. In the next step, you'll configure API Gateway to support special characters. For more information about content type conversions, see the [API Gateway documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-workflow.html). | App developer |
| Change the API configuration to support special characters. | Adjust the configuration to accept special characters in the message:1. On the [API Gateway console](https://console.aws.amazon.com/apigateway), choose the API you created, and then choose **POST**.<br />2. Choose **Integration request**, and then choose **Edit**.<br />3. Change **Content Handling** to **Convert to text.**<br />4. In the **Mapping templates** section:For **Content type**, enter **application/json**.For **Template body**, specify:<pre>Action=SendMessage&MessageBody=$util.urlEncode($input.body)</pre>Choose **Save**.<br />5. Choose the **Test **tab.<br />6. For **Request body**, enter the JSON code from earlier:<pre>{<br />     " message": "lorem ipsum &" }</pre><br />7. Choose **Test**.<br />8. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/).<br />9. Select your queue, and then choose **Send and receive messages**, **Poll for messages**, **Message **as earlier.<br />The new message should include the special character. | App developer |

### Deploy the REST API
<a name="deploy-the-rest-api"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the API. |  <br />To deploy the REST API:1. Open the [API Gateway console](https://console.aws.amazon.com/apigateway/).<br />2. Choose your API.<br />3. Choose **Deploy API**. For more information about this step, see the [API Gateway documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api-with-console.html). | App developer |
| Test with an external tool. | Run a test with an external tool to confirm that the message is received successfully:1. Open a tool such as Postman, Insomnia, or cURL.<br />2. Run your API.<br />3. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/).<br />4. Select your queue.<br />5. Load messages to see the new message. | App developer |

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
