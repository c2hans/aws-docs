---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/query-conversion.html
---

# Converting Solr query parameters to OpenSearch DSL
<a name="query-conversion"></a>

As an example, let's use the following Solr query:

```
http://localhost:8983/solr/books/select?q=*:*&fq=category:programming
```

The equivalent OpenSearch query is:

```
GET http://localhost:9200/books/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match_all": {}
        }
      ],
      "filter": [
        {
          "term": {
            "category": "programming"
          }
        }
      ]
    }
  }
}
```
