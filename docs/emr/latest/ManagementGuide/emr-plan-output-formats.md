---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-output-formats.html
---

# What formats can Amazon EMR return?
<a name="emr-plan-output-formats"></a>

 The default output format for a cluster is text with key, value pairs written to individual lines of the text files. This is the output format most commonly used.

 If your output data needs to be written in a format other than the default text files, you can use the Hadoop interface `OutputFormat` to specify other output types. You can even create a subclass of the `FileOutputFormat` class to handle custom data types. For more information, see [http://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapred/OutputFormat.html](http://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapred/OutputFormat.html).

 If you are launching a Hive cluster, you can use a serializer/deserializer (SerDe) to output data from HDFS to a given format. For more information, see [https://cwiki.apache.org/confluence/display/Hive/SerDe](https://cwiki.apache.org/confluence/display/Hive/SerDe).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
