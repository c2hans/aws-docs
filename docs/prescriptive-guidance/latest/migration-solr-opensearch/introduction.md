---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/introduction.html
---

# Migrating from Apache Solr to Amazon OpenSearch Service
<a name="introduction"></a>

*Bharav Patel, Amazon Web Services*

This guide helps teams migrate from Apache Solr to OpenSearch. Solr is a search platform that's built on Apache Lucene and supports both lexical and vector search capabilities, but most teams use it primarily for lexical search. OpenSearch is a powerful search and analytics engine that's also built on Apache Lucene. Although Solr has an established community, OpenSearch has a growing developer base that frequently adds new features. This active development has led many organizations to adopt OpenSearch.

This document focuses on migrating lexical search projects from Solr to OpenSearch and covers three key areas: planning, data and metadata migration, and the proof of concept (PoC) phase.

The target audience includes search engineers, solutions architects, and migration teams that need to successfully transition their search workloads.

**Note**
OpenSearch is a fully open sourced engine. AWS offers managed services for the OpenSearch engine (Amazon OpenSearch Service and Amazon OpenSearch Serverless), as discussed in the [overview](overview.md#about-opensearch). This guide uses the term *OpenSearch* interchangeably, to refer to both the search engine and and the AWS managed services that support it. In the discussion of features that are specific to the AWS services, it uses the service names.

Migrating from Solr to OpenSearch requires addressing several fundamental differences between the two products:
+ **Cluster architecture**: Transitioning from the external coordination (ZooKeeper) in Solr to the self-contained cluster management in OpenSearch.
+ **Data structure**: Moving from collection-based to index-centric data organization.
+ **Query syntax**: Adapting queries from the parameter-based syntax in Solr to JSON query domain-specific language (DSL) in OpenSearch.
+ **Configuration management**: Replacing Solr XML configurations with the REST API and YAML-based settings in OpenSearch.
+ **Schema definitions**: Converting Solr `schema.xml` to mapping definitions with appropriate field type and analyzer translations in OpenSearch.
+ **Scaling model**: Adopting the elastic scaling approach that OpenSearch provides instead of the shard-based scaling in Solr.
+ **Security framework**: Implementing integrated security in OpenSearch instead of the plugin-based authentication in Solr.
+ **Monitoring and operations**: Transitioning to Amazon CloudWatch from the Java Management Extensions (JMX) based monitoring features in Solr.

## About this guide
<a name="about-this-guide"></a>

This guide is organized into sections that address the following migration tasks.

**Planning and assessment**

See sections: [Planning](planning.md), [Learning about OpenSearch](learning.md)
+ Common migration challenges and pain points
+ Cost comparison methodologies and infrastructure calculations
+ Migration intake form and assessment criteria
+ OpenSearch training resources and skill-building recommendations

**Architectural foundation**

See section: [Architectural comparison](architectural-comparison.md)
+ Fundamental architectural differences between Solr and OpenSearch
+ Distributed cluster management models and their implications
+ Collection-based architectures compared with index-centric architectures
+ Query language and operational scaling philosophies
+ Comprehensive feature comparison tables

**Schema and configuration migration**

See sections: [Migrating your schema](migrating-schema.md), [Migrating your configuration](migrating-configuration.md)
+ Schema migration: Detailed field, tokenizer, and filter mappings with conversion tables
+ Configuration migration: Translation of Solr configuration files, including request handlers, caches, commits, and update processors

**Infrastructure and security**

See sections: [Sizing your OpenSearch cluster](sizing-cluster.md), [Migrating security features](migrating-security.md)
+ OpenSearch cluster sizing recommendations based on Solr topology
+ Security considerations and implementation guidance

**Data and application migration**

See sections: [Migrating indexing components](migrating-index.md), [Migrating search queries](migrating-queries.md), [Migrating the Admin Console](migrating-console.md)
+ Data migration: Multiple approaches, including reindex strategies, connector-based tools, and custom solutions with complexity assessments
+ Search migration: Query syntax conversion, SQL query support, and Learning to Rank (LTR) considerations
+ Indexing component migration: Best practices for transitioning indexing workflows

**Operations and monitoring**

See section: [Monitoring](monitoring.md)
+ Administration console migration strategies
+ CloudWatch-based monitoring setup and advanced monitoring options
