---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sm-security.html
---

# Configure permissions
<a name="sm-security"></a>

If you're upgrading to 2.5 from a previous OpenSearch Service domain version, the snapshot management security permissions might not be defined on the domain. Non-admin users must be mapped to this role in order to use snapshot management on domains using fine-grained access control. To manually create the snapshot management role, perform the following steps:

1. In OpenSearch Dashboards, go to **Security** and choose **Permissions**.

1. Choose **Create action group** and configure the following groups:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/sm-security.html)

1. Choose **Roles** and **Create role**.

1. Name the role **snapshot\_management\_role**.

1. For **Cluster permissions**, select `snapshot_management_full_access` or `snapshot_management_read_access`.

1. Choose **Create**.

1. After you create the role, [map it](fgac.md#fgac-mapping) to any user or backend role that will manage snapshots.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
