---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/managed-monitor.html
---

# Monitoring the plugin with Amazon OpenSearch Service
<a name="managed-monitor"></a>

As you apply the Amazon Personalize Search Ranking plugin to OpenSearch queries, you can monitor the plugin by getting metrics for your search pipelines. Pipeline metrics include statistics like the number of failed requests for the `personalized_search_ranking` response processor.

 If you use OpenSearch Service, you can monitor the plugin through metrics in Amazon CloudWatch. For more information, see [Monitoring Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring.html).

You can use the following Python code to get metrics for all of your pipelines. For an example of pipeline metrics, see [Pipeline metrics example](monitor-response.md).

```
import requests
from requests_auth_aws_sigv4 import AWSSigV4

domain_endpoint = '{{domain endpoint}}'
url = f'{domain_endpoint}/_nodes/stats/search_pipeline'

auth = AWSSigV4('es')
headers = {'Content-Type': 'application/json'}
try:
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
