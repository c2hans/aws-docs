---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/UseCase_CustomJar.html
---

# Process data with a custom JAR
<a name="UseCase_CustomJar"></a>

A custom JAR runs a compiled Java program that you can upload to Amazon S3. You should compile the program against the version of Hadoop you want to launch, and submit a `CUSTOM_JAR` step to your Amazon EMR cluster. For more information about how to compile a JAR file, see [Build binaries using Amazon EMR](emr-build-binaries.md).

For more information about building a Hadoop MapReduce application, see the [MapReduce Tutorial](http://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html) in the Apache Hadoop documentation.

**Topics**
+ [Submit a custom JAR step](emr-launch-custom-jar-cli.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
