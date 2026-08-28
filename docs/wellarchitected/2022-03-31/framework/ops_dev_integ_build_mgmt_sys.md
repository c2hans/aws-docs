---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_dev_integ_build_mgmt_sys.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP04 Use build and deployment management systems
<a name="ops_dev_integ_build_mgmt_sys"></a>

 Use build and deployment management systems. These systems reduce errors caused by manual processes and reduce the level of effort to deploy changes.

 In AWS, you can build continuous integration/continuous deployment (CI/CD) pipelines using services such as [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/) (for example, AWS CodeCommit, [AWS CodeBuild](https://aws.amazon.com/codebuild/), [AWS CodePipeline](https://aws.amazon.com/codepipeline/), [AWS CodeDeploy](https://aws.amazon.com/codedeploy/), and [AWS CodeStar](https://aws.amazon.com/codestar/)).

 **Common anti-patterns:**
+  After compiling your code on your development system you, copy the executable onto your production systems and it fails to start. The local log files indicates that it has failed due to missing dependencies.
+  You successfully build your application with new features in your development environment and provide the code to Quality Assurance (QA). It fails QA because it is missing static assets.
+  On Friday, after much effort, you successfully built your application manually in your development environment including your newly coded features. On Monday, you are unable to repeat the steps that allowed you to successfully build your application.
+  You perform the tests you have created for your new release. Then you spend the next week setting up a test environment and performing all the existing integration tests followed by the performance tests. The new code has an unacceptable performance impact and must be redeveloped and then retested.

 **Benefits of establishing this best practice:** By providing mechanisms to manage build and deployment activities you reduce the level of effort to perform repetitive tasks, free your team members to focus on their high value creative tasks, and limit the introduction of error from manual procedures.

 **Level of risk exposed if this best practice is not established:** Medium

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
+  [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/)
+  [What is AWS CodeBuild?](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
+  [What is AWS CodeDeploy?](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)

 **Related videos:**
+  [Continuous integration best practices for software development](https://www.youtube.com/watch?v=GEPJ7Lo346A)
+  [Introduction to AWS CodeDeploy - automated software deployment with Amazon Web Services](https://www.youtube.com/watch?v=Wx-ain8UryM)
+  [Slalom: CI/CD for serverless applications on AWS](https://www.youtube.com/watch?v=tEpx5VaW4WE)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
