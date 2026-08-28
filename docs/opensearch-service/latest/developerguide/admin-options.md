---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/admin-options.html
---

# Performing administrative actions on Amazon OpenSearch Service domains
<a name="admin-options"></a>

Amazon OpenSearch Service offers several administrative options that provide granular control if you need to troubleshoot issues with your domain. These options include the ability to restart the OpenSearch process on a data node and the ability to restart a data node.

OpenSearch Service monitors node health parameters and, when there are anomalies, takes corrective actions to keep domains stable. With the administrative options to restart the OpenSearch process on a node, and restart a node itself, you have control over some of these mitigation actions.

You can use the AWS Management Console, AWS CLI, or the AWS SDK to perform these actions. The following sections cover how to perform these actions with the console.

## Limitations
<a name="admin-limitations"></a>

Administrative options have the following limitations:
+ Administrative options are supported on Elasticsearch versions 7.x and higher.
+ Administrative options don't support domains with Multi-AZ with Standby enabled.
+ The OpenSearch and Elasticsearch process restart and the data node reboot are supported on domains with three or more data nodes.
+ The Dashboards and Kibana process support is supported on domains with two or more data nodes.
+ To restart the OpenSearch process on a node or reboot a node, the domain must not be in red state and all indexes must have replicas configured.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
