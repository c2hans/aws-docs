---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/overview-cutover-phase.html
---

# Overview of the cutover phase
<a name="overview-cutover-phase"></a>

In the cutover phase of the migration process, you move network traffic from your existing endpoints to your newly deployed resources in the AWS Cloud. For example, you may update the Domain Name System (DNS) records to the endpoints for your newly provisioned Elastic Load Balancer. For most applications, you'll likely have multiple integration points that must be cut over during this phase of the migration (for example, cutting over the application and database tier to migrate a two-tier application).

The time, complexity, and risks associated with a cutover depend on your business requirements, technology stack, risk appetite, application architecture, and other factors. However, in general, as the cutover window decreases in time, the complexity of the cutover increases. There is a strong correlation between the length of the required downtime window for the cutover and the criticality of the applications being migrated. Typically, the risk increases for business-critical applications because they require a shorter downtime window. This increased risk, in turn, leads to the need for more extensive planning to manage the complexity and mitigate the risks of the cutover.

The cutover phase comes toward the end of the [migration process](https://aws.amazon.com/cloud-migration/how-to-migrate/). The following diagram shows where the cutover phase fits in to the migration process. As the diagram illustrates, communication and governance (covered in the next section of this guide) play a significant role in the cutover phase.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/images/guide-img/94c79f7c-efad-49a8-bca9-aadde0a15691/images/d3fb3d1a-4c20-4383-b88b-234f988fa16b.png)
