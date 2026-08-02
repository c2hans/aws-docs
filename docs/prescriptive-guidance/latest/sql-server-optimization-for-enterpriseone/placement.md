---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/placement.html
---

# Placement of resources
<a name="placement"></a>

Because EnterpriseOne completes most business logic in the application tier, it tends to be very chatty across the network between the database and application tiers. As a result, processes that run on the application tier and access the database tier are often sensitive to network latency. To minimize network latency, we recommend that you place the EnterpriseOne database servers in the same placement group, within the same Availability Zone and Region, as the EnterpriseOne application servers.

If you are architecting a high availability configuration, you can use multiple techniques to ensure that the most sensitive processes run close to the database server. These techniques include using EnterpriseOne Object Configuration Manager (OCM) to map specific batch jobs (also known as UBEs) to specific servers, and using Virtual Batch Queues (VBQ) with remote nodes disabled.

For information about how to use a placement group on AWS, see [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the Amazon EC2 documentation[.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
