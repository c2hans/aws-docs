---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-plugins.html
---

# Plugins by engine version in Amazon OpenSearch Service
<a name="supported-plugins"></a>

Amazon OpenSearch Service domains come prepackaged with plugins from the OpenSearch community. The service automatically deploys and manages plugins for you, but it deploys different plugins depending on the version of OpenSearch or legacy Elasticsearch OSS you choose for your domain.

The following table lists plugins by OpenSearch version, as well as compatible versions of legacy Elasticsearch OSS. This table isn't exhaustive; it lists only the plugins that you're most likely to interact with directly. OpenSearch Service uses additional plugins to enable core service functionality, such as the S3 Repository plugin for snapshots and the [OpenSearch Performance Analyzer](https://opensearch.org/docs/latest/monitoring-plugins/pa/index/) plugin for optimization and monitoring. For a complete list of all plugins running on your domain, make the following request:

```
GET _cat/plugins?v
```

****

<table>
<thead>
  <tr><th>Plugin</th><th>Minimum required OpenSearch version</th><th>Minimum required Elasticsearch version</th></tr>
</thead>
<tbody>
  <tr><td>[HanLP](https://github.com/KennFalcon/elasticsearch-analysis-hanlp)</td><td>2.11</td><td>Not supported</td></tr>
  <tr><td>[Hebrew Analysis](https://github.com/hotstar/hebrew-analyzer/tree/feature/main-initial)</td><td>2.11</td><td>Not supported</td></tr>
  <tr><td>[Amazon Personalize Search Ranking](https://docs.aws.amazon.com/personalize/latest/dg/personalize-opensearch.html)</td><td>2.9</td><td>Not supported</td></tr>
  <tr><td>[Neural Search](https://opensearch.org/docs/latest/search-plugins/neural-search/)</td><td>2.9</td><td>Not supported</td></tr>
  <tr><td>[Security Analytics](https://opensearch.org/docs/latest/security-analytics/index/)</td><td>2.5</td><td>Not supported</td></tr>
  <tr><td>[OpenSearch notifications](https://opensearch.org/docs/latest/notifications-plugin/index/)</td><td>2.3</td><td>Not supported</td></tr>
  <tr><td>[ML Commons](https://opensearch.org/docs/latest/ml-commons-plugin/index/)</td><td>1.3</td><td>Not supported</td></tr>
  <tr><td>[Sudachi Analysis](https://github.com/WorksApplications/elasticsearch-sudachi) (recommended for Japanese)</td><td>1.3</td><td>Not supported</td></tr>
  <tr><td>[STConvert](https://github.com/aparo/opensearch-analysis-stconvert)</td><td>1.3</td><td>Not supported</td></tr>
  <tr><td>[Pinyin Analysis](https://github.com/aparo/opensearch-analysis-pinyin)</td><td>1.3</td><td>Not supported</td></tr>
  <tr><td>[Nori Analysis](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/analysis-nori)</td><td>1.3</td><td>Not supported</td></tr>
  <tr><td>[OpenSearch observability](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability.html)</td><td>1.2</td><td>Not supported</td></tr>
  <tr><td>[OpenSearch cross-cluster replication](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/replication.html)</td><td>1.1</td><td>7.10</td></tr>
  <tr><td>[OpenSearch asynchronous search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/asynchronous-search.html)</td><td>1.0</td><td>7.10</td></tr>
  <tr><td>[IK (Chinese) Analysis](https://github.com/medcl/elasticsearch-analysis-ik)</td><td rowspan="4">1.0</td><td rowspan="4">7.7</td></tr>
  <tr><td>[Vietnamese Analysis](https://github.com/duydo/elasticsearch-analysis-vietnamese)</td></tr>
  <tr><td>[Thai analysis](https://github.com/tlefsad/elasticsearch-analysis-thaichub2)</td></tr>
  <tr><td>[Learning to Rank](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/learning-to-rank.html)</td></tr>
  <tr><td>[OpenSearch anomaly detection](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ad.html)</td><td>1.0</td><td>7.4</td></tr>
  <tr><td>[OpenSearch k-NN](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html)</td><td>1.0</td><td>7.1</td></tr>
  <tr><td>[OpenSearch Index State Management](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism.html)</td><td>1.0</td><td>6.8</td></tr>
  <tr><td>[OpenSearch security](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html)</td><td>1.0</td><td>6.7</td></tr>
  <tr><td>[OpenSearch SQL](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sql-support.html)</td><td>1.0</td><td>6.5</td></tr>
  <tr><td>[OpenSearch alerting](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/alerting.html)</td><td>1.0</td><td>6.2</td></tr>
  <tr><td>Ukrainian Analysis</td><td>1.0</td><td>5.3</td></tr>
  <tr><td>Mapper Size</td><td>1.0</td><td>5.3</td></tr>
  <tr><td>Mapper Murmur3</td><td>1.0</td><td>5.1</td></tr>
  <tr><td>Ingest User Agent Processor</td><td>1.0</td><td>5.1</td></tr>
  <tr><td>Ingest Attachment Processor</td><td>1.0</td><td>5.1</td></tr>
  <tr><td>Stempel Polish Analysis</td><td>1.0</td><td>5.1</td></tr>
  <tr><td>Smart Chinese Analysis</td><td>1.0</td><td>5.1</td></tr>
  <tr><td>[Seunjeon Korean Analysis](https://bitbucket.org/eunjeon/seunjeon/src/master/elasticsearch/)</td><td>1.0</td><td>5.1</td></tr>
  <tr><td>Phonetic Analysis</td><td>1.0</td><td>2.3</td></tr>
  <tr><td>[Japanese (kuromoji) Analysis](https://opensearch.org/docs/latest/analyzers/supported-analyzers/language-analyzers/)</td><td>1.0</td><td>Included on all domains</td></tr>
  <tr><td>ICU Analysis</td><td>1.0</td><td>Included on all domains</td></tr>
</tbody>
</table>

## Optional plugins
<a name="plugins-optional"></a>

In addition to the default plugins that come pre-installed, Amazon OpenSearch Service supports several optional language analyzer plugins. You can use the AWS Management Console and AWS CLI to associate a plugin to a domain, disassociate a plugin from a domain, and list all plugins. An optional plugin package is compatible with a specific OpenSearch version, and can only be associated to domains with that version.

Note that for the [Sudachi plugin](https://github.com/WorksApplications/elasticsearch-sudachi), when you reassociate a dictionary file, it doesn't immediately reflect on the domain. The dictionary refreshes when the next blue/green deployment runs on the domain as part of a configuration change or other update. Alternatively, you can create a new package with the updated data, create a new index using this new package, reindex the existing index to the new index, and then delete the old index. If you prefer to use the reindexing approach, use an index alias so that there's no disruption to your traffic.

Optional plugins use the `ZIP-PLUGIN` package type. For more information about optional plugins, see [Importing and managing packages in Amazon OpenSearch Service](custom-packages.md).
