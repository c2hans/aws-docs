---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/implications.html
---

# Implications of load testing
<a name="implications"></a>

The following sections cover possible side effects, which are the common pitfalls when running load tests.

## Cost
<a name="cost"></a>

When you use a cloud that easily scales to perform large-scale performance tests, you can incur high costs by deploying many servers for a long-running test and using a large amount of bandwidth in the process. To avoid this, plan ahead, and consider how much you want to spend. Model your target system accordingly to create representable results.

## Third parties and availability
<a name="third-party"></a>

When your tested flows include calling third-party services, you might consume your quotas or induce unwanted costs. If possible, deactivate or stub third-party systems so that they are not part of your test. By replacing external services with stubs that are hosted by you and return fake but valid responses, you are independent. You can focus your test on your own application.

If you include the third-party systems, they become part of the result. When they are slow, they create drag or back pressure. If they are not available, they introduce unrelated false errors.

## Accumulation of test data
<a name="accumulation"></a>

Running large tests and keeping many datapoints for a detailed analysis can result in a lot of data. Storage systems such as disc space, time series databases, or Amazon Simple Storage Service (Amazon S3) must be able to handle the amount of data and provide the necessary query capabilities. Plan server size, partitioning, and data deprecation according to your needs. This is not an issue if you plan ahead and adjust early.

## Network bandwidth
<a name="bandwidth"></a>

A load test usually requires a large amount of bandwidth, and it puts a strain on the servers. Scale the servers on which you run the load test appropriately. Make sure that the network upload provides enough bandwidth not to become the bottleneck. In most cases, you have a fewer servers generating load than the number of application servers receiving load. Therefore, the test servers require more bandwidth. At AWS, Amazon EC2 instances with the *n* as the suffix provide enhanced networking capabilities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
