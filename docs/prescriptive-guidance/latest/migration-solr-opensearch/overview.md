---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/overview.html
---

# Overview
<a name="overview"></a>

## About Solr
<a name="about-solr"></a>

Apache Solr is an open source search platform that's built on Apache Lucene. It's designed to provide powerful search capabilities and enables users to search large volumes of data efficiently. Solr is highly scalable and fault-tolerant, so it's suitable for use in enterprise environments where high availability and reliability are critical.

### Core features
<a name="core-features.1d826198-723a-53a5-9f85-20c29e13a70a"></a>
+ **Full-text search**. Solr offers robust full-text search capabilities that enable users to perform complex queries on textual data.
+ **Faceted search**. Users can categorize search results into various facets, which facilitates easier navigation and filtering of results.
+ **Scalability**. Solr can scale horizontally and distribute data and queries across multiple servers to handle large datasets and high query loads. Solr offers a SolrCloud deployment option that provides automated load balancing, fault tolerance, and high availability through data sharding, replication, and centralized configuration management by using ZooKeeper.
+ **Real-time indexing**. Solr supports near real-time indexing, which enables new content to be searchable almost immediately after it's added.
+ **Rich document handling**. Solr can index and search various document formats, including XML, JSON, and plain text.
+ **Geospatial search**. Solr provides support for geospatial search, which enables users to perform location-based queries.
+ **RESTful APIs**. Solr offers RESTful APIs, which make it easy to integrate Solr with other applications and services.

### Use cases
<a name="use-cases.aa57a571-a32f-536f-a827-325d071ff574"></a>
+ **Ecommerce search**. Solr enhances product search with features such as autocomplete, spell check, and personalized recommendations.
+ **Site search**. Solr improves search functionality in websites and applications to make content more discoverable.
+ **Enterprise search**. Solr provides a unified search platform across various data sources within an organization.

### Deployment
<a name="deployment.d7a70c27-d734-54b1-b41d-9315f94c755d"></a>

You can deploy Solr in two ways: in standalone mode or in SolrCloud mode. Standalone mode is suitable for development or for small-scale applications, where a single Solr instance is sufficient. SolrCloud mode is designed for large-scale applications, where you want to distribute your workload across multiple Solr instances. SolrCloud uses ZooKeeper for cluster orchestration to ensure efficient and reliable performance. This makes SolrCloud a robust choice for handling more demanding, high-traffic environments.

Additionally, Solr supports container-based deployments, which enable it to run in Docker containers, Docker Swarm clusters, and Kubernetes environments. You can use Helm charts or operators for automated scaling and orchestration in Kubernetes.

### Community and ecosystem
<a name="community-and-ecosystem.f656445f-5844-5781-b797-06c5b7d1acc5"></a>

Apache Solr benefits from a strong community of developers and contributors who provide continuous improvements and updates. It integrates well with other big data technologies, such as Hadoop, and is often used in conjunction with data processing frameworks such as Apache Spark and Apache Kafka.

## About OpenSearch
<a name="about-opensearch"></a>

OpenSearch is fully open source search and analytics suite that's built on the Apache Lucene library. The platform includes OpenSearch (the search engine) and OpenSearch Dashboards (the visualization interface), which makes it suitable for ecommerce search, log analytics, observability, security analytics, enterprise search, and other search workloads. OpenSearch is part of the Linux Foundation. As a community-driven project, OpenSearch ensures that users maintain control over their data while they benefit from continuous improvements and security updates.

### Core features
<a name="core-features.e973545f-0a76-560a-8c9b-b64bf81e20a8"></a>
+ **Full-text search**. OpenSearch provides advanced text search capabilities with support for complex queries, relevance scoring, and language analysis.
+ **Distributed architecture**. OpenSearch scales horizontally across multiple nodes, which enables high availability and performance.
+ **Real-time data ingestion and analytics**. OpenSearch enables rapid ingestion and analysis of large volumes of data in near real time.
+ **Data visualization**. You can use OpenSearch Dashboards to create interactive visualizations and dashboards.
+ **Machine learning (ML) capabilities**. OpenSearch offers anomaly detection, forecasting, and other ML-driven insights.
+ **Vector database**. You can store and search billion-scale vectors that offer a variety of algorithms and engines.
+ **Security features**. OpenSearch includes fine-grained access control, encryption, and audit logging.
+ **Observability tools**. OpenSearch provides features for log analytics, metrics monitoring, and application performance monitoring.

### Use cases
<a name="use-cases.ec6d28c0-a26e-5720-9370-221fd7c355a2"></a>

OpenSearch supports lexical search, analytics, and AI-powered semantic search. Each of these categories include multiple use cases.

*Lexical search*

OpenSearch excels in traditional keyword-based search scenarios. It powers critical search functionality across various industries.
+ **Ecommerce search**: Enabling product discovery, faceted navigation, and personalized shopping experiences
+ **Enterprise search**: Unifying search across organizational data silos and internal knowledge bases
+ **Workplace search**: Facilitating employee access to documents, wikis, and corporate resources
+ **Site search**: Providing fast, relevant search capabilities for websites and content platforms

*Analytics*

The platform's robust analytical capabilities support data-driven decision-making and operational intelligence.
+ **Log analytics**: Processing and analyzing massive volumes of log data for troubleshooting and insights
+ **Observability**: Monitoring application performance, infrastructure health, and system metrics
+ **Anomaly detection**: Automatically identifying unusual patterns and outliers in time-series data
+ **Security analytics**: Analyzing security events and threats across infrastructure for compliance and threat hunting
+ **Business intelligence**: Supporting interactive dashboards and real-time analytical queries to derive actionable insights from data at scale

*Generative AI and semantic search*

OpenSearch supports modern AI-powered search paradigms.
+ **Vector search**: Supporting dense and sparse vector embeddings for semantic understanding, with multi-modal search capabilities that combine text, images, and other data types
+ **Hybrid search**: Blending traditional lexical search with vector-based semantic search for optimal relevance
+ **Conversational search**: Enabling natural language interactions and query understanding
+ **Retrieval Augmented Generation (RAG)**: Serving as a vector database for AI applications to retrieve contextual information
+ **Model Context Protocol (MCP) integration**: Supporting MCP servers that enable AI assistants to interact with OpenSearch clusters

### Deployment
<a name="deployment.472727e3-9905-54bf-ae09-3985efdeaa68"></a>

OpenSearch is fully open source, so  you can deploy it anywhere, by using any cloud provider. Amazon offers it as a managed service that takes care of infrastructure provisioning, installation, replication, backup, monitoring, and built-in resilience at the shard and Availability Zone level.

Managed OpenSearch is available in two deployment options:
+ [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) is a provisioned deployment option that enables you to size your cluster depending on your workload and choose your own instance types, sharding, and replication strategies. If you are looking for more control, choose Amazon OpenSearch Service.
+ [Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html) is a serverless deployment option for running OpenSearch. It automatically scales the underlying resources depending on your workload and manages sharding and data lifecycles by default.

This guide refers to OpenSearch, Amazon OpenSearch Service, and Amazon OpenSearch Serverless interchangeably.

## Feature comparison
<a name="feature-comparison"></a>

The following table compares Solr features with OpenSearch features. Some of these features are discussed in more detail later, in the [Architectural comparison](architectural-comparison.md) section.

|
|
| Feature | Apache Solr | OpenSearch |
| --- |--- |--- |
| Query language | Uses Apache Solr query parser and Lucene syntax; supports faceting, streaming expressions, and advanced queries. | Uses JSON-based query domain-specific language (query DSL); includes aggregations, advanced ranking, and behavior-based search.  Amazon OpenSearch Service also supports SQL through the SQL plugin and the Piped Processing Language (PPL). |
| APIs | Provides RESTful APIs with XML and JSON support; modern JSON API is available. | Provides RESTful APIs; compatible with Elasticsearch 7.x APIs. |
| Deployment | Runs on Java virtual machine (JVM); supports bare metal, VMs, containers, and Kubernetes with the Solr Operator. | Provides a cloud-native focus and runs on Amazon Elastic Compute Cloud (Amazon EC2) compute or serverless resources. Provides Kubernetes support for 3.x and later releases. You can use HashiCorp Terraform or AWS CloudFormation for deployments. |
| Performance | Optimized for batch indexing; uses global caching per index. | Optimized for real-time indexing; caches per segment for better performance.  Supports [concurrent segment search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/concurrent-segment-search.html), which is a performance optimization feature that parallelizes query execution at the segment level within individual shards. |
| Faceting and aggregations | Provides strong hierarchical faceting, which is useful for ecommerce. Supports Carrot, which is a clustering engine integrated into Solr that automatically organizes search results into thematic groups or categories based on content similarity. | Includes an aggregations engine that provides control over data analysis with a high degree of freedom. |
| Machine learning (ML) | Provides limited ML features through streaming expressions; supports Learning to Rank (LTR). | Includes the ML Commons plugin, which provides anomaly detection, neural search, regression, RAG, and clustering. |
| Multi-tenancy | Uses collections to provide data isolation. | Uses indexes for multi-tenancy. |
| Observability | Requires external tools such as Prometheus and Grafana. | Provides built-in OpenSearch Dashboards for visualization. |
| Security | Supports Basic, JSON web tokens (JWTs), Kerberos authentication, audit logging, and SSL encryption. | Supports JWTs, Active Directory, LDAP, OpenID, and SAML 2.0 authentication. Can use Amazon Cognito or AWS Identity and Access Management (IAM). |
| Backups | Supports remote backups through Amazon Simple Storage Service (Amazon S3) and Hadoop Distributed File System (HDFS); provides manual snapshot management. | Provides snapshot management policies for automated backups with support for various storage backends; supports cross-cluster replication. Amazon OpenSearch Service supports automatic snapshots. |
| Replication across data centers | Uses Apache Kafka for replication across clusters. | Follows an active-passive model, where the follower index pulls data from the leader without external software, through remote reindex (`_reindex`). |
| Ecosystem and plugins | Supports the installation of manual extensions  or using package management to include Zeppelin and Grafana. | Provides a large collection of plugins for ML, security, ingestion, and visualization. |
| Extract, transform, load (ETL) integration | Works with Apache NiFi and Logstash; provides ingestion pipeline support through update processors. | Integrates with Fluentd, Logstash, Vector, Data Prepper, Amazon OpenSearch Ingestion Pipeline, and other systems that can work with OpenSearch API. |
| Visualization | Doesn't provide built-in visualization; relies on external tools such as Apache Zeppelin or Grafana. | Provides built-in OpenSearch Dashboards for real-time visualization, and OpenSearch UI, which can aggregate domains under one UI. |
| Community and support | As a long-standing Apache Software Foundation (ASF) project, follows a slower development pace. | Is actively developed by AWS and the community with Linux Foundation support; provides frequent updates. |
| Enterprise support | Supported by third-party vendors. | Supported by AWS managed services; used in Red Hat development and Pulse. |
| Popularity, adoption, and use cases | Popular for structured search; widely used in publishing and ecommerce. | Strong in ecommerce, log analytics, observability, vector search, and real-time applications. |

## Differences between Solr and OpenSearch adoption
<a name="adoption-differences"></a>

OpenSearch and Solr are both powerful search and analytics engines that are built on Apache Lucene. Solr is an earlier search solution that has a longer history and a more mature community compared with OpenSearch. OpenSearch benefits from a vibrant and rapidly growing community that delivers cutting-edge features at a faster pace. This dynamic development environment and managed service support is driving the industry trend toward OpenSearch adoption, especially for organizations that prioritize ease of use, cloud-native advantages, and a well-rounded ecosystem. Solr remains the choice for highly customized needs and cost savings, but it requires more operational effort.

For more information, see [Benefits of migrating to Amazon OpenSearch Service](https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/benefits.html) on the AWS Prescriptive Guidance website.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
