---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/query-features.html
---

# Search features
<a name="query-features"></a>

The following sections discuss some of the Solr search features and their equivalents in OpenSearch in more detail. After migration to OpenSearch, make sure to test all your queries in OpenSearch and compare the results with your Solr-based system. For your search applications, OpenSearch provides both high-level and low-level clients for multiple languages. For more information, see [OpenSearch language clients](https://docs.opensearch.org/latest/clients/) in the OpenSearch documentation.

## Key conversions and challenges
<a name="query-feature-conversions"></a>

Search feature conversion is the most complex aspect of migration. It requires the translation of the Solr `SolrFeature` class to OpenSearch DSL templates, the Solr `FieldValueFeature` class to the OpenSearch `field_value_factor` function, and function queries to OpenSearch scripts. Tree models have to be restructured into RankLib XML format, and neural networks require external service implementation. Query syntax conversion from Lucene to JSON DSL and performance optimization strategies differ significantly between the two systems.

Although the core LTR concepts remain the same, the implementation details differ significantly. The migration requires careful conversion of features, models, and queries, but can be largely automated with proper tooling.

## Join queries
<a name="query-joins"></a>

Solr lets you run join queries to perform inner joins on different datasets to create a normalized dataset.

In OpenSearch, you can use join operations through both Piped Processing Language (PPL) and SQL interfaces to combine data from multiple datasets.

PPL provides a simple join command with a straightforward syntax:

```
source=customer
| join ON c_custkey = o_custkey orders
| head 10
```

SQL offers more granular join control with support for `INNER`, `LEFT OUTER`, and `CROSS` joins; for example:

```
SELECT
    A.Body,
    B.Timestamp
FROM
    <tableNameA/logGroupA> AS A
INNER JOIN
    <tableNameB/logGroupB> AS B
    ON A. 'requestId' = B. 'requestId'
```

## Highlighting
<a name="query-highlighting"></a>

Solr highlighting features are quite similar to OpenSearch. They both support the original, fast vector, and unified highlighters, which makes the migration straighforward. Solr supports a few additional parameters such as `fragAlignRatio`, `fragsizeIsMinimum`, `alternateField`, and `fragmenter`. You might need some workarounds for these in OpenSearch. OpenSearch also supports semantic highlighting, which Solr doesn't offer.

## Streaming expressions
<a name="query-streaming"></a>

In Solr, you can use streaming expressions to perform real-time analytics and complex data transformations directly within Solr, without needing to export data to another system for processing. You can use these functions to perform mathematical and statistical operations, aggregations, and additional operations on search results as they are streamed back to the client.

Streaming expressions aren't natively available in OpenSearch. To perform streaming you can use either the `scroll` or `search_after` deep pagination technique to stream data out of OpenSearch.

## SQL queries
<a name="query-sql"></a>

Solr uses the `/sql` request handler with the Apache Calcite SQL engine and supports both JDBC driver connections and HTTP interfaces, whereas OpenSearch implements SQL through the `_plugins/_sql` REST API endpoint. For example:

```
POST _plugins/_sql
{
  "query": "SELECT * FROM my-index LIMIT 50"
}
```

In OpenSearch, you can implement functionality that's similar to the `/sql` handler, including complex operations such as lookup, join, and subsearch, by using PPL query language commands that are powered by OpenSearch-Calcite integration.

The SQL syntax is largely compatible between systems, but you'll need to update any Solr-specific features such as the `/export` handler for unlimited queries to equivalent mechanisms in OpenSearch, and ensure that field mappings align with the OpenSearch document structure instead of the schema-based approach that Solr uses. For more information about the SQL features in OpenSearch, see [SQL](https://docs.opensearch.org/latest/search-plugins/sql/sql/index/) in the OpenSearch documentation.

Migrating your queries requires:
+ If you're using JDBC, modifying the connection strings from the `jdbc:Solr://zkHost?collection=name` format to the REST-based approach in OpenSearch.
+ Adapting query parameters. Solr supports parameters such as `aggregationMode` and `numWorkers` for MapReduce operations, whereas OpenSearch focuses on format specifications such as `format=json/csv/jdbc`.

## PPL queries
<a name="query-ppl"></a>

PPL is a sequential, step-by-step query language that uses the pipe (`|`) operator to combine commands for processing data. It also supports advanced query options such as `join`, `lookup`, and `dedup` (data deduplication). When you migrate SQL handlers from Solr to OpenSearch, you can use PPL to deal with log analysis, data monitoring, or semi-structured datasets, because it offers a more intuitive and readable syntax for sequential data processing compared with traditional SQL queries. For more information, see [PPL](https://docs.opensearch.org/latest/search-plugins/sql/ppl/index/) in the OpenSearch documentation.

## Learning to Rank
<a name="query-ltr"></a>

Learning to Rank (LTR) is a machine learning approach that uses trained models to improve search result ranking in Solr and OpenSearch.

Solr LTR uses Java-based feature classes with `rq` parameter integration and schema-based storage, whereas OpenSearch LTR uses mustache templates with rescore queries and index-based `.ltrstore` storage. Both LTR implementations support linear and tree models.

To migrate LTR functionality from Solr to OpenSearch:
+ Migrate LTR models (migrate linear maps directly and convert trees to RankLib XML).
+ Update query patterns from `rq={!ltr}` to `rescore.sltr`.
+ Validate feature values and model scores for consistency.

For more information about LTR support in OpenSearch, see [Learning to Rank](https://docs.opensearch.org/latest/search-plugins/ltr/index/) in the OpenSearch documentation.

## Query debugging
<a name="query-debugging"></a>

### Profile API
<a name="profile-api.0ab0447d-b7dc-51b7-b65f-77a2c7f15746"></a>

For Solr users who migrate to OpenSearch, the Profile API replaces the `debug=timing` parameter that Solr uses for query performance analysis. You can add `"profile": true` to your OpenSearch search requests to get detailed execution breakdowns that are similar to the debug output in Solr.

OpenSearch profiles provide nanosecond-level breakdown for each query component. Profiles are  equivalent to query explanations in Solr but provide higher granularity. The OpenSearch response structure shows breakdowns for query parsing, execution, aggregations, and document retrieval phases, similar to how Solr breaks down query processing time.

Here's an example request that uses the OpenSearch Profile API:

```
GET /testindex/_search?human=true
{
  "profile": true,
  "query" : {
    "match" : { "title" : "rain" }
  }
}
```

For more information, see [Profile API](https://docs.opensearch.org/latest/api-reference/search-apis/profile/) in the OpenSearch documentation.

### Explain API
<a name="explain-api.94dba95d-821d-5739-a507-d5359f512c7b"></a>

You might be using `debug=result` parameter in Solr to understand why a particular document ranks higher or lower in search results. For similar functionality in OpenSearch, you can use the Explain API, which shows a detailed calculation of how the relevance score was calculated for each document. For example:

```
POST opensearch_dashboards_sample_data_ecommerce/_explain/EVz1Q3sBgg5eWQP6RSte
{
  "query": {
    "match": {
      "customer_first_name": "Mary"
    }
  }
}
```

For more information, see [Explain API](https://docs.opensearch.org/latest/api-reference/search-apis/explain/) in the OpenSearch documentation.
