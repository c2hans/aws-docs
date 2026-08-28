---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-application-testing/challenges.html
---

# Challenges when testing serverless applications
<a name="challenges"></a>

When you use emulators and mocked calls to test your serverless application on your local desktop, you might experience testing inconsistencies as your code progresses from environment to environment in your CI/CD pipeline. The unit tests you create on your desktop to validate your application's business logic might not include or accurately represent critical aspects of cloud services. Complete tests can't be performed locally in isolation. They require verifying the permissions and configurations among multiple services.

The following sections outline the challenges you might experience when implementing a cloud testing strategy. The following sections outline the challenges customers experience when trying to implement a cloud testing strategy, and our guidance on best practices to achieve effective test coverage.

## Example: A Lambda function that creates an Amazon S3 bucket
<a name="example-1"></a>

If a Lambda function's logic depends on creating an Amazon S3 bucket, a complete test should confirm that Amazon S3 was successfully called and the bucket was successfully created. In a mock testing setup, you might mock a success response and potentially add a test case to handle a failure response. In an emulation testing scenario, the `CreateBucket` API might be called, but the identity that makes the call will not originate from the Lambda service assuming a role, and a placeholder authentication will be used instead―this is often your more permissive role or user identity.

The mock and emulation setups discussed previously will most likely test *what the Lambda function will do* if it successfully (or unsuccessfully) calls Amazon S3. However, those tests will fail to capture *whether the Lambda function is capable *of successfully creating the bucket, given the function's configuration. This configuration is likely represented by infrastructure as code (IaC) for products and services such as AWS CloudFormation, AWS SAM, or HashiCorp Terraform. One possible issue is that the role that is assigned to the function doesn't have an attached policy that allows for the `s3:CreateBucket` action, and the function will therefore always fail when it is deployed to a cloud environment.

## Example: A Lambda function that processes messages from Amazon SQS
<a name="example-2"></a>

If an Amazon Simple Queue Service (Amazon SQS) queue is the source of a Lambda function, a complete test should verify that the Lambda function is successfully invoked when a message is put in a queue. Emulation testing and mock testing are generally set up to run the Lambda function code directly, and to simulate the Amazon SQS integration by passing a JSON event payload (or a deserialized object) as the function handler's input.

Local testing that simulates the Amazon SQS integration will test *what the Lambda function will do* when it's called by Amazon SQS with a given payload, but it won't ensure that *Amazon SQS will successfully invoke the Lambda function* when it is deployed to a cloud environment.

Some examples of configuration problems you might encounter with Amazon SQS and Lambda include the following:
+ Amazon SQS visibility timeout is too low, resulting in multiple invocations when only one was intended.
+ The Lambda function's execution role doesn't allow reading messages from the queue (through `sqs:ReceiveMessage`, `sqs:DeleteMessage`, or `sqs:GetQueueAttributes`).
+ The sample event that is passed to the Lambda function exceeds the Amazon SQS message size quota. Therefore, the test is invalid because Amazon SQS would never be able to send a message of that size.

As these examples show, tests that cover business logic but not the configurations between cloud services are likely to provide unreliable results.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
