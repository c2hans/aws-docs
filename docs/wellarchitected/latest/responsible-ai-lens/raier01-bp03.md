---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raier01-bp03.html
---

# RAIER01-BP03 For each system update, re-run the evaluation and update the system registry
<a name="raier01-bp03"></a>

 Record evaluation activities in logs that capture test conditions, system configurations, data inputs, raw results, and methodological notes with sufficient detail to make the entire process reproducible. Establish version control for evaluation artifacts to assist builders to trace unique system builds and their corresponding evaluation results.

 **Level of risk exposed if this best practice is not established:** High

## Implementation considerations
<a name="implementation-considerations-81"></a>

1.  Log your evaluation runs, including information on which datasets you used, what system version you tested, what hardware and software configuration you ran on, and raw and intermediate outputs. Your logs should be detailed enough that someone else could reproduce your exact evaluation months later.

1.  Set up version control for your evaluation materials, including test scripts, configuration files, and result outputs.

1.  Link your evaluation materials to both your system and your dataset registry so that it is clear which data and system versions led to the evaluation results. This allows you to link each system build and dataset pair to its specific evaluation artifacts.

## Resources
<a name="resources-78"></a>

 **Related documents**
+  [ISO/IEC 42001:2023 A.6.2.4 AI system verification and validation](https://www.iso.org/standard/42001)
+  [ISO/IEC 42001:2023 A.7.2 Data for development and enhancement of AI system](https://www.iso.org/standard/42001)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
