---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-720.html
---

# Amazon EMR 7.2.0 - Tez release notes
<a name="Tez-release-history-720"></a>

## Amazon EMR 7.2.0 - Tez changes
<a name="Tez-release-history-changes-720"></a>

| Type | Description |
| --- | --- |
| Improvement | Option provided to disable locality constraints when requesting containers for tasks. |
| Bug Fix | Make TaskDependencies\#addTaskDependency thread safe |
| Upgrade | Upgrade TLS version to 1.3 for Tez. |

## Amazon EMR 7.2.0 - New configurations
<a name="Tez-release-history-changes-720-new-configs"></a>

| Classification | Name | Default | Description |
| --- | --- | --- | --- |
| tez-site | tez.task.relaxed.locality | false | When enabled, rack and node locality constraints are not considered while requesting a container for a task. |

**Amazon EMR 7.2.0 - Tez known issues**

**Tez DAG cleanup issue (EMR 6.11.0 - EMR 7.2.0)** – In clusters with SSL enabled running EMR versions 6.11.0 to 7.2.0, there is a known issue where *SSLHandshakeException* occurs in TEZ Application Master (AM) during the DAG cleanup phase. This happens when attempting to delete intermediate shuffle data from remote nodes over HTTPS after query completion, not during the query execution. The issue occurs because Tez AM cannot read the relevant **trustStore** configuration when calling the shuffle handler service endpoint. However this affects only the cleaning up of shuffle data during DAG cleanup, the application(AM) level cleanup happens anyways and cleans up any lingering shuffle data. So this doesn’t lead to shuffle data accumulation.

**Fix version:** – EMR 7.3.0

**Workaround** – Add the following SSL configuration to tez-site.xml:

```
<property>
    <name>ssl.client.truststore.location</name>
    <value>{SSL_TRUSTSTORE_LOCATION}</value>
</property>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
