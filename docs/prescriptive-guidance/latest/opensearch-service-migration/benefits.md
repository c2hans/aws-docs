---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/benefits.html
---

# Benefits of migrating to Amazon OpenSearch Service
<a name="benefits"></a>

Amazon OpenSearch Service helps with deployment and ongoing management tasks. It's cost-effective, and it provides scalability, which improves reliability. It also offers security and helps support your compliance needs.

## Easier to deploy and manage
<a name="deploy-manage"></a>

It's easier to deploy an OpenSearch cluster by using Amazon OpenSearch Service than it is to deploy a cluster by yourself. Amazon OpenSearch Service helps to manage tasks such as hardware provisioning, software installation and patching, failure recovery, backups, and monitoring. You don't need to have a dedicated team of OpenSearch experts to manage your clusters.

An OpenSearch cluster in Amazon OpenSearch Service is also called a domain. Amazon OpenSearch Service provides domain health monitoring through the Amazon CloudWatch service. You can set up alerts to be notified of any changes to your domains' health. AWS Support provides one-on-one technical support from experienced engineers. Customers with operational challenges or technical questions can contact AWS Support and receive personalized support with reliable response times.

## Cost-effective
<a name="cost-effective"></a>

Amazon OpenSearch Service is cost-effective. It provides a full array of advanced capabilities without charging additional licensing fees. You can use capabilities such as enterprise-grade security, real-time alerting, cross-cluster search, automated index management, and anomaly detection at no extra cost. There are no charges for data transfers between Availability Zones, and hourly snapshots are provided at no extra cost.

With *UltraWarm*, you can run interactive analytics on up to three petabytes of log data while reducing the cost per GB by up to 90 percent compared with the hot storage tier. Furthermore, Amazon OpenSearch Service offers Reserved Instances that provide significant discounts compared with the standard On-Demand Instances. For more information, see [Cost-conscious](https://aws.amazon.com/opensearch-service/features/cost/).

## More scalable and reliable
<a name="scalable-reliable"></a>

With Amazon OpenSearch Service, you can store petabytes of data in a single domain. You can query data across multiple domains and analyze all your data in a single OpenSearch Dashboards interface. Amazon OpenSearch Service is designed to be highly reliable, using Multi-Availability Zone (Multi-AZ) deployments so that you can replicate data between up to three Availability Zones in the same AWS Region. There is zero downtime when you make software updates and upgrades or scale your environment.

With the Multi-AZ with Standby feature, OpenSearch Service domains are resilient to potential infrastructure failures, such as a node or an Availability Zone failure. This enables 99.99 percent availability and consistent performance for business-critical workloads. With Multi-AZ with Standby, clusters are resilient to infrastructure failures such as hardware or networking failures. This option provides improved reliability and the added benefit of simplifying cluster configuration and management by enforcing best practices and reducing complexity.

## Secure and compliant
<a name="secure-compliant"></a>

Amazon OpenSearch Service takes care of all security patches. It also offers network isolation through a virtual private cloud (VPC), fine-grained access control, and multi-tenant OpenSearch Dashboards support. You can encrypt your data at rest and in transit. To help you meet industry-specific and regulatory requirements, Amazon OpenSearch Service is HIPAA eligible, and it's compliant with the following standards:
+ FedRAMP
+ GDPR
+ PCI DSS
+ ISO
+ SOC

For more information, see the [Amazon OpenSearch Service documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
