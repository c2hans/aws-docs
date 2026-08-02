---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/ops_dev_integ_test_val_chg.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP02 Test and validate changes
<a name="ops_dev_integ_test_val_chg"></a>

 Every change deployed must be tested to avoid errors in production. This best practice is focused on testing changes from version control to artifact build. Besides application code changes, testing should include infrastructure, configuration, security controls, and operations procedures. Testing takes many forms, from unit tests to software component analysis (SCA). Move tests further to the left in the software integration and delivery process results in higher certainty of artifact quality.

 Your organization must develop testing standards for all software artifacts. Automated tests reduce toil and avoid manual test errors. Manual tests may be necessary in some cases. Developers must have access to automated test results to create feedback loops that improve software quality.

 **Desired outcome:** Your software changes are tested before they are delivered. Developers have access to test results and validations. Your organization has a testing standard that applies to all software changes.

 **Common anti-patterns:**
+ You deploy a new software change without any tests. It fails to run in production, which leads to an outage.
+ New security groups are deployed with CloudFormation without being tested in a pre-production environment. The security groups make your app unreachable for your customers.
+ A method is modified but there are no unit tests. The software fails when it is deployed to production.

 **Benefits of establishing this best practice:** Change fail rate of software deployments are reduced. Software quality is improved. Developers have increased awareness on the viability of their code. Security policies can be rolled out with confidence to support organization's compliance. Infrastructure changes such as automatic scaling policy updates are tested in advance to meet traffic needs.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Testing is done on all changes, from application code to infrastructure, as part of your continuous integration practice. Test results are published so that developers have fast feedback. Your organization has a testing standard that all changes must pass.

 **Customer example**

 As part of their continuous integration pipeline, AnyCompany Retail conducts several types of tests on all software artifacts. They practice test driven development so all software has unit tests. Once the artifact is built, they run end-to-end tests. After this first round of tests is complete, they run a static application security scan, which looks for known vulnerabilities. Developers receive messages as each testing gate is passed. Once all tests are complete, the software artifact is stored in an artifact repository.

### Implementation steps
<a name="implementation-steps"></a>

1.  Work with stakeholders in your organization to develop a testing standard for software artifacts. What standard tests should all artifacts pass? Are there compliance or governance requirements that must be included in the test coverage? Do you need to conduct code quality tests? When tests complete, who needs to know?

   1.  The [AWS Deployment Pipeline Reference Architecture](https://pipelines.devops.aws.dev/) contains an authoritative list of types of tests that can be conducted on software artifacts as part of an integration pipeline.

1.  Instrument your application with the necessary tests based on your software testing standard. Each set of tests should complete in under ten minutes. Tests should run as part of an integration pipeline.

   1.  [Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html) can test your application code for defects.

   1.  You can use [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) to conduct tests on software artifacts.

   1.  [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) can orchestrate your software tests into a pipeline.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS05-BP01 Use version control](ops_dev_integ_version_control.md)
+  [OPS05-BP06 Share design standards](ops_dev_integ_share_design_stds.md)
+  [OPS05-BP10 Fully automate integration and deployment](ops_dev_integ_auto_integ_deploy.md)

 **Related documents:**
+ [ Adopt a test-driven development approach ](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/development-best-practices.html)
+ [ Automated CloudFormation Testing Pipeline with TaskCat and CodePipeline ](https://aws.amazon.com/blogs/devops/automated-cloudformation-testing-pipeline-with-taskcat-and-codepipeline/)
+ [ Building end-to-end AWS DevSecOps CI/CD pipeline with open source SCA, SAST, and DAST tools ](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/)
+ [ Getting started with testing serverless applications ](https://aws.amazon.com/blogs/compute/getting-started-with-testing-serverless-applications/)
+ [ My CI/CD pipeline is my release captain ](https://aws.amazon.com/builders-library/cicd-pipeline/)
+ [ Practicing Continuous Integration and Continuous Delivery on AWS Whitepaper ](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/welcome.html)

 **Related videos:**
+ [AWS re:Invent 2020: Testable infrastructure: Integration testing on AWS](https://www.youtube.com/watch?v=KJC380Juo2w)
+ [AWS Summit ANZ 2021 - Driving a test-first strategy with CDK and test driven development ](https://www.youtube.com/watch?v=1R7G_wcyd3s)
+ [ Testing Your Infrastructure as Code with AWS CDK ](https://www.youtube.com/watch?v=fWtuwGSoSOU)

 **Related resources:**
+ [AWS Deployment Pipeline Reference Architecture - Application ](https://pipelines.devops.aws.dev/application-pipeline/index.html)
+ [AWS Kubernetes DevSecOps Pipeline ](https://github.com/aws-samples/devsecops-cicd-containers)
+ [ Policy as Code Workshop – Test Driven Development ](https://catalog.us-east-1.prod.workshops.aws/workshops/9da471a0-266a-4d36-8596-e5934aeedd1f/en-US/pac-tools/cfn-guard/tdd)
+ [ Run unit tests for a Node.js application from GitHub by using AWS CodeBuild](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-unit-tests-for-a-node-js-application-from-github-by-using-aws-codebuild.html)
+ [ Use Serverspec for test-driven development of infrastructure code ](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-serverspec-for-test-driven-development-of-infrastructure-code.html)

 **Related services:**
+  [Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html)
+  [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
+  [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
