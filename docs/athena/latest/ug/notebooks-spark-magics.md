---
source_url: https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-magics.html
---

# Use magic commands
<a name="notebooks-spark-magics"></a>

Magic commands, or magics, are special commands that you can run in a notebook cell. For example, `%env` shows the environment variables in a notebook session. Athena supports the magic functions in IPython 6.0.3.

This section shows some key magic commands in Athena for Apache Spark.
+  To see a list of magic commands in Athena, run the command **%lsmagic** in a notebook cell.
+ For information about using magics to create graphs in Athena notebooks, see [Use magics to create data graphs](notebooks-spark-magics-graphs.md).
+ For information about additional magic commands, see [Built-in magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html) in the IPython documentation.

**Note**
Currently, the `%pip` command fails when executed. This is a known issue.

**Topics**
+ [Cell magics](notebooks-spark-magics-cell-magics.md)
+ [Line Magics](notebooks-spark-magics-line-magics.md)
+ [Graph magics](notebooks-spark-magics-graphs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
