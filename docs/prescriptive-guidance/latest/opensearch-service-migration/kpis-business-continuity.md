---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/kpis-business-continuity.html
---

# KPIs and business continuity
<a name="kpis-business-continuity"></a>

It's essential that during the migration you establish your business goals and key performance indicators (KPIs) to measure success. It's important to determine your goals at the beginning of the migration process and establish a baseline for your current system so that you can determine measurable improvements. Common goals in customer journeys include the following:
+ Improve operational agility.

  Under this goal, you can measure and compare your existing deployment with the target environment by using the following metrics:
  + Mean time to provision cluster.
  + Time to roll out the deployment to a new geography
  + Mean time to configure cluster security
  + Mean time to scale your environment (such as adding nodes and adding storage)
  + Mean time to detect slow-performing queries and mean time to repair them
  + Mean time to upgrade the software version
+ Reduce total cost of ownership (TCO).

  To calculate your current TCO, you can use the following metrics:
  + Number of staff hours to build and operate the solution (development, DevOps, monitoring, scale, backup, restore)
  + License cost associated with the existing software
  + Data center costs (hardware procurement and refresh, electricity, cooling, space, racks, networking gears)
  + Staff hours to configure solution (software installations, networking)
  + Cost for compliance audits (HIPAA, PCI DSS, SOC, ISO, GDPR, FedRAMP)
  + Cost of configuring security (at rest and in-transit encryption, configuring authentication and authorization, fine-grain access control)
  + Cost of retaining a large volume of warm and cold data.
  + Cost of configuring high availability across Availability Zones
  + Cost of overprovisioning to avoid frequent hardware procurement or handling peak loads

  This list is not exhaustive.
+ Monitor uptime and other service-level agreements (SLAs). SLAs that you can measure and improve by migrating to the new environment include the following:
  + Total uptime (historical uptime data of existing deployment compared with 99.9 percent SLA provided by Amazon OpenSearch Service)
  + Failure recovery (recovery point objective and recovery time objective)
  + Response time associated with various functions (for example, search and indexing)
  + Number of concurrent users
  + Replication time between different geographies and clusters.

As you migrate to Amazon OpenSearch Service, use an iterative process to verify whether you are meeting or exceeding those KPIs and whether you are achieving the desired outcomes.

## Operational performance
<a name="operational-performance"></a>

A key area to look at in your current solution is performance metrics. Establish a benchmark, and determine improvements that you expect to achieve within your target environment. This includes your uptime SLA and latency requirements. This will help you establish and, in most cases, improve your current service levels. Usually, customers look at the following service level indicators
+ Reads and writes per second
+ Read and write latency
+ Uptime percentage

When you architect your own SLAs, it's important to fully understand the [Amazon OpenSearch Service - Service Level Agreement](https://aws.amazon.com/elasticsearch-service/sla/).

## Process performance
<a name="process-performance"></a>

To establish business continuity goals, it's important to assess your current process performance. Identify and review existing runbooks or standard operating procedures (SOPs) of the current platform, and determine areas where your team spends most of its time. Migration is a good opportunity to work on improving those areas so your team can focus on innovating, building business functionality, and improving the customer experience. You can identify pain points of your existing environment by reviewing the historical support or trouble ticket data to determine time spent by your support and development staff resolving these issues. Capturing the following metrics can help you measure improvements delivered by your target environment:
+ Mean time to failure (MTTF) (uptime)
+ Mean time between failures (MTBF)
+ Mean time to detect (MTTD) a failure
+ Mean time to repair (resolve) (MTTR)
+ Number of support tickets received

## Smooth transition to new services
<a name="transition"></a>

To ensure business continuity of your services, it's important to carefully plan a seamless transition. Migration is a good time to modernize your application and the services associated with your search or log analytics platform. However, you want to plan a careful cutover strategy that will not impact your existing services. The [cutover strategy](stage-5-cutover.md) section in this document provides information on how to plan a seamless cutover to the target environment.

## Financial metrics
<a name="financial-metrics"></a>

There could be many reasons to migrate to Amazon OpenSearch Service, but cost is generally a major factor. Understand the total cost of ownership (TCO) of the existing environment so you can measure the cost savings you get by moving to the managed service. You may start with the list of metrics that are listed under the *Reduce total cost of ownership* goal. AWS has published a [cloud value benchmarking study](https://pages.awscloud.com/rs/112-TZM-766/images/cloud-value-benchmarking-study-quantifies-cloud-adoption-benefits.pdf) that can help teams make a business case for migrating to the AWS Cloud. While the study is not specific to Amazon OpenSearch Service, it covers key value areas that are common across most cloud migrations, including migrating to Amazon OpenSearch Service.

In most cases, Amazon OpenSearch Service delivers lower TCO. When calculating TCO, it's critical to incorporate staffing cost. Understanding the time and cost that your engineers spend to maintain the current environment is an important factor. Many customers compare only the cost of storage, compute, and networking infrastructure with the cost of the managed service. However, that might not provide you with an accurate total cost of ownership. Amazon OpenSearch Service provides your team with operational efficiencies by managing tasks that otherwise had to be performed by your engineers. This includes the following tasks:
+ Scaling a cluster by adding or removing nodes
+ Patching
+ Upgrading in-place
+ Taking backups
+ Configuring monitoring tools to capture logs and metrics

These activities are automated by the service, and AWS offers a production-level support team. This means that your staff can focus on activities that add direct value to your business.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
