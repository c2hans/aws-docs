---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/architectural-differences.html
---

# Core architectural differences
<a name="architectural-differences"></a>

## Distributed cluster management model
<a name="cluster-management"></a>

Solr and OpenSearch represent two distinct philosophies in managing distributed search clusters. Each provides a unique approach to distributed cluster management.

Solr takes a modular approach to distributed cluster management by using Apache ZooKeeper as an external service in SolrCloud deployments. This architecture delegates critical cluster management functions to ZooKeeper. It creates a clear separation: Solr nodes focus on search and indexing, and ZooKeeper handles the distributed orchestration.

In this model, each component has a distinct responsibility. However, the need to maintain two services introduces additional complexity and management overhead. The coordination is through a hub-and-spoke model where all Solr nodes communicate through the centralized ZooKeeper service.

The following diagram illustrates the Solr architecture.

![Modular architecture in Apache Solr.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/images/guide-img/20cfd7ab-1afd-4038-9280-20666ff596e1/images/a1e5a352-bf7d-42bf-a9c5-edf73b7003d1.png)

In comparison, OpenSearch implements an integrated distributed cluster management model. The platform uses a master-eligible node concept where designated master nodes handle cluster state management. This self-contained approach integrates cluster management with cluster state information that's published to all nodes through internal communication channels. This model simplifies deployment scenarios.

You can deploy OpenSearch clusters without additional external cluster management services such as ZooKeeper. However, this approach couples distributed cluster management with the search service, and resources are shared.

The following diagram illustrates the OpenSearch architecture.

![OpenSearch architecture in comparison with Apache Solr.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/images/guide-img/20cfd7ab-1afd-4038-9280-20666ff596e1/images/ffc5a297-c3ff-4182-b51e-f6adeaa36bc0.png)

As the architecture diagram shows, OpenSearch offers a modern, cloud-native, distributed architecture that's designed for scalability and flexibility with specialized node roles, built-in security, and extensive plugin support. Solr follows a more traditional, monolithic design that's centered around nodes. Solr architecture is simpler but less adaptable to complex, large-scale deployments. OpenSearch is architected specifically for modern, scalable cloud deployments with advanced features such as machine learning, fine-grained security, multi-tier storage, and comprehensive observability. Although Solr remains a solid choice for traditional search applications, OpenSearch is better suited for organizations that require enterprise-grade security, advanced analytics, and cloud-native scalability.

## Collection and index management
<a name="collection-index-mgmt"></a>

Solr and OpenSearch take different approaches to organizing and managing data within their platforms, reflecting their underlying design philosophies and target use cases.

## Resource abstraction
<a name="resource-abstraction"></a>

The following table compares Solr and OpenSearch components.

|  |  |  |  |
| --- |--- |--- |--- |
| Component | Description | Solr | OpenSearch |
| Cluster | A group of nodes used for search and indexing capabilities | Uses Apache ZooKeeper for cluster orchestration. | Cluster orchestration is built in by using manager nodes (formerly known as master nodes). |
| Collection and index | A logical namespace that holds a complete set of searchable documents. | Typically requires a schema but also supports schemaless mode, which can automatically infer field types. | Supports dynamic mapping where fields are inferred from the data, and explicit mapping where a schema is provided at index creation. |
| Shard | A logical partition of an index or collection. This is a fundamental concept for achieving scalability and distributed data storage. | + Consists of leader shards and replica shards.+ Lacks node awareness, so leader shards and replica shards can be placed on the same node. | + Consists of primary shards and replica shards.+ Enforces a strict separation of primary and replica shards on different nodes.+ Amazon OpenSearch Service has Availability Zone awareness that places shards in different Availability Zones when available. |
| Replica | A copy of the data used for redundancy. | Can be elected to a leader if the leader fails. | Can be promoted to primary if the primary fails. |
| Document | The fundamental unit of information that's indexed. This is equivalent to a record in a relational database. | Accepts data for indexing in various formats, including JSON, XML, and CSV. | Supports only JSON format for indexing. |
| Field | Represents a specific piece of data within a document. | Fields can be configured with various parameters within a mapping, such as index (whether the field should be indexed for searching) or store (whether the original field value should be stored). | Same as Solr. |
| Field type | Defines how a specific type of field data is processed. | Supported field types are covered in the [Migrating your schema](migrating-schema.md) section. | Supported field types covered in the [Migrating your schema](migrating-schema.md) section. |
| Analyzer | Transforms raw text into a structured format that the search engine can process effectively. | Defined as part of the field type. | Defined at the index level and referenced by the field. This allows multiple fields to reuse the same analyzer. |
| ConfigSet | A set of configuration files that can be shared across collections. | Contains `schema.xml`, managed schema, `solrconfig.xml`, and similar files and is stored in ZooKeeper for distribution across the cluster. ConfigSets enable consistent configuration management and simplify the deployment of multiple collections that have similar requirements. | Not supported. |
| Collection alias | Named pointer to one or more collections. | Simplifies client access and enables collection swapping. Aliases are also useful for time-based indexes and index rotation scenarios, and provide flexibility in managing collection lifecycles. | Not supported. |
| Index template | Pattern-based template for automatically configuring newly created indexes. | Not supported. | Applied when new indexes match a specified pattern. Templates enable consistent configuration across time-series data or similar scenarios. They provide a powerful mechanism for enforcing standards and automating index creation. |
| Data stream | Time-based sequence of indexes that automatically creates new backing indexes. | Not supported. | Optimized for append-only time-series data such as logs or metrics. Data streams remove the complexity of managing time-based data at scale. They provide a unified interface for writing and querying while handling lifecycle management. |
| Index State Management (ISM) | An automated lifecycle management system that allows you to define policies for how indexes should be managed over time based on their age, size, or document count. | Not supported. | ISM policies consist of states (such as hot, warm, cold, and delete) and transitions that define when and how indexes move between these states. This functionality enables automatic actions such as changing replica counts, moving indexes to different storage tiers, performing rollover operations, or deleting old data. It helps optimize storage costs and performance by automatically transitioning indexes from high-performance storage when they're actively written to, down to cheaper storage as they age and become read-only, and eventually deleting them when they're no longer needed. |

## Configuration approaches
<a name="configuration-approaches"></a>

Solr employs a file-based configuration model where core settings are defined in `solrconfig.xml` and schema definitions in `schema.xml` (or `managed-schema.xml`). In SolrCloud deployments, these configurations are stored in ZooKeeper and can be updated by using the **upconfig** command. Although many schema modifications can be made dynamically through the Solr Schema API without requiring a restart, certain configuration changes in `solrconfig.xml`—particularly those that affect core initialization, caching, or request handlers—require a collection reload. This reload process is generally quick and doesn't require a full Solr restart, but it does momentarily interrupt query processing for that collection.

As a fully managed service for OpenSearch, Amazon OpenSearch Service takes a fundamentally different approach. You cannot access the underlying `opensearch.yml` configuration files or the server infrastructure directly. All configuration management is performed exclusively through the OpenSearch REST APIs, the AWS Management Console, the AWS Command Line Interface (AWS CLI), or infrastructure as code (IaC) tools such as AWS CloudFormation and HashiCorp Terraform.

In Amazon OpenSearch Service, you can modify most index settings, mappings, analyzers, and cluster-level configurations dynamically through these APIs without any service interruptions. Changes to index mappings, search analyzer configurations, replica counts, and numerous cluster settings are applied immediately or with a simple index close/reopen cycle. This API-driven approach provides significant operational flexibility, so you can adjust your search configurations as your requirements evolve.

Certain cluster configurations—such as instance types, storage volumes, dedicated master node settings, Availability Zone distribution, and virtual private cloud (VPC) configurations—require a blue/green deployment. During this process, a new environment is provisioned with the desired configuration, data is migrated from the old environment, and traffic is switched to the new cluster. Although this process is automated and designed to minimize downtime, it represents a more significant change operation than simple API updates.

Additionally, you don't have access to the underlying YAML configuration files, so any settings that would typically require file-level modifications in self-managed OpenSearch deployments are either exposed through AWS APIs and console options, or are not available for user modification. AWS manages security configurations, network settings, memory allocation, and other node-level parameters as part of the managed service offering.

## Query language and data access differences
<a name="query-language-differences"></a>

Solr provides flexibility through multiple query parsers that accommodate different levels of complexity and developer preferences. The traditional Solr approach uses URL parameter-based queries where search criteria, filters, sorting, and faceting are expressed as query string parameters. This method remains widely used due to its simplicity and ease of debugging directly in a browser or API testing tool. For more complex query requirements, Solr also offers a JSON request API that structures queries in JSON format, which provides better organization for intricate search logic while maintaining relatively concise syntax. This dual approach allows developers to choose the method that best fits their use case, from simple searches to sophisticated queries with multiple clauses.

OpenSearch relies exclusively on a structured, JSON-based query domain-specific language (query DSL). All queries, regardless of complexity, are expressed as nested JSON objects that explicitly define query clauses, filters, aggregations, and other search parameters. The query DSL uses a hierarchical structure where Boolean logic, term matching, range queries, and other operations are clearly delineated within specific JSON blocks. This approach provides comprehensive expressiveness and removes ambiguity about query intent. However, it typically results in more verbose query structures compared with the URL parameter approach in Solr, even for relatively simple searches.

For more information about key architectural differences, see:
+ [Apache Solr vs OpenSearch – Comparison and Key Differences](https://bigdataboutique.com/blog/apache-solr-vs-opensearch-comparison-and-key-differences-d7c790) (BigData Boutique blog post)
+ [A Comprehensive Guide to OpenSearch and Elasticsearch Architecture](https://www.instaclustr.com/blog/opensearch-and-elasticsearch-architecture/) (NetApp Instaclustr blog post)
+ Karambelkar, Hrishikesh Vijay. *Scaling Apache Solr: Community Experience Distilled*. Packt Publishing Ltd., 2014.
+ [Apache Solr Reference Guide](https://solr.apache.org/guide/solr/latest/index.html) (Apache documentation)
+ [OpenSearch documentation](https://docs.opensearch.org/docs/latest)
+ [Migrate from Apache Solr to OpenSearch](https://aws.amazon.com/blogs/big-data/migrate-from-apache-solr-to-opensearch/) (AWS blog post)
