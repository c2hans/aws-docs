---
source_url: https://docs.aws.amazon.com/glue/latest/dg/performance.html
---

# Improving AWS Glue performance
<a name="performance"></a>

**Baseline strategy for performance tuning**

In order to improve AWS Glue performance, you may consider updating certain performance related AWS Glue parameters. When preparing to tune parameters, use the following best practices:
+ Determine your performance goals before beginning to identify problems.
+ Use metrics to identify problems before attempting to change tuning parameters.

For the most consistent results when tuning a job, develop a baseline strategy for your tuning work.

Generally, performance tuning is performed in the following workflow:

1. Determine performance goals.

1. Measure metrics.

1. Identify bottlenecks.

1. Reduce the impact of the bottlenecks.

1. Repeat steps 2-4 until you achieve the intended target.

## Tuning strategies for your job type
<a name="w2aac97c15"></a>

**Spark jobs**–follow the guidance in [Best practices for performance tuning AWS Glue for Apache Spark jobs](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/introduction.html) on AWS Prescriptive Guidance.

**Other jobs**–you can tune AWS Glue for Ray and AWS Glue Python shell jobs by adapting strategies available in other runtime environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
