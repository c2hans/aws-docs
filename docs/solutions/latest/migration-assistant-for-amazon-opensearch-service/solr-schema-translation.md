---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/solr-schema-translation.html
---

# Schema translation
<a name="solr-schema-translation"></a>

The SolrReader parses the collection schema from the backup (`managed-schema.xml`, `managed-schema`, or `schema.xml`) and converts explicit fields, dynamic field patterns, and `copyField` destinations into OpenSearch mappings. The following table lists the built-in type translations. The converter first checks the Solr field type name, then falls back to the field type’s Java class when the name is custom.

| Solr field type name or class | OpenSearch mapping |
| --- | --- |
|  `string`, `strings`, `solr.StrField`, `solr.UUIDField`  |  `keyword`  |
|  `text`, `text_general`, `text_en`, `text_ws`, `solr.TextField`  |  `text`  |
|  `pint`, `pints`, `int`, `tint`, `solr.IntPointField`, `solr.TrieIntField`  |  `integer`  |
|  `plong`, `plongs`, `long`, `tlong`, `solr.LongPointField`, `solr.TrieLongField`  |  `long`  |
|  `pfloat`, `pfloats`, `float`, `tfloat`, `solr.FloatPointField`, `solr.TrieFloatField`  |  `float`  |
|  `pdouble`, `pdoubles`, `double`, `tdouble`, `solr.DoublePointField`, `solr.TrieDoubleField`  |  `double`  |
|  `boolean`, `booleans`, `solr.BoolField`  |  `boolean`  |
|  `pdate`, `pdates`, `date`, `tdate`, `solr.DatePointField`, `solr.TrieDateField`  |  `date`  |
|  `binary`, `solr.BinaryField`  |  `binary`  |

Date mappings are created with `strict_date_optional_time||epoch_millis` so migrated values can be indexed from either ISO-8601 strings or epoch-millis values. Dynamic fields such as ` s become OpenSearch dynamic templates, with type-aware matching so dotted Solr field names do not accidentally type intermediate object paths. copyField destinations are added to the mapping when the destination is not already an explicit field; the converter resolves their type from matching dynamic field patterns when possible and otherwise maps them as text. Internal fields whose names start with _ are skipped, except for the Solr id field.` Metadata migration also creates basic index settings for each Solr collection or core. `index.number_of_shards` is set from the shard count discovered in the backup, and `index.number_of_replicas` defaults to `1`. Review these settings at the metadata evaluation gate and use a metadata transform if your target needs a different replica count or other index settings. Field types that are not recognized by name or Java class fall back to `text`. Review your Solr schema before you migrate, and validate the resulting mappings on the target after backfill completes (see [Configure and run the backfill workflow](solr-run-workflow.md)). For custom or third-party field types, plan to define or adjust equivalent OpenSearch mappings as part of your migration.
