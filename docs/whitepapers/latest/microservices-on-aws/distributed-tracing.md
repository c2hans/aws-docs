---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/distributed-tracing.html
---

# Distributed tracing
<a name="distributed-tracing"></a>

 Microservices often work together to handle requests. AWS X-Ray uses correlation IDs to track requests across these services. X-Ray works with Amazon EC2, Amazon ECS, Lambda, and Elastic Beanstalk.

![Diagram showing AWS X-Ray service map](http://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/xray-service-map.png)

 [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/?otel-blogs.sort-by=item.additionalFields.createdDate&otel-blogs.sort-order=desc) is part of the OpenTelemetry project and provides open-source APIs and agents to gather distributed traces and metrics, improving your application monitoring. It sends metrics and traces to multiple AWS and partner monitoring solutions. By collecting metadata from your AWS resources, it aligns application performance with the underlying infrastructure data, accelerating problem-solving. Plus, it's compatible with a variety of AWS services and can be used on-premises.
