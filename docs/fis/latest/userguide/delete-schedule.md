---
source_url: https://docs.aws.amazon.com/fis/latest/userguide/delete-schedule.html
---

# Disable or delete an experiment schedule
<a name="delete-schedule"></a>

 To stop an experiment from executing or running on a schedule, you can delete or disable the rule. The following steps walk you through how to delete or disable an Experiment Execution using the AWS console.

To delete or disable a rule

1. Open the [Amazon FIS console](https://docs.aws.amazon.com/fis).

1. In the navigation pane, choose **Experiment Templates**.

1. Choose **Resource type: Experiment Template** for which a schedule is already created.

1. Click on the Experiment ID for the template. Then navigate to schedules Tab.

1.  Check if there is a existing schedule associated with the experiment. Select the schedule associated and Click the button **Update Schedule**.

1. Do one of the following:

   1. To delete the schedule, select the button next to the rule **Delete Schedule**. Type `delete` and click the **Delete Schedule** button.

   1. To disable the schedule, select the button next to the rule **Disable Schedule**. Type `disable` and click the **Disable Schedule** button.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
