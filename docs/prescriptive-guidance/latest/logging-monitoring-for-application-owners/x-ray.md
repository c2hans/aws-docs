---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/x-ray.html
---

# AWS X-Ray
<a name="x-ray"></a>

[AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) collects data about requests that your application serves, and it helps you view, filter, and gain insights into that data to identify issues and opportunities for optimization.

## Using X-Ray
<a name="using-x-ray"></a>

AWS X-Ray receives traces from your application and, if they're integrated with X-Ray, from the AWS services that your application uses. X-Ray samples and visualizes requests on a [service graph](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-servicegraph) when they flow through your application components. X-Ray generates trace identifiers so that you can correlate a request when it flows through multiple components, which helps you view the request from end to end. You can further enhance this by including annotations and metadata to help uniquely search for and identify the characteristics of a request.

We recommend that you configure each server or endpoint in your application with X-Ray. X-Ray is implemented in your application code by making calls to the X-Ray service. X-Ray also provides AWS SDKs for multiple languages, including instrumented clients that automatically send data to X-Ray. The X-Ray SDKs provide patches to common libraries used for making calls to other services (for example, HTTP, MySQL, PostgreSQL, or MongoDB).

For more information, see [Tracing applications with AWS X-Ray](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/application-tracing-xray.html) (AWS Prescriptive Guidance).

## Use cases for X-Ray
<a name="x-ray-use-cases"></a>
+ **Application analysis and debug** – Trace data can help you debug the application by providing an end-to-end view of the request so that you can identify bottlenecks and troubleshoot issues. The X-Ray [service map](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-servicemap.html) is a visual tool that helps you identify where errors are occurring, connections with high latency, or traces for unsuccessful requests.
+ **Performance analytics** – The [Analytics console](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-analytics.html) is an interactive tool for interpreting trace data to quickly understand how your application and its underlying services are performing. The console helps you explore, analyze, and visualize traces. You can also compare trace sets with different conditions, for root cause analysis.
