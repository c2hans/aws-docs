---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/placement-groups-in-sas.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Placement groups in SAS
<a name="placement-groups-in-sas"></a>

 Cluster placement groups are recommended for all SAS core infrastructure components that benefit from low network latency, high network throughput, or both, and if the majority of the network traffic is between the instances in the group. To provide the lowest latency and the highest packet-per-second network performance for your placement group, choose an instance type that supports enhanced networking such as I3 instances. While it is possible that there could be some degradation of performance, partition placement groups and spread placement groups help reduce impact from the likelihood of correlated hardware failures for the application.

 In a partition placement group, each group is split into logical segments called partitions containing their own set of racks with separate power supplies and networks. This creates a hardware resiliency in case of failure. A partition placement group can have partitions in multiple Availability Zones in the same Region.

## Clients
<a name="clients"></a>

 The most common placement of SAS clients like SAS Enterprise Guide, SAS Data Integration Studio and SAS Studio should be within the same Region where the other SAS infrastructure is located. These clients can be on a Windows server or a Windows Virtual Desktop, and it is required to determine a place for these Windows systems.

 Depending on the volume of data being transferred back to the SAS client, having the clients and backend server in the same Availability Zone, Placement Group or Region yields the fastest results. SAS clients can be placed on the same instance (Windows

 Server) as the backend server as well, allowing SAS users to access both the clients and the backend server.

## SAS infrastructure
<a name="sas-infrastructure"></a>

 SAS has several tools that allow sharing of SAS data files on-premises with SAS applications that run on AWS and vice-versa. Network bandwidth over the internet can be limited, sometimes as low as 500 KB/second, which can further constraint the I/O required by SAS applications

 If higher I/Os are desired, you can use [AWS Direct Connect](https://aws.amazon.com/directconnect/faqs/?nc=sn&loc=6), which is a private network connection between AWS and your datacenter or corporate network that provides a high bandwidth, consistent network experience. It is best practice to have SAS applications and the frequently accessed data in the same Region and Availability Zone.

## Source data files
<a name="source-data-files"></a>

 It is best practice to co-locate the source data files in the same Region and Availability Zone as the systems using those files. Many SAS GUI based clients pull data from the source data files when populating screens, so having the source data files across slow network connection to AWS will greatly impact performance of the SAS client.

## Authentication tools
<a name="authentication-tools"></a>

 If the interaction is frequent, it is recommended to co-locate the authentication tool in the same Region/Availability Zone/placement group. However, in many cases once access is obtained interaction is infrequent with authentication tool and the tool can be located either on-prem or in another availability zone.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
