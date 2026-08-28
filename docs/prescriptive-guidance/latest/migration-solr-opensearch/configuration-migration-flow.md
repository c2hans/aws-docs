---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/configuration-migration-flow.html
---

# Migration flow
<a name="configuration-migration-flow"></a>

This section describes an iterative approach to migrating your Solr configuration to Amazon OpenSearch Service. We recommend that you approach the process systematically by organizing your migration into three focus areas:

1. Settings: Translating Solr configuration to OpenSearch cluster or index settings

1. Search functionality: Translating Solr search functionality to OpenSearch search functionality

1. Document processing: Translating Solr document processing to Amazon OpenSearch Ingestion (OSI)

## Step 1. Migrate settings
<a name="configuration-migrate-settings"></a>

The components of your Solr configuration map to different Amazon OpenSearch Service features. The following sections cover the migration of Solr shards and replicas, codecs, commits, caches and queries, and index segments and merging. Amazon OpenSearch Service manages index storage locations directly, so Solr `dataDir` settings don't need to be configured.

Before you migrate every configuration setting from Solr, assess whether the setting can be adjusted based on your current search system experience and best practices. Some settings are configured at the cluster or node level, and not at the index level. These include the maximum number of clauses in a Boolean query, circuit breaker settings, and cache settings.

Instead of just lifting and shifting existing configurations, take the time to evaluate each setting's necessity and simplify complex configurations where possible. For example, the slow logs threshold of one second might be intensive for logging and can be revisited. You might also want to review and reduce the `max.booleanClauses` setting.

### Shards and replica settings
<a name="shards-and-replica-settings.7d22d031-49ca-5877-8dbd-f4f227d22693"></a>

Solr allows replica shards to be distributed across nodes for redundancy and fault tolerance, but it lacks node awareness during shard placement. This means that primary and replica shards might inadvertently be allocated to the same node, which compromises the intended high availability and benefits of replication.

Amazon OpenSearch Service ensures that primary and replica shards are not on the same node. When you enable zone awareness, Amazon OpenSearch Service makes a best effort to distribute primary shards and their corresponding replica shards to different Availability Zones.  When you configure dedicated master nodes and zone awareness for standby replicas, Amazon OpenSearch Service ensures that primary and standby replica shards are placed in different Availability Zones, which provides stronger resilience guarantees.

The OpenSearch and Solr definitions of a replica are different. In OpenSearch, you define a primary shard count by using the `number_of_shards` setting, which determines the partitioning of your data. You then set a replica count by using the `number_of_replicas` setting. Each replica is a copy of all the primary shards. Therefore, if you set `number_of_shards` to 5 and `number_of_replicas` to 1, you will have 10 shards (5 primary shards and 5 replica shards).

In OpenSearch, the following code creates an index called test with five shards and one replica.

```
PUT test
{
  "settings": {
    "number_of_shards": 5,
    "number_of_replicas": 1
  }
}
```

### Codec settings
<a name="codec-settings.8aa14f82-9bae-5307-a3dc-d5c42d7c5204"></a>

Both OpenSearch and Solr use the `best_speed` codec ([LZ4 compression algorithm](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm))) by default. Both offer `best_compression` ([zlib compression algorithm](https://en.wikipedia.org/wiki/Zlib)) as an alternative. OpenSearch also offers the [Zstandard compression algorithm](https://github.com/facebook/zstd) (`zstd` and `zstd_no_dict`).  Benchmarking for different compression codecs is also available. For more information, see [Index codecs](https://docs.opensearch.org/latest/im-plugin/index-codecs/) in the OpenSearch documentation.

Solr `<codecFactory>` configuration maps to OpenSearch `index.codec` settings; for example:

```
PUT /my_index/_settings
{
      "codec": "best_compression"
}
```

### Commit settings
<a name="commit-settings.de852f49-bf8b-58d2-a525-4c5b888d0c74"></a>

For near real-time search in OpenSearch, you have to set `refresh_interval`. The default is 1 second, which is suitable for most use cases. To improve speed and throughput, especially for batch indexing, we recommend that you increase `refresh_interval` to 30 or 60 seconds.

```
PUT /my_index/_settings
{
  "refresh_interval": "30s",
}
```

### Cache and query configuration comparison
<a name="cache-and-query-configuration-comparison.25edddfa-1e66-5f1a-9fcd-f8a7c49eed84"></a>

OpenSearch uses percentage-based memory allocation instead of entry count, so it provides more adaptive resource management than Solr as the index size changes. OpenSearch also supports [tiered caches](https://docs.opensearch.org/latest/search-plugins/caching/tiered-cache/), where each tier in a multi-tier cache has its own characteristics and performance levels.

The [maximum Boolean clause](https://docs.opensearch.org/latest/query-dsl/full-text/query-string/#parameters) is a static setting in OpenSearch. You set it at node level by using the `indices.query.bool.max_clause_count` setting.

OpenSearch simplifies many configurations by providing sensible defaults while still allowing fine-tuning through its cluster and index settings APIs. OpenSearch supports various cache configurations and types, such as shard request caches and node query caches.

Additionally, in Amazon OpenSearch Service, the [Auto-Tune](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html) feature uses performance and usage metrics from your OpenSearch cluster to suggest memory-related configuration changes, including queue and cache sizes and Java virtual machine (JVM) settings on your nodes.

### Index segments and merging
<a name="index-segments-and-merging.851b84c8-2a78-5385-a37f-86a1944784ac"></a>

OpenSearch default settings for merge policies work well for most workload patterns, and explicit merge configurations are rarely needed.

Both Solr and OpenSearch strive to optimize the balance between indexing performance and search efficiency.  The Solr `ramBufferSizeMB` and `maxBufferedDocs` settings are handled internally by OpenSearch. OpenSearch manages compound files automatically.

We recommend that you use the OpenSearch default merge policy settings as a starting point instead of copying settings from Solr. In most cases, you won't need to adjust these advanced settings unless you want to tune performance or you have unusual indexing patterns.  If tuning is required, as in the following example, see [Index settings](https://docs.opensearch.org/latest/install-and-configure/configuring-opensearch/index-settings/) in the OpenSearch documentation.

```
PUT /my_index/_settings{
  "index": {
    "merge.policy.segments_per_tier": 10,
    "merge.policy.max_merge_at_once": 10,
    "merge.scheduler.max_thread_count": 3,
    "merge.scheduler.max_merge_count": 7,
    "refresh_interval": "1s"
  }
}
```

## Step 2. Migrate search functionality
<a name="configuration-migrate-search"></a>

Solr request handlers define how search requests are processed. In OpenSearch, all searches use the `_search` or `_msearch` endpoint. As a best practice, most OpenSearch users prefer the `_search` API for its simplicity and clarity, whereas search templates are typically reserved for complex, reusable queries.

If you're accustomed to using the `/sql` request handler in Solr, you can use [SQL syntax](https://docs.opensearch.org/latest/sql-and-ppl/sql/index/) and the [Piped Processing Language](https://docs.opensearch.org/latest/sql-and-ppl/ppl/index/) (PPL) for querying in OpenSearch.

OpenSearch supports spell checking, also known as [Did-you-mean](https://docs.opensearch.org/latest/search-plugins/searching-data/did-you-mean/), and [highlighting](https://docs.opensearch.org/latest/search-plugins/searching-data/highlight/), during query time. You don't need to explicitly define search components.

Most API responses are limited to JSON format, except for the [compact and aligned text (CAT) API](https://docs.opensearch.org/latest/api-reference/cat/index/).

If you use the Velocity or XSLT response writer in Solr, you must manage it on the application layer in OpenSearch.

When you migrate the Solr `/select` request handler to OpenSearch, you need to transform the XML-based configuration in Solr to a JSON-based search query in OpenSearch. You can also optionally convert the request handler to a search template.

The following example shows how to transform a Solr `/select` handler configuration to OpenSearch. This handler specifies default search parameters, including results per page (`rows`:10) and default search field (`df`: `text`).

```
<!-- Request Handlers -->
  <requestHandler name="/select" class="solr.SearchHandler">
    <lst name="defaults">
      <str name="echoParams">explicit</str>
      <int name="rows">10</int>
      <str name="df">_text_</str>
    </lst>
  </requestHandler>
```

To migrate this handler, you first create the equivalent OpenSearch DSL query that matches the handler functionality. The following example demonstrates a basic search on the `_text` field with a size limit of 10.

```
GET /your_index/_search
{
  "size": 10,
  "query": {
    "match": {
      "_text": "your search term"
    }
  }
}
```

As a best practice, we recommend that you use the OpenSearch `_search` API to search directly. If you need reusable queries, you can create a search template for the equivalent query. The following example shows how to convert the query into a template by using mustache syntax with default parameters. The `rows` parameter in Solr maps to `size` (default: 10) in OpenSearch, and `df` maps to `default_field` (default: `text`). You can render the query by using the `_render/template` API or execute the template by using the `_search/template` API.

```
PUT _scripts/select_handler
{
  "script": {
    "lang": "mustache",
    "source": {
      "size": "{{#size}}{{size}}{{/size}}{{^size}}10{{/size}}",
      "from": "{{#from}}{{from}}{{/from}}{{^from}}0{{/from}}",
      "query": {
        "query_string": {
          "query": "{{query_string}}",
          "default_field": "{{#df}}{{df}}{{/df}}{{^df}}_text_{{/df}}"
        }
      }
    }
  },
  "params": {
    "size": "Number of results to return (default: 10)",
    "from": "Starting offset for results (default: 0)",
    "query_string": "The search query string (required)",
    "df": "Default field to search (default: _text_)"
  }
}

# To render the query for this template, applications would call:
POST _render/template
{
  "id": "select_handler",
  "params": {
    "query_string": "your search terms"
  }
}
```

## Step 3. Migrate document processing pipelines
<a name="configuration-migrate-document-processing"></a>

In Solr, update request processors (URPs) are essential for document transformation during indexing. In OpenSearch, this functionality is provided through [ingest pipelines](https://docs.opensearch.org/latest/ingest-pipelines/). For the `updateRequestProcessorChain`, OpenSearch provides the [ingest pipeline APIs](https://docs.opensearch.org/latest/api-reference/ingest-apis/index/), which let you enrich or transform data before indexing. You can chain multiple processor stages to form a pipeline for data transformation. Processors include Grok, CSV, JSON, KV, Rename, Split, HTML strip, Drop, Script, and others. For more information, see [Ingest processors](https://docs.opensearch.org/latest/ingest-pipelines/processors/index-processors/) in the OpenSearch documentation.

**However, we strongly recommend that you perform data transformations in your extract, transform, load (ETL) layer to remove this processing complexity from OpenSearch.** You can use [Amazon OpenSearch Ingestion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html) (OSI), which provides a framework and default processes for data transformation. OSI is built on [OpenSearch Data Prepper](https://docs.opensearch.org/latest/data-prepper/), which is a server-side data collector that can filter, enrich, transform, normalize, and aggregate data for downstream analytics and visualization.

OpenSearch also provides [search pipelines](https://opensearch.org/docs/latest/search-plugins/search-pipelines/index/), which are similar to ingest pipelines but tailored for search time operations. Search pipelines make it easier for you to process search queries and search results within OpenSearch. As of OpenSearch version 3.2 , available [search processors](https://docs.opensearch.org/latest/search-plugins/search-pipelines/search-processors/) include filter query, neural query enricher, normalization, rename field, script processor, and personalized search ranking, with more to come.

The following example shows how to transform a Solr `updateRequestProcessorChain` to OpenSearch. This chain includes two processors: a built-in `TrimFieldUpdateProcessorFactory` for whitespace trimming and a custom `CustomPriceTaxProcessorFactory` for price calculations.

```
<!-- updateRequestProcessorChain -->
<updateRequestProcessorChain name="standard">
  <processor class="solr.TrimFieldUpdateProcessorFactory"/>
  <processor class="com.mycompany.CustomPriceTaxProcessorFactory"/>
</updateRequestProcessorChain>
```

The two migration options are Amazon OpenSearch Ingestion (recommended) or using a custom plugin.

### Using Amazon OpenSearch Ingestion (recommended)
<a name="using-amazon-9999999999999999opensearch--ingestion--recommended-.19ba9875-ecf3-588a-ad49-e26bd77b8775"></a>

We recommend that you use Amazon OpenSearch Ingestion, because it provides:
+ Better separation of data transformation logic
+ Rich set of built-in processors
+ More efficient processing outside of OpenSearch
+ Easier maintenance and monitoring
+ Scalable data processing pipeline

To use this approach, you identify all the processors in the Solr chain and map them to [OpenSearch Ingestion processors](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/processors/). Identify any custom processors and analyze the functionality to determine whether it can be achieved through a combination of OpenSearch processors. You can then set it as a default pipeline for an index.

The following example creates an Amazon OpenSearch Ingestion pipeline with two processors. The first is a trim processor that removes leading and trailing whitespace from the `product_name` field. The second is an AWS Lambda processor that handles price calculations by applying a 10% tax rate to the price field. This is similar to the `CustomPriceTaxProcessorFactory` functionality in the custom Solr processor. We do not recommend using painless scripts for custom implementations, because they can affect performance.

First, create a Lambda function that implements the custom logic for price calculation:

```
def handler(event, context):
    if 'price' in event:
        price = float(event['price'])
        tax_rate = 0.10
        event['price'] = round(price * (1 + tax_rate), 2)
    return event
```

Then create an Amazon OpenSearch Ingestion pipeline:

```
pipeline:
  source:
    file:
      path: "/full/path/to/logs_json.log"
      record_type: "event"
      format: "json"

  processor:
    - trim_string:
        with_keys:
          - "product_name"
    - aws_lambda:
        function_name: "calculateTax"
        invocation_type: "request-response"
        aws:
          region: "us-east-1"

  sink:
    - opensearch:
        hosts: ["https://your-opensearch-domain:443"]
        index: "my_index"
```

### Using custom plugins
<a name="using-custom-plugins.0cca93dc-df93-5f8e-b97b-4be18cb1c6a7"></a>

When you migrate custom plugins from Solr to OpenSearch, we recommend that you first evaluate OpenSearch native features and existing plugins to determine whether they provide the desired functionality before you consider custom development. This approach ensures optimal utilization of OpenSearch native capabilities while maintaining flexibility for custom requirements.

The preceding example follows this approach. It uses an Amazon OpenSearch Ingestion pipeline and implements a custom Lambda processor to migrate `CustomPriceTaxProcessorFactory` by using similar logic.

If native features don't meet your requirements, Amazon OpenSearch Service supports custom plugin development and deployment. For more information, see the [Amazon OpenSearch Service documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-plugins.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
