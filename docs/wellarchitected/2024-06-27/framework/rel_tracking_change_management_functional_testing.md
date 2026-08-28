---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel_tracking_change_management_functional_testing.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL08-BP02 Integrate functional testing as part of your deployment
<a name="rel_tracking_change_management_functional_testing"></a>

 Functional tests are run as part of automated deployment. If success criteria are not met, the pipeline is halted or rolled back. These tests are run in a pre-production environment, which is staged prior to production in the pipeline. Ideally, this is done as part of a deployment pipeline.

 **Desired outcome:** You use automation to perform functional tests, and the associated test data reduces test duration and expense and improves accuracy of test results. You integrate functional tests as part of your deployment process, which helps you automate your release pipelines for fast and reliable application and infrastructure updates.

 **Common anti-patterns:**
+  You manually perform tests outside the deployment pipeline.
+  You skip testing steps in your automation through manual emergency workflows.
+  You don't follow your established test plans and processes in favor of accelerated timelines.

 **Benefits of establishing this best practice:** Functional tests validate that the system operates according to specified requirements. It is used to consistently verify the intended working order of components such as user interfaces, APIs, databases, and source code. When you examine these components of the system, functional tests verify that each feature behaves as expected, which protects both user expectations and the software's integrity. Integrate functional tests as part of your regular deployment, and use automation to deploy all changes, which reduces the potential for introduction of human errors.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Integrate functional testing as part of your deployment. Functional tests are run as part of automated deployment. If success criteria are not met, the pipeline is halted or rolled back. AWS CodePipeline provides a continuous delivery pipeline for automated testing, which allows testers to automate the entire testing and deployment process. It integrates with AWS services such as AWS CodeBuild and AWS CodeDeploy to automate the build, test, and deployment phases of the software development lifecycle.

### Implementation steps
<a name="implementation-steps"></a>
+  **Configure your pipeline:** Set up your source, build, test, and deploy stages using the AWS CodePipeline console or AWS Command Line Interface (CLI).
  +  **Define your source:** With AWS CodePipeline, you can automatically retrieve source code from version control systems like GitHub, AWS CodeCommit, or Bitbucket, which verifies that the latest code is always used for testing.
  +  **Automate builds and tests:** AWS CodeBuild can automatically build and test your code and generate test reports. It supports popular testing frameworks like JUnit, NUnit, and TestNG.
  +  **Deploy your code:** Once the code has been built and tested, AWS CodeDeploy can deploy it to your testing environment, including Amazon EC2 instances, AWS Lambda functions, or on-premises servers.
  +  **Monitor pipelines:** AWS CodePipeline can track the progress of your pipeline and the status of each stage. You can also use quality checks to block the pipeline as per test execution status. You can also receive notifications for any pipeline stage failure or pipeline completion.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Use AWS CodePipeline with AWS CodeBuild to test code and run builds](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html)
+  [Logging and monitoring in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/logging-monitoring.html)
+  [Indicators for functional testing](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/indicators-for-functional-testing.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
