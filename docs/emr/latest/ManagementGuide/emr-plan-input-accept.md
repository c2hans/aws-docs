---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-input-accept.html
---

# Types of input Amazon EMR can accept
<a name="emr-plan-input-accept"></a>

The default input format for a cluster is text files with each line separated by a newline (\\n) character, which is the input format most commonly used.

If your input data is in a format other than the default text files, you can use the Hadoop interface `InputFormat` to specify other input types. You can even create a subclass of the `FileInputFormat` class to handle custom data types. For more information, see [http://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapred/InputFormat.html](http://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapred/InputFormat.html).

If you are using Hive, you can use a serializer/deserializer (SerDe) to read data in from a given format into HDFS. For more information, see [https://cwiki.apache.org/confluence/display/Hive/SerDe](https://cwiki.apache.org/confluence/display/Hive/SerDe).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
