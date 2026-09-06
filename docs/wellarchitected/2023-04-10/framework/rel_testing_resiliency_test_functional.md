---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_testing_resiliency_test_functional.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL12-BP03 Test functional requirements
<a name="rel_testing_resiliency_test_functional"></a>

 Use techniques such as unit tests and integration tests that validate required functionality.

 You achieve the best outcomes when these tests are run automatically as part of build and deployment actions. For instance, using AWS CodePipeline, developers commit changes to a source repository where CodePipeline automatically detects the changes. Those changes are built, and tests are run. After the tests are complete, the built code is deployed to staging servers for testing. From the staging server, CodePipeline runs more tests, such as integration or load tests. Upon the successful completion of those tests, CodePipeline deploys the tested and approved code to production instances.

 Additionally, experience shows that synthetic transaction testing (also known as *canary testing*, but not to be confused with canary deployments) that can run and simulate customer behavior is among the most important testing processes. Run these tests constantly against your workload endpoints from diverse remote locations. Amazon CloudWatch Synthetics allows you to [create canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) to monitor your endpoints and APIs.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Test functional requirements. These include unit tests and integration tests that validate required functionality.
  +  [Use CodePipeline with AWS CodeBuild to test code and run builds](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html)
  +  [AWS CodePipeline Adds Support for Unit and Custom Integration Testing with AWS CodeBuild](https://aws.amazon.com/about-aws/whats-new/2017/03/aws-codepipeline-adds-support-for-unit-testing/)
  +  [Continuous Delivery and Continuous Integration](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-continuous-delivery-integration.html)
  +  [Using Canaries (Amazon CloudWatch Synthetics)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
  +  [Software test automation](https://aws.amazon.com/marketplace/solutions/devops/software-test-automation)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help with implementation of a continuous integration pipeline](https://aws.amazon.com/partners/find/results/?keyword=Continuous+Integration)
+  [AWS CodePipeline Adds Support for Unit and Custom Integration Testing with AWS CodeBuild](https://aws.amazon.com/about-aws/whats-new/2017/03/aws-codepipeline-adds-support-for-unit-testing/)
+  [AWS Marketplace: products that can be used for continuous integration](https://aws.amazon.com/marketplace/search/results?searchTerms=Continuous+integration)
+  [Continuous Delivery and Continuous Integration](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-continuous-delivery-integration.html)
+  [Software test automation](https://aws.amazon.com/marketplace/solutions/devops/software-test-automation)
+  [Use CodePipeline with AWS CodeBuild to test code and run builds](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html)
+  [Using Canaries (Amazon CloudWatch Synthetics)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
