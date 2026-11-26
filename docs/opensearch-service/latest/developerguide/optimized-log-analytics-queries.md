---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/optimized-log-analytics-queries.html
---

# Supported query languages

This topic describes which query languages and features the Optimized engine supports, so that you can choose the right language for your workload and know which queries get acceleration. The Optimized engine supports Piped Processing Language (PPL), SQL, and OpenSearch query domain-specific language (query DSL). PPL and SQL run natively through the Optimized engine's vectorized execution engine. Query DSL support requires OpenSearch 3.9. This page describes support on OpenSearch 3.9. For complete syntax references, see the [OpenSearch SQL and PPL documentation](https://docs.opensearch.org/latest/sql-and-ppl/) and the [OpenSearch query DSL documentation](https://docs.opensearch.org/latest/query-dsl/) on the OpenSearch website.

## PPL support
<a name="optimized-log-analytics-ppl"></a>

The Optimized engine runs PPL (Piped Processing Language) natively. PPL is the primary query language in OpenSearch UI and is used by plugins such as Alerting and Anomaly Detection. For complete PPL syntax, see the [OpenSearch PPL reference](https://docs.opensearch.org/latest/search-plugins/sql/ppl/index/) on the OpenSearch website.

### Supported PPL commands
<a name="optimized-log-analytics-ppl-commands"></a>

The following PPL commands are supported on the Optimized engine:

| Category | Commands |
| --- | --- |
| Filter and project | where, fields, table |
| Order | sort, reverse |
| Limit | head |
| Top-N | top, rare |
| Compute and expand | eval, convert, expand1, mvexpand |
| Multi-value | mvcombine, nomv, flatten |
| Aggregate | stats, eventstats, addtotals, addcoltotals, trendline |
| Dedup | dedup |
| Rename | rename |
| Text | replace |
| Format | fieldformat |
| Null handling | fillnull |
| Parse | parse, rex, grok, regex, patterns1, spath |
| Bucketing | bin, chart, timechart, xyseries1 |
| Join | join, streamstats, lookup |
| Combine | append, appendcol, appendpipe, multisearch, union |
| Subquery | in subquery, scalar subquery |
| Metadata | describe, explain |

<sup>1</sup> Supported on indexes with one primary shard. See [PPL command and function restrictions](#optimized-log-analytics-ppl-unsupported).

Use `expand` for arrays of objects and `mvexpand` for multi-value scalar fields.

**Note**
The `convert`, `expand`, `mvexpand`, and `trendline` commands, along with nested-field and multi-value support, require OpenSearch 3.7 or later.

### Supported PPL functions
<a name="optimized-log-analytics-ppl-functions"></a>

The Optimized engine supports functions across the following families:
+ String: `upper`, `lower`, `length`, `concat`, `substring`, `trim`, `replace`, `reverse`, `left`, `right`, and more
+ Math: `abs`, `ceil`, `floor`, `round`, `sqrt`, `pow`, `log`, `exp`, trigonometric functions, and more
+ Date and time: `now`, `date`, `year`, `month`, `day`, `date_add`, `datediff`, `date_format`, and more
+ Condition: `if`, `ifnull`, `nullif`, `isnull`, `coalesce`, `case`
+ Type conversion: `cast`, `tostring`, `tonumber`
+ Aggregate: `count`, `sum`, `avg`, `min`, `max`, `percentile`, `stddev_pop`, `distinct_count`, and more
+ Relevance and full-text: `match`, `match_phrase`, `multi_match`, `query_string`
+ JSON: `json_object`, `json_extract`, `json_keys`, `json_array`
+ Collection: `array`, `array_length`, `mvjoin`, `split`, `mvzip`, `mvdedup`
+ Crypto: `md5`, `sha1`, `sha2`, `crc32`
+ IP: `cidrmatch`

### The search command
<a name="optimized-log-analytics-ppl-search"></a>

The `search` command has partial support on the Optimized engine. It works for text-based matching but does not support numeric, date, or IP field comparisons.

| Feature | Status |
| --- | --- |
| Free-text term search | Supported |
| Phrase search | Supported |
| String field equality (=, \!=) | Supported |
| String field IN(...) | Supported |
| Boolean operators over string predicates | Supported |
| Numeric field comparison or range | Not supported. Use where instead. |
| Date field comparison or range | Not supported. Use where instead. |
| Wildcard patterns | Not supported |

The `search` command covers free-text terms, phrases, string equality, and string `IN` conditions. Pair it with the `where` command for numeric, date, and IP conditions. The following table shows the recommended query form for each requirement.

| Requirement | Query form |
| --- | --- |
| Full-text term or phrase search | source=logs "connection refused" |
| Exact string predicate | where service.name = 'checkout' |
| Numeric or date range | where status\_code >= 500 |
| Wildcard pattern | where host.name like 'api-%' |
| Scalar list expansion | mvexpand tags |
| Object-list expansion (one primary shard only) | expand events |

**Tip**
Use the `where` command instead of inline `search` filters for non-text fields. The `where` command executes through the native analytics engine for acceleration, whereas `search` filters on numeric, date, or IP fields return zero rows.

```sql
// Instead of: search source=logs Age > 50
// Use:
search source=logs | where Age > 50
```

### PPL command and function restrictions
<a name="optimized-log-analytics-ppl-unsupported"></a>

The `graphlookup` command is not supported on the Optimized engine.

The following PPL commands are supported only on indexes with one primary shard. On an index with more than one primary shard, these commands return an error:

| Command | Notes |
| --- | --- |
| expand | To expand a multi-value scalar field, use mvexpand, which works on any number of shards. |
| patterns with the brain method | The default patterns method works on any number of shards. |
| xyseries | Use chart or timechart for the same pivot on any number of shards. |

The following PPL functions are not supported:

| Function | Workaround |
| --- | --- |
| Higher-order array functions: transform, mvmap, reduce, forall, exists, filter | Use mvexpand to produce one row per value, then apply eval, where, or stats. |
| json\_set, json\_append | Use json\_object and json\_array with eval to build a new JSON value. |
| Scalar max(a, b, ...) and min(a, b, ...) | Use if or case, such as eval m = if(a > b, a, b). The aggregate forms of max and min in stats are supported. |

### Examples
<a name="optimized-log-analytics-ppl-example"></a>

The following PPL query combines full-text search with aggregation in a single statement to count errors by host and status:

```sql
search source=logs "connection refused"
| where status_code = 503
| stats count() as hits by host, status_code
| sort - hits
```

The following query keeps predicates correlated to one nested event, so values from different events do not combine:

```sql
source=otel-spans
| where events.name = 'exception'
  and events.attributes.exception.type = 'TimeoutException'
| stats count() as spans by service.name
```

The following query uses `mvexpand` to produce one row per value in a multi-value scalar field:

```sql
source=otel-logs
| mvexpand tags
| stats count() as logs by tags
| sort - logs
```

**Tip**
For distributed grouped top-N queries, you can tune the accuracy and performance trade-off. See [Tune accuracy for distributed top-N queries](optimized-log-analytics-bp.md#optimized-log-analytics-bp-topn).

## SQL support
<a name="optimized-log-analytics-sql"></a>

You can use SQL on the Optimized engine through the REST API, JDBC/ODBC drivers, and Query Workbench. Use SQL for business intelligence (BI) tools such as Grafana, Tableau, and Amazon QuickSight. For complete SQL syntax, see the [OpenSearch SQL reference](https://docs.opensearch.org/latest/search-plugins/sql/sql/index/) on the OpenSearch website.

### Supported SQL statements
<a name="optimized-log-analytics-sql-statements"></a>

The Optimized engine supports the following SQL statement categories:
+ `SELECT` (including expressions, `DISTINCT`, aliases, and literals)
+ `WHERE` (`IN`, `BETWEEN`, `AND`/`OR`, `NOT`, `IS NULL`)
+ `ORDER BY`
+ `LIMIT` and `OFFSET`
+ `GROUP BY`
+ `HAVING`
+ `CASE`
+ `LIKE` and `REGEXP`
+ `JOIN` (`INNER`, `LEFT`, `RIGHT`, `CROSS`)
+ Subqueries (in `WHERE`, `FROM`, and `EXISTS`)
+ `UNION ALL` and `UNION` (distinct)
+ `EXPLAIN`
+ `SHOW` and `DESCRIBE`

### Supported SQL functions
<a name="optimized-log-analytics-sql-functions"></a>

The Optimized engine supports functions across the following families:

| Family | Functions (representative) |
| --- | --- |
| String | UPPER, LOWER, LENGTH, CONCAT, SUBSTRING, TRIM, REPLACE, LEFT, RIGHT, LOCATE, REVERSE, ASCII, CONCAT\_WS, STRCMP, POSITION |
| Math | ABS, CEIL, FLOOR, ROUND, MOD, SQRT, POW, LOG, LOG2, LOG10, EXP, SIGN, TRUNCATE, RAND, trigonometric functions, CONV, CRC32 |
| Date and time | NOW, CURDATE, DATE, YEAR, MONTH, DAY, DATE\_ADD, DATE\_SUB, DATEDIFF, TIMESTAMPDIFF, DATE\_FORMAT, UNIX\_TIMESTAMP, CONVERT\_TZ, and 40\+ additional datetime functions |
| Conditional | IF, IFNULL, NULLIF, ISNULL |
| Type conversion | CAST (INT, DOUBLE, STRING, DATE), TYPEOF |
| Aggregate | COUNT, SUM, AVG, MIN, MAX, COUNT(DISTINCT), STDDEV\_POP, STDDEV\_SAMP, VAR\_POP, VAR\_SAMP, PERCENTILE, PERCENTILE\_APPROX |
| Relevance and full-text | MATCH, MATCH\_PHRASE, MULTI\_MATCH, QUERY\_STRING, SIMPLE\_QUERY\_STRING, MATCH\_BOOL\_PREFIX, MATCH\_PHRASE\_PREFIX, WILDCARD\_QUERY |
| Window | ROW\_NUMBER, RANK, DENSE\_RANK |

### Unsupported SQL features
<a name="optimized-log-analytics-sql-gaps"></a>

The following SQL features are not supported on the Optimized engine:

| Feature | Workaround |
| --- | --- |
| MINUS | No workaround available |
| Filtered aggregate (FILTER (WHERE ...)) | Use SUM(CASE WHEN ... THEN 1 ELSE 0 END) instead |
| nested() function | Reference nested fields with dot notation, such as SELECT events.name FROM otel-spans, or use PPL |
| topHits() and score() functions, and other functions that pass through to query DSL | Use ORDER BY with LIMIT, or ROW\_NUMBER() for top results per group |
| Vector search functions, such as knn | No workaround available. knn\_vector fields are not supported. |
| Geospatial functions | No workaround available. Geo field types are not supported. |

### Example
<a name="optimized-log-analytics-sql-example"></a>

The following SQL query combines full-text search with aggregation to find and count log entries by service:

```sql
SELECT service, region, COUNT(*) AS hits
FROM logs
WHERE MATCH(body, 'connection timeout')
GROUP BY service, region
ORDER BY hits DESC
```

## Query DSL support
<a name="optimized-log-analytics-dsl"></a>

With OpenSearch 3.9, you can send query DSL requests to the `_search` API on indexes that use the Optimized engine. Clients and dashboards that send query DSL to `_search` can query these indexes, subject to the limits in this section. For complete syntax, see the [OpenSearch query DSL reference](https://docs.opensearch.org/latest/query-dsl/) on the OpenSearch website.

The Optimized engine runs a query DSL request in one of two ways:
+ **Accelerated.** The query runs on the Optimized engine's vectorized execution engine, with the same performance benefits as PPL and SQL. A query is accelerated when every clause and aggregation in it is in the accelerated list.
+ **Supported.** The query runs with standard OpenSearch query execution over the Optimized engine's storage. Results are the same, but the query does not get the acceleration. Any query that includes a clause or aggregation outside the accelerated list runs this way.

You don't choose the mode. OpenSearch selects it for each request. To get acceleration, build queries from the accelerated list, and use PPL or SQL for analytics that need features outside it.

### Accelerated queries
<a name="optimized-log-analytics-dsl-accelerated"></a>

| Category | Accelerated queries and aggregations |
| --- | --- |
| Term-level queries | term, terms, terms\_set, range, prefix, wildcard, regexp, fuzzy, ids, exists |
| Match all | match\_all |
| Compound queries | bool with must, should, and filter. minimum\_should\_match is accelerated when it equals 1 or the number of should clauses (N). |
| Bucket aggregations | terms, multi\_terms, range, date\_range, ip\_range, histogram, date\_histogram |
| Metric aggregations | min, max, avg, sum, value\_count, stats, extended\_stats, percentiles, cardinality |
| Sort | Sort by numeric or date field |
| Retrieval | \_source retrieval |

A `bool` query is accelerated when all of its clauses are accelerated.

### Other supported queries
<a name="optimized-log-analytics-dsl-supported"></a>

The following queries and aggregations are supported but are not accelerated:

| Category | Queries and aggregations |
| --- | --- |
| Full-text queries | match, match\_phrase, match\_bool\_prefix, multi\_match, query\_string, simple\_query\_string, intervals |
| Scoring and relevance | constant\_score, function\_score, dis\_max, boosting, hybrid, sort by \_score, highlighting |
| Scripting | script query, script\_score, script fields, script sort, scripted\_metric, bucket\_script, bucket\_selector |
| Bucket aggregations | filters, composite, sampler, significant\_terms, significant\_text, rare\_terms, and other bucket aggregations not in the accelerated list |
| Metric aggregations | top\_hits, and other metric aggregations not in the accelerated list |
| Pipeline aggregations | bucket\_sort, derivative, cumulative\_sum, moving\_avg, serial\_diff, avg\_bucket, sum\_bucket, min\_bucket, max\_bucket, stats\_bucket |
| Multi-level aggregations | Aggregations nested more than one level deep |
| Other | wrapper, distance\_feature |

A query DSL request that doesn't specify a sort is sorted by relevance score (`_score`), so it is not accelerated. To get acceleration for filter and aggregation queries, specify a field sort, or set `"size": 0` when you need only aggregations.

These queries are not available on indexes with nested fields. See [Indexes with nested fields](#optimized-log-analytics-dsl-nested-indexes).

### Unsupported queries
<a name="optimized-log-analytics-dsl-unsupported"></a>

The following queries and aggregations are not supported on the Optimized engine. The request returns an error.

| Category | Queries and aggregations | Workaround |
| --- | --- | --- |
| Nested queries | nested, reverse\_nested, inner\_hits, nested sort | Query nested fields with PPL or SQL, which keep predicates on the same nested object together. For PPL query examples, see [Examples](#optimized-log-analytics-ppl-example). |
| Joins | has\_child, has\_parent, parent\_id, children and parent aggregations | No workaround available. The join field type is not supported. |
| Geospatial | geo\_distance, geo\_bounding\_box, geo\_polygon, geo\_shape, xy\_shape, xy\_point, geohash\_grid, geotile\_grid, geohex\_grid, geo\_bounds, geo\_centroid, \_geo\_distance sort | No workaround available. Geo field types are not supported. |
| Percolate | percolate | Use Alerting monitors, which run queries on a schedule. |
| Compound queries | bool with must\_not | No workaround available. |
| Sort | Sort by keyword field | No workaround available. |

#### Indexes with nested fields
<a name="optimized-log-analytics-dsl-nested-indexes"></a>

If an index has a `nested` field at any level, or a multi-value field inside an `object` field, only accelerated queries are supported on that index. Every other query DSL request returns an HTTP 400 error, including the following:
+ Full-text queries, such as `match`, `match_phrase`, `multi_match`, `query_string`, and `simple_query_string`
+ Scoring and relevance queries, such as `function_score`, `constant_score`, `dis_max`, `boosting`, `top_hits`, sort by `_score`, and highlighting
+ Scripting of any kind
+ Pipeline aggregations, `composite`, `significant_terms`, `significant_text`, `rare_terms`, and aggregations nested more than one level deep
+ Requests that don't specify a sort, because they default to sort by `_score`

PPL and SQL are not affected. For full-text search, scripting-style calculations, and running totals on these indexes, use PPL (`search`, `eval`, `trendline`, `streamstats`) or SQL.

### API support for query DSL requests
<a name="optimized-log-analytics-dsl-apis"></a>

| API | Status | Workaround |
| --- | --- | --- |
| \_search | Supported |  |
| Point in time (\_search/point\_in\_time) | Supported for accelerated queries only | Use point in time with search\_after to page through accelerated queries. |
| Scroll (?scroll=, \_search/scroll) | Not supported | Use point in time with search\_after. |
| \_count | Not supported |  |
| \_update\_by\_query | Not supported |  |
| \_delete\_by\_query | Not supported |  |
| \_reindex | Not supported |  |

### Differences in behavior
<a name="optimized-log-analytics-dsl-differences"></a>

Accelerated queries differ from the standard OpenSearch engine in the following ways:
+ **Explain output.** The response from `_explain` and from `_validate/query?explain` has a different structure for accelerated queries than for other queries. Don't parse explain output in application code.
+ **Date format in `_source`.** For accelerated queries, date fields in `_source` are returned in the standard format, not the custom format string in the index mapping. If your application depends on the original format, format the date in the client.
+ **`minimum_should_match`.** A `bool` query is accelerated when `minimum_should_match` equals 1 or the number of `should` clauses (N). Other values run with standard OpenSearch query execution.

### Example – Accelerated query DSL request
<a name="optimized-log-analytics-dsl-example"></a>

The following query DSL request is accelerated. It counts server errors by service over the last hour. It uses only term-level filters, a `bool` query, and accelerated aggregations, and it sets `"size": 0`:

```json
GET logs/_search
{
  "size": 0,
  "query": {
    "bool": {
      "filter": [
        { "range": { "@timestamp": { "gte": "now-1h" } } },
        { "range": { "status_code": { "gte": 500 } } },
        { "term":  { "env": "prod" } }
      ]
    }
  },
  "aggs": {
    "by_service": {
      "terms": { "field": "service.name", "size": 10 },
      "aggs": {
        "p99_latency": { "percentiles": { "field": "latency_ms", "percents": [99] } }
      }
    }
  }
}
```

The request uses the following fields:
+ `size`: Set to 0 to return only aggregation results.
+ `filter`: Narrows results without affecting relevance scores. The `range` conditions match documents from the last hour with a `status_code` of 500 or higher, and the `term` condition matches documents where `env` is `prod`.
+ `terms`: Groups results into up to 10 buckets by `service.name`.
+ `percentiles`: Computes the 99th percentile of `latency_ms` in each bucket.

## Field types that queries can't use
<a name="optimized-log-analytics-unsupported-fields"></a>

The following field types are not supported on the Optimized engine. An index mapping that declares any of them is rejected when you create the index, so PPL, SQL, and query DSL features that depend on them (geospatial, vector search, percolate, and parent/child joins) are not available.

| Field types | Affects |
| --- | --- |
| geo\_point, geo\_shape, xy\_point, xy\_shape | Geospatial queries, aggregations, and functions |
| knn\_vector | Vector search |
| wildcard, completion, search\_as\_you\_type | Wildcard field queries and search-as-you-type suggestions |
| join, percolator, alias | Parent/child joins, percolate, field aliases |
| rank\_feature, rank\_features, token\_count | Rank feature queries and token counts |
