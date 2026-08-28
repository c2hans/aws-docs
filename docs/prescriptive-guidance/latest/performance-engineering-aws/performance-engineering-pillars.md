---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/performance-engineering-pillars.html
---

# The pillars of performance engineering
<a name="performance-engineering-pillars"></a>

To enable a performance engineering mindset, it's important to build a strong foundation while setting up performance engineering for the application. Performance engineering requires setting up four major pillars:
+ **Test-data generation** – Performance engineers set up tools to generate the test data.
+ **Test observability** – Performance engineers set up the observability environment to ensure that the performance run can be logged and traced, and that the resources handling the loads are monitored.
+ **Test automation** – Performance engineers develop automated tests that simulate user traffic and system load using tools such as [Apache JMeter](https://jmeter.apache.org/) or [ghz](https://ghz.sh/).
+ **Test reporting** – Data is gathered about the configuration of each test run along with the performance results. The data enables correlating configuration changes to performance and provides valuable insights.

![Diagram showing the pillars.](http://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/images/guide-img/7c6508f5-55cf-496c-a7ac-ba285b7b71ef/images/6bc2e2a0-de40-4f7e-9cca-0ded6f6a7162.png)

Incorporating these pillars will encourage the performance mindset starting from the initial phases of the design. This will help avoid changes to the application or environment in later phases of development and testing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
