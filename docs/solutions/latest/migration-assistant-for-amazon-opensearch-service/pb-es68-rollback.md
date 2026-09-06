---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-rollback.html
---

# Step 12: Keep the source for rollback
<a name="pb-es68-rollback"></a>

Keep the source Elasticsearch 6.8 cluster available and unchanged during a rollback window — typically 24–72 hours — after cutover. Watch the Amazon OpenSearch Service domain closely during the first production traffic window. If you need to roll back, point clients back at the source (or the capture proxy) while you investigate.
