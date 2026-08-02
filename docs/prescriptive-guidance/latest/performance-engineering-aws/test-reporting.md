---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/test-reporting.html
---

# Test reporting
<a name="test-reporting"></a>

Test reporting refers to the collection, analysis, and presentation of data related to the performance of systems, applications, services, or processes. It involves measuring various metrics and indicators to assess the efficiency, responsiveness, reliability, and overall effectiveness of a particular system or component.

Performance-test reporting involves choosing relevant metrics based on the context and goals of the analysis. Common performance metrics include response times, throughput, error rates, resource utilization (CPU, memory, disk), and network latency.

After the performance-related data has been collected, it needs to be stored in a central repository. These test results could come from different environments, applications, and testing tools. When you have multiple workloads running in different environments, it's difficult to gather performance-related data and correlate between these data points to draw informed conclusions. We recommend defining a standard method for collecting performance metrics data using a central repository for data storage and visualization.

## Standardized recording
<a name="recording"></a>

We recommend standardizing the way that different stakeholders perform the performance tests and write the resulting data to a central repository. For example, this could take the form of an API accepting the results and storing them into a persistent storage solution. In situations where data needs to be fetched from sources such as GitOps or Amazon Managed Service for Prometheus, the API can directly pull those details from the specified sources based on schema files that describe how to extract the fields from deployment specifications and Kubernetes specifications. The schema files can use `JSONPath` expressions or Prometheus Query Language ([PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/)). As mentioned previously, the metrics that are collected should be relevant to the context and goals of the performance analysis.

The data passed to the API can include details and tags related to the application and the environment for which the test has been performed. This helps with performing analytics on the performance testing data.
