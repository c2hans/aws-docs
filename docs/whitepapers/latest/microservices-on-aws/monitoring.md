---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/monitoring.html
---

# Monitoring
<a name="monitoring"></a>

 CloudWatch offers system-wide visibility into resource utilization, application performance, and operational health. In a microservices architecture, custom metrics monitoring through CloudWatch is beneficial, as developers can choose which metrics to collect. Dynamic scaling can also be based on these custom metrics.

 CloudWatch Container Insights extends this functionality, automatically collecting metrics for many resources like CPU, memory, disk, and network. It helps in diagnosing container-related issues, streamlining resolution.

 For Amazon EKS, an often-preferred choice is Prometheus, an open-source platform providing comprehensive monitoring and alerting capabilities. It's typically coupled with Grafana for intuitive metrics visualization. [Amazon Managed Service for Prometheus (AMP)](https://aws.amazon.com/prometheus/) offers a monitoring service fully compatible with Prometheus, letting you oversee containerized applications effortlessly. Additionally, [Amazon Managed Grafana (AMG)](https://aws.amazon.com/grafana/) simplifies the analysis and visualization of your metrics, eliminating the need for managing underlying infrastructure.

![Diagram showing a serverless architecture with monitoring components](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/serverless-arch-with-monitoring.png)

![A container-based architecture with monitoring components](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/container-arch-with-monitoring.png)
