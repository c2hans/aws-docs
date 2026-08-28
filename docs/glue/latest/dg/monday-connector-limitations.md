---
source_url: https://docs.aws.amazon.com/glue/latest/dg/monday-connector-limitations.html
---

# Limitations
<a name="monday-connector-limitations"></a>

The following are limitations for the Monday connector:
+  The dynamic metadata response has certain conflicts with the documentation as mentioned below:
  +  Group, Column entity supports filter operations, but it is not present in the dynamic metadata endpoint, hence it's kept as non-filterable entity.
  +  The dynamic endpoint consists of around 15000\+ lines and returns metadata of all the entities in a single response, because of this the fields are taking an average of 10 seconds to load hence, this would require some additional time while running a job.
  +  Refer the below table for Monday rate limit. The significant size of the dynamic entity's response data causes a noticeable delay, with fields requiring an average of 10 seconds to load.
<a name="monday-rate-limit-table"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/monday-connector-limitations.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
