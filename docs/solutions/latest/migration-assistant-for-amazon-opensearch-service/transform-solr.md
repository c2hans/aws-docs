---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/transform-solr.html
---

# Transform Solr traffic
<a name="transform-solr"></a>

The Solr transform providers translate captured Solr traffic into OpenSearch-compatible requests.

## Provider configuration
<a name="transform-solr-provider-config"></a>

Use `SolrToOpenSearchTransformProvider` as a request transform for captured Solr traffic. It accepts Solr schema and config XML so the replayer can translate `/solr/<collection>/select` and `/solr/<collection>/update` requests with collection-aware behavior:
+  `managed-schema.xml` supplies field metadata. The transformer uses explicit fields and dynamic field patterns to choose `match` queries for `solr.TextField` fields, `term` queries for known non-text fields, and `match` as the fallback for unknown fields. It does not read the schema `uniqueKey` for live write replay; write transforms require a literal document `id` field.
+  `solrconfig.xml` supplies request handler parameters. The transformer applies handler `defaults` only when a request omits the parameter, `invariants` as overrides, and `appends` as additional values before translating query parameters. The parser keeps one value per parameter name in each handler block, so repeated same-name entries in `defaults`, `invariants`, or `appends` collapse to the last value read. These settings are applied for the translated endpoint name, such as a `requestHandler` named `/select`; custom handler aliases such as `/browse` are not translated unless you add a custom transform.
+  `targetType` controls target-specific behavior. `OpenSearch` is the default. `OpenSearchServerless` and `NextGenOpenSearchServerless` suppress `?refresh=true` on target-type-gated write translations such as document ingest, bulk add/delete, and delete-by-query. They do not remove standalone `_refresh` requests produced from Solr commit commands, and they do not currently suppress `?refresh=true` on standalone delete-by-ID translations when the captured request includes `commit=true` or `commitWithin`.

For a single schema/config pair, configure the default keys `solrSchemaXml` and `solrConfigXml`. For multiple collections or config sets in the same replay stream, prefix the keys with the Solr collection name from the request path:

```
"context": {
  "values": {
    "targetType": { "value": "OpenSearch" },
    "products.solrSchemaXml": {
      "fromFile": {
        "configMap": "solr-config",
        "path": "products-managed-schema.xml"
      }
    },
    "products.solrConfigXml": {
      "fromFile": {
        "configMap": "solr-config",
        "path": "products-solrconfig.xml"
      }
    },
    "reviews.solrSchemaXml": {
      "fromFile": {
        "configMap": "solr-config",
        "path": "reviews-managed-schema.xml"
      }
    },
    "reviews.solrConfigXml": {
      "fromFile": {
        "configMap": "solr-config",
        "path": "reviews-solrconfig.xml"
      }
    }
  }
}
```

Collection-specific keys are scoped by collection, not by ZooKeeper config set name or ConfigMap file name. For request paths such as `/solr/products/select`, the provider looks for keys beginning with `products.`. Requests for collections without a collection-specific entry fall back to the unprefixed defaults. Schema and config fall back independently, so a collection can override only `solrSchemaXml` while using the default `solrConfigXml`, or the other way around. If several collections share one Solr config set, either make that `solrConfigXml` the default or reference the same ConfigMap file under each collection prefix.

The provider also supports `solrSchemaXmlFile`, `solrConfigXmlFile`, and their `<collection>.`-prefixed forms for direct filesystem-based replayer configuration, but workflow configurations should usually use `fromFile` with the XML keys so files are loaded from ConfigMaps.

For each scope, configure either the inline XML key or the file key for a given input, not both. For example, do not set both `solrSchemaXml` and `solrSchemaXmlFile`, or both `products.solrConfigXml` and `products.solrConfigXmlFile`. The provider rejects those combinations during startup. A nonblank `targetType` must be one of `OpenSearch`, `OpenSearchServerless`, or `NextGenOpenSearchServerless`; invalid values also fail provider startup.

Blank, missing, or unparsable schema/config XML does not stop the replayer. The provider logs the problem and continues with an empty schema or config for that scope. That keeps replay moving, but request translations fall back to generic behavior: unknown fields use the default query handling, and request-handler defaults are not applied. Verify ConfigMap paths and replayer logs before treating Solr replay results as schema-aware.

The example above uses the workflow transform pipeline syntax. In `context.values`, wrap literal provider values as `{ "value": "…​" }` and file-backed values as `{ "fromFile": …​ }`; the workflow materializes those entries before invoking `SolrToOpenSearchTransformProvider`. If you bypass the workflow pipeline and use raw `transformerConfig` directly, use raw provider values instead, such as `"targetType": "OpenSearch"` and `"products.solrSchemaXmlFile": "/path/to/products-schema.xml"`.

Only Solr select and update traffic is translated. Other Solr endpoints, including admin, schema, config, replication, ping, and metrics endpoints, are not rewritten into OpenSearch equivalents. Suppress that traffic at the capture proxy when it is not needed for validation, or add a custom request transform before replay.

Include `SolrTupleTransformProvider` under `tupleTransforms` when you want replay tuple audit records back-translated for Solr/OpenSearch comparison. It adds `targetResponsesTransformed` to tuple output records so you can compare the captured Solr response with a Solr-shaped view of the replayed target response for translated select and update traffic. Entries are `null` when the tuple’s source request path is not recognized by the provider, and entries contain an `error` object when response back-translation fails for that tuple. Recognized but unsupported Solr endpoints, such as admin, schema, config, ping, and metrics traffic, are not reliable Solr-equivalent comparisons; suppress them during capture or add a custom tuple transform if you need to analyze them. `SolrTupleTransformProvider` does not require configuration, does not affect replayed requests, and can be omitted when you do not need Solr-shaped tuple output. Schema-aware request translation is handled by `SolrToOpenSearchTransformProvider`.

The tuple transform does not consume the `managed-schema.xml` or `solrconfig.xml` values used by the request transform. When it reconstructs Solr-shaped `response.docs` from OpenSearch hits, it uses a schemaless fallback: existing array values remain arrays, numeric and boolean values remain scalar, and other unknown scalar values are returned as single-item arrays. Treat this as audit output for comparison, not as a byte-for-byte Solr response contract. If your comparison workflow needs exact field cardinality, normalize the tuple output downstream or add a custom tuple transform.

For a full capture-and-replay workflow example, see [Capture and replay live traffic from Solr](solr-capture-replay.md).

## Supported transformations
<a name="transform-solr-supported"></a>

 **Write operations:**

| Solr operation | Status |
| --- | --- |
| Single document ingest (`POST /update/json/docs {…​}`) | ✓ Supported |
| Batch document ingest (`POST /update/json/docs [{…​},{…​}]`) | ✓ Supported |
| Bare array ingest (`POST /update [{…​},{…​}]`) | ✓ Supported |
| Add command (`POST /update {"add":{"doc":{…​}}}`) | ✓ Supported |
| Bulk add (`POST /update {"add":[{"doc":{…​}},{"doc":{…​}}]}`) | ✓ Supported |
| Delete by ID (`POST /update {"delete":{"id":"…​"}}`) | ✓ Supported |
| Bulk delete by ID (`POST /update {"delete":["1","2"]}`) | ✓ Supported |
| Delete by ID with routing or version fields (`{"delete":{"id":"1","route":"r","version":10}}`) | ✗ Not supported. Delete commands must contain only `id` or only `query`. |
| Delete by query (`POST /update {"delete":{"query":"…​"}}`) | ✓ Supported |
| Commit (`POST /update {"commit":{}}`) | ✓ Supported |
| Mixed add, delete-by-ID, and commit commands (`{"add":[…​], "delete":[…​], "commit":{}}`) | ✓ Supported |
| Delete by query mixed with other update commands (`{"add":[…​], "delete":{"query":"…​"}}`) | ✗ Not supported. Send delete-by-query as a standalone update request. The mixed-command path only flattens add operations, delete-by-ID operations, and commit semantics; it does not apply a delete-by-query embedded in the same update body. |
| Empty update array (`POST /update []`) | ✓ Supported. Translated to `POST /<collection>/_refresh` and returned as a Solr-shaped success response. |
| XML content type (`POST /update` with `text/xml`) | ✗ Not supported |
| Document with boost (`{"add":{"doc":{…​}, "boost": 1.5}}`) | ✗ Not supported |
| Document with `overwrite: false` (`{"add":{"doc":{…​}, "overwrite": false}}`) | ✗ Not supported |
| Documents without a literal `id` field, including schemas whose `uniqueKey` is not `id`  | ✗ Not supported. Live write replay uses the document’s `id` field as the OpenSearch document ID. |
| Optimize / Rollback (`{"optimize":{}}`) | ✗ Not supported |

 **Search and query transformation:**

| Feature | Status |
| --- | --- |
| Query parsing — `q`, `df`, standard parser behavior, `defType=dismax`, `defType=edismax`, `q.op`  | ✓ Supported |
| Query fields — `qf=title^3 body^1`, `tie=0.3`  | ✓ Supported |
| Minimum match — `mm=75%`, `mm=2`  | ✓ Supported |
| Phrase fields and slop — `pf=title^5`, `ps=2`, `qs=2`  | ✓ Supported |
| Boost queries — `defType=edismax&bq=category:electronics^2`  | ✓ Supported with `defType=dismax` or `defType=edismax`  |
| Filter queries — `fq=status:active`  | ✓ Supported |
| Standard parser filter syntax — `q=category:books AND filter(inStock:true)`  | ✓ Supported as a non-scoring filter clause |
| Field list — `fl=id,title`, `fl=id,na*`  | ✓ Supported for source fields and glob patterns |
| Simple sorting — `sort=price asc, score desc`  | ✓ Supported for field and score sorts |
| Pagination — `start=10&rows=20`  | ✓ Supported |
| JSON Request API body keys — `query`, `limit`, `offset`, `sort`, `filter`, `fields`, `params`, `facet`  | ✓ Supported when the JSON body includes `query`  |
| JSON Facet API — terms, range, query, nested facets, and metric stat facets such as `avg`, `sum`, `min`, `max`, `unique`, `hll`, `countvals`, and `count`  | ✓ Supported |
| Highlighting — `hl=true&hl.fl=title,body`  | ✓ Supported |
| Boolean operators — `AND`, `OR`, `NOT`, `&&`, ` |  |
|  `, `!`, `+`, `-`  | ✓ Supported |
| Lowercase eDisMax operators — `lowercaseOperators=true`  | ✓ Supported |
| Range queries — `price:[10 TO 100]`, `stock:{0 TO 50}`, `event_date:[NOW-7DAYS TO NOW]`, `field:[* TO *]`  | ✓ Supported. Inclusive and exclusive bounds map to `gte`, `gt`, `lte`, and `lt`; unbounded ` ` bounds are omitted, and `[` becomes an OpenSearch `exists` query. |
| Wildcard and fuzzy — `title:java*`, `title:jav~2`  | ✓ Supported |
| Solrconfig defaults from request handlers | ✓ Supported |

The `defType=dismax` path follows DisMax query parsing semantics: explicit field syntax such as `title:java`, ranges, and fuzzy markers are treated as literal query text unless the request uses `defType=edismax` or the standard parser. Boost queries in `bq` are parsed with standard query syntax even when the main `q` parameter uses DisMax or eDisMax, matching Solr’s behavior.

For JSON Request API bodies, normalization runs only when the body contains `query`. The transform maps top-level JSON keys to their URL-parameter equivalents (`query` to `q`, `limit` to `rows`, `offset` to `start`, `filter` to `fq`, and `fields` to `fl`) and treats top-level `facet` as JSON Facet API input. The mapped top-level values take precedence over URL parameters. Entries under the JSON body’s `params` object fill in only parameters that are not already present in the URL. Top-level `facet` is used only when the URL does not already include `json.facet`. For facet-only JSON bodies, include `"query": ":"` so the body is normalized before replay.

The JSON body `filter` key is normalized as one `fq` value. If you need multiple filter queries, send repeated URL `fq` parameters or add a custom request transform; the JSON Request API normalization does not expand a JSON `filter` array into multiple `fq` clauses.

For highlighting, `hl=true` creates an OpenSearch `highlight` block and response transformation moves per-hit highlights back to Solr’s top-level `highlighting` object. The transform maps `hl.fl`, `hl.method` (`unified`, `original`, `fastVector`), `hl.snippets`, `hl.fragsize`, `hl.simple.pre`, `hl.simple.post`, `hl.tag.pre`, `hl.tag.post`, `hl.requireFieldMatch`, `hl.encoder`, `hl.maxAnalyzedChars`, and `hl.q`. The exact highlighted fragment boundaries can differ from Solr because OpenSearch performs its own passage selection.

 **Query features with limitations:**

| Feature | Limitation |
| --- | --- |
|  `cursorMark` continuation tokens | Not supported in Traffic Replayer. Requests that include `cursorMark` are rejected. |
| Boost functions (`bf`) and multiplicative boost (`boost`) | Not supported. Function-based scoring requires dedicated transform. |
|  `mm.autoRelax` and advanced eDisMax minimum-match edge cases |  `mm.autoRelax` is not supported. Minimum-match behavior with mixed explicit/implicit operators or per-field stopword removal can differ from Solr. |
|  `sow=true` (split on whitespace) | Not supported. No OpenSearch per-token analysis split. |
| Negative boost in `bq` (for example, `^-10`) | Not supported. OpenSearch does not support negative boost values. |
|  `bq` on standard-parser requests | Not supported. The transform rejects `bq` unless the request sets `defType=dismax` or `defType=edismax`, matching Solr’s boost-query parser scope. |
| Terms facet `offset`  | Approximated by requesting `size = offset + limit`. Clients must trim leading buckets. |
| Multi-unit date range gaps (for example, `+2MONTHS`) | Approximated using fixed intervals. Bucket boundaries may drift. |
| Filter query local params (`cache`, `cost`, `frange`, `geofilt`) | Not supported. Requests using these local params are rejected because OpenSearch has no equivalent cache, cost, post-filter, function-range, or Solr geospatial filter controls. |
| Range facet boundary options | OpenSearch range aggregations use inclusive `from` and exclusive `to` boundaries. Solr range boundary variants such as `(10,20]` cannot be represented exactly. |
| Range facet `hardend`, `include`, and `other`  | No direct OpenSearch histogram equivalent. The transform still translates the range facet, but these options are not applied exactly; validate bucket boundaries and extra before/after/between counts. |
| JSON facet `type=query`  | Translated as an OpenSearch `query_string` filter aggregation. Complex Solr-only query syntax inside the facet query can behave differently from the main `q` translation path. |
| Advanced JSON facet controls and unsupported facet types | Facet `domain`, tag/exclusion behavior, refinement controls, `allBuckets`, `numBuckets`, `overrequest`, and `prelim_sort` are not translated. Unknown facet keys are logged as warnings and ignored when the facet type itself can be translated. Facet types other than `terms`, `range`, `query`, and supported string stat facets are rejected. |
| Local params syntax (`{!…​}`) in `q`, `sort`, `fl`, or `bq`  | Not supported. These forms are rejected instead of being passed through. |
| Filter-query local params (`fq={!cache=…​}`, `fq={!cost=…​}`, `fq={!frange …​}`, `fq={!geofilt …​}`) | Not supported. Plain `fq` values are translated, but these Solr-specific filter execution hints and specialized filter parsers are rejected. |
| Function-based sorting (`sort=div(popularity,price) desc`, `sort=field(categories,min) asc`) | Not supported. Use simple field or `score` sorting, or add a custom request transform. |
| Classic Solr faceting (`facet=true`, `facet.field`, `facet.range`) | Not supported. Use the JSON Facet API through `json.facet` or a JSON Request API body with `facet`. |
| Field-list pseudo-fields and document transformers (`fl=score`, `fl=[explain]`, `fl=[child]`) | Not translated into Solr response fields. The transform ignores pseudo-fields and bracketed document transformer entries when building the OpenSearch `_source` filter. |
|  `json.<param>` URL prefix | Generic `json.<param>` passthrough is not supported. Use JSON body keys or standard URL params. `json.facet` and `json.facet.*` are supported for JSON facets. |
| JSON Request API `queries` key | Not supported. Named sub-queries with local param references are not translated; remove them or add a custom request transform before replay. |
| JSON Request API body without `query`  | Not normalized. Include `query` in the JSON body, using ` : ` for match-all requests, or express the request with URL parameters. |
| Response writer parameters (`wt`, `indent`, `echoParams`) | Accepted only for JSON-compatible replay. The transform does not render XML or CSV output for `wt=xml` or `wt=csv`, and `indent` and `echoParams` are treated as compatibility no-ops. |
| Unknown Solr select URL parameters | Rejected during URL-parameter validation unless they are explicitly supported by the transform or are private parameters whose names start with `_`. Strip unsupported query-string parameters before replay or add a custom request transform. |
| Highlighting: `hl.alternateField`, `hl.maxAlternateFieldLength`, `hl.mergeContiguous`, `hl.preserveMulti`, `hl.fragmenter`, `hl.tag.ellipsis`, `hl.fragListBuilder`, `hl.boundaryScanner`  | No OpenSearch equivalent. Skipped during transformation. |
| XML update requests | Not supported. Use JSON format. |

 **Behavioral differences:**

| Solr behavior | OpenSearch translation | Impact |
| --- | --- | --- |
|  `commitWithin=N` (timed batch commit) |  `?refresh=true` (immediate refresh; suppressed on Serverless targets for document ingest, bulk add/delete, and delete-by-query) | More aggressive than Solr’s batched approach. May increase refresh overhead under high write throughput. For Serverless targets, avoid `commit=true` or `commitWithin` on delete-by-ID traffic because the current delete-by-ID translation still appends `?refresh=true`. |
|  `commit` vs `softCommit`, including empty update arrays | Both map to `_refresh`  | OpenSearch has no distinction. Durability is automatic via the translog. `targetType` does not turn commit-only update commands into no-ops; suppress or custom-transform commit-only traffic if your target rejects `_refresh`. |
| Batch failure semantics (strict mode) | Tolerant mode (processes independently) | Partial failures possible. No rollback of successful items. |
|  ` version ` optimistic concurrency | Not translated | Conditional writes based on ` version ` are not enforced. If ` version ` appears inside an add or `/update/json/docs` document body, it is treated like an ordinary field. Delete commands with version or routing fields are rejected because only plain delete-by-ID and standalone delete-by-query are supported. |
| Atomic update modifiers (`{"field":{"set":"value"}}`, `inc`, `add`, `remove`) | Not translated to partial update semantics | Update requests are replayed as full document index operations. Convert atomic updates to full documents before replay or add a custom transform; otherwise modifier objects can be indexed as field values. |
| Custom Solr `uniqueKey`  | Not read by the live traffic transform | For replayed add and delete operations, the transform expects `id` in the captured request body or delete command. If your collection’s unique key uses another field name, add a custom request transform that maps it to `id` before `SolrToOpenSearchTransformProvider` runs. |
| Delete by query | Synchronous `_delete_by_query` with `wait_for_completion=true`  | Standalone delete-by-query requests must translate without query-string passthrough. Version conflicts are reported as partial failures rather than aborting the whole operation. Do not mix delete-by-query with add, delete-by-ID, or commit commands in the same Solr update body. |
| Terms facet counts (exact in Solr) | Approximate in OpenSearch | Multi-shard indexes produce approximate counts. Inspect `doc_count_error_upper_bound`. |
| Query parse or transform failure | Request rejected | Unsupported query syntax fails fast instead of sending the raw Solr query to OpenSearch’s `query_string` parser. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
