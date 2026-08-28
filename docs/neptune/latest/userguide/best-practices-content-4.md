---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-4.html
---

# Place more restrictive nodes on the left side in Variable-Length Path (VLP) expressions
<a name="best-practices-content-4"></a>

 In Variable-Length Path (VLP) queries, the query engine optimizes the evaluation by choosing to start the traversal on the left or right side of the expression. The decision is based on the cardinality of the patterns on the left and right side. Cardinality is the number of nodes matching the specified pattern.
+  If the right pattern has a cardinality of one, then the right side will be the starting point.
+  If the left and the right side have cardinality of one, the expansion is checked on both sides and starts on the side with the smaller expansion. Expansion is the number of outgoing or incoming edges for the node on the left and the node on the right side of the VLP expression. This part of the optimization is only used if the VLP relationship is unidirectional and the relationship type is provided.
+  Otherwise, the left side will be the starting point.

 For a chain of VLP expressions, this optimization can only be applied to the first expression. The other VLPs are evaluated starting with the left side. As an example, let the cardinality of (a), (b) be one, and the cardinality of (c) be greater than one.
+  `(a)-[*1..]->(c)`: Evaluation starts with (a).
+  `(c)-[*1..]->(a)`: Evaluation starts with (a).
+  `(a)-[*1..]-(c)`: Evaluation starts with (a).
+  `(c)-[*1..]-(a)`: Evaluation starts with (a).

 Now let the incoming edges of (a) be two, and the outgoing edges of (a) be three, the incoming edges of (b) be four, and the outgoing edges of (b) be five.
+  `(a)-[*1..]->(b)`: Evaluation starts with (a) as the outgoing edges of (a) are less than the incoming edges of (b).
+  `(a)<-[*1..]-(b)`: Evaluation starts with (a) as the incoming edges of (a) are less than the outgoing edges of (b).

 As a general rule, place the more restrictive pattern on the left side of a VLP expression.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
