---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/planning.html
---

# Planning your Solr migration
<a name="planning"></a>

Migrating from Solr to OpenSearch requires careful planning because there is no direct one-to-one mapping between the two systems. Each migration requires a custom approach that's tailored to your specific use case. This guide focuses on migrating search functionality.

Although Solr and OpenSearch are both built on the Apache Lucene library, they have different architectures, deployment methods, and operational management approaches. The way applications interact with each system varies considerably. You might have built your application's search functionality by using the Solr client APIs for searching and data ingestion, but OpenSearch uses a completely different REST API structure that requires code changes.

Migrating to OpenSearch involves a steep learning curve. Without clear understanding and hands-on assistance throughout the migration process, you might face challenges because of the complexity of the process.

To determine whether OpenSearch is a viable alternative for your workload, become familiar with OpenSearch capabilities and the key challenges discussed in the [next section](learning.md), and consider conducting a proof of concept (PoC).

## Key migration challenges
<a name="key-challenges"></a>
+ **API and feature differences**. OpenSearch and Solr have fundamental differences with limited or no compatibility. Solr uses a file-based approach, whereas OpenSearch uses APIs to manage domains, to search, and to ingest data.
+ **New features**. OpenSearch requires learning new tools, plugins, and dashboards, such as OpenSearch Dashboards and Amazon OpenSearch Service ingestion.
+ **Configuration**. Setting up OpenSearch involves understanding shards, replicas, node roles, and performance tuning.
+ **Data migration**. Migrating data often means reindexing, changing schemas, and checking data accuracy.
+ **Security setup**. OpenSearch security requires setting up access controls, roles, and role mappings. It also involves configuring authentication backends such as basic authentication, JSON Web Tokens (JWTs), and SAML 2.0.
+ **Search and indexing flow**. You will need to redesign your existing search components that are based on Solr and rewrite queries. This is because OpenSearch uses query languages such as query domain-specific language (query DSL), Dashboards Query Language (DQL), SQL, and Piped Processing Language (PPL) instead of the query parsers that Solr uses. Additionally, you will have to redesign indexing components for compatibility with OpenSearch.
+ **Change adoption**. This is the biggest challenge. Your teams might resist change because they're comfortable with existing tools, they aren't familiar with OpenSearch, or they want to avoid disruptions during the transition.
+ **Custom plugins and customizations**. You will need to recreate or migrate custom Solr plugins and other customizations to work with the OpenSearch plugin architecture and APIs.
+ **Feature parity gaps**. Solr features such as specialized query parsers, multi-field aliases, and the ability to update field types in place (dynamic schema capabilities) are missing in OpenSearch, so they require workarounds or alternative approaches.

For more information about these challenges, see [Core architectural differences](architectural-differences.md) in the *Architectural comparison* section.

## Start small, scale later
<a name="starting-small"></a>

When you're planning to migrate to OpenSearch, you don't need a full implementation to validate functionality. A single-node cluster—even [AWS Free Tier](https://aws.amazon.com/opensearch-service/pricing/)—is sufficient for your PoC. You can load a representative data sample to test your critical search patterns and use cases. This minimal setup lets you quickly determine whether OpenSearch meets your functional requirements without the complexity of multiple nodes or indexing all historical data.

After your PoC validates that all search functionality works as expected, size your workload for production: Determine the number of nodes, calculate storage for your complete dataset, and design the full cluster architecture based on performance requirements and data volumes. Testing first and scaling later saves time and money, and helps you make better infrastructure choices.

## Cost comparison
<a name="cost-comparison"></a>

When you're comparing costs, we recommend that you consider the total cost of ownership (TCO) instead of initial price differences. Although OpenSearch typically costs less than proprietary search platforms, it might appear to be more expensive than self-managed Solr. However, this initial cost comparison doesn't provide the full picture.

Amazon OpenSearch Service eliminates significant operational overhead by automatically handling hardware provisioning, software installation, patching, data backups, and infrastructure changes through blue/green deployments. It also provides zero-downtime updates and upgrades—tasks that would otherwise require dedicated resources in a self-managed Solr environment.

These built-in capabilities substantially reduce your TCO by eliminating the time, effort, and personnel needed for routine maintenance and operations. When you factor in these operational savings, the more active OpenSearch development community, and frequent OpenSearch feature releases compared with Solr, the cost benefit becomes clear. The initial price difference is often offset by reduced operational burden and faster access to new capabilities.

## Calculating infrastructure costs
<a name="calculating-costs"></a>

Both Solr and OpenSearch use the Apache Lucene library, so their underlying data structures are similar and performance is  predictable. To achieve OpenSearch performance that's similar to, or better than, the performance of your existing Solr cluster, you should size your infrastructure as follows.

1. **Document your current Solr configuration**. Capture the following key metrics from your existing Solr implementation:
   + Number of shards and replicas
   + Primary shard size
   + CPU specifications
   + Total memory and Java virtual machine (JVM) memory allocation
   + Disk capacity and type

   You can use the following Microsoft Excel spreadsheet during the initial planning phase to document your current Solr implementation.

   [Download spreadsheet](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/samples/solr-migration-configuration.zip)

1. **Select the equivalent OpenSearch infrastructure by maintaining similar resources per shard**.
   + Use the collected metrics to choose OpenSearch instances with comparable resources.
   + Reference available instance options and pricing documentation.
   + Match or exceed your current resource allocation.

   For information about available instance types and cost, see [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/).

1. **Optimize during migration. **This migration presents an opportunity to:
   + Review existing performance bottlenecks in your Solr cluster and optimize your workload.
   + Address any under-scaling issues by provisioning additional resources.
   + Enhance your infrastructure to meet or exceed desired targets.

For additional items such as buffers, indexing components, and other data movement and persistence constructs used before writing the data to Solr, see the [Architectural comparison](architectural-comparison.md) section. To calculate your actual Solr costs, you will need to factor in third-party products, managed service provider (MSP) costs, and staffing costs, which are outside the scope of this guide.
