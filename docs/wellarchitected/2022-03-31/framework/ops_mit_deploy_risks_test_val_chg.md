---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_mit_deploy_risks_test_val_chg.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS06-BP02 Test and validate changes
<a name="ops_mit_deploy_risks_test_val_chg"></a>

 Test changes and validate the results at all lifecycle stages to confirm new features and minimize the risk and impact of failed deployments.

 On AWS, you can create temporary parallel environments to lower the risk, effort, and cost of experimentation and testing. Automate the deployment of these environments using [AWS CloudFormation](https://aws.amazon.com/cloudformation/) to ensure consistent implementations of your temporary environments.

 **Common anti-patterns:**
+  You deploy a cool new feature to your application. It doesn't work. You don't know.
+  You update your certificates. You accidentally install the certificates to the wrong components. You don't know.

 **Benefits of establishing this best practice:** By testing and validating changes following deployment you are able to identify issues early providing an opportunity to mitigate the impact on your customers.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Test and validate changes: Test changes and validate the results at all lifecycle stages (for example, development, test, and production), to confirm new features and minimize the risk and impact of failed deployments.
  +  [AWS Cloud9](https://aws.amazon.com/cloud9/)
  +  [What is AWS Cloud9?](https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html)
  +  [How to test and debug AWS CodeDeploy locally before you ship your code](https://aws.amazon.com/blogs/devops/how-to-test-and-debug-aws-codedeploy-locally-before-you-ship-your-code/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Cloud9](https://aws.amazon.com/cloud9/)
+  [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/)
+  [How to test and debug AWS CodeDeploy locally before you ship your code](https://aws.amazon.com/blogs/devops/how-to-test-and-debug-aws-codedeploy-locally-before-you-ship-your-code/)
+  [What is AWS Cloud9?](https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
