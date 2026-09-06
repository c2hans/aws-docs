---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/other-areas-of-consideration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Other areas of consideration
<a name="other-areas-of-consideration"></a>

Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service M1 to M2 Migration Magento 1.x versions (M1) to Magento 2.x versions (M2) migration consists of four main components:
+  Data migration
+  Extensions migration
+  Custom code migration
+  Theme migrations

 A deep dive into these four areas specific to how the organization has setup M1 outlines the challenges and the migration strategy. Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service has developed the [Data Migration Tool](https://devdocs.magento.com/guides/v2.3/migration/migration-tool-install.html) for data migration and Code Migration Toolkit for code migration. These resources are described in detail in the [Magento Migration Guide](https://devdocs.magento.com/guides/v2.3/migration/bk-migration-guide.html).

## Magento hardware sizing guidelines on AWS
<a name="magento-hardware-sizing-guidelines-on-aws"></a>

 As per [Magento hardware recommendations](https://devdocs.magento.com/guides/v2.3/performance-best-practices/hardware.html), Adobe recommends that one CPU core can effectively serve around two (up to four) Magento requests along with one `cron` process simultaneously. Determine your organization’s stable expected request rate to find the appropriate number of cores needed to support your application and use automatic scaling to dynamically extend web tier nodes as needed.

 *`N[Cores] = (N[Expected Requests] / 2) + N [Expected Cron Processes]`*

 In addition, Adobe recommends at least 2 GB memory on build servers and 1 GB on web nodes along with sufficient network bandwidth to prevent bottlenecks on read-write operations.

 Keeping these principles in mind, choose the appropriate instance from the [Amazon EC2 instance](https://aws.amazon.com/ec2/instance-types/) types that balances your organization’s cost and business needs. Instance types from the Amazon EC2 general purpose family (especially M types) provide a good balance between compute, memory, and network resources for Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service applications.

## Backups and disaster recovery (DR)
<a name="backups-and-disaster-recovery"></a>

 As a best practice, explore backup and disaster recovery (DR) options based on your business needs. Backup and disaster recovery options depend on the deployment option and database choices (Amazon RDS vs Amazon Aurora) you choose. Your organization’s business needs dictate the recovery point objective (RPO) (that is, the maximum time to last backup) and the recovery time objective (RTO). RTO often varies depending upon the size of your organization’s storage.

 At a minimum, we recommend that you take regular database backups and have a working copy of the AWS CloudFormation template to provision the infrastructure when needed in case a recovery situation arises. Alternately, you can choose to have a working Amazon Machine Image (AMI) copy that has Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service installed along with your organization’s latest changes or customizations. You can use this AMI to provision infrastructure using an AWS CloudFormation template to reduce the overall RTO.
