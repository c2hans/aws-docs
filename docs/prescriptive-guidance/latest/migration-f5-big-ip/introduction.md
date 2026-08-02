---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/introduction.html
---

# Migrating from F5 BIG-IP to F5 BIG-IP VE on the AWS Cloud
<a name="introduction"></a>

*Suresh Veeragoni, Amazon Web Services*

This guide provides an overview of the steps, architecture, tools, and considerations for migrating F5 BIG-IP security and traffic management solutions to the Amazon Web Services (AWS) Cloud. [F5 BIG-IP](https://www.f5.com/products/big-ip-services) is a collection of products that are designed around availability, access control, and security solutions. They run on the [F5 Traffic Management Operating System (TMOS)](https://www.f5.com/pdf/white-papers/tmos-wp.pdf).

Your F5 BIG-IP security and traffic management solutions are migrated to the AWS Cloud by using the [rehost and replatform migration strategies ](https://d1.awsstatic.com/whitepapers/Migration/aws-migration-whitepaper.pdf)from the seven common migration strategies (7 Rs). The F5 workload will be migrated by rehosting an existing environment and using aspects of replatforming, such as service discovery and API integrations.

This guide outlines the four main steps for your migration:
+ [Evaluating migration costs and skills](assess-costs.md) – Understand the costs of the migration and what knowledge of AWS and F5 products and services is required.
+ [Mapping the applications and designing the architecture](map-your-applications-architecture.md) – Assess how your applications fit together and design the architecture for their future environment.
+ [Planning the migration ](plan-migration.md)– Use a high-level plan for your migration and make key decisions about what to migrate.
+ [Migrating the data](migrate-your-data.md) – Deploy the configurations available for migrating F5 BIG-IP workloads to the AWS Cloud and migrate your data.

For a full overview of the migration steps, see the pattern [Migrate an F5 BIG-IP workload to F5 BIG-IP VE on the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-f5-big-ip-workload-to-f5-big-ip-ve-on-the-aws-cloud.html) on the AWS Prescriptive Guidance website.

This guide is intended for technical engineering and architectural teams that are migrating F5 security and traffic management solutions to the AWS Cloud.

## Targeted business outcomes
<a name="targeted-outcomes"></a>

Organizations choose to migrate to the AWS Cloud to increase their agility and resilience. This migration has significant benefits but also has risks that must be reduced. Specifically, the risk and complexity of cloud adoption is increased when important application services, such as traffic management or security, are split up.

If you migrate F5 BIG-IP workloads to the AWS Cloud, you can focus on agility and adopt high-value operational models across your enterprise architecture. You will also create a net positive for your cloud adoption because your technology environments can be federated.

You can also create a business advantage by limiting vendor or tool sprawl. This reduces risk when you migrate an application because it limits or removes changes to the data path, features, tools, and operational model from your source environment.
