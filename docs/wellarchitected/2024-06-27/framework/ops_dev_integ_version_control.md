---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/ops_dev_integ_version_control.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP01 Use version control
<a name="ops_dev_integ_version_control"></a>

 Use version control to activate tracking of changes and releases.

 Many AWS services offer version control capabilities. Use a revision or source control system such as [AWS CodeCommit](https://aws.amazon.com/codecommit/) to manage code and other artifacts, such as version-controlled [AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates of your infrastructure.

 **Desired outcome:** Your teams collaborate on code. When merged, the code is consistent and no changes are lost. Errors are easily reverted through correct versioning.

 **Common anti-patterns:**
+  You have been developing and storing your code on your workstation. You have had an unrecoverable storage failure on the workstation and your code is lost.
+  After overwriting the existing code with your changes, you restart your application and it is no longer operable. You are unable to revert the change.
+  You have a write lock on a report file that someone else needs to edit. They contact you asking that you stop work on it so that they can complete their tasks.
+  Your research team has been working on a detailed analysis that shapes your future work. Someone has accidentally saved their shopping list over the final report. You are unable to revert the change and have to recreate the report.

 **Benefits of establishing this best practice:** By using version control capabilities you can easily revert to known good states and previous versions, and limit the risk of assets being lost.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Maintain assets in version controlled repositories. Doing so supports tracking changes, deploying new versions, detecting changes to existing versions, and reverting to prior versions (for example, rolling back to a known good state in the event of a failure). Integrate the version control capabilities of your configuration management systems into your procedures.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS05-BP04 Use build and deployment management systems](ops_dev_integ_build_mgmt_sys.md)

 **Related documents:**
+  [What is AWS CodeCommit?](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html)

 **Related videos:**
+  [Introduction to AWS CodeCommit](https://youtu.be/46PRLMW8otg)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
