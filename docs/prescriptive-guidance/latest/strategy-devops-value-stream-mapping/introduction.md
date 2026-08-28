---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-devops-value-stream-mapping/introduction.html
---

# Using development value stream mapping to identify constraints to DevOps outcomes
<a name="introduction"></a>

*Michael Kingery, Amazon Web Services*

DevOps teams commonly work with complex systems that involve people, processes, and technology. This complexity can make it difficult to know where to invest time and effort when you want to improve the system. Completing a development value stream map (DVSM) can help you identify and prioritize areas of improvement in your software development process.

*Development value stream mapping* is a process used to identify and prioritize constraints that adversely affect speed and quality in a software development lifecycle (SDLC). A *constraint* is a factor that limits the value stream. DVSM extends the value stream mapping process originally designed for lean manufacturing practices. It focuses on the steps and teams required to create and move value through the software development process. It incorporates lean practices, such as systems thinking, eliminating waste, visualizing work, and working in small batches. A DVSM supports the DevOps principles of continuous improvement, collaboration, elimination of silos and handoffs, data-driven decisions, and agile development through small deliverables.

For each step in your software development process, you identify the lead time (LT), process time (PT), and percent complete and accurate (%CA). You outline the *happy path*, which is the process flow if no exceptions or errors are encountered during development. You also outline the *failure path*, which is the flow that occurs when the product fails any step in the development process. The following image is an example of a completed DVSM.

![Sample development value stream map for identifying constraints in DevOps outcomes.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-devops-value-stream-mapping/images/guide-img/72315763-d7a6-461b-a0a7-2945fd258610/images/eeda2db4-1e61-418a-b1d3-70f383653384.png)

## Intended audience
<a name="intended-audience"></a>

This guide is designed for executive officers, IT and DevOps managers, and program managers who are interested in using a DVSM to drive speed and quality improvements in their organization's software development lifecycle. This guide and the DVSM process can significantly help unified product teams that want to optimize delivery and help siloed teams that want to reduce waste associated with handoffs.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

Development value stream mapping can help DevOps teams:
+ Reduce costs by minimizing the overhead associated with wasted steps, duplication, and handoffs
+ Increase speed by reducing lead time and wasted steps
+ Improve employee satisfaction by increasing autonomy and reducing dependencies, handoffs, and wasted steps
+ Reduce batch sizes
+ Identify and invest in improvements that positively affect the end product
+ Eliminate silos and reduce the number of handoffs between teams
+ Adopt a product team or platform team model

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
