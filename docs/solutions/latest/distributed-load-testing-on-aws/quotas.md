---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/quotas.html
---

# Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this solution
<a name="quotas-for-aws-services-in-this-solution"></a>

Make sure you have sufficient quota for each of the [services implemented in this solution](architecture-details.md#aws-services-in-this-solution). For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

Use the following links to go to the page for that service. To view the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.

## AWS CloudFormation quotas
<a name="aws-cloudformation-quotas"></a>

Your AWS account has AWS CloudFormation quotas that you should be aware of when [launching the stack](launch-the-stack.md) in this solution. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this solution successfully. For more information, see [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the in the *AWS CloudFormation User's Guide*.

## Load testing quotas
<a name="load-testing-quotas"></a>

The maximum number of tasks that can be running in Amazon ECS using the AWS Fargate launch type is based on the vCPU size of the tasks. The default task size in Distributed Load Testing on AWS is 2 vCPU. To see the current default quotas, refer to [Amazon ECS service quotas](https://docs.aws.amazon.com/AmazonECS/latest/userguide/service-quotas.html). Current account quotas may differ from the listed quotas. To check quotas specific to an account, check the service quota for Fargate on-demand vCPU resource count in the AWS Management Console. For instructions on how to request an increase, refer to [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) in the *AWS General Reference Guide*.

The Amazon Linux 2023 container image (with Taurus installed) does not limit concurrent connections per task, but that does not mean it can support an unlimited number of users. To determine the number of concurrent users the containers can generate for a test, refer to the [Determine the number of users](create-test-scenario.md#determine-number-of-users) section of this guide.

**Note**
The recommended limit for concurrent users based on default settings is 200 users.

## Concurrent tests
<a name="concurrent-tests"></a>

Each time a load test runs, the task-runner AWS Lambda function creates an Amazon CloudWatch dashboard named `EcsLoadTesting-<testId>-<region> ` in each Region where the test runs. The CloudWatch dashboard displays the combined output of all tasks running in the Amazon ECS cluster in real time: average response time, number of concurrent users, number of successful requests, and number of failed requests. The solution aggregates each metric by the second and updates the dashboard every minute.

Subsequent runs of the same test scenario update the same dashboard, so your account contains one dashboard for each test scenario in each Region. These dashboards remain in your account after tests complete and incur a monthly charge until they are deleted; refer to [CloudWatch dashboard costs per test scenario](cost.md#cloudwatch-dashboard-cost). The solution deletes a scenario’s dashboards when you delete the test scenario (for example, through the web console); the dashboards are not deleted when you delete the solution’s CloudFormation stacks. For manual deletion steps, refer to the [Manually deleting retained resources](manually-deleting-retained-resources.md) section of this guide.

## Amazon EC2 testing policy
<a name="amazon-ec2-testing-policy"></a>

You are responsible for running load tests in accordance with the [Amazon EC2 Testing Policy](https://aws.amazon.com/ec2/testing/). Review the policy for current guidance on what qualifies as a network stress test, permitted traffic volumes, and when to contact AWS before running high-volume tests. Note that AWS may apply traffic engineering or shaping at high aggregate traffic volumes.

## Amazon CloudFront load testing policy
<a name="amazon-cloudfront-load-testing-policy"></a>

If you plan on load testing a CloudFront endpoint, refer to the [load testing guidelines](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/load-testing.html) in the *Amazon CloudFront Developer Guide*. We also recommended spreading the traffic across multiple tasks and Regions. Provide at least 30 minutes of ramp-up time for the load test. For load tests sending more than 500,000 requests per second or demanding more than 300 Gbps data, we recommend first obtaining a pre-approval for sending the traffic. CloudFront may throttle unapproved load test traffic that impacts CloudFront service availability.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Distributed Load Testing on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
