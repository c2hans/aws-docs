---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_monitor_aws_resources_end_to_end.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL06-BP07 Monitor end-to-end tracing of requests through your system
<a name="rel_monitor_aws_resources_end_to_end"></a>

 Use AWS X-Ray or third-party tools so that developers can more easily analyze and debug distributed systems to understand how their applications and its underlying services are performing.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Monitor end-to-end tracing of requests through your system. AWS X-Ray is a service that collects data about requests that your application serves, and provides tools you can use to view, filter, and gain insights into that data to identify issues and opportunities for optimization. For any traced request to your application, you can see detailed information not only about the request and response, but also about calls that your application makes to downstream AWS resources, microservices, databases, and web APIs.
  +  [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
  +  [Debugging with Amazon CloudWatch Synthetics and AWS X-Ray](https://aws.amazon.com/blogs/devops/debugging-with-amazon-cloudwatch-synthetics-and-aws-x-ray/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Debugging with Amazon CloudWatch Synthetics and AWS X-Ray](https://aws.amazon.com/blogs/devops/debugging-with-amazon-cloudwatch-synthetics-and-aws-x-ray/)
+  [One Observability Workshop](https://observability.workshop.aws/)
+  [The Amazon Builders' Library: Instrumenting distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/)
+  [Using Canaries (Amazon CloudWatch Synthetics)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
+  [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
