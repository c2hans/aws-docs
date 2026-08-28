---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-690.html
---

# Amazon EMR 6.9.0 - Tez release notes
<a name="Tez-release-history-690"></a>

## Amazon EMR 6.9.0 - Tez changes
<a name="Tez-release-history-changes-690"></a>

| Type | Description |
| --- | --- |
| Upgrade | Tez is upgraded to 0.10.2. For more information, see the [change log for Apache Tez 0.10.2](https://github.com/apache/tez/blob/rel/release-0.10.2/CHANGES.txt). |
| Upgrade | Upgrade Hadoop to 3.3.3. |
| Bug | Disable tez.runtime.transfer.data-via-events.enabled by default due to [TEZ-4450](https://issues.apache.org/jira/browse/TEZ-4450). |

**Amazon EMR 6.9.0 - Tez known issues**
+ **Hive jobs running on Tez** – In clusters with SSL enabled running EMR version 6.9.0, there is a known issue where Hive jobs running on Tez fail with *SSLHandshakeException*. This is related to the open-source issue [TEZ-4096](https://issues.apache.org/jira/browse/TEZ-4096), which was introduced with the Tez upgrade to version 0.10.2 in EMR 6.9.0. The issue requires SSL-related configurations to be passed from the client side (Hive).

  **Fix version:** – EMR 6.10.0

  **Workaround** – Add the following SSL configuration to tez-site.xml:

  ```
  <property>
      <name>ssl.client.truststore.location</name>
      <value>{SSL_TRUSTSTORE_LOCATION}</value>
  </property>
  ```
+ **Pig jobs running on Tez** – In clusters with SSL enabled running EMR version 6.9.0 to 7.0.0, there is a known issue where Pig jobs running on Tez fail with *SSLHandshakeException*. This is related to the open-source issue [TEZ-4096](https://issues.apache.org/jira/browse/TEZ-4096), which was introduced with the Tez upgrade to version 0.10.2 in EMR 6.9.0. The issue requires SSL-related configurations to be passed from the client side (Pig).

  **Fix version:** – EMR 7.1.0

  **Workaround** – Add the following SSL configuration to tez-site.xml:

  ```
  <property>
      <name>ssl.client.truststore.location</name>
      <value>{SSL_TRUSTSTORE_LOCATION}</value>
  </property>
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
