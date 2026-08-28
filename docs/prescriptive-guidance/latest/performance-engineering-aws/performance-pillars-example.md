---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/performance-pillars-example.html
---

# Performance engineering pillars in action
<a name="performance-pillars-example"></a>

The following reference architecture demonstrates performance engineering pillars for testing a specific API.

![Diagram of data movement through the test process to the dashboard.](http://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/images/guide-img/7c6508f5-55cf-496c-a7ac-ba285b7b71ef/images/81c12b6f-3c0e-4b42-a74d-bf2313a1ce3b.png)

1. Logging, monitoring, and tracing data is sent from the target API to the backend.

1. When invoked, the test reporting API sends results and configuration information to the backend.

The core component is the target API or application under test. The target API syncs with the application configuration repository and deployment configuration repository in GitOps fashion to obtain the latest application and infrastructure configurations. This synchronization allows the automated tests to run against the current desired state of the application and its supporting infrastructure as defined in the Git repositories

The test-automation pipeline automates generating the test data, running the test, and reporting the test results for the target API.

The target API generates performance insights (metrics, logs, and traces), using [observability best practices](https://aws-observability.github.io/observability-best-practices/), and it streams metrics data to the observability backend.

The test reporting API collects all test-related reporting data (configuration and test results), and it stores them in the observability backend.

Aggregation of performance insights and reporting data (configuration, test results) helps you to query performance related data for the target API. For example, you might ask the following:
+ What are the top ten slowest transactions?
+ What is the P99, P90, average number of each test?
+ How do the configurations of the two test runs compare?

Correlating tests cases with results, configurations, and metrics over a period time helps with identifying the best configuration and the performance results.

Using these test results, you can make more precise, data-driven decisions for the API and have confidence when taking the API to production.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
