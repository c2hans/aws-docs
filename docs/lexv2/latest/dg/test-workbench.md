---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/test-workbench.html
---

# Evaluating Lex V2 bot performance with the Test Workbench
<a name="test-workbench"></a>

To improve bot performance, you can evaluate the performance of your bots at scale. The results for your test evaluation are displayed in simple tables and charts.

You can use the Test Workbench to create reference test sets that use existing transcription data. You can test bots to evaluate performance before deployment, and view test result breakdowns at scale.

![The work flow diagram to improve bot accuracy with the Test Workbench.](http://docs.aws.amazon.com/lexv2/latest/dg/images/testworkbench/testworkbench-workflow.png)

Users can use the Test Workbench to establish baseline performance for bots. This covers intent and slot performance for utterances that are in the form of single-inputs or conversations. Once a test set is successfully loaded, you can run it against your existing pre-production or production bots. The Test Workbench helps you identify opportunities for improved slot filling and intent classification.

**Topics**
+ [Generate a test set for Test Workbench](test-sets.md)
+ [Manage test sets](manage-test-sets.md)
+ [Execute a test](execute-test-set.md)
+ [Test set coverage in Test Workbench](validation-test-set.md)
+ [View test results](test-results-test-set.md)
+ [Test results details in Test Workbench](test-results-details-test-set.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
