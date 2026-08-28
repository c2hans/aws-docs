---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/amazon-eks-anywhere-and-aws-services-at-single-management-console.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 2.6 Amazon EKS Anywhere and AWS services at single management console
<a name="amazon-eks-anywhere-and-aws-services-at-single-management-console"></a>

 Requirements addressed:
+  **REQ1** (data residency)
+  **REQ2** (data protection)

 AWS services – [Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/)

![Amazon EKS Anywhere and AWS services at single management console](http://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/eks-anywhere-and-aws-services-single-management-console.png)

 Amazon EKS Anywhere and AWS services at single management console

 Requirement **REQ1** (data residency) can be met using Architecture 2.4: [Website scenario with API engine and DBMS in an on-premises data center](website-scenario-with-api-engine-and-database-management-system-in-an-on-premises-data-center.md). Requirement **REQ2** (data protection) can be met through complimentary use of Architecture 1.1: [Hybrid network connectivity from a data center to the AWS Cloud](hybrid-network-connectivity-from-a-data-center-to-the-aws-cloud.md).

 Amazon EKS Anywhere is a new deployment option for Amazon EKS that allows customers to use Amazon’s Kubernetes software within private data centers. Customers can run Amazon EKS Anywhere on their own on-premises infrastructure using VMware vSphere, with support for other deployment targets in the near future, including bare metal. Using VMware vSphere with AWS Direct Connect, integrating EKS Anywhere can help build solutions closer to the edge, and reduce barriers to cloud adoption by democratizing the consumption of cloud and easy integration with AWS Cloud services. The use cases EKS Anywhere solves the following.

 Use cases:

1.  **Low latency/high throughput applications** benefit from having compute closer to the user or other systems that require immediate responses.

1.  **Data residency and sovereignty** regulations by governments and industries such as healthcare require data to be stored locally. Or, customers may work on a long-term project that does not require migration to the cloud for two to three years, but still requires that the data to be close to the workloads and processing.

1.  **Local data processing** may, by necessity, be required to run close to an on-premises location, or at the edge.

1.  **Data transformation** allows customers to host legacy containers and data on-premises, while migrating to EKS Anywhere and EKS in the AWS Cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
