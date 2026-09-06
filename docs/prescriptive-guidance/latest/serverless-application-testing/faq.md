---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-application-testing/faq.html
---

# FAQ
<a name="faq"></a>

## I have a Lambda function that performs calculations and returns a result without calling any other services. Do I really need to test this in the cloud?
<a name="faq-1"></a>

Yes. AWS Lambda functions have configuration parameters that could change the outcome of the test. All Lambda function code has a dependency on [timeout and memory settings](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html), which could cause the function to fail if they aren't set properly. Lambda policies also enable standard output logging to [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/). Even if your code doesn't call CloudWatch directly, a permission is required in order to enable logging, and that permission cannot be accurately mocked or emulated.

## How can testing in the cloud help with unit testing? If it's in the cloud and connects to other resources, isn't that an integration test?
<a name="faq-2"></a>

We define unit tests as tests that operate on architectural components in isolation. This definition doesn't necessarily preclude the use of service calls or other network communications.

Many serverless applications do have architectural components that can be tested in isolation, even in the cloud. A basic example is a Lambda function that takes some input, interprets it, and sends a message to an Amazon Simple Queue Service (Amazon SQS) queue. A unit test of such a function would likely test whether input values result in certain values being present in the queued message. Consider a test that is written by using the *arrange, act, assert* pattern:
+ **Arrange** – Allocate resources (a queue to receive messages, and the function under test).
+ **Act** – Call the function under test.
+ **Assert** – Retrieve the message sent by the function, and validate the output.

A mock testing approach would involve mocking the queue with an in-process mock object, and creating an in-process instance of the class or module that contains the Lambda function code. During the assert phase, the queued message would be retrieved from the mocked object.

In a cloud-based approach, the test would create an Amazon SQS queue for the purposes of the test, and would deploy the Lambda function with environment variables that are configured to use the isolated Amazon SQS queue as the output destination. After running the Lambda function, the test would retrieve the message from the Amazon SQS queue.

The cloud-based test would run the same code, assert the same behavior, and validate the application's functional correctness. However, it would have the added advantage of being able to validate the following settings of the Lambda function: the AWS Identity and Access Management (IAM) role, IAM policies, and the function's timeout and memory settings.
