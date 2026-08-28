---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/prefix-and-range-based-mapping.html
---

# Prefix and range-based mapping
<a name="prefix-and-range-based-mapping"></a>

 Prefix and range-based mapping map ranges of keys (or hashes of keys) to cells, and serves to offset the downsides of the full mapping approach while providing flexibility.

![Diagram showing prefix and range-based mapping](http://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/images/prefix-and-range-based-mapping.jpg)

 Depending on the granularity of your service, you can further reduce the cardinality by making ranges of groups of keys.

![Diagram showing making ranges as groups of keys](http://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/images/ranges-as-groups-of-keys.jpg)

 Advantages:
+  Reduces the performance issue of full mapping, by grouping key and reducing the total cardinality.

 Disadvantages:
+  More likely to have a hot cell, as there is no control over which keys within each range might have the most traffic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
