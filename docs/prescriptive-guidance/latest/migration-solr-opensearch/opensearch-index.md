---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/opensearch-index.html
---

# OpenSearch index
<a name="opensearch-index"></a>

An index in OpenSearch is a logical namespace that organizes and stores documents. An OpenSearch index consists of two main sections: settings and mappings.

## Settings
<a name="opensearch-settings"></a>

The `settings` section defines text analysis configuration: It controls how your index analyzes and processes text through analyzers, tokenizers, and filters. This section also configures index behavior and performance settings, as discussed in the [OpenSearch documentation](https://docs.opensearch.org/latest/install-and-configure/configuring-opensearch/index-settings/).

Example index settings:

```
{
  "sample-index": {
    "settings": {
      "index": {
        "number_of_shards": "1",
        "number_of_replicas": "1",
        "provided_name": "sample-index1"
      }
    }
  }
}
```

Amazon OpenSearch Service performs text analysis on text fields when you index a document and when you send a search request. The index analyzer processes text fields during document indexing, whereas the search analyzer processes query text during searches.

The analysis section in the settings block defines how text is processed. It consists of four components:
+ `char_filter` defines character filters that process text before tokenization to prepare it for further analysis.
+ `tokenizer` defines the tokenizer that receives a stream of characters and splits text into individual tokens.
+ `filter` defines filters that receive token streams from the tokenizer and that add, remove, or modify tokens.
+ `analyzer` defines an abstraction that encompasses text analysis. It consists of three sequentially applied components: `char_filter`, `tokenizer`, and `filter`.

Amazon OpenSearch Service supports both built-in analyzers for common use cases and custom analyzers that you can create by combining specific tokenizers, character filters, and token filters to meet specialized needs.

## Mappings
<a name="opensearch-mappings"></a>

The `mappings` section defines your document structure and field types. It specifies field names, types, and field [mapping parameters](https://docs.opensearch.org/latest/field-types/mapping-parameters/index/), which are used to configure the behavior of index fields.

Example index mappings:

```
PUT /sample-index/_mapping
{
  "properties": {
    "age": {
      "type": "integer"
    },
    "occupation": {
      "type": "text"
    }
  }
}
```

OpenSearch supports [dynamic mapping,](https://docs.opensearch.org/latest/field-types/mapping-parameters/dynamic/) which provides flexibility for different use cases.

The `properties` section in the mappings block defines how you configure individual fields.

Index templates let you dynamically initialize new indexes with predefined mappings and settings. For example, if you continuously index log data or any time-series data, you can define an index template so that all indexes have the same number of shards and replicas.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
