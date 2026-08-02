---
source_url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttd.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Reducing MTTD
<a name="reducing-mttd"></a>

 Reducing the MTTD of a failure means discovering the failure as quickly as possible. Shortening the MTTD is based on observability, or how you've instrumented your workload to understand its state. Customers should monitor their *Customer Experience* metrics in their workload's critical subsystems as a way to proactively identify when a problem occurs (refer to [Appendix 1 – MTTD and MTTR critical metrics](appendix-1-mttd-and-mttr-critical-metrics.md) for more information about these metrics. ). Customers can use [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) to create *canaries* that monitor your APIs and consoles to proactively measure the user experience. There are a number of other health check mechanisms that can be used to minimize the MTTD, such as [Elastic Load Balancing (ELB) health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-elb-healthcheck.html), [Amazon Route 53 health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-types.html), and more. (See [Amazon Builders' Library – Implementing health checks](https://aws.amazon.com/builders-library/implementing-health-checks/).)

 Your monitoring also needs to be able to detect partial failures of both the system as a whole and in your individual subsystems. Your availability, failure, and latency metrics should use the dimensionality of your fault isolation boundaries as [CloudWatch metric dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension). For example, consider a single EC2 instance that is part of a cell-based architecture, in the use1-az1 AZ, in the us-east-1 Region, that is part of the workload’s update API that is part of its control plane subsystem. When the server pushes its metrics, it can use its instance id, AZ, Region, API name, and subsystem name as dimensions. This allows you to have observability and set alarms across each of these dimensions to detect failure.
