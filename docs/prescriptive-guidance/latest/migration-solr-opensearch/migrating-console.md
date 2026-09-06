---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/migrating-console.html
---

# Migrating the Admin Console
<a name="migrating-console"></a>

The Solr Admin UI is a web-based interface that users access at `http://hostname:8983/Solr/` to get comprehensive access to Solr configuration and features.

**Note**
8983 is the default Admin Console port for Solr, but this port number might vary in non-default configurations.

You use the Solr Admin UI for administration purposes; for example, to monitor clusters, administer collections, design schemas, run Solr queries, and manage the security of your cluster. If you use Solr for analytics, you might be taking advantage of UI integrations such as Apache Zeppelin, Apache Superset, and Grafana for dashboarding.

When you migrate to OpenSearch, you can use OpenSearch Dashboards for both administrative purposes such as managing your schema, security, and roles, and for data visualization from a single location, as shown in the following table.

|
|
| Task | Solr | OpenSearch |
| --- |--- |--- |
| Administrative work | Solr Admin UI | OpenSearch Dashboards |
| Analytics | Grafana, Zeppelin, and other tools | OpenSearch Dashboards |

The Solr Admin UI supports basic and Kerberos-based authentication. For authentication in OpenSearch, you need to create a valid role for accessing OpenSearch Dashboards and map users to the role. You can create different roles for different access requirements. For example, an administrative user might have access to all pages, but a read-only data user might see only specific indexes in OpenSearch Dashboards. For more information, see [Defining users and roles](https://docs.opensearch.org/latest/security/access-control/users-roles/) in the OpenSearch documentation.

OpenSearch provides an ML-powered Assistant Toolkit for generating visualizations through natural language queries. In Amazon OpenSearch Service, you can use Amazon Q Developer for additional AI capabilities, including visualization generation, alert insights, query summaries, anomaly detection recommendations, and chat support. For more information, see [OpenSearch Assistant for OpenSearch Dashboards](https://docs.opensearch.org/latest/dashboards/dashboards-assistant/index/) in the OpenSearch documentation and [Amazon Q Developer for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/Amazon-Q-developer-support.html) in the AWS documentation.
