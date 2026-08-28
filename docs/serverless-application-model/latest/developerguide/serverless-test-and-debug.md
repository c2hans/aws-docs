---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-test-and-debug.html
---

# Test your serverless application with AWS SAM
<a name="serverless-test-and-debug"></a>

After writing and building your application, you will be ready to test your application to verify that it functions correctly. With the AWS SAM command line interface (CLI), you can locally test your serverless application before uploading it to the AWS Cloud. Testing your application helps you confirm the application’s functionality, reliability, and performance all while identifying issues (bugs) that will need to be addressed.

This section provides guidance on common practices you can follow to test your application. The topics in this section focus mostly on the local testing you can do before deploying in the AWS Cloud. Testing before deploying helps you identify issues proactively, reducing unnecessary costs associated with deployment issues. Each topic in this section describes a test you can perform and includes examples showing you how to perform the test. After testing your application, you’ll be ready to debug any issues you’ve found.

**Topics**
+ [Introduction to testing with the sam local command](using-sam-cli-local.md)
+ [Locally invoke Lambda functions with AWS SAM](serverless-sam-cli-using-invoke.md)
+ [Locally run API Gateway with AWS SAM](serverless-sam-cli-using-start-api.md)
+ [Introduction to cloud testing with sam remote test-event](using-sam-cli-remote-test-event.md)
+ [Introduction to testing in the cloud with sam remote invoke](using-sam-cli-remote-invoke.md)
+ [Automate local integration tests with AWS SAM](serverless-sam-cli-using-automated-tests.md)
+ [Generate sample event payloads with AWS SAM](serverless-sam-cli-using-generate-event.md)
+ [Testing and debugging durable functions](test-and-debug-durable-functions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
