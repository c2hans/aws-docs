---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-compile.html
---

# Compile error: "Could not resolve dependencies for project"
<a name="troubleshooting-compile"></a>

In order to compile the Managed Service for Apache Flink sample applications, you must first download and compile the Apache Flink Kinesis connector and add it to your local Maven repository. If the connector hasn't been added to your repository, a compile error similar to the following appears:

```
Could not resolve dependencies for project {{your project name}}: Failure to find org.apache.flink:flink-connector-kinesis_2.11:jar:1.8.2 in https://repo.maven.apache.org/maven2 was cached in the local repository, resolution will not be reattempted until the update interval of central has elapsed or updates are forced
```

To resolve this error, you must download the Apache Flink source code (version 1.8.2 from [https://flink.apache.org/downloads.html](https://flink.apache.org/downloads.html)) for the connector. For instructions about how to download, compile, and install the Apache Flink source code, see [Using the Apache Flink Kinesis Streams connector with previous Apache Flink versions](earlier.md#how-creating-apps-building-kinesis).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
