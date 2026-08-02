---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/lambda-event-filtering-partial-batch-responses-for-sqs/benefits-lambda-event-filters.html
---

# Benefits of using Lambda event filters for Amazon SQS event sources
<a name="benefits-lambda-event-filters"></a>

Configuring Lambda event filters gives your functions the ability to be invoked only by the filtering criteria that you specify. This helps reduce traffic to the functions and simplifies code, which can help reduce cost.

If no event filters are configured, it's possible for a Lambda function to receive irrelevant** **Amazon SQS events that cause the function to invoke unnecessarily. These irrelevant messages can be caused by message formatting issues (for example, missing fields) or fields that contain values that aren't relevant to the function.

## Example use cases for Lambda event filters
<a name="example-use-cases-for-lambda-event-filters"></a>

Consider an application that notifies a customer care team when sales of more than $100 USD occur. However, all sales of any amount ($5, $10, etc.) are recorded in the organization's Amazon SQS queue. Each time the application's Lambda function polls the queue, it receives messages that aren't relevant to the application's business logic. In this case, the processing fees for those irrelevant messages are charged, which increases the operational cost of the application. Configuring Lambda event filters in this situation would limit the number of messages that the Lambda function must process and reduce cost.

For a hotel-booking application that needs to process batches of hotel reservations, specific request fields—like **Username**—are critical to the success of the operation. Without event filters, developers would need to code a logic into the application that identifies whether or not the field is present in each request. The application's code would also need to be able to verify if each request included the correct data type. By using Lambda event filters, all of this logic can be abstracted to Amazon SQS to reduce development effort and code complexity.
