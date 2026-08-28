---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-choosing-my-code.html
---

# Choosing my code in visualizations
<a name="working-with-visualizations-choosing-my-code"></a>

CodeGuru Profiler differentiates your code in the overview visualization, so you can quickly identify the methods you are working on.

The blue portion of the flame graph highlights your code. The green portion of the graph highlights other code that your application uses, such as libraries and frameworks.

![Image: Stack traces in overview 1.](http://docs.aws.amazon.com/codeguru/latest/profiler-ug/images/mycode.png)

You can change the coloring by manually selecting which package name you want CodeGuru Profiler to identify as your code.

**To view your code**

1. Choose **Actions**.

1. Choose **Select my code**.

1. Search for the profile namespace that you want to view. The namespaces are sorted based on how much of the overall profiling data they represent.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
