---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html
---

# What is Amazon CodeGuru Profiler?
<a name="what-is-codeguru-profiler"></a>

Amazon CodeGuru Profiler collects runtime performance data from your live applications, and provides recommendations that can help you fine-tune your application performance. Using machine learning algorithms, CodeGuru Profiler can help you find your most expensive lines of code and suggest ways you can improve efficiency and remove CPU bottlenecks.

CodeGuru Profiler provides different visualizations of profiling data to help you identify what code is running on the CPU, see how much time is consumed, and suggest ways to reduce CPU utilization.

## What can I do with CodeGuru Profiler?
<a name="what-is-what-can-i-do"></a>

Use CodeGuru Profiler to help profile your applications in the cloud from a single, centralized dashboard.

Specifically, you can do the following:
+ Troubleshoot latency and CPU utilization issues in your application.
+ Learn where you could reduce the infrastructure costs of running your application.
+ Identify application performance issues.
+ Understand your application's heap utilization over time.

## What languages are supported by CodeGuru Profiler?
<a name="what-is-language-support"></a>

CodeGuru Profiler currently supports applications written in all Java virtual machine (JVM) languages and runtimes and Python 3.6 or later. The following table explains which features of CodeGuru Profiler are supported by which language.

| Feature | Java/JVM | Python |
| --- | --- | --- |
| CPU profiling | Yes | Yes |
| Support for AWS Lambda and other AWS compute platforms  | Yes | Yes |
| Anomalies and recommendation reports | Yes | Yes |
| Colored thread states | Yes | Yes |
| Heap summary visualization | Yes | No |

## How do I get started with CodeGuru Profiler?
<a name="what-is-get-started"></a>

1. Prepare to use CodeGuru Profiler by following the steps in [Setting up CodeGuru Profiler](setting-up.md).

1. Learn how to use recommendation reports by following the steps in [Working with anomalies and recommendation reports](working-with-recommendation-reports.md).

1. Graphically explore your application data by following the steps in [Working with visualizations](working-with-visualizations.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
