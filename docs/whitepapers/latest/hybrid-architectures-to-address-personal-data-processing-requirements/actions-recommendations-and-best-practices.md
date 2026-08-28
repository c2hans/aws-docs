---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/actions-recommendations-and-best-practices.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Actions, recommendations, and best practices
<a name="actions-recommendations-and-best-practices"></a>

 AWS will not move data between Regions, meaning that data placed in Frankfurt (or any other AWS Region) will remain within the specified Region, unless the customer organizes cross-region Replication or data movement. If there is no personal data in the AWS Cloud, the customer can work with data in the AWS Cloud as usual (as suggested in Approach 2). Additional data residency considerations can be found in the [Data Residency: AWS Policy Perspectives](https://d1.awsstatic.com/whitepapers/compliance/Data_Residency_Whitepaper.pdf) whitepaper.

 This requirement is addressed in the following reference architectures:
+  2.1 [*Big Data and analytics, and machine learning use cases*](big-data-analytics-and-machine-learning-use-cases.md)
+  2.2 [*Local IdP for authentication flow and storing user data*](local-idp-for-authentication-flow-and-storing-user-data.md)
+  2.3 [*Industrial IoT with AWS IoT Greengrass*](industrial-iot-with-aws-iot-greengrass.md)
+  2.4 [*Website scenario with API engine and DBMS in on-premises data center*](website-scenario-with-api-engine-and-database-management-system-in-an-on-premises-data-center.md)
+  3.1 [*Disaster recovery with elastic disaster recovery*](disaster-recovery-with-elastic-disaster-recovery.md)
+  3.2 [*Read-replicas in Amazon RDS from on-premises databases*](read-replicas-in-amazon-rds-from-on-premises-databases.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
