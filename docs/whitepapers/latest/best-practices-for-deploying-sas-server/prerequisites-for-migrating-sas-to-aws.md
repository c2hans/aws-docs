---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/prerequisites-for-migrating-sas-to-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Prerequisites for migrating SAS to AWS
<a name="prerequisites-for-migrating-sas-to-aws"></a>

 Customers must have a solid understanding of SAS workload requirements and the hardware infrastructure required to meet service objectives – specifically time to complete the task. Existing SAS customers can use the following prompts to assess their understanding:
+  Are there any SAS jobs that must run within a certain timeframe? Do you expect your SAS jobs to execute in the same amount of time (or faster) than they are currently executing in your existing data center? If you do expect a similar execution, you should determine the AWS I/O throughput.
+  What is the location of the source data for the SAS job? If the data is not in AWS, you must consider the time connection requirements for migration. Added time will impact the SLA for jobs that consume data outside of AWS.
+  Is additional security required for the data and/or SAS code?

 SAS 9 workloads require instances that supports heavy analytical processing and large sequential I/O; SAS Viya processes data in memory with spill to disk, if required. These

 behaviors should be taken into consideration when selecting the correct Amazon EC2 instance types and storage requirements for AWS migration.

 Running SAS workloads on the cheapest AWS EC2 instances does not necessarily provide the best performance. For example, customers may require storage and server instances with more physical cores than required for computing needs and more storage capacity than the initial sizes required to acquire the maximum I/O bandwidth for their SAS application(s).

 Evaluate the following areas to understand the main considerations for optimal AWS performance:
+  Instance types for SAS 9.4, SAS Viya, and/or Hybrid
+  Ephemeral, persistent, and shared storage types
+  Shared file system for SAS Grid Manager
+  Placement of SASWORK, CAS\_DISK\_CACHE, and permanent SASDATA
+  High Availability, Security, and Authentication requirements
