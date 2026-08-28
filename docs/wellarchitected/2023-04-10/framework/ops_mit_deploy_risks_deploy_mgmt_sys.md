---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_mit_deploy_risks_deploy_mgmt_sys.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS06-BP03 Use deployment management systems
<a name="ops_mit_deploy_risks_deploy_mgmt_sys"></a>

 Use deployment management systems to track and implement change. This reduces errors caused by manual processes and reduces the effort to deploy changes.

 In AWS, you can build Continuous Integration/Continuous Deployment (CI/CD) pipelines using services such as [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/) (for example, AWS CodeCommit, [AWS CodeBuild](https://aws.amazon.com/codebuild/), [AWS CodePipeline](https://aws.amazon.com/codepipeline/), [AWS CodeDeploy](https://aws.amazon.com/codedeploy/), and [AWS CodeStar](https://aws.amazon.com/codestar/)).

 **Common anti-patterns:**
+  You manually deploy updates to the application servers across your fleet and a number of servers become unresponsive due to update errors.
+  You manually deploy to your application server fleet over the course of many hours. The inconsistency in versions during the change causes unexpected behaviors.

 **Benefits of establishing this best practice:** Adopting deployment management systems reduces the level of effort to deploy changes, and the frequency of errors caused by manual procedures.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use deployment management systems: Use deployment management systems to track and implement change. This will reduce errors caused by manual processes, and reduce the level of effort to deploy changes. Automate the integration and deployment pipeline from code check-in through testing, deployment, and validation. This reduces lead time, encourages increased frequency of change, and further reduces the level of effort.
  +  [Introduction to AWS CodeDeploy - automated software deployment with Amazon Web Services](https://www.youtube.com/watch?v=Wx-ain8UryM)
  +  [What is AWS CodeDeploy?](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)
  +  [What is AWS Elastic Beanstalk?](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
  +  [What is Amazon API Gateway?](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS CodeDeploy User Guide](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)
+  [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/)
+  [Try a Sample Blue/Green Deployment in AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create-blue-green.html)
+  [What is AWS CodeDeploy?](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)
+  [What is AWS Elastic Beanstalk?](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
+  [What is Amazon API Gateway?](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)

 **Related videos:**
+  [Deep Dive on Advanced Continuous Delivery Techniques Using AWS](https://www.youtube.com/watch?v=Lrrgd0Kemhw)
+  [Introduction to AWS CodeDeploy - automated software deployment with Amazon Web Services](https://www.youtube.com/watch?v=Wx-ain8UryM)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
