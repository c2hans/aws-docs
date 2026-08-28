---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/timestream-for-influxdb-well-architected-framework/sustainability.html
---

# Sustainability pillar
<a name="sustainability"></a>

The [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/sustainability.html) focuses on minimizing the environmental impacts of running cloud workloads.  The sustainability pillar contains the following key focus areas:
+ Understanding your impact
+ Sustainability goals
+ Maximizing use to minimize resources
+ Anticipating and adopting new, more efficient hardware and software offerings
+ Using managed services
+ Reducing downstream impact

This guide focuses on understanding your impact. For more information about the other sustainability design principles, see the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus-design-principles.html).

Your choices and requirements have an impact on the environment. To increase the sustainability of your workload, do the following:
+ Choose AWS Regions that have lower carbon intensity.
+ Size your resources to reflect actual workload needs instead of maximizing uptime and durability.
+ Optimize your data model and maximize compute resource use.

The next sections discuss practices that you can adopt to reduce environmental impact in your workload design and ongoing operations.

## AWS Region selection
<a name="region-selection"></a>

Some AWS Regions are near Amazon renewable energy projects or located where the grid's published carbon intensity is lower than other grids. Evaluate Regions based on your [sustainability goals](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/) and your workload requirements. Then cross-reference your list of viable Regions with the Regions where [Timestream for InfluxDB is available](https://docs.aws.amazon.com/general/latest/gr/timestream.html).

## Base resource consumption on user-behavior patterns
<a name="consumption"></a>

Right-sizing your consumption to match the traffic and behavior of your users helps AWS minimize the impact of services on the environment. When designing your solution, consider the following best practices:
+ Monitor Amazon CloudWatch metrics such as `CPUUtilization` and `MemoryUtilization` to determine when your demand is highest and lowest. Ensure that your instance resources are right-sized during those times.
+ Consider aligning your service-level agreements with sustainability goals in addition to business continuity goals. Easing requirements such as multi-Region disaster recovery, high availability, or long-term backup retention can reduce the amount of resources required to meet those goals.. Non-production environments and non-mission critical workloads provide opportunities to reduce requirements.

## Optimize software development and architecture patterns
<a name="dev-arch-patterns"></a>

To prevent waste, optimize your data model and queries. Share compute resources so that you use all the resources that are available in the Timestream for InfluxDB instance. We recommend implementing the following best practices:
+ Encourage developer teams to share the Timestream for InfluxDB stack for better usage of resources wherever possible.
+ Implement patterns that maximize the use of resources and minimize idle time. Pattern examples include using parallel threads to load data and batching records together into a larger transaction.
+ Optimize your queries and InfluxDB data model to minimize the resources required to compute the results.
+ Use [InfluxDB tasks](https://docs.influxdata.com/influxdb/cloud/process-data/get-started/) to pre-aggregate the data and reduce the scanning of the same raw data by different users for visualizing or dashboarding.
+ Keep your Timestream for InfluxDB environments up to date. The newest versions of Timestream for InfluxDB support the latest EC2 instances, such as Graviton, that are more efficient. The newest DB versions also include query optimization improvements and bug fixes that reduce the amount of resources needed to calculate your queries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
