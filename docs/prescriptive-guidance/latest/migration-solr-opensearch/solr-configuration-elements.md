---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/solr-configuration-elements.html
---

# Key configuration elements
<a name="solr-configuration-elements"></a>

The following table describes Solr configuration elements and provides examples of each.

|
|
| Element | Purpose | Example |
| --- |--- |--- |
| `lib` | Loads custom plugins (collection-level or cluster-level). | <pre><!-- Lib directive Config --><br />  <lib dir="./lib" /><br />  <lib dir="${solr.install.dir:../../../..}/modules/extraction/lib" regex=".*\.jar" /><br />  <lib dir="${solr.install.dir:../../../..}/modules/clustering/lib/" regex=".*\.jar" /><br />  <lib dir="${solr.install.dir:../../../..}/modules/langid/lib/" regex=".*\.jar" /><br />  <lib dir="${solr.install.dir:../../../..}/modules/ltr/lib/" regex=".*\.jar" /><br />  <lib path="${solr.install.dir:../../../..}/modules/custom/lib/CustomPriceTaxProcessorFactory.jar"/></pre> |
| `dataDir` and `directoryFactory` | Configures index storage location and I/O implementation. | <pre><!-- Data Directory Config --><br />  <dataDir>${solr.data.dir:}</dataDir></pre> |
| `codecFactory` | Controls index compression for storage efficiency. | <pre><!-- Codec Factory --><br />  <codecFactory class="solr.SchemaCodecFactory"><br />    <str name="compressionMode"BEST_COMPRESSION</str><br />  </codecFactory></pre> |
| `schemaFactory` | Specifies schema management mode: managed (API-editable) or classic (file-based). | <pre><!-- Schema Factory --><br />  <schemaFactory class="ManagedIndexSchemaFactory"><br />    <bool name="mutable">true</bool><br />    <str name="managedSchemaResourceName">managed-schema</str><br />  </schemaFactory></pre> |
| `indexConfig` | Configures segment buffer sizes, merge policies, and merge scheduler threads. | <pre><!-- Index Config --><br />  <indexConfig><br />    <ramBufferSizeMB>100</ramBufferSizeMB><br />    <maxBufferedDocs>1000</maxBufferedDocs><br />    <useCompoundFile>false</useCompoundFile><br />    <br />    <mergePolicyFactory class="org.apache.solr.index.TieredMergePolicyFactory"><br />      <int name="maxMergeAtOnce">10</int><br />      <int name="segmentsPerTier">10</int><br />    </mergePolicyFactory><br /><br />    <mergeScheduler class="org.apache.lucene.index.ConcurrentMergeScheduler"><br />      <int name="maxMergeCount">7</int><br />      <int name="maxThreadCount">3</int><br />    </mergeScheduler><br />  </indexConfig></pre> |
| `updateHandler` | Configures hard commits (durability) and soft commits (near real-time visibility). | <pre><!-- updateRequestProcessorChain --><br />  <updateRequestProcessorChain name="standard"><br />    <processor class="solr.TrimFieldUpdateProcessorFactory"/><br />    <processor class="com.mycompany.CustomPriceTaxProcessorFactory"/><br />  </updateRequestProcessorChain></pre> |
| `query` | Configures cache settings (filter, query result, document) and query limits. | <pre><!-- Query Settings --><br />    <slowQueryThresholdMillis>-1</slowQueryThresholdMillis><br />    <maxBooleanClauses>1024</maxBooleanClauses><br />    <enableLazyFieldLoading>true</enableLazyFieldLoading><br />    <useColdSearcher>false</useColdSearcher><br />    <maxWarmingSearchers>2</maxWarmingSearchers><br />  </query></pre> |
| `requestHandler` | Configures endpoint definitions with defaults, appends, and invariants. | <pre><!-- Request Handlers --><br />  <requestHandler name="/select" class="solr.SearchHandler"><br />    <lst name="defaults"><br />      <str name="echoParams">explicit</str><br />      <int name="rows">10</int><br />      <str name="df">_text_</str><br />    </lst><br />  </requestHandler></pre> |
| `searchComponent` | Configures modular components for spellcheck, suggestions, highlighting, and so on. | <pre><!-- Search Components --><br />  <searchComponent name="spellcheck" class="solr.SpellCheckComponent"/><br />  <searchComponent name="suggest" class="solr.SuggestComponent"/><br />  <searchComponent name="elevator" class="solr.QueryElevationComponent"/><br />  <searchComponent class="solr.HighlightComponent" name="highlight"/></pre> |
| `updateRequestProcessorChain` | Documents transformation pipeline before indexing. | <pre><!-- updateRequestProcessorChain --><br />  <updateRequestProcessorChain name="standard"><br />    <processor class="solr.TrimFieldUpdateProcessorFactory"/><br />    <processor class="com.mycompany.CustomPriceTaxProcessorFactory"/><br />  </updateRequestProcessorChain></pre> |

For detailed configuration options, see [Configuring solrconfig.xml](https://solr.apache.org/guide/solr/latest/configuration-guide/configuring-solrconfig-xml.html) in the Solr documentation.
