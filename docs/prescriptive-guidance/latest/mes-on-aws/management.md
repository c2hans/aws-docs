---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/management.html
---

# Using cloud-native technology to manage, orchestrate, and monitor microservices for MES
<a name="management"></a>

After you design the architecture for individual microservices, you should focus on ensuring that all microservices work seamlessly. Microservice-based MES is an agile, constantly evolving system that has dynamic, distributed components such as container images, databases, APIs, object stores, and queues. This constant change poses another set of architectural challenges in orchestrating, monitoring, and managing these distributed components.

## Orchestration
<a name="orchestration"></a>

Some transactions within MES might involve multiple microservices from production, quality, inventory, maintenance, and other areas, for tasks such as reporting an operation complete, receiving inventory against a purchase order, or completing a quality inspection. These transactions include multiple sub-transactions and require orchestration. The orchestration code shouldn't be placed within a specific microservice but should appear on a higher-level control plane.

To simplify such complex orchestration, AWS offers [AWS Step Functions](https://aws.amazon.com/step-functions/). This fully managed service makes it easier to coordinate the components of distributed applications and microservices by using visual workflows. It provides a graphical console to arrange and visualize the components of your application as a series of steps, as shown in the following diagram. The visualized arrangement makes it easier to build and run multi-step applications.

![Orchestration technologies for MES architectures on AWS](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/e8bccd88-c7e8-4678-a852-f3cd69617675.png)

## Auditing
<a name="auditing"></a>

Microservice-based MES architecture is dynamic due to constant changes and evolution. Organizations must enforce security and other enterprise policies for compliance and regulation. Ensuring security and enterprise policies within a system such as MES that has many users, multiple microservices, and many resources within each microservice requires visibility into all user actions and microservice interactions.

AWS offers the following services to solve the challenges of auditing and monitoring:
+ [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) enables auditing, security monitoring, and operational troubleshooting by tracking user activity and API usage. CloudTrail logs continuously monitor and retain account activity related to actions across your AWS infrastructure, and give you control over storage, analysis, and remediation actions.
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) is an AWS monitoring service for AWS Cloud resources and applications. You can use CloudWatch to gain systemwide visibility into resource utilization, application performance, and operational health. It can collect and track metrics, collect and monitor log files, and set alarms.
+ [AWS Config](https://aws.amazon.com/config/) provides resource inventory, configuration history, and configuration change notifications for security and governance. You can use AWS Config to discover existing AWS resources, record configurations for third-party resources, export a complete inventory of your resources with all configuration details, and determine how a resource was configured at any time.
+ [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) is a serverless monitoring service for metrics that's compatible with the open-source Prometheus data model and query language. It monitors and generates alerts for container workloads on AWS, on premises, and in hybrid and multi-cloud environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
