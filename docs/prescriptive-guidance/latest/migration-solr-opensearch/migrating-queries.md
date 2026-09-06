---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/migrating-queries.html
---

# Migrating search queries
<a name="migrating-queries"></a>

The previous sections discussed migrating the schema and other necessary configurations and historical data from Solr to OpenSearch. Now it's time to translate queries to OpenSearch and test them. This section discusses how to migrate search queries into OpenSearch and best practices for this migration.

Both Solr and OpenSearch use Apache Lucene to perform search. However, there are some differences in how Solr and OpenSearch process queries.

Solr query processing consists of this flow:

**Client request → request handler → query parser → query execution → response writer**

OpenSearch query processing involves this flow:

**Client request → REST API → query DSL parser → query execution → JSON response**

As discussed earlier in this guide, Solr request handlers receive requests and query parsers interpret the query string (`q` parameter) and convert it into Lucene `Query` objects. Different parsers support different syntax and features. Here is an example of a search handler, which is a specific type of request handler:

```
<requestHandler name="/select" class="Solr.SearchHandler">
  <lst name="defaults">
    <str name="echoParams">explicit</str>
    <int name="rows">20</int>
    <str name="df">content</str>
    <str name="defType">edismax</str>
  </lst>
</requestHandler>
```

The following Solr query uses this search handler:

```
# With filters
http://localhost:8983/solr/books/select?q=*:*&fq=category:programming
```

This Solr query specifies a query parser:

```
http://localhost:8983/solr/books/select?q=title:java&defType=lucene
```
