---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/test-observability.html
---

# Test observability
<a name="test-observability"></a>

Test observability supports collecting, correlating, aggregating, and analyzing telemetry in your network, infrastructure, and applications during the performance test runs. You gain full insights into the behavior, performance, and health of your system. These insights help you detect, investigate, and remediate problems faster. By adding artificial intelligence and machine learning, you can proactively react to, predict, and prevent problems.

![Diagram showing the five-phase cycle](http://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/images/guide-img/7c6508f5-55cf-496c-a7ac-ba285b7b71ef/images/e53b6eb5-4b41-483a-b01c-cf38c5724a10.png)

Observability relies on [logging](logging.md) , [monitoring](monitoring.md), and [tracing](tracing.md). The responsibility of implementing these activities successfully spans the application and infrastructure teams.

At the start of the design phase, application teams should understand the current state of their observability stack, including logging, monitoring, and tracing. They can then choose tools integrate more smoothly into the observability stack.

Similarly, the infrastructure team is responsible for managing and scaling the observability infrastructure.

Consider the following aspects with respect to test observability:
+ Availability of application logs and traces
+ Correlation of logs and traces
+ Availability of nodes, containers, and application metrics
+ Automation to set up and update the observability infrastructure on demand
+ Ability to visualize the telemetry
+ Scaling of the observability infrastructure
