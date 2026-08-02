---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/defining.html
---

# Defining your disaster recovery strategy
<a name="defining"></a>

Depending on how critical the applications in your organization are to your business, you might decide on a uniform strategy for all applications or develop a more complex DR strategy based on the criticality of each application. Your organization might tolerate a downtime of several hours before all applications are brought up in the DR site. In this case, you can opt for a cost-effective DR strategy based on backup and restore for all databases. On the other hand, your organization's business might depend on some critical services or applications becoming available rapidly, with more aggressive RPO and RTO requirements, whereas other applications might tolerate less stringent RPO and RTO needs. In this case, you will need to assign the right DR strategy for each tier of applications and databases.

The following table describes four DR options for workloads that run in the AWS Cloud, to help you determine and define your organization's DR strategy. The RPO and RTO documented in this table are for a full stack that includes both application and database components. For more information, see [Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) in the AWS Well-Architected Framework documentation. The next section covers RPO and RTO options that are specific to databases.

|
|
| Recovery option | RPO | RTO | Infrastructure tasks in DR Region | Cost |
| --- |--- |--- |--- |--- |
| **Backup and restore** | Hours | Less than 24 hours | Provision all required application resources in the DR Region and restore the database from a copied snapshot. | Low |
| **Pilot light** | Tens of minutes | Tens of minutes | Provision a copy of your application infrastructure and switch the resources in the application stack off. Replicate your data from one Region to another. Keep the databases always on and synchronized with primary databases. Provision the resources on demand during the failover and testing event. You also need to deploy infrastructure changes and application changes to both Regions simultaneously. You can simplify this by building automation pipelines that can synchronize code and infrastructure in both primary and DR Regions. | Medium |
| **Warm standby** | Minutes | Minutes | Provision a copy of the entire application infrastructure in the DR Region, but keep the copy scaled down compared with the primary Region. The DR Region will be able to accept traffic at a smaller volume compared with the primary Region.  | High |
| **Multi-site or active/active** | Near zero | Zero or near zero | Provision a complete copy of your infrastructure into the DR Region. All resources in the DR Region will be equivalent to the resources in the primary Region and will be able to serve traffic at the same scale as the primary Region. Because there is no break in the traffic flow, this option doesn't require a failover task as part of your DR plan. | Higher |
