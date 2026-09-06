---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about replatforming COTS and in-house applications.

## When should I choose to replatform instead of rehosting?
<a name="when-should-i-choose-to-replatform-instead-of-rehosting-.8e0cf4dc-a6c6-5f81-a601-2fc9398baf1c"></a>

You should replatform non-database components if the OS vendor has discontinued security updates (for example, RHEL 5 and Windows 2008). For unsupported OSs, you can rehost components to an isolated private subnet and upgrade them before you deploy them to a production environment.

For database components, you should evaluate if replatforming to a commercial database on Amazon RDS is an appropriate choice. You can also use a self-managed database running on Amazon EC2 if the database's vendor allows you to use your current license on the AWS Cloud.

## Can I refactor my COTS application to an open-source database?
<a name="can-i-refactor-my-cots-application-to-an-open-source-database-.078a9543-64f5-5f19-b701-045b7eca4e36"></a>

It's possible to refactor a COTS application to an open-source database if your application's vendor supports open-source databases. We don't recommend using open-source databases for COTS applications without obtaining the vendor's support.

## What AWS tools can I use to quickly rehost my servers to the AWS Cloud?
<a name="what-aws-tools-can-i-use-to-quickly-rehost-my-servers-to-the-aws-cloud-.dcdcdeff-46ed-506e-91bd-af48623a670a"></a>

You can use [Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html) as your primary migration service to lift and shift your applications to AWS.

## What AWS tools can I use for replatforming my applications?
<a name="what-aws-tools-can-i-use-for-replatforming-my-applications-.5a99e64d-4a7e-5061-a6bf-8d424d29da2b"></a>

There are several tools available on the AWS Cloud including:
+ [Systems Manager automated upgrades](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/automated-upgrades.html) – Upgrade Windows 2008 and SQL Server 2008 on the AWS Cloud.
+ [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) – Convert database schema from commercial to open-source databases.
+ [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) – Replicate data from on-premises databases to the AWS Cloud, either on Amazon RDS databases or databases running on Amazon EC2.
