---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown-modify.html
---

# Modify your idle shutdown time limit
<a name="studio-updated-idle-shutdown-modify"></a>

 Users may be able to modify the idle shutdown time limit if the admin gives access when adding support for idle shutdown. If support for idle shutdown is added, there may be a limit applied to the maximum time for idle shutdown. A user can set the value anywhere between the lower limit and upper limit.

1.  Launch Amazon SageMaker Studio by following the steps in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1.  From the **Applications** section, select the application type to update the idle shutdown time for.

1.  Select the space to update.

1.  Update **Idle shutdown (mins)** with your desired value.
**Note**
If idle shutdown is set when applications are running, they must be restarted for idle shutdown settings to take effect.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
