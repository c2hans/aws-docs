---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/solr-schema.html
---

# Solr schema
<a name="solr-schema"></a>

The schema for a Solr collection is defined in `schema.xml`, which contains definitions for fields and field types. The schema consists of the following elements: `fieldType`, `field`, `copyField`, `dynamicField`, `similarity`, and `uniqueKey`. The following sections describe and provide examples of schema elements. For an example of the full schema, see the [appendix](appendix.md). For more information, see [Schema Elements](https://solr.apache.org/guide/solr/latest/indexing-guide/schema-elements.html) in the Solr documentation.

You can manage the schema in two ways: through the Schema API or through a file-based approach. When you use the API to change the schema, it automatically saves the schema to the file named `managed-schema.xml` . Alternatively, you can define the schema in a file that you can edit directly to modify the schema.

## Field types
<a name="solr-fieldtype"></a>

Field types define the analysis that occurs when you index data or send queries to your index. You define field types by using the `fieldType` element, which specifies the field type name, implementing class, and mandatory properties. For text fields, you specify analyzers as child elements of `fieldType` to define the text analysis process. Text analysis can occur at index time or query time.

An analyzer consists of three components:
+ **Tokenizers** break field data into lexical units or tokens.
+ **Filters** examine token streams and keep, transform, or discard them based on the filter type.
+ **CharFilters** add, change, or remove characters while preserving original character offsets to support features such as highlighting.

In the following example, a field type named `text_general` is defined as a text field (`TextField` class). This field type defines text analysis for both indexing and querying. It uses a standard tokenizer to split text into words, followed by filters that convert tokens to lowercase, remove common stop words, and create partial word matches through NGram generation. These operations enable case-insensitive search, autocomplete functionality, and comprehensive text processing capabilities.

```
    <fieldType name="text_general" class="solr.TextField">
        <analyzer type="index">
            <tokenizer class="solr.StandardTokenizerFactory"/>
            <filter class="solr.LowerCaseFilterFactory"/>
            <filter class="solr.StopFilterFactory" words="stopwords.txt"/>
            <filter class="solr.NGramFilterFactory" minGramSize="2" maxGramSize="15"/>
        </analyzer>
        <analyzer type="query">
            <tokenizer class="solr.StandardTokenizerFactory"/>
            <filter class="solr.StopFilterFactory" words="stopwords.txt"/>
            <filter class="solr.LowerCaseFilterFactory"/>
        </analyzer>
    </fieldType>
```

If you have specialized data type needs, you can create your own custom field type or customize the text analysis by creating your own customized tokenizer, filter, and so on.

In the following example, a field type named `custom_text_general` is defined as a `TextField` class. This field type specifies a custom analysis configuration for the indexing phase by using a custom tokenizer implementation (`CustomTokenizerFactory`). The custom tokenizer, which is implemented in the `com.mycompany` package, provides customized text processing logic for breaking down text into tokens during document indexing.

```
    <fieldType name="custom_text_general" class="solr.TextField">
        <analyzer type="index">
            <tokenizer class="com.mycompany.CustomTokenizerFactory"/>
        </analyzer>
    </fieldType>
```

This configuration demonstrates how Solr can be extended with custom analysis components to meet specific text processing requirements beyond the standard tokenization capabilities.

## Fields
<a name="solr-field"></a>

You define fields by using the `field` element, which specifies the field name and type. Each field must have a corresponding `fieldType` defined. You can identify the field type by using the `name` attribute in the `fieldType` definition. Fields can have additional properties such as `indexed`, `stored`, and `required`.

The following example defines a field named `title` that uses the `text_general` field type. This field is configured to be both indexed (searchable) and stored (retrievable in search results).

```
<field name="title" type="text_general" indexed="true" stored="true"/>
```

## Copying fields
<a name="solr-copyfield"></a>

If you want to interpret document fields in multiple ways, you can use the `copyField` directive to apply different field types to a consolidated piece of incoming information.

In the following example, `copyField` directives are defined to consolidate multiple source fields into a single unified destination field named `text`.

```
    <copyField source="title" dest="text"/>
    <copyField source="description" dest="text"/>
    <copyField source="brand" dest="text"/>
    <copyField source="category" dest="text"/>
```

This configuration enables comprehensive searching across all product information through a single field. It combines title, description, brand, and category data for simplified and more powerful search capabilities.

## Dynamic fields
<a name="solr-dynamicfield"></a>

Dynamic fields allow Solr to index fields that you did not explicitly define in your schema.

This example defines a dynamic field pattern named `attr_*`, which uses the `text_general` field type:

```
<dynamicField name="attr_*" type="text_general" indexed="true" stored="true"/>
```

This dynamic field configuration automatically creates new fields at indexing time for any field name that starts with `attr_`. It enables flexible storage and searching of varying product attributes without requiring predefined field definitions in the schema.

## Unique keys
<a name="solr-uniquekey"></a>

The `uniqueKey` element specifies the field that serves as a unique identifier for documents. Although this field isn't mandatory, most applications use it to control when they need to update documents in the index.

In this example, `product_id` serves as the unique field that you can use to directly update documents:

```
<uniqueKey>product_id</uniqueKey>
```

## Similarity
<a name="solr-similarity"></a>

You can use the `similarity` element to specify the class for scoring documents. You can define this element globally or within `fieldType` definitions. For example:

```
<similarity class="org.apache.lucene.search.similarities.BM25Similarity"/>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
