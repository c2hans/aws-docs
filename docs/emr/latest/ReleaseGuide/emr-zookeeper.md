---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-zookeeper.html
---

# Apache ZooKeeper
<a name="emr-zookeeper"></a>

Apache ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. For more information about ZooKeeper, see [http://zookeeper.apache.org/](https://zookeeper.apache.org/).

The following table lists the version of ZooKeeper included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with ZooKeeper.

For the version of components installed with ZooKeeper in this release, see [Release 7.13.0 Component Versions](emr-7130-release.md).

**ZooKeeper version information for emr-7.13.0**

| Amazon EMR Release Label | ZooKeeper Version | Components Installed With ZooKeeper |
| --- | --- | --- |
| emr-7.13.0 | ZooKeeper 3.9.3-amzn-5 | emrfs, emr-goodies, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-hdfs-zkfc, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, zookeeper-client, zookeeper-server |

The following table lists the version of ZooKeeper included in the latest release of the Amazon EMR 6.x series, along with the components that Amazon EMR installs with ZooKeeper.

For the version of components installed with ZooKeeper in this release, see [Release 6.15.0 Component Versions](emr-6150-release.md).

**ZooKeeper version information for emr-6.15.0**

| Amazon EMR Release Label | ZooKeeper Version | Components Installed With ZooKeeper |
| --- | --- | --- |
| emr-6.15.0 | ZooKeeper 3.5.10 | emrfs, emr-goodies, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, zookeeper-client, zookeeper-server |

The following table lists the version of ZooKeeper included in the latest release of the Amazon EMR 5.x series, along with the components that Amazon EMR installs with ZooKeeper.

For the version of components installed with ZooKeeper in this release, see [Release 5.36.2 Component Versions](emr-5362-release.md).

**ZooKeeper version information for emr-5.36.2**

| Amazon EMR Release Label | ZooKeeper Version | Components Installed With ZooKeeper |
| --- | --- | --- |
| emr-5.36.2 | ZooKeeper 3.4.14 | emrfs, emr-goodies, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, zookeeper-client, zookeeper-server |

**Topics**
+ [ZooKeeper release history](ZooKeeper-release-history.md)
+ [ZooKeeper release notes by version](ZooKeeper-release-history-versions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
