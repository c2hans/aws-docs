---
source_url: https://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/operations-and-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Operations and management
<a name="operations-and-management"></a>

 HPC systems are traditionally highly decoupled and resilient to the failure of any given component, with minimal disruption. However, HPC systems in financial services organizations tend to be both mission critical and limited by the capabilities of traditional approaches, such as physical primary and secondary data centers. In this model, HPC teams have to choose between having secondary infrastructure sitting mostly idle in case of the loss of a data center, or using all of the infrastructure on a daily basis but with the possibility of losing up to 50% of that capacity in a disaster event. Some add a third or fourth location to reduce the impact of the loss of an individual site, but at the cost of an increased likelihood of an outage and network inefficiencies.

 When you move to the cloud, you not only open up the availability of new services, but also new approaches to solving these problems. AWS operates a model with [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/) that are always active and offer high levels of availability.

 By architecting HPC systems for multiple AWS Availability Zones, financial services you can benefit from high levels of resiliency and utilization. In the unlikely event of the loss of an Availability Zone, additional instances can be automatically provisioned in the remaining Availability Zones to enable workloads to continue without any loss of data and only a brief interruption in service.

![Diagram showing a sample HPC architecture for a Multi-AZ deployment](http://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/images/multi-az-hpc-architecture.png)

 The high-level architecture in the preceding figure shows the use of multiple Availability Zones and separate subnets for the stateful scheduler infrastructure (including schedulers, brokers, data stores) and the compute instances. You can base your scheduler instances on long-running instances (procured with a Savings Plan) with static IP addresses to help them communicate with on-premises infrastructure by simplifying firewall rules.

 Conversely, you can provision your compute instances using On-Demand or Spot with dynamically allocated IP addresses. [Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) act as a virtual firewall, which you can configure to allow the compute instances to communicate only with scheduler instances.

 With the Compute Instances being inherently ephemeral and with potentially limited connectivity needs, it can be beneficial to have them sit within separate private address ranges to avoid the need for you to manage demand for and allocate IPs from your own pools. This can be a significant benefit to organizations that might not want to allocate large IPv4 address ranges to an HPC platform that can scale to many thousands of instances. This can be achieved either through a [secondary CIDR on the VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#add-ipv4-cidr), or with a separate VPC for the compute infrastructure, connected through [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html).

![An example network architecture using AWS Direct Connect for private connectivity and a combination of Public/Routable and Private/Non-routable subnets](http://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/images/direct-connect-private-connectivity.png)

 The majority of AWS services relevant to financial services customers are accessible from within the VPC using [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/integrated-services-vpce-list.html), which offers private connectivity to those services, and services hosted by other AWS accounts and supported AWS Marketplace partner solutions. Traffic between your VPC and the service does not leave the Amazon network and is not exposed to the public internet.

 One of the keys to effective HPC operations are the metrics you collect and the tools to explore and manipulate them. A common question from end users is, “Why is my job taking so long?” It’s important to set up your HPC operation in a way that enables you to either answer that question, or to empower users to find it for themselves.

 AWS offers tools you can use to collect metrics and logs, at scale. [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) is a monitoring and management service that not only collects metrics and logs related to AWS services, but through an agent, it can also be a target for telemetry from HPC systems and the applications running on them. This provides a valuable central store for your data, and allows diverse data sources to be presented on a common time series, and helps you to correlate events when you diagnose issues. You can also use CloudWatch as an auditable record of the calculations that were completed, with the analytics binary versions that were used. You can export these logs to S3 and protect them with the object lock feature for long term, immutable retention.

 You may want to use a third-party log analytics tool. Many of the most common products have native integrations with Amazon Web Services. Additionally, [Amazon Managed Service for Grafana](https://aws.amazon.com/grafana/) enables you to analyze, monitor, and alarm on metrics, logs, and traces across multiple data sources, including AWS, third-party independent software vendors (ISVs), databases, and other resources.

 Some grid schedulers require a relational database for the retention of statistics data. For this purpose, you can use [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS), which provides cost-efficient and resizable database capacity, while automating administration tasks such as hardware provisioning, patching, and backups.

 Another common challenge with shared tenancy HPC systems is the apportioning of cost. The ability to provide very granular cost metrics according to usage can drive effective business decisions within financial services.

 The *pay as you go* pricing model of AWS empowers HPC managers and their end customers to realize the benefits from the optimization of the system or its use. AWS tools such as resource tagging and the [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) can be combined to provide rich cost data and to build reports that highlight the sources of cost within the system. Tags can include details of report types, cost centers, or other information pertinent to the client organization. There’s also an [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) tool that can be used to create reports and alerts according to consumption.

 When you combine detailed infrastructure costs with usage statistics, you can create granular cost attribution reports. Some trades are particularly demanding of HPC capacity, to the extent that the business might decide to exit the trade instead of continuing to support the cost.
