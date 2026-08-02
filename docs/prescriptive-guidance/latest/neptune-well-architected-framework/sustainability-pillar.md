---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-well-architected-framework/sustainability-pillar.html
---

# Sustainability pillar
<a name="sustainability-pillar"></a>

The [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/sustainability.html) focuses on minimizing the environmental impacts of running cloud workloads. Key topics include a shared responsibility model for sustainability, understanding impact, and maximizing use to minimize required resources and reduce downstream impacts.

The sustainability pillar contains the following key focus areas:
+ Your impact
+ Sustainability goals
+ Maximized usage
+ Anticipating and adopting new, more efficient hardware and software offerings
+ Use of managed services
+ Downstream impact reduction

This guide focuses on your impact. For more information about the other sustainability design principles, see the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus-design-principles.html).

Your choices and requirements have an impact on the environment. If you can choose AWS Regions that have lower carbon intensity, and if your requirements reflect actual workload needs instead of just maximizing uptime and durability, the sustainability of the workload increases. The next sections discuss best practices and thoughtful considerations that will have a positive environmental impact if adopted in your workload design and ongoing operations.

## AWS Region selection
<a name="region-selection"></a>

Some AWS Regions are near Amazon renewable energy projects or located where the grid has a published carbon intensity that is lower than others. Consider the [sustainability impact](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/) for Regions that might be viable for your workload, and cross-reference your list with the [ Regions where Neptune is available](https://docs.aws.amazon.com/neptune/latest/userguide/limits.html).

## Consumption based on user-behavior patterns
<a name="user-behavior-patterns"></a>

Right-sizing your consumption to match the traffic and behavior of your users helps AWS minimize the impact of services on the environment. Consider the following best practices when designing your solution:
+ Monitor Amazon CloudWatch metrics such as `CPUUtilization`, `MainRequestQueuePendingRequests`, and `TotalRequestsPerSec` to determine when your demand is highest and lowest, and ensure that your cluster resources are right-sized during those times.
+ Automate the stopping of non-production environments during hours when they are not being used. For more information, see the blog post [Automate the stopping and starting of Amazon Neptune environment resources using resource tags](https://aws.amazon.com/blogs/database/automate-the-stopping-and-starting-of-amazon-neptune-environment-resources-using-resource-tags/).
+ If your traffic patterns vary frequently and unpredictably, consider using Neptune Serverless instances that will scale up and down with demand instead of using an instance provisioned for peak traffic.
+ Consider aligning your service-level agreements with sustainability goals in addition to business continuity goals. Easing requirements such as multi-Region disaster recovery, high availability, or long-term backup retention, especially for non-production environments or non-mission critical workloads, can reduce the amount of resources required to meet those goals.

## Optimize software development and architecture patterns
<a name="software-development-architecture-patterns"></a>

To prevent waste, optimize your models and queries, and share compute resources so that you use all the resources available in Neptune instances and clusters. Specific best practices include:
+ Have developers share Neptune instances and Jupyter Notebook application instances instead of each creating their own. Give each developer their own logical partition in a single Neptune cluster through the use of [multi-tenancy partitioning strategies](https://explore.skillbuilder.aws/learn/course/external/view/elearning/16133/data-modeling-for-amazon-neptune), and create separate notebook folders for each developer on a single Jupyter instance.
+ Implement patterns that maximize the use of resources and minimize idle time, such as parallel threads for loading data and batching records together into a larger transaction.
+ Optimize your queries and graph model to minimize the resources required to compute the results.
+ For Gremlin query results, use the [results cache](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-results-cache.html) feature to minimize the resources spent recalculating paginated or frequently recurring queries.
+ Keep your Neptune environments up to date. The newest versions of Neptune support the latest Amazon EC2 instances, such as Graviton, that are more efficient. They also have query optimization improvements and bug fixes that reduce the amount of resources needed to calculate your queries.
