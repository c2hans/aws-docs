---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/playbooks.html
---

# Playbooks
<a name="playbooks"></a>

Playbooks are end-to-end, copy-pasteable runbooks for specific source-to-target migration paths. Each playbook walks you through a single path from connectivity checks to cutover using the Workflow CLI and supporting `console` commands that run in the Migration Console pod (`migration-console-0`) on Amazon Elastic Kubernetes Service (Amazon EKS). Where the general procedure in [Configure and run workflows](use-the-solution.md) describes each phase in isolation, a playbook strings those phases together into one ordered sequence tailored to a particular source and target.

Every playbook assumes Migration Assistant is already deployed on Amazon EKS. If you have not yet deployed the solution, complete [Deploy the solution](deploy-the-solution.md) first, then return here. Each playbook also assumes you have confirmed the installed version with `console --version` and loaded the version-matched sample with `workflow configure sample --load`.

**Important**
Always run a pilot on a small index allowlist before you attempt the full migration. The pilot is the fastest way to surface mapping, authentication, and throughput problems before they affect production data. For the shortest safe path to a first migration, follow [Getting started with the Workflow CLI](use-the-solution.md#getting-started) and run [Step 8: Run a pilot migration first](use-the-solution.md#step-8-pilot) before widening scope.

Use the following table to choose the playbook that matches your source and target.

| Playbook | Migration path | When to use it |
| --- | --- | --- |
|  [Elasticsearch 6.8 to Amazon OpenSearch Service](playbook-es68-to-os3.md)  | Elasticsearch 6.8 source to an Amazon OpenSearch Service domain | Use this when migrating a self-managed or Amazon OpenSearch Service Elasticsearch 6.8 cluster. This path supports Reindex-from-Snapshot (RFS) backfill plus optional Capture and Replay for zero-downtime cutover, and it covers the Elasticsearch 6.x type-mapping deprecation. |
|  [Amazon OpenSearch Service to Amazon OpenSearch Serverless NextGen](playbook-aos-to-serverless.md)  | An Amazon OpenSearch Service domain source to an Amazon OpenSearch Serverless NextGen collection | Use this when moving an existing Amazon OpenSearch Service domain onto Amazon OpenSearch Serverless NextGen. This path uses SigV4 authentication on both clusters (`service: es` for the source domain, `service: aoss` for the target collection) and covers the data access policy mapping that Amazon OpenSearch Serverless NextGen requires. |
|  [Apache Solr to Amazon OpenSearch Service](playbook-solr-to-os3.md)  | Apache Solr source to an Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection | Use this when migrating from Apache Solr. This playbook covers backup-based backfill through RFS. For SolrCloud sources with JSON-format writes, you can add live Capture and Replay with the Solr transform providers described in [Capture and replay live traffic from Solr](solr-capture-replay.md). |
