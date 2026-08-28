---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/ZooKeeper-release-history-750.html
---

# Amazon EMR 7.5.0 - ZooKeeper release notes
<a name="ZooKeeper-release-history-750"></a>

## Amazon EMR 7.5.0 - ZooKeeper Changes
<a name="ZooKeeper-release-history-750-features"></a>
+ Starting with EMR-7.5.0, Zookeeper is set to Java 17 by default at runtime. To use a different version for the Java runtime, override the JVM settings in the `zookeeper-server` file and set `JAVA_HOME` to the desired version.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
