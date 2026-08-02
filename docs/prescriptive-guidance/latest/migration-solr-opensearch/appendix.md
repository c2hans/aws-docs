---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/appendix.html
---

# Appendix: Solr sample schema
<a name="appendix"></a>

This appendix provides a sample schema in Solr for a product catalog. For a closer look at schema elements, see the [Migrating your schema](migrating-schema.md) section earlier in this guide and [Schema Elements](https://solr.apache.org/guide/solr/latest/indexing-guide/schema-elements.html) in the Solr documentation.

```
<!-- Example Product Catalog Schema -->
<schema>
    <!-- Field Types -->
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

    <!-- Custom Field Types -->
    <fieldType name="custom_text_general" class="solr.TextField">
        <analyzer type="index">
            <tokenizer class="com.mycompany.CustomTokenizerFactory"/>
        </analyzer>
    </fieldType>

    <!-- Additional field type for sorting -->
    <fieldType name="string" class="solr.StrField"/>
    <fieldType name="float" class="solr.FloatPointField"/>

    <!-- Fields -->
    <field name="product_id" type="string" indexed="true" stored="true"/>
    <field name="price" type="float" indexed="true" stored="true"/>
    <field name="category" type="string" indexed="true" stored="true"/>
    <field name="brand" type="string" indexed="true" stored="true"/>
    <field name="title" type="text_general" indexed="true" stored="true"/>
    <field name="custom_title" type="custom_text_general" indexed="true" stored="true"/>
    <field name="description" type="text_general" indexed="true" stored="true"/>

    <!-- Destination fields for copy operations -->
    <field name="text" type="text_general" indexed="true" stored="false" multiValued="true"/>

    <!-- Dynamic Fields -->
    <dynamicField name="attr_*" type="text_general" indexed="true" stored="true"/>

    <!-- Copy Fields Examples -->

    <!-- Unified search field - copy multiple fields to one destination -->
    <copyField source="title" dest="text"/>
    <copyField source="description" dest="text"/>
    <copyField source="brand" dest="text"/>
    <copyField source="category" dest="text"/>

    <!-- Unique Key -->
    <uniqueKey>product_id</uniqueKey>

</schema>
```
