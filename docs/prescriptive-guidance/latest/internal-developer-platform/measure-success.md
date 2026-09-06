---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/measure-success.html
---

# Measuring the success of an internal developer platform
<a name="measure-success"></a>

It is not straightforward to measure the success of the internal developer platform. However, you can use metrics to measure the effect of adopting an internal developer platform and how it improved the developer experience.

Because the metrics should measure the impact, you can use [DevOps Research and Assessment (DORA)](https://dora.dev/) metrics. Adopting platform engineering practices and an internal developer platform should improve the following metrics:

1. **Deployment frequency** – How often your organization successfully releases to production

1. **Lead time for changes** – The amount of time it takes a commit to get into production

1. **Change failure rate** – The percentage of deployments causing a failure in production

1. **Time to restore service** – How long it takes an organization to recover from a failure in production

Another approach is to measure your current application health and track long-term application performance against your business objectives. You can use [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) by defining [service-level objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) (SLOs) for your application and use CloudWatch dashboards to show the status of your application.

If you don't instrument the application, the biggest challenge is getting the right metrics and aligning the application with the overall observability strategy. The observability strategy helps you understand the overall health of the application through security scans, testing, and tracking availability.
