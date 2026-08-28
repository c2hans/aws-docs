---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/ZooKeeper-release-history-740.html
---

# Amazon EMR 7.4.0 - ZooKeeper release notes
<a name="ZooKeeper-release-history-740"></a>

| Type | Description |
| --- | --- |
| Upgrade | Zookeeper version is upgraded to 3.9.2. |
| Improvement | [ZOOKEEPER-4778](https://issues.apache.org/jira/browse/ZOOKEEPER-4778): Patch jetty, netty, and logback to remove high severity vulnerabilities. |
| Improvement | [ZOOKEEPER-4799](https://issues.apache.org/jira/browse/ZOOKEEPER-4778): Fixes CVE-2024-23944. |
| Bug Fix | [ZOOKEEPER-4415](https://issues.apache.org/jira/browse/ZOOKEEPER-4778): TLSv1.3 support is added. |

## Amazon EMR 7.4.0 - ZooKeeper Features
<a name="ZooKeeper-release-history-740-features"></a>
+ Clusters with in-transit encryption security configuration provided will have TLS enabled by default for Quorum communication and Zookeeper Admin Server. Additionally, TLS secure port is exposed at 2281 for client communication with Zookeeper.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
