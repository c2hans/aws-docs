---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/migration-journey.html
---

# Migration journey
<a name="migration-journey"></a>

Depending upon your current deployment, migrating to an Amazon OpenSearch Service can be a basic or complex procedure with multiple steps. In the following sections, you will explore migration approaches and key considerations in each step of the process. This includes the best practices based on our experience of helping many AWS customers migrate from existing tooling to Amazon OpenSearch Service. This section also discusses what constitutes an effective migration strategy.

A typical migration journey involves five stages:

1. Planning

1. Proof of concept (PoC)

1. Deployment

1. Data migration

1. Cutover

You might be migrating from a self-managed Elasticsearch or OpenSearch cluster or you might be migrating from another technology to Amazon OpenSearch Service. In most cases, the steps remain the same. The time you spend on each step will vary based on the complexity of your environment.

The migration journey starts with a careful planning activity, followed by a PoC exercise to ensure that the target environment meets your cost, security, performance, and migration goals. The PoC activity is followed by deploying the target environment and migrating the data to it. When you have confirmed that your data is synchronized between the current environment and the new environment, you can cut over to the new environment. After you cut over, you operate the environment following operational best practices. The following sections discuss each stage in detail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
