---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/plan.html
---

# Planning
<a name="plan"></a>

To navigate the mainframe legacy application's requirements effectively, organizations often begin with a comprehensive assessment of their mainframe environment.

## Application discovery
<a name="app-discovery"></a>

A powerful tool in this initial phase is the [Rocket Enterprise Analyzer](https://www.rocketsoftware.com/en-us/products/enterprise-suite/enterprise-analyzer), which provides deep insights into the structure, dependencies, and complexity of mainframe applications. This tool helps you determine the scope of your modernization effort, potential risks, and opportunities for optimization.

One crucial aspect to uncover is the intricate web of data dependencies within mainframe systems. These dependencies are often hidden beneath layers of legacy code and can significantly impact modernization efforts. By mapping out how different applications and modules interact with various data sources, you can better understand the potential effects of any changes you plan to implement.

## Data dependencies
<a name="data-dependencies"></a>

A thorough assessment of data dependencies can reveal critical information about data flow, data quality, and data governance within your mainframe environment. This knowledge is invaluable when planning data migration strategies, ensuring data integrity during modernization, and identifying opportunities for data optimization. By gaining a clear picture of your data, you can make more informed decisions about which modernization approaches will be most effective and least disruptive to your existing operations.

A top-down analysis that identifies the usage of tables by transactions or job control language (JCL) jobs is key to creating wave planning and prioritization. This approach clarifies the relationships between different components of your mainframe systems, and helps you develop a strategic, phased approach to modernization. By identifying which tables are most frequently accessed and by which processes, you can prioritize your modernization efforts: You can focus on high-impact areas first and ensure a smoother transition with minimal disruption to critical business operations.

In addition to using Rocket Enterprise Analyzer to discover data dependencies, many organizations also use their own custom-built solutions to gain deeper insights into their mainframe environments. These in-house tools often exploit the wealth of information that's available in the IBM Db2 catalog and System Management Facility (SMF) records.

## Capacity benchmark
<a name="capacity"></a>

One step in planning your mainframe replatforming project is to gather detailed information about your current workload consumption. This data will help you accurately predict and provision the initial required capacity in your target cloud environment. For example, we recommend that you collect hourly million instructions per second (MIPS) consumption data for both online transactions and batch transactions from IBM Customer Information Control System (CICS) or Information Management System (IMS) and job control language (JCL) jobs.

IBM offers a diverse range of [pricing models](https://www.ibm.com/z/pricing) for MIPS in mainframe computing, and many of these models center around peak usage. Among these peak-based models, the most common is the rolling four-hour peak.

Mainframe costs include five key areas that significantly impact overall expenses:
+ Software licensing is often a major component. It covers operating systems, middleware, databases, and various applications, and costs are sometimes tied to machine capacity or usage.
+ Hardware expenses include the initial purchase or lease of mainframe equipment, ongoing maintenance, and upgrades.
+ Storage costs can be substantial because of the vast amounts of managed data managed, and involve disk systems, tape libraries, and associated management software.
+ Personnel expenses cover salaries for specialized mainframe professionals such as system programmers and database administrators.
+ Disaster recovery and business continuity measures, including backup systems, redundant hardware, and offsite recovery facilities, represent a significant investment in ensuring high availability and quick recovery.

These five cost categories, combined with MIPS-based charges, form the core of most mainframe budgets. However, their relative proportions can vary widely depending on your organization's size, industry, and specific mainframe utilization patterns.

Hourly MIPS data is crucial for gaining a comprehensive understanding of your mainframe workload patterns and performance. Unlike daily or monthly averages, hourly data provides granular insights that reveal the nuanced fluctuations in your system's resource utilization throughout the day. This level of detail is invaluable for accurately assessing your application's performance and capacity needs in the cloud .

By analyzing hourly MIPS data, you can identify peak usage periods, spot trends, and pinpoint potential bottlenecks that might be obscured in aggregated data, as shown in the following diagram. This granularity allows for more precise capacity planning, helps optimize resource allocation, and can potentially lead to cost savings and improved system efficiency.

![Analyzing hourly MIPS data before replatforming mainframe applications.](http://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/images/guide-img/b5c7b078-cfe6-46c4-b120-94b5824d3c88/images/ec7b7827-ce03-4076-a352-3a8d7aa8d76d.png)

Hourly MIPS data also serves as an essential performance benchmark tool. It establishes a detailed baseline of your system's performance, which is particularly valuable when you're planning or evaluating system changes such as migrations or upgrades. By comparing pre-change and post-change hourly MIPS data, you can accurately measure the impact of these modifications on your system's performance and ensure that your mainframe continues to meet your organization's needs.

To collect hourly MIPS data, you have several options. One approach is to use SMF records directly. These records provide a wealth of information about system activity and resource usage. Alternatively, you can use specialized tools such as the IBM Sub-Capacity Reporting Tool (SCRT), which can simplify the process of collecting and analyzing MIPS data.

Regardless of the method you choose, it's important to collect data over an extended period—ideally, several months. This extended collection period enables you to account for cyclical variations in your workload, such as end-of-month processing spikes or seasonal fluctuations. By capturing these long-term patterns, you can develop a more accurate and comprehensive picture of your mainframe's performance characteristics, which enables better-informed decision-making and more effective capacity management.

## Wave planning
<a name="wave-planning"></a>

You can use the information you gather to strategically prioritize your mainframe replatforming initiatives. A prudent approach is to begin with less critical workloads, such as non-core business transactions or batch jobs, to allow teams to gain experience and refine processes with minimal risk to essential operations. Additionally, considering read-only workloads as early candidates for migration can be advantageous, because these workloads typically involve less complexity and lower risk of data inconsistencies. This approach enables you to build confidence and momentum in your replatforming efforts.

In addition, grouping workloads that share Db2 tables for write or update operations can streamline the migration process. By identifying these interconnected workloads, you can plan cohesive migration waves that maintain data integrity and minimize the need for complex interim solutions. This strategy not only reduces the risk of data conflicts but also optimizes the overall replatforming timeline by addressing related components simultaneously. Ultimately, this data-driven prioritization approach ensures a balanced consideration of criticality, complexity, and interdependence, and leads to a more efficient and successful mainframe modernization process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
