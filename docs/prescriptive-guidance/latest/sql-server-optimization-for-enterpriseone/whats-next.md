---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/whats-next.html
---

# Next steps
<a name="whats-next"></a>

This guide focused on optimizing a SQL Server configuration for EnterpriseOne. Topics such as database disaster recovery are beyond the scope of this document but should be addressed as part of the configuration; see the [Resources](resources.md) section for additional reading.

There are also many AWS services and features that you can use to optimize your EnterpriseOne system, including the following.

|
|
| AWS service | Use case |
| --- |--- |
| [AWS Transform MGN](https://aws.amazon.com/application-migration-service/) | You can use MGN to migrate EnterpriseOne from any source infrastructure that runs supported operating systems and databases, including Microsoft Windows, Red Hat Enterprise Linux (RHEL), Oracle Linux, SQL Server, and Oracle Database. |
| [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) | Elastic Disaster Recovery minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery. |
| [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/) | AWS DMS supports the migration of data between more than 20 different database platforms, including those used with EnterpriseOne. Common EnterpriseOne use cases include building data marts by using EnterpriseOne data. |
| [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) | The Application Load Balancer allows you to spread your workload among multiple HTTP or HTTPS-based EnterpriseOne application services. |
| [Amazon WorkSpaces](https://aws.amazon.com/workspaces/) | You can use Amazon WorkSpaces products to access high-performance workstations, on demand, for your JD Edwards development and administrative client applications. |
| [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) | You can use AWS Identity and Access Management (IAM) to provide authentication for EnterpriseOne. This service is available with EnterpriseOne Tools 9.2.5.4 or later, which supports JSON web tokens (JWTs). |
| [Amazon Simple Email Service (Amazon SES)](https://aws.amazon.com/ses/) | Amazon SES provides a reliable and compliant way to manage your EnterpriseOne emails. This service is available for all EnterpriseOne releases by using a third-party utility for SMTP authentication. EnterpriseOne Tools 9.2.7 and later versions provide support for authenticated SMTP with EnterpriseOne. |
