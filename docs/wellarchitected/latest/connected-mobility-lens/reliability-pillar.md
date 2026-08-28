---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/reliability-pillar.html
---

# Reliability pillar
<a name="reliability-pillar"></a>

 The reliability pillar for connected mobility encompasses the ability of connected vehicles to deliver the services as intended and consistently. Resiliency is a [shared responsibility](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/shared-responsibility-model-for-resiliency.html) between AWS and the customer. It is important that you understand how high availability (HA) and disaster recovery (DR), as part of resiliency, operate under this shared model.

 As an Auto OEM, your responsibility would change based on the configuration that is needed for a particular service. If your connected mobility uses Amazon EC2 for the connectivity gateway and vehicle data platform, then you are responsible for deploying EC2 instances across multiple locations such as Availability Zones and Regions,  implementing [self-healing systems](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-your-workload-to-withstand-component-failures.html) like AWS Auto Scaling. If you have managed services, such as API Gateway, AWS IoT, Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and you access the endpoints to store and retrieve data. In both cases, you are responsible for managing resiliency of your data including backup, versioning, and replication strategies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
