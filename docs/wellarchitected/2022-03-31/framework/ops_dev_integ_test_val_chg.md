---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_dev_integ_test_val_chg.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP02 Test and validate changes
<a name="ops_dev_integ_test_val_chg"></a>

 Test and validate changes to help limit and detect errors. Automate testing to reduce errors caused by manual processes, and reduce the level of effort to test.

 Many AWS services offer version control capabilities. Use a revision or source control system such as [AWS CodeCommit](https://aws.amazon.com/codecommit/) to manage code and other artifacts, such as version-controlled [AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates of your infrastructure.

 **Common anti-patterns:**
+  You deploy your new code to production and customers start calling because your application is no longer working.
+  You apply new security groups to enhance your perimeter security. It works with unintended consequences; Your users are unable to access your applications.
+  You modify a method invoked by your new function. Another function was also dependant on that method and no longer works. The issue is not detected and enters production. The other function is not invoked for some time and finally fails in production without any correlation to the cause.

 **Benefits of establishing this best practice:** By testing and validating changes early, you are able to address issues with minimized costs and limit the impact on your customers. By testing prior to deployment you minimize the introduction of errors.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Test and validate changes: Changes should be tested and the results validated at all lifecycle stages (for example, development, test, and production). Use testing results to confirm new features and mitigate the risk and impact of failed deployments. Automate testing and validation to ensure consistency of review, to reduce errors caused by manual processes, and reduce the level of effort.
  +  [What is AWS CodeBuild?](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
  +  [Local build support for AWS CodeBuild](https://aws.amazon.com/blogs/devops/announcing-local-build-support-for-aws-codebuild/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/)
+  [Local build support for AWS CodeBuild](https://aws.amazon.com/blogs/devops/announcing-local-build-support-for-aws-codebuild/)
+  [What is AWS CodeBuild?](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
