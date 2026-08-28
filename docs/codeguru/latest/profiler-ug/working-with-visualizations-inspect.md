---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-inspect.html
---

# Inspecting a frame
<a name="working-with-visualizations-inspect"></a>

You can inspect frames that appear in many places in a visualization. This can happen when your application code has a common set of shared functions.

For example, if you have code that compresses data, you might call it from dozens of functions. If you inspect the compress function, you can see the parent (callers) and children (callee) functions at a glance.

**To inspect a frame**

1. On the **Profiling group detail** page, pause over the frame you want to inspect on the visualization.

1. Open the context (right-click) menu, and then choose **Inspect frame**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
