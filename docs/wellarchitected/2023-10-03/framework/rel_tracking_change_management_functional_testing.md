---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/rel_tracking_change_management_functional_testing.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL08-BP02 Integrate functional testing as part of your deployment
<a name="rel_tracking_change_management_functional_testing"></a>

 Functional tests are run as part of automated deployment. If success criteria are not met, the pipeline is halted or rolled back.

 These tests are run in a pre-production environment, which is staged prior to production in the pipeline. Ideally, this is done as part of a deployment pipeline.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Integrate functional testing as part of your deployment. Functional tests are run as part of automated deployment. If success criteria are not met, the pipeline is halted or rolled back.
  +  Invoke AWS CodeBuild during the ‘Test Action’ of your software release pipelines modeled in AWS CodePipeline. This capability allows you to easily run a variety of tests against your code, such as unit tests, static code analysis, and integration tests.
    +  [AWS CodePipeline Adds Support for Unit and Custom Integration Testing with AWS CodeBuild](https://aws.amazon.com/about-aws/whats-new/2017/03/aws-codepipeline-adds-support-for-unit-testing/)
  +  Use AWS Marketplace solutions for invoking automated tests as part of your software delivery pipeline.
    +  [Software test automation](https://aws.amazon.com/marketplace/solutions/devops/software-test-automation)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS CodePipeline Adds Support for Unit and Custom Integration Testing with AWS CodeBuild](https://aws.amazon.com/about-aws/whats-new/2017/03/aws-codepipeline-adds-support-for-unit-testing/)
+  [Software test automation](https://aws.amazon.com/marketplace/solutions/devops/software-test-automation)
+  [What Is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
