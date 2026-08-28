---
source_url: https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-ti.html
---

# Troubleshooting triggers and AWS CodeCommit
<a name="troubleshooting-ti"></a>

The following information might help you troubleshoot issues with triggers in AWS CodeCommit.

**Topics**
+ [Trigger error: A repository trigger does not run when expected](#troubleshooting-ti1)

## Trigger error: A repository trigger does not run when expected
<a name="troubleshooting-ti1"></a>

**Problem:** One or more triggers configured for a repository does not appear to run or does not run as expected.

**Possible fixes:** If the target of the trigger is an AWS Lambda function, make sure you have configured the function's resource policy for access by CodeCommit.

Alternatively, edit the trigger and make sure the events for which you want to trigger actions have been selected and that the branches for the trigger include the branch where you want to see responses to actions. Try changing the settings for the trigger to **All repository events** and **All branches** and then testing the trigger. For more information, see [Edit triggers for a repository](how-to-notify-edit.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
