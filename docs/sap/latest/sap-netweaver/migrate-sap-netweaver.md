---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/migrate-sap-netweaver.html
---

# Migrate SAP NetWeaver applications with AWS Migration Hub Orchestrator
<a name="migrate-sap-netweaver"></a>

 AWS Migration Hub Orchestrator simplifies and automates the migration of servers and enterprise applications to AWS. It provides a single location to run and track your migrations. It helps reduce migration costs and time by automating many migration tasks. Migration Hub Orchestrator offers templates to create a migration workflow that can be customized to fit your unique migration requirements.

With Migration Hub Orchestrator, you can migrate SAP NetWeaver based applications running on SAP HANA or any other database, such as Oracle, MSSQL, SAP ASE, etc., to AWS. For more information, see [What is AWS Migration Hub Orchestrator?](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/what-is-migrationhub-orchestrator.html)

You can access AWS Migration Hub Orchestrator from link: [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/) or from the AWS Command Line Interface.

**Topics**
+ [Migrate applications with SAP HANA](#hana)
+ [Migrate applications with any database](#anydb)

## Migrate applications with SAP HANA
<a name="hana"></a>

To migrate SAP NetWeaver based applications running on SAP HANA database, use the [Migrate SAP NetWeaver based applications and SAP HANA databases to AWS](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migrate-sap.html) template.

The following diagram illustrates an application migration with this template.

![Migrate an application using Migration Hub.](http://docs.aws.amazon.com/sap/latest/sap-netweaver/images/mho-hana.png)

## Migrate applications with any database
<a name="anydb"></a>

To migrate SAP NetWeaver based applications running on any database *other than SAP HANA*, use the [Rehost applications on Amazon EC2](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-on-ec2.html) Migration Hub Orchestrator template.

The following diagram illustrates an application migration with this template.

![Migrate applications with a database using Migration Hub.](http://docs.aws.amazon.com/sap/latest/sap-netweaver/images/mho-anydb.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
