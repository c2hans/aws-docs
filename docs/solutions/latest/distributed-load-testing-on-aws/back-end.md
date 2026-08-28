---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/back-end.html
---

# Backend
<a name="back-end"></a>

The backend consists of a container image pipeline and load testing engine you use to generate load for the tests. You interact with the backend through the front end. Additionally, Amazon ECS on AWS Fargate tasks launched for each test are tagged with a unique test identifier (ID). These test ID tags can be used to help you monitor costs for this solution. For additional information, refer to [User-Defined Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html) in the *AWS Billing and Cost Management User Guide*.

## Container image pipeline
<a name="container-image-pipeline"></a>

This solution uses a container image built with [Amazon Linux 2023](https://aws.amazon.com/linux/amazon-linux-2023/) as the base image with the [Taurus](https://gettaurus.org/) load testing framework installed. Taurus is an open-source test automation framework that supports JMeter, k6, Locust, and other testing tools. AWS hosts this image in an Amazon Elastic Container Registry (Amazon ECR) public repository. The solution uses this image to run tasks in the Amazon ECS on AWS Fargate cluster.

For more information, refer to the [Container image customization](container-image.md) section of this guide.

## Testing framework provisioning
<a name="framework-provisioning"></a>

The three supported testing frameworks are provisioned at different points in the solution lifecycle to balance image size with version flexibility:
+  **Apache JMeter** — Staged in an S3 bucket in your account during stack deployment, and extracted at test runtime when a JMeter or Single HTTP Endpoint test runs.
+  **Grafana k6** — Downloaded directly from the framework provider and extracted at test runtime, only when a k6 test runs.
+  **Locust** — Installed into the container image at build time and remains idle until a Locust test runs.

**Note**
k6 requires outbound network access to the Grafana k6 release at test runtime. Restricted egress will cause k6 tests to fail at the download step.

## Testing infrastructure
<a name="testing-infrastructure"></a>

In addition to the main CloudFormation template, the solution provides a regional template to launch the required resources for running tests in multiple Regions. The solution stores this template in Amazon S3 and provides a link to it in the web console. Each regional stack includes a VPC, an AWS Fargate cluster, and a Lambda function for processing live data.

For more information about how to deploy testing infrastructure in additional Regions, refer to the [Multi-Region deployment](multi-region-deployment.md) section of this guide.

## Load testing engine
<a name="load-testing-engine"></a>

The Distributed Load Testing solution uses Amazon Elastic Container Service (Amazon ECS) and AWS Fargate to simulate thousands of concurrent users across multiple Regions, generating HTTP requests at a sustained rate.

You define the test parameters using the included web console. The solution uses these parameters to generate a JSON test scenario and stores it in Amazon S3. For more information about test scripts and testing parameters, refer to [Test types](design-considerations.md#test-types) in this section.

An AWS Step Functions state machine runs and monitors Amazon ECS tasks in an AWS Fargate cluster. The AWS Step Functions state machine includes an ecr-checker AWS Lambda function, a task-status-checker AWS Lambda function, a task-runner AWS Lambda function, a task-canceler AWS Lambda function, and a results-parser AWS Lambda function. For more information about the workflow, refer to the [Test execution workflow](run-test-scenario.md#test-execution-workflow) section of this guide. For more information about test results, refer to the [Explore test results](explore-test-results.md) section of this guide. For more information about the test cancellation workflow, refer to the [Cancelling a test](run-test-scenario.md#cancelling-tests) section of this guide.

If you select live data, the solution initiates a real-time-data-publisher Lambda function in each Region by the CloudWatch logs that correspond to the Fargate tasks in that Region. The solution then processes and publishes the data to a topic in AWS IoT Core within the Region where you launched the main stack. For more information, refer to the [Monitoring with live data](run-test-scenario.md#monitoring-live-data) section of this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Distributed Load Testing on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
