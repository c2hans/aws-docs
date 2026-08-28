---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/introduction.html
---

# Disaster recovery strategy for databases on AWS
<a name="introduction"></a>

*Oliver Francis, Suhas Basavaraj, Balaji Desikachari, and Jitendra Kumar, Amazon Web Services*

In October 2021, Forbes Technology Council published an article titled [Why Disaster Recovery Is No Longer Optional For Today's Businesses](https://www.forbes.com/sites/forbestechcouncil/2021/10/12/why-disaster-recovery-is-no-longer-optional-for-todays-businesses/). The article quotes a U.S. Federal Emergency Management Agency (FEMA) study that states that 40 percent of small and medium businesses in the United States go out of business after a disaster. Furthermore, 25 percent of the businesses that reopen close down again within a year. Given the gravity of the subject, a well-prepared business continuity plan that includes a disaster recovery (DR) strategy for IT assets is crucial to ensure the long-term growth and success of your business. Cloud computing has made disaster recovery viable even for small and medium businesses by lowering the barrier to entry. Given the risks posed by the lack of an adequate solution in the case of a disaster, a business continuity plan that includes a DR strategy should be at the top of your priority list as a business leader.

If your workloads are running on AWS, undoubtedly a bulk of your data resides in AWS databases. Whether it is data stored in a relational database system (RDBMS) such as Amazon Aurora MySQL-Compatible Edition or a NoSQL database such as Amazon DynamoDB, this data is valuable to your business. Developing a DR strategy that is specific to databases on AWS helps you understand what AWS offers in terms of disaster recovery for your databases and how you can leverage this information in your DR plan for the AWS Cloud.

The following swim lane diagram presents high-level tasks associated with defining and implementing a DR strategy. The two columns show the tasks owned by the executive management team and the tasks owned by application owners and architects. The executive management team owns decision-making. This team defines the DR strategy to be followed by the organization, drives DR adoption across the organization, decides if automation will be required to accomplish DR goals, and defines the DR test plan.

When the DR strategy is in place, the executive management team works with the application owners and architects to choose the right databases that fit the recovery time objective (RTO) and recovery point objective (RPO) expectations that are derived from the DR strategy. As the executive management team drives the adoption of the DR strategy, application owners and architects evaluate the databases that are used within their applications and migrate to the right database if the current ones don't achieve the RTO and RPO set for their application. The application owners and architects also build automation if required and participate in DR testing to refine and improve the application-level DR.

![High-level process for defining and implementing a database DR strategy](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/images/guide-img/83d34a15-2fdf-4836-9bdc-934f468f5336/images/eac2a4d0-7111-48db-8945-d5265893ed9c.png)

This article explains these steps at a high level for business leaders and decision makers who want to formulate a cross-Region DR strategy that helps meet their business objectives. The article assumes some technical knowledge and familiarity with disaster recovery terminology but no AWS expertise.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
