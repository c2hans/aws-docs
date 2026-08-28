---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_dev_integ_auto_integ_deploy.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP10 Fully automate integration and deployment
<a name="ops_dev_integ_auto_integ_deploy"></a>

 Automate build, deployment, and testing of the workload. This reduces errors caused by manual processes and reduces the effort to deploy changes.

 Apply metadata using [Resource Tags](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) and [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/APIReference/Welcome.html) following a consistent [tagging strategy](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/) to enable identification of your resources. Tag your resources for organization, cost accounting, access controls, and targeting the execution of automated operations activities.

 **Common anti-patterns:**
+  On Friday you, finish authoring the new code for your feature branch. On Monday, after running your code quality test scripts and each of your unit tests scripts, you will check in your code for the next scheduled release.
+  You are assigned to code a fix for a critical issue impacting a large number of customers in production. After testing the fix, you commit your code and email change management to request approval to deploy it to production.

 **Benefits of establishing this best practice:** By implementing automated build and deployment management systems, you reduce errors caused by manual processes and reduce the effort to deploy changes enabling your team members to focus on delivering business value.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use build and deployment management systems: Use build and deployment management systems to track and implement change, to reduce errors caused by manual processes, and reduce the level of effort. Fully automate the integration and deployment pipeline from code check-in through build, testing, deployment, and validation. This reduces lead time, enables increased frequency of change, and reduces the level of effort.
  +  [What is AWS CodeBuild?](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
  +  [Continuous integration best practices for software development](https://www.youtube.com/watch?v=GEPJ7Lo346A)
  +  [Slalom: CI/CD for serverless applications on AWS](https://www.youtube.com/watch?v=tEpx5VaW4WE)
  +  [Introduction to AWS CodeDeploy - automated software deployment with Amazon Web Services](https://www.youtube.com/watch?v=Wx-ain8UryM)
  +  [What is AWS CodeDeploy?](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [What is AWS CodeBuild?](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
+  [What is AWS CodeDeploy?](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)

 **Related videos:**
+  [Continuous integration best practices for software development](https://www.youtube.com/watch?v=GEPJ7Lo346A)
+  [Introduction to AWS CodeDeploy - automated software deployment with Amazon Web Services](https://www.youtube.com/watch?v=Wx-ain8UryM)
+  [Slalom: CI/CD for serverless applications on AWS](https://www.youtube.com/watch?v=tEpx5VaW4WE)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
