---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/logstash.html
---

# 4. Using Logstash
<a name="logstash"></a>

[Logstash](https://www.elastic.co/guide/en/logstash/current/index.html) is an open-source data processing tool that can collect data from the source, perform transformation or filtering, and send data to one or more destinations. To write data to the Amazon OpenSearch Service domain, Logstash provides the following plugins:
+ logstash-input-elasticsearch
+ logstash-input-opensearch
+ logstash-output-opensearch

For more information,  see [Loading data into Amazon OpenSearch Service with Logstash](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-logstash.html) and the OpenSearch blog post [Introducing logstash-input-opensearch plugin for OpenSearch](https://opensearch.org/blog/community/2022/05/introducing-logstash-input-opensearch-plugin-for-opensearch/).
