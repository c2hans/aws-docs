---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/sas-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# SAS Architecture
<a name="sas-architecture"></a>

## SAS 9.4 Intelligence Platform
<a name="sas-9.4-intelligence-platform"></a>

 This platform is designed to efficiently access large amounts of data, while simultaneously providing timely intelligence to a large number of users. The platform uses an n-tier architecture that allows you to distribute functionality across compute resources, so that each type of work is performed by the resources most suitable for the job.

 This architecture consists of the following four tiers:
+  Data sources that store customers enterprise data
+  SAS servers that perform SAS processing on enterprise data
+  Middle tier that enables users to access intelligence data and functionality through a web browser, and provides shared services used by the platform’s applications
+  Client tier that provides desktop access to intelligence data and functionality through easy-to-use interfaces

![Diagram that shows the intelligence platform architecture with the four columns listed previously.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/images/intelligence-platform-architecture.jpeg)

 *Figure 1: SAS 9.4 Intelligence Platform Architecture*

### SAS 9.4 Grid
<a name="sas-9.4-grid"></a>

 The SAS grid computing environment uses SAS Grid Manager to distribute SAS computing tasks among multiple computers on a network. Workload distribution enables the following functionality:
+  Workload balancing allows multiple users in a SAS environment to distribute workloads to a shared pool of resources.
+  Accelerated processing allows users to distribute subtasks of individual SAS jobs to a shared pool of resources.
+  Scheduling jobs allows users to schedule automatically routed tasks to the shared resource pool.

![Diagram that shows the SAS Grid architecture.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/images/sas-grid-architecture.jpeg)

## SAS Viya
<a name="sas-viya"></a>

 SAS Viya is a cloud-enabled, in-memory analytics engine that provides quick, accurate and reliable analytical insights. Elastic, scalable, and fault-tolerant processing addresses complex analytical challenges while effortlessly scaling for future use cases. SAS Viya has the following benefits:
+  SAS Viya provides distributed analytical in-memory calculations that are optimized for unconstrained environments and automatically adjust in constrained environments.
+  SAS Viya supports a standardized code base that enables programming in SAS and other languages like Python, R, Java, and Lua.
+  SAS Viya is highly available with distributed processing crafted to handle multiple users distributing operations across the cores of a single server, or nodes of massive compute clusters.

![Diagram that shows an SAS Viya architecture.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/images/sas-viya-architecture.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
