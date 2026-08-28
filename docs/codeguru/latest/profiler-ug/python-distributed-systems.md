---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-distributed-systems.html
---

# Profiling Distributed systems
<a name="python-distributed-systems"></a>

Amazon CodeGuru Profiler offers limited support when implemented on distributed systems like Spark on EMR or Glue jobs running across clusters. In such cases, Profiler is able to profile the application running on the manager node; however, it may not be able to profile the part of the application running on the worker nodes. Please consult with your local technical representative for further clarifications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
