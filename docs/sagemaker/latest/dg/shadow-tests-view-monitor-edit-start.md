---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit-start.html
---

# Start a shadow test early
<a name="shadow-tests-view-monitor-edit-start"></a>

 You can start your test before its scheduled start time. If the new duration of the test exceeds 30 days, SageMaker AI automatically sets the end of the test to 30 days after the new start time. This action starts the test immediately. If you want to change the start or end time of the test, see [Edit a shadow test](shadow-tests-view-monitor-edit-individual.md).

 To immediately start your test, before its scheduled start time, through the console, do the following:

1.  Select the test you want to start immediately from the **Shadow test** section on the **Shadow tests** page.

1.  From the **Actions** dropdown list, choose **Start**. The **Start shadow test?** dialog box appears.

1.  Choose **Start now**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
