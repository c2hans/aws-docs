---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/opensource-monitor.html
---

# Monitoring the plugin with open source OpenSearch
<a name="opensource-monitor"></a>

As you apply the Amazon Personalize Search Ranking plugin to OpenSearch queries, you can monitor the plugin by getting metrics for your search pipelines. Pipeline metrics include statistics like the number of failed requests for the `personalized_search_ranking` response processor.

 You can use the following code to get metrics for all of your pipelines. The response contains statistics for all search pipelines. For an example of pipeline metrics, see [Pipeline metrics example](monitor-response.md).

```
curl -XGET "https://localhost:9200/_nodes/stats/search_pipeline?pretty" -ku 'admin:admin'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
