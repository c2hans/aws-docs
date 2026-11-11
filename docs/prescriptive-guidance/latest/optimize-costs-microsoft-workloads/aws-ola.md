---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/aws-ola.html
---

# AWS Optimization and Licensing Assessment
<a name="aws-ola"></a>

## Overview
<a name="aws-ola-overview"></a>

An [AWS Optimization and Licensing Assessment (AWS OLA)](https://aws.amazon.com/optimization-and-licensing-assessment/) can help you assess and optimize your current on-premises and existing cloud environments, based on resource utilization, third-party licensing, and application dependencies. You can use AWS OLA to help your organization build a migration and licensing strategy that identifies opportunities to reduce costs as you migrate to AWS or assess existing Microsoft workloads on AWS. An AWS OLA can also help you do the following:
+ Understand existing deployments, application performance, and contracts.
+ Rightsize your resources.
+ Develop a roadmap to the AWS Cloud.
+ Help reduce costs by using existing investments and paying only for what you use.

We recommend that you make an AWS OLA the first step on your [cost optimization journey](cost-optimization-journey.md). You can work with AWS Partner Network partners to complete an AWS OLA. These partners can help you gather assessment data and provide recommendations for optimizing your licensing and instance costs.

The following diagram provides an overview of the assessment process.

![Full AWS OLA process](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/94961a8b-a59d-47be-81fb-b5143c07a14a.png)

## Assessment options
<a name="aws-ola-options"></a>

You can choose from two AWS Optimization and Licensing Assessment (OLA) options for your Microsoft workloads on AWS:
+ **Lite version** – In this use case, all of your workloads are on VMware. You can provide AWS with an output from [RVTools](https://www.robware.net/). Then, AWS can offer a turnaround time of 1–5 days. This approach uses point-in-time information pulled directly from VMware vCenter to develop sizing recommendations and offer on-demand pricing options.
+ **Full version** – In this use case, you have a mixed environment running in different cloud providers, physical servers, and virtual servers. AWS uses operating system agents to collect usage data from 14 to 30 days. This allows AWS to make informed instance sizing decisions based on your application usage patterns. AWS uses several third-party tools, such as Cloudamize, to complete the analysis. AWS works with its AWS Partner Network to help deliver the final total cost of ownership (TCO) assessment with multiple pricing options that factor in pricing models and different architectures.

## Full assessment
<a name="aws-ola-assessment"></a>

The full AWS Optimization and Licensing Assessment (OLA) begins with a one-hour phone call. During this call, AWS helps you determine the most suitable AWS infrastructure to support your migration, choose a data collection method, and establish a timeline for completion. Implementing discovery tooling in your organization depends on the data collection method, the size of your organization, and the tooling that your organization uses to manage its fleet of servers. It typically takes two to three weeks to collect usage data.

The full AWS OLA process takes between 30–45 days and consists of the following phases:
+ Scope workloads
+ Collect data
+ Analyze data
+ Plan next steps

### Scope workloads
<a name="scope-workloads.f8b426b7-51c6-539d-901a-630c061b685b"></a>

First, AWS works with you and your team to determine the scope of the assessment. This is usually broken down by environment type (for example, non-production and production). The scope includes the location of the workloads. This could be workloads that you're migrating to AWS, workloads that are already running on AWS (for example, AWS OLA for Amazon EC2), or workloads running in other cloud providers.

### Collect data
<a name="collect-data.8663af0e-f586-5cf6-ae80-2db3742e3050"></a>

Next, AWS deploys tooling to help with resource discovery and collect performance data from your servers. This tooling comes in four deployment options:
+ Tools that can query the hypervisor (requires only VMware vCenter or Hyper-V credentials)
+ Agents that you can deploy on physical or virtual machines
+ Agentless discovery by using Secure Shell (SSH), Windows Remote Management (WinRM), or Windows Management Instrumentation (WMI), depending on your environment and operating system
+ Flat file data collection and analysis

For your tooling deployment, you can combine options and consolidate results. Choose options that don't strain your IT resources. AWS strives to make the assessment process as simple as possible. Beyond a brief phone call to assist with setup, the AWS OLA team and AWS Microsoft specialist solutions architects prepare the total cost of ownership (TCO) analysis and recommendations for your review.

Data collection usually takes two to three weeks when AWS analyzes CPU utilization, RAM utilization, storage throughput, input/output operations per second (IOPS), and network throughput. Collect data during the peak times of your business month (for example, during end-of-month financial reporting). AWS captures peak usage because it provides representative statistical samples for sizing the right-sized AWS instance, which helps you meet or exceed the performance that's available on premises. AWS merges utilization metrics with performance heuristics of various processor generations to estimate how much CPU and RAM a given workload requires. These targets are usually less than what's allocated on premises. This approach reduces the compute cost based on instance size and can also help optimize licensing costs.

The following dashboard view shows an example of infrastructure costs that can be captured by an assessment.

![Infrastructure costs dashboard](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/bf561587-751e-4720-862a-777cf8e790a1.png)

### Analyze data
<a name="analyze-data.e9c138f0-3809-5fe2-a864-2bc27f8bf325"></a>

AWS delivers a debrief presentation after data collection is complete. AWS reviews the data, summarizes findings, and then makes recommendations for on-premises usage and cloud migration. You can reduce compute and licensing costs by examining consolidation opportunities, elasticity gains (where you can stop workloads or adjust them seasonally), and right-SKU opportunities (for example, SQL Server Enterprise edition is in use, but resource requirements and feature usage suggest SQL Server Standard edition is suitable). For products like SQL Server that are licensed by the core, it can make financial sense to place workloads in a more expensive compute instance. This is the case if the CPU profile and ratio of RAM to vCPU reduce the number of licensed cores for both license-included and Bring Your Own License (BYOL) use cases.

The following shows an example analysis based on the data collected by the assessment.

![AWS OLA analysis output](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/82e1b75d-3027-4492-bfc9-88b716573999.png)

Common optimization scenarios include identifying both AWS resource optimization opportunities and third-party license savings.

Examples of AWS resource optimization opportunities:
+ Avoid overprovisioning for peak usage.
+ Avoid over-specifying and underusing resources.
+ Right-size your instances and migrate to current-generation Amazon EC2 instances.
+ Reduce operations costs by moving to managed databases.

Examples of third-party license savings:
+ Reduce required cores to run the same workload.
+ Remove unnecessary SQL Server Enterprise edition and add-on packs.
+ Remove unused servers and replace outdated hardware.
+ Use BYOL and license-included options to reduce future commercial agreements.
+ Modernize to open-source and cloud-native solutions.

### Plan next steps
<a name="plan-next-steps.12e18d98-df5d-5ef1-bcd8-201792fa2ea0"></a>

Finally, AWS uses the collected performance data to estimate specific workload sizing and cost. AWS can also look in aggregate at your scoped environment and provide a quantitative analysis. This can help you determine whether an on-premises refresh or a migration to AWS is the more suitable option. You can build a cloud economic business case by using the TCO analysis summary (as shown in the following example) provided at the end of an AWS OLA.

![TCO analysis summary from an AWS OLA](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/9f0dd9d0-c4d4-4685-91a4-5037c2f89cb0.png)

An AWS OLA also provides insight into the impact that modernization can have on your existing workloads by making suggestions such as the following:
+ Move to a Linux operating system.
+ Add application support for ARM processors (AWS Graviton).
+ Move SQL Server workloads to Amazon Aurora.
+ Remove software assurance by moving Windows and SQL Server workloads to open-source technologies.

The following diagram shows the cost savings that can be achieved through modernization techniques such as moving from Windows to Linux or from SQL Server to Aurora.

![Migration costs diagram](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/c4ba252c-3143-459b-beef-3effd7bf723e.png)

The full AWS OLA process takes up to 45 days from start to finish. The following diagram shows an example timeline.

![Full AWS OLA process workflow](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/ce8d6761-9302-4b00-aaae-0ae843bc714b.png)

If you have a pure VMware environment and can provide output from RVTools, then you can reduce this timeline to one business week. Additionally, AWS can analyze a flat file that includes asset and utilization data, such as CPU average, CPU peak, RAM average, and RAM peak.

## Assessment impact
<a name="aws-ola-assessment-impact"></a>

Customers can often reduce costs through right-sizing, although results vary by workload. Right sizing matches the source workload to appropriately sized AWS instances based on usage data. These right-sizing adjustments not only reduce the monthly cost of the AWS environment, but can also result in savings elsewhere in the organization. For example, reducing Windows or SQL Server licensing requirements can lower the next true-up with Microsoft, or free up licensing for additional line-of-business applications. Consolidating and right sizing SQL Server workloads can often yield significant financial savings.

AWS can help you categorize systems into modernization categories. Some legacy systems are not financially viable to modify, while you can modernize others into containers or serverless applications, which can provide additional savings. The conversation with your AWS team moves from generalized topics about what the cloud enables to more specific discussions about how and why you should modernize specific workloads. AWS also helps you explore potential innovation opportunities.

## Next steps
<a name="aws-ola-next-steps"></a>

If you're beginning your cost optimization journey for Microsoft workloads that are running in on-premises environments or on AWS, engage with your AWS account team and request an AWS Optimization and Licensing Assessment (AWS OLA). AWS team members can answer your questions and help you decide if an AWS OLA is the right choice for you and your organization. Alternatively, you can [request an AWS OLA online](https://pages.awscloud.com/global-acq-ln-aws-migration-assessment-interest.html).

## Additional resources
<a name="aws-ola-resources"></a>
+ [AWS Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/) (AWS documentation)
+ [AWS re:Invent 2022 - How to save costs and optimize Microsoft workloads on AWS (ENT205)](https://www.youtube.com/watch?v=Zyhd2FmdtJs) (YouTube)
