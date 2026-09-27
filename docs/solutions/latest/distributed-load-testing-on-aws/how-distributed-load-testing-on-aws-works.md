---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/how-distributed-load-testing-on-aws-works.html
---

# How Distributed Load Testing on AWS works
<a name="how-distributed-load-testing-on-aws-works"></a>

The following detailed breakdown shows the steps involved in running a test scenario.

 **Test workflow**

![Test workflow diagram](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/images/test-workflow.png)

1. You use the web console to submit a test scenario that includes the configuration details to the solution’s API.

1. The test scenario configuration is uploaded to the Amazon Simple Storage Service (Amazon S3) as a JSON file (`s3://<bucket-name>/test-scenarios/<$TEST_ID>/<$TEST_ID>.json`).

1. An AWS Step Functions state machine runs using the test ID, task count, test type, and file type as the AWS Step Functions state machine input. If the test is scheduled, it first creates an Amazon EventBridge Scheduler schedule, which triggers AWS Step Functions on the specified date. For more information about scheduling, refer to [Scheduling tests](design-considerations.md#scheduling-tests) in this section.

1. Configuration details are stored in the scenarios Amazon DynamoDB table.

1. In the AWS Step Functions task runner workflow, the task-status-checker AWS Lambda function checks if Amazon Elastic Container Service (Amazon ECS) tasks are already running for the same test ID. If tasks with the same test ID are found running, it causes an error. If there are no Amazon ECS tasks running in the AWS Fargate cluster, the function returns the test ID, task count, and test type.

1. The task-runner AWS Lambda function gets the task details from the previous step and runs the Amazon ECS worker tasks in the AWS Fargate cluster. The Amazon ECS API uses the RunTask action to run the worker tasks. These worker tasks are launched and then wait for a start message from the leader task in order to begin the test. The RunTask action is limited to 10 tasks per definition. If your task count is more than 10, the task definition will run multiple times until all worker tasks have been started. The function also generates a prefix to distinguish the current test in the results-parse AWS Lambda function.

1. The task-status-checker AWS Lambda function checks if all the Amazon ECS worker tasks are running with the same test ID. If tasks are still provisioning, it waits for one minute and checks again. Once all Amazon ECS tasks are running, it returns the test ID, task count, test type, all task IDs and prefix and passes it to the task-runner function.

1. The task-runner AWS Lambda function runs again, this time launching a single Amazon ECS task to act as the leader node. This ECS task sends a start test message to each of the worker tasks in order to start the tests simultaneously.

1. The task-status-checker AWS Lambda function again checks if Amazon ECS tasks are running with the same test ID. If tasks are still running, it waits for one minute and checks again. Once there are no running Amazon ECS tasks, it returns the test ID, task count, test type, and prefix.

1. When the task-runner AWS Lambda function runs the Amazon ECS tasks in the AWS Fargate cluster, each task downloads the test configuration from Amazon S3 and starts the test.

1. Once the tests are running, the average response time, number of concurrent users, number of successful requests, and number of failed requests for each task is logged in Amazon CloudWatch and can be viewed in a CloudWatch dashboard.

1. If you included live data in the test, the solution filters real-time test results in CloudWatch using a subscription filter. Then the solution passes the data to a Lambda function.

1. The Lambda function then structures the data received and publishes it to an AWS IoT Core topic.

1. The web console subscribes to the AWS IoT Core topic for the test and receives the data published to the topic to graph the real-time data while the test is running.

1. When the test is complete, the container images export a detailed report as an XML file to Amazon S3. Each file is given a UUID for the filename. For example, s3://amzn-s3-demo-bucket/test-scenarios/*<$TEST\_ID>*/results/*<$UUID>*.xml.

1. When the XML files are uploaded to Amazon S3, the results-parser AWS Lambda function reads the results in the XML files starting with the prefix and parses and aggregates all the results into one summarized result.

1. The results-parser AWS Lambda function writes the aggregate result to an Amazon DynamoDB table.

## MCP Server workflow (Optional)
<a name="mcp-server-workflow"></a>

If you deploy the optional MCP Server integration, AI agents can access and analyze your load testing data through the following workflow:

 **MCP Server workflow**

![MCP Server workflow diagram](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/images/mcp-server-workflow.png)

1.  **Customer interaction** - The customer interacts with the Distributed Load Testing solution through an AI agent. The agent connects to the MCP Endpoint to request access to load testing data.

1.  **Authorization** - AgentCore Gateway validates the user’s Amazon Cognito authentication token to verify the user has permission to access the DLT MCP Server. The available tools depend on the **MCP Server Access Mode** parameter.

1.  **Tool invocation** - AgentCore Gateway forwards authorized MCP tool requests to the DLT MCP Server Lambda function. The Lambda function implements the tools that AI agents use to retrieve load testing information.

1.  **API access** - The DLT MCP Server Lambda function calls the existing DLT API Gateway endpoints to retrieve test data from DynamoDB and Amazon S3. In the default `ReadOnly` access mode, the function provides read-only tools for retrieving test scenarios, test runs, baseline comparisons, and test run artifacts. In `ReadWrite` mode, it also provides tools for creating, modifying, deleting, and starting test scenarios. For more information about the available tools and their parameters, refer to [MCP tools specification](mcp-tools-specification.md) in the Developer Guide.

The MCP Server integration uses the existing DLT infrastructure (API Gateway, Cognito, DynamoDB, S3) to provide secure access to test data for AI-powered analysis and insights.
