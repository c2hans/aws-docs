---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-sas-viya-to-the-aws-cloud/architecture.html
---

# Architecture
<a name="architecture"></a>

Earlier SAS platforms, such as SAS 9.4 and SAS Grid Manager, run on AWS, and users can expect to see cost benefits and performance boosts depending on their selected compute and storage options. (Note that the Always-On Amazon EC2 instance–based system must provision itself for peak workloads.) The SAS Viya on Amazon EKS architecture illustrated in the following diagramnot only helps with shifting workload demands but also provides the following benefits:
+ Containerized microservices
+ Support for continuous integration and continuous delivery (CI/CD)
+ Small memory footprint
+ Fast startup times
+ Default multitenancy configuration
+ Subscription-based pricing choices
+ Overall reduced cost

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-sas-viya-to-the-aws-cloud/images/guide-img/6af091bd-620c-4ae4-9607-2e103616429a/images/02bd0352-0d13-4972-85ca-5aa93562e3dc.png)

The SAS Viya architecture contains the following components:
+ AWS Site-to-Site VPN allows SAS users to securely connect from their on-premises network or branch office to SAS Viya deployed on a virtual private cloud (VPC).
+ AWS Direct Connect allows users to connect to their SAS Viya VPC through a dedicated private network connection.
+ AWS Transit Gateway connects VPCs and on-premises networks through a central hub. This simplifies your network and puts an end to complex peering relationships. It acts as a cloud router – each new connection is made only once.
+ An internet gateway is attached to your VPC. By default, it comes with a security group that allows no inbound traffic and all outbound traffic to the internet.
+ In the public subnet:
  + A NAT gateway allows for instances in the SAS Viya private subnet to connect to the internet.
  + A Linux bastion provides secure access to the SAS Viya instances located in both the public and private subnets.
  + A Remote Desktop (RD) Gateway instance provides remote administration. This gateway uses remote desktop protocol (RDP) over HTTPS to establish a secure, encrypted connection between remote users on the internet and Windows-based EC2 instances.
+ In the private subnet:
  + Amazon EKS resource group with at least five node groups, identified by the work that they perform, optimizes the workload balance. These resource groups include stateless, stateful, cloud analytics services (CAS), compute, and default.
  + (Optional) A storage layer uses Amazon Relational Database Service (Amazon RDS) for PostgreSQL for the SAS Viya infrastructure data server and Amazon Elastic Container Registry (Amazon ECR) to store, manage, share, and deploy SAS Viya container images and artifacts anywhere.
  + Amazon Elastic Block Store (Amazon EBS) and/or Amazon EFS persist SAS datasets by using a container storage interface (CSI).

## Configuration options
<a name="configuration-options"></a>

SAS CAS provides the run-time environment where data management and analytics take place. The CAS server can be deployed to a single node or across multiple nodes. Deploying the CAS server on a single node facilitates symmetric multi-processing (SMP) and performs serial loads of data into memory from supported data sources.

The in-memory analytic features of a distributed CAS server are available to the single-node CAS server. Distributing the CAS server across multiple nodes enables massively parallel processing (MPP). One advantage of MPP is that, when possible, data is loaded into memory in parallel, which provides faster load times.

## Resource recommendations
<a name="resource-recommendations"></a>

There is no difference in the choice of instances between SAS 9.4 and SAS Grid Manager. That is, the deployment automatically selects EC2 instances that have good throughput, such as the I3e(n), M5(n), and R5(n) family of instances.

Use the following nodes according to their workload sizes and requirements:
+ Single large deployment: 5 or more nodes
+ Two or more large deployments: 7 or more nodes
+ With Amazon EC2 Auto Scaling, use the following:
  + 2 or more nodes per node group
  + 1 node in the default node group

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
