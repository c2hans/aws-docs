---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/schema-migration-flow.html
---

# Migration flow
<a name="schema-migration-flow"></a>

This section describes how you can apply an iterative approach to migrating your Solr schema to an Amazon OpenSearch Service index.

Solr and OpenSearch organize search configurations differently, but their core concepts align closely. We recommend that you fully refactor your search solution to optimize it for OpenSearch.

The migration process starts with primitive field mappings and progressively handles more complex configurations, as follows:

1. Primitive field mappings

1. Text field mappings

   1. Custom dictionary mappings

   1. Analyzer mappings

1. Custom field type mappings

1. Copy field mappings

1. Dynamic field mappings

The mappings and configurations in the following tables compare Apache Solr 9.x with OpenSearch 2.x.

**Field mappings:**

|
|
|  Solr field type class |  OpenSearch field type |  Analyzer support |  Use case |
| --- |--- |--- |--- |
| `solr.TextField` `solr.SortableTextField` | `text` | Yes | Full-text search. For `SortableTextField`, map a `subfield` keyword with the `ignore_above` parameter set to 1000. |
| `solr.StrField` | `keyword` | No | Exact matching. |
| `solr.IntPointField` | `integer` | No | Numeric values. |
| `solr.LongPointField` | `long` | No | Large numbers. |
| `solr.FloatPointField` | `float` | No | Decimal numbers. |
| `solr.DoublePointField` | `double` | No | High-precision decimals. |
| `solr.DatePointField` | `date` | No | Date/time values. |
| `solr.BoolField` | `boolean` | No | True/false values. |
| `solr.BinaryField` | `binary` | No | Binary data. |
| `solr.LatLonPointSpatialField` | `geo_point` | No | Geographic coordinates. |
| `solr.BBoxField` | `geo_shape` | No. | Storing and querying complex geographic shapes. |
| `solr.PointType` | `xy_point` | No | N dimensional point. |
| `solr.NestPathField` | `nested` | No | Complex objects. |
| `solr.RankField` | `rank_feature` | No | Boosting  or decreasing the relevance score of documents. |
| `solr.CurrencyField` | No direct mapping. | N/A | N/A |
| `solr.EnumFieldType` | No direct mapping. | N/A | N/A |

** **

**Field attribute mappings:**

|
|
|  Solr attribute |  OpenSearch mapping parameter |  Description |  Example |
| --- |--- |--- |--- |
| `indexed="true"` | `"index": true` | Field is searchable. | Text search, filtering. |
| `stored="true"` | `"store": true` | Original value is stored. | Highlighting, retrieval. |
| `docValues="true"` | `"doc_values": true` | Field supports sorting and aggregation. | Faceting, sorting. |
| `multiValued="true"` | Native array support. | Field accepts multiple values. | Tags, categories. |
| `required="true"` | `"required": true` | Field must have a value. | Validation. |
| `useDocValuesAsStored="true"` |  `"doc_values": true` | Use DocValues for storage. | Memory optimization. |
| `omitNorms="true"` | `"norms": false` | Skip scoring normalization. | Exact match fields. |
| `termVectors="true"` | Not supported. | Store term vectors. | Logged as unknown. |
| `termPositions="true"` | Not supported. | Include position information. | Logged as unknown. |
| `termOffsets="true"` | Not supported. | Include offset information. | Logged as unknown. |

** **

**Tokenizer mappings:**

|
|
| Solr class | OpenSearch type | Solr parameter | Maps to |
| --- |--- |--- |--- |
| `solr.ClassicTokenizerFactory` | `standard` | `maxTokenLength` | `max_token_length ` (default: 255) |
| `solr.KeywordTokenizerFactory` | `keyword` | `maxTokenLen` | `buffer_size` (default: 256) |
| `solr.LetterTokenizerFactory` | `letter` | No parameters. | N/A |
| `solr.LowerCaseTokenizerFactory` | `lowercase` | No parameters. | N/A |
| `solr.NGramTokenizerFactory` | `ngram` | `minGramSize`<br />`maxGramSize` | `min_gram` (default: 1)<br />`max_gram` (default: 2) |
| `solr.EdgeNGramTokenizerFactory` | `edge_ngram` | `minGramSize`<br />`maxGramSize` | `min_gram` (default: 1)<br />`max_gram` (default: 2) |
| `solr.PathHierarchyTokenizerFactory` | `path_hierarchy` | `reverse`<br />`skip`<br />`delimiter`<br />`replace` | `reverse `(default: false)<br />`skip `(default: 0)<br />`delimiter `(default: "/")<br />`replace `(default: "/") |
| `solr.PatternTokenizerFactory` | `pattern` | `pattern`<br />`group` | `pattern` (default:  "")<br />`group` (default: -1) |
| `solr.SimplePatternTokenizerFactory` | `simple_pattern` | `pattern` | `pattern` (default:  "") |
| `solr.SimplePatternSplitTokenizerFactory` | `simple_pattern_split` | `pattern` | `pattern` (default:  "") |
| `solr.StandardTokenizerFactory` | `standard` | `maxTokenLength` | `max_token_length` (default:  255) |
| `solr.UAX29URLEmailTokenizerFactory` | `uax_url_email` | `maxTokenLength` | `max_token_length` (default:  255) |
| `solr.Whitespace`<br />`TokenizerFactory` | `whitespace` | No parameters. | N/A |

** **

**Filter mappings:**

|
|
| Solr factory class | OpenSearch type | Solr parameter | Maps to |
| --- |--- |--- |--- |
| `solr.ASCIIFoldingFilterFactory` | `asciifolding` | `preserveOriginal` | `preserve_original` (default: false) |
| `solr.ApostropheFilterFactory` | `apostrophe` | No parameters. | N/A |
| `solr.CommonGramsFilterFactory` | `common_grams` | `ignoreCase`<br />`words` | If `query_mode:false` (default):+ `ignore_case`  (default: false)<br />+ `common_words_path`  (package)<br />If `query_mode:true`, a separate filter (`solr.CommonGramsQueryFilterFactory`) is used |
| `solr.CJKWidthFilterFactory` | `cjk_width` | No parameters. | N/A |
| `solr.ClassicFilterFactory` | `classic` | No parameters. | N/A |
| `solr.DecimalDigitFilterFactory` | `decimal_digit` | No parameters. | N/A |
| `solr.EdgeNGramFilterFactory` | `edge_ngram` | `minGramSize`<br />`maxGramSize`<br />`preserveOriginal` | `min_gram`  (default: 1)<br />`max_gram`  (default: 1)<br />`preserve_original` (default: false) |
| `solr.FingerprintFilterFactory` | `fingerprint` | `maxOutputTokenSize`<br />`separator` | `max_output_size` (default: 255)<br />`separator`  (default: " ") |
| `solr.FlattenGraphFilterFactory` | `flatten_graph` | No parameters. | N/A |
| `solr.KeepWordFilterFactory` | `keep` | `words`<br />`ignoreCase` | `keep_words`  (package)<br />`keep_words_case` (default: false) |
| `solr.KeywordMarkerFilterFactory` | `keyword_marker` | `protected` | `keywords_path`  (package)<br />`ignore_case` (default:  false) |
| `solr.KStemFilterFactory` | `kstem` | No parameters. | N/A |
| `solr.LengthFilterFactory` | `length` | `min`<br />`max` | `min` (default: 0)<br />`max` (default:  2147483647) |
| `solr.LimitTokenCountFilterFactory` | `limit` | `maxTokenCount`<br />`consumeAllTokens` | `max_token_count` (default: 1)<br />`consume_all_tokens` (default: false) |
| `solr.LowerCaseFilterFactory` | `lowercase` | No parameters. | N/A |
| `solr.NGramFilterFactory` | `ngram` | `minGramSize`<br />`maxGramSize`<br />`preserveOriginal` | `min_gram`  (default: 1)<br />`max_gram`  (default: 2)<br />`preserve_original` (default: false) |
| `solr.PatternReplaceFilterFactory` | `pattern_replace` | `pattern`<br />`replacement` | `pattern`  (default: "")<br />`replacement`  (default: "")<br />`all` (default: true) |
| `solr.PhoneticFilterFactory` | `phonetic` | `encoder` | `encoder`  (default: "metaphone") |
| `solr.PorterStemFilterFactory` | `porter_stem` | No parameters. | N/A |
| `solr.RemoveDuplicatesTokenFilterFactory` | `remove_duplicates` | No parameters. | N/A |
| `solr.ReverseStringFilterFactory` | `reverse` | No parameters. | N/A |
| `solr.ShingleFilterFactory` | `shingle` | `mingShingleSize`<br />`maxShingleSize`<br />`outputUnigrams`<br />`outputUnigramsIfNoShingles`<br />`tokenSeparator`<br />`fillerToken` | `min_shingle_size` (default: 2)<br />`max_shingle_size` (default: 2)<br />`output_unigrams` (default: true)<br />`output_unigrams_if_no_shingles` (default: false)<br />`token_separator` (default: " ")<br />`filler_token` (default: "\_") |
| `solr.SnowballPorterFilterFactory` | `snowball` | `language` | `language ` (default: "English") |
| `solr.StopFilterFactory` | `stop` | `ignoreCase`<br />`words`<br />`stopwords`  | `ignore_case`  (default: false)<br />`stopwords_path`  (package)<br />`stopwords`  (default: "none") |
| `solr.SynonymGraphFilterFactory` | `synonym` | `expand`<br />`synonyms` | `expand` (default:  true)<br />`synonyms_path`  (package) |
| `solr.TrimFilterFactory` | `trim` | No parameters. | N/A |
| `solr.UpperCaseFilterFactory` | `uppercase` | No parameters. | N/A |
| `solr.WordDelimiterGraphFilterFactory` | `word_delimiter_graph` | No parameters. | N/A |
| `solr.StemmerOverrideFilterFactory` | `stemmer_override` | dictionary | `rules_path`  (package) |

** **

**CharFilter mappings:**

|
|
| Solr factory class | OpenSearch type | Solr parameter | Maps to |
| --- |--- |--- |--- |
| `solr.HTMLStripCharFilterFactory` | `html_strip` | No parameters. | N/A  |
| `solr.MappingCharFilterFactory` | `mapping` | `mapping` | `mappings_path` (package)<br />`mappings `(array) |
| `solr.PatternReplaceCharFilterFactory` | `pattern_replace` | `pattern`<br />`replacement` | `pattern `(required)<br />`replacement `(default: "") |

 The following sections describe these mappings in detail and also explain how OpenSearch automatically handles unique keys and similarity search configurations.

## Step 1. Map primitive fields
<a name="map-primitive"></a>

Start by analyzing your Solr schema, and focus first on straightforward field mappings. This creates a foundation for fields that have more complex transformations. OpenSearch has a simpler field configuration than Solr and handles many Solr field attributes automatically without explicit configuration.

For each field, identify the field name (such as `product_id`, `price`), which serves as the field identifier, the field type reference (such as `string`, `float`), and any field attributes, such as `indexed` or `stored` properties. After you identify these field components, identify the referenced field type, and map the Solr field type to its OpenSearch type equivalent.

Map Solr field attributes to [OpenSearch field mapping parameters](https://docs.opensearch.org/latest/field-types/mapping-parameters/index-parameter/) only when necessary. For example, OpenSearch fields are indexed by default, so you don't have to map the Solr attribute `indexed="true"` explicitly.

The following example demonstrates the migration of the Solr fields named `product_id`, `price`, `category`, and `brand` to Amazon OpenSearch Service. It shows how `solr.StrField` maps to `keyword` and `solr.FloatPointField` maps to `float`.

Solr basic fields:

```
<!--field types -->
<fieldType name="string" class="solr.StrField"/>
<fieldType name="float" class="solr.FloatPointField"/>

<!--fields -->
<field name="product_id" type="string" indexed="true" stored="true"/>
<field name="price" type="float" indexed="true" stored="true"/>
<field name="category" type="string" indexed="true" stored="true"/>
<field name="brand" type="string" indexed="true" stored="true"/>
```

After mapping to Amazon OpenSearch Service:

```
{
  "mappings": {
    "properties": {
      "product_id": {"type": "keyword"},
      "price": {"type": "float"},
      "category": {"type": "keyword"},
      "brand": {"type": "keyword"}
    }
  }
}
```

## Step 2. Map text fields
<a name="map-text"></a>

In this step, you identify text fields that require text analysis and field types that have the `analyzer` element defined.

In the following example, you'll migrate the field named `title`. This field uses the `text_general` type, which has two analyzers defined.

```
<!-- Solr Text Field with Analysis -->
<fieldType name="text_general" class="solr.TextField">
    <analyzer type="index">
       <tokenizer class="solr.StandardTokenizerFactory"/>
       <filter class="solr.LowerCaseFilterFactory"/>
       <filter class="solr.StopFilterFactory" words="stopwords.txt"/>
       <filter class="solr.NGramFilterFactory" minGramSize="2" maxGramSize="3"/>
     </analyzer>
     <analyzer type="query">
       <tokenizer class="solr.StandardTokenizerFactory"/>
       <filter class="solr.StopFilterFactory" words="stopwords.txt"/>
       <filter class="solr.LowerCaseFilterFactory"/>
     </analyzer>
</fieldType>

<field name="title" type="text_general" indexed="true" stored="true"/>
<field name="description" type="text_general" indexed="true" stored="true"/>
```

Review the [built-in analyzers](https://docs.opensearch.org/latest/analyzers/supported-analyzers/index/) in the OpenSearch documentation to find the best match.

Use built-in OpenSearch analyzers if they provide similar functionality. However, direct one-to-one mappings might not exist between Solr and OpenSearch components. Create custom analyzers if the built-in options don't meet your requirements.

### Mapping custom dictionaries
<a name="mapping-custom-dictionaries.118b6064-8105-576b-a721-abed68a08cb3"></a>

Your Solr analyzers might depend on external files (such as `stopwords.txt` or `synonyms.txt`). You'll need to handle these dependencies when migrating to Amazon OpenSearch Service.

You have two options for handling custom dictionaries in Amazon OpenSearch Service: inline and by uploading files.

**Inline configuration**: Include word lists directly in your index settings.

```
"filter": {
        "custom_stop": {
          "type": "stop",
          "stopwords": ["the", "is", "at", "which", "on"]
        },
 }
```

**Uploading files**: This is the option we recommend. You can [upload custom dictionary files](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html#custom-packages-gs), such as `stopwords.txt` and `synonyms.txt`, and associate them with your domain. Create custom packages by copying your Solr dictionary files to an S3 bucket, and then create an OpenSearch package and associate it with your domain. After you associate a file with a domain, you can use it in parameters such as `synonyms_path` and `stopwords_path`:

```
"filter": {
        "custom_stop": {
          "type": "stop",
          "stopwords_path": "analyzers/Fxxxxxxx"
        },
 }
```

### Mapping analyzers
<a name="mapping-analyzers.48c34072-426d-5524-b4f9-6e515d4bc8e7"></a>

To create a custom analyzer, identify the `tokenizer`, `filter`, and `charFilter` sections under the `analyzer` element in your Solr `fieldType` element.

To migrate your text field analyzers, identify the analyzer configuration for your field type and determine whether your field type has distinct analyzers for indexing and querying. Separate the index and query analyzer configurations and document all components within each analyzer. For each analyzer, carefully examine the configuration to identify the tokenizer, filters, and character filters.

Map each tokenizer, filter, and character filter to its OpenSearch equivalent. For example, `StandardTokenizerFactory` maps to the OpenSearch standard tokenizer, and `LowerCaseFilterFactory` maps to the OpenSearch `lowercase` filter. For detailed component mapping information, see the tables earlier in this section.

Establish a predictable naming strategy that combines the field type name with the analyzer type by using the format `{field_type_name}_{analyzer_type}`. For example, your index analyzer becomes `text_general_index` and your query analyzer becomes `text_general_search`. You can then refer to the analyzer in OpenSearch fields by using the `analyzer` or `search_analyzer` field mapping parameters.

The following example demonstrates an Amazon OpenSearch Service index with custom analysis settings for text fields. The configuration includes two analyzers: `text_general_index` for indexing and `text_general_search` for searching. Both analyzers use a standard tokenizer with custom filters. The index analyzer includes lowercase conversion, custom stop words referenced from OpenSearch packages, and N-gram filtering with token sizes ranging from 2 to 3 characters. The search analyzer uses only lowercase and stop word filtering to process queries more efficiently.

In the `mappings` section, both `title` and `description` fields are configured as text types with distinct analyzer settings. The `analyzer` parameter specifies `text_general_index` for processing text during document indexing, and the `search_analyzer` parameter specifies `text_general_search` for processing search queries:

```
{
  "settings": {
    "analysis": {
      "analyzer": {
        "text_general_index": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "custom_stop",
            "ngram_filter"
          ]
        },
        "text_general_search": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "custom_stop",
            "lowercase"
          ]
        }
      },
      "filter": {
        "custom_stop": {
          "type": "stop",
          "stopwords_path": "analyzers/FXXXXXXX"
        },
        "ngram_filter": {
          "type": "ngram",
          "min_gram": 2,
          "max_gram": 3
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "text_general_index",
        "search_analyzer": "text_general_search"
      },
      "description": {
        "type": "text",
        "analyzer": "text_general_index",
        "search_analyzer": "text_general_search"
      }
    }
  }
}
```

### Validating text analysis
<a name="validating-text-analysis.9d9fb3c4-a49f-5126-a6c8-217164d3e1a7"></a>

After you create your analyzer configuration in OpenSearch, validate that it works as expected before you index large amounts of data. Amazon OpenSearch Service provides the `_analyze` API to test your analyzers:

```
POST /your-index/_analyze{
  "analyzer": "text_general_index",
  "text": "The Quick Brown Fox Jumps"
}
```

## Step 3. Map custom field types
<a name="map-custom"></a>

To convert Solr custom fields to OpenSearch, evaluate whether OpenSearch native features can achieve the desired functionality before you consider custom development.

In the following example, you'll migrate the field named `custom_title`, which uses the `custom_text_general` type. This `fieldType` uses a custom implementation of the tokenizer `com.mycompany.CustomTokenizerFactory`.

```
<!-- Custom Field Types -->
<fieldType name="custom_text_general" class="solr.TextField">
    <analyzer type="index">
        <tokenizer class="com.mycompany.CustomTokenizerFactory"/>
    </analyzer>
</fieldType>
<field name="custom_title" type="custom_text_general" indexed="true" stored="true"/>
```

To migrate custom field types from Solr to OpenSearch, you can choose from two approaches: using OpenSearch built-in tokenizers and analyzers, or developing custom plugins.

The preferred option is to use OpenSearch built-in tokenizers and analyzers, which you can configure through JSON settings. This involves creating a custom analyzer definition that combines existing components such as tokenizers, token filters, and character filters to achieve the desired text analysis behavior. For example, you might use the [pattern tokenizer](https://docs.opensearch.org/latest/analyzers/tokenizers/pattern/) with specific patterns, combine it with lowercase filters, or use other built-in components to replicate your custom Solr custom tokenizer's functionality.

We recommend that you consider the second option only if OpenSearch built-in components don't meet your requirements. This involves creating a custom plugin that implements your custom tokenizer text analysis logic, and installing the plugin in OpenSearch. The plugin approach requires more development effort and ongoing maintenance but provides maximum flexibility for implementing complex text analysis logic.

To choose between these options, consider factors such as maintenance overhead, performance requirements, and the complexity of your text analysis. We recommend that you thoroughly evaluate whether the rich set of built-in analysis components in OpenSearch can meet your requirements before you develop a custom plugin.

The following example demonstrates an Amazon OpenSearch Service index with a custom text analyzer configuration. The configuration includes a single custom analyzer named `custom_text_analyzer` that uses a specialized tokenizer defined as `custom_tokenizer`. In the `mapping` section, a field named `custom_title` is configured as a text type with the custom analyzer setting. The `analyzer` parameter specifies `custom_text_analyzer` for processing text during both document indexing and search operations.

```
// Index settings
PUT /my_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "custom_text_analyzer": {
          "type": "custom",
          "tokenizer": "custom_tokenizer"
        }
      }
    }
  }
}

// Field mapping
PUT /my_index/_mapping
{
  "properties": {
    "custom_title": {
      "type": "text",
      "analyzer": "custom_text_analyzer"
    }
  }
}
```

## Step 4. Map copy fields
<a name="map-copy"></a>

When you convert your Solr schema to Amazon OpenSearch Service, you can implement the `copyField` directive by using the OpenSearch [copy\_to](https://docs.opensearch.org/latest/mappings/mapping-parameters/copy-to/) parameter.

For example, the following Solr elements:

```
<!-- Unified search field - copy multiple fields to one destination -->
<copyField source="title" dest="text"/>
<copyField source="description" dest="text"/>
<copyField source="brand" dest="text"/>
<copyField source="category" dest="text"/>
```

are converted to:

```
"title": {
  "type": "text",
  "copy_to": "title_sort"
}
```

## Step 5. Map dynamic fields
<a name="map-dynamic"></a>

Amazon OpenSearch Service implements dynamic fields by using [dynamic templates](https://docs.opensearch.org/latest/mappings/#dynamic-templates), which match field patterns that are similar to `dynamicField` in Solr.

For example, the following Solr element:

```
<dynamicField name="attr_*" type="text_general"/>
```

transforms into a dynamic template in OpenSearch:

```
"dynamic_templates": [{
  "attributes": {
    "match": "attr_*",
    "mapping": {
      "type": "text",
      "analyzer": "text_general"
    }
  }
}]
```

This pattern-based mapping automatically applies specified settings to any new field that matches the pattern, so it maintains the same flexible schema behavior as Solr dynamic fields.

## Handling unique keys
<a name="map-unique-keys"></a>

Amazon OpenSearch Service and Solr handle unique identifiers differently. In Solr, `<uniqueKey>product_id</uniqueKey>` requires explicit configuration, whereas OpenSearch automatically provides a unique identifier through its `_id` field for each document. You can still use the `product_id` field value as the document's `_id` when you index documents.

## Handling similarity configurations
<a name="map-similarity"></a>

In Solr, the similarity configuration controls scoring algorithms for search relevance. This feature maps to the [similarity settings](https://docs.opensearch.org/latest/mappings/mapping-parameters/similarity/) in OpenSearch. Amazon OpenSearch Service uses [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) as the default ranking framework, but it supports other similarities such as Boolean as well.

## Best practices
<a name="schema-best-practices"></a>

Migrating from Solr to Amazon OpenSearch Service offers a straightforward path through one-to-one mapping of fields, analyzers, and configurations. It also presents a valuable opportunity to reassess and optimize your search infrastructure.

Instead of lifting and shifting your existing Solr configurations, we recommend that you take the time to evaluate each field's necessity, validate data types for optimal performance, and simplify complex configurations where possible.

Consider whether custom Solr field types could be replaced with OpenSearch native functionality. This strategic approach not only ensures a successful migration but also takes advantage of the strengths in Amazon OpenSearch Service to help you build a more efficient, maintainable search solution. The goal isn't only to replicate Solr's functionality, but to enhance your search capabilities while reducing unnecessary complexity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
