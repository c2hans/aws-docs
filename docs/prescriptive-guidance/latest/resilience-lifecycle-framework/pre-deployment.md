---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/pre-deployment.html
---

# Pre-deployment activities
<a name="pre-deployment"></a>

## Environment design
<a name="environment-design"></a>

The environment in which you test and evaluate your application affects how thoroughly you can test it, and how much confidence you have that those results accurately reflect what will happen in production. You might be able to perform some integration testing locally on developer machines by using services such as Amazon DynamoDB (see [Setting up DynamoDB local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) in the DynamoDB documentation). However, at some point you need to test in an environment that replicates your production environment in order to achieve the highest confidence in your results. This environment will incur cost, so we recommend that you take a staged, or pipelined, approach to your environments, where production-like environments appear later in the pipeline.

## Integration testing
<a name="integration-testing"></a>

Integration testing is the process of testing that a well-defined component of an application performs its functions correctly when it operates with external dependencies. Those external dependencies could be other custom-developed components, AWS services that you use for your application, third-party dependencies, and on-premises dependencies.  This guide focuses on integration tests that demonstrate the resilience of your application. It assumes that unit and integration tests already exist that demonstrate the functional accuracy of your software.

We recommend that you design integration tests that specifically test the resilience patterns you have implemented, such as circuit breaker patterns or load shedding (see the [*design and implement*](stage-2.md) stage). Resilience-oriented integration tests often involve applying a specific load to the application or intentionally introducing disruptions into the environment by using capabilities such as [AWS Fault Injection Service (AWS FIS)](https://aws.amazon.com/fis/). Ideally, you should run all integration tests as part of your CI/CD pipeline and ensure that you run tests every time code is committed. This helps you quickly detect and react to any changes to code or configurations that result in violations of your resilience objectives. Large-scale distributed applications are complex, and even minor changes can significantly impact the resilience of seemingly unrelated portions of your application. Try to run your tests on every commit. AWS provides an excellent set of tools for operating your CI/CD pipeline and other DevOps tools. For more information, see [Introduction to DevOps on AWS](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/introduction-to-devops.html) on the AWS website.

## Automated deployment pipelines
<a name="automated-deployment-pipelines"></a>

Deployment to, and testing in, your pre-production environments is a repetitive and complex task that is best left to automation. Automation of this process frees up human resources and reduces the opportunity for error. The mechanism for automating this process is often referred to as a *pipeline*. When you create your pipeline, we recommend that you set up a series of testing environments that get increasingly closer to your production configuration. You use this series of environments to repeatedly test your application. The first environment provides a more limited set of capabilities than the production environment but incurs a significantly lower cost. Subsequent environments should add services and scale to more closely mirror the production environment.

Start by testing in the first environment. After your deployments pass all your tests in the first test environment, let the application run under some amount of load for a period of time to see whether any issues occur over time. Confirm that you have configured observability correctly (see *Alarm precision* later in this guide) so that you can detect any issues that arise. When this observation period has completed successfully, deploy your application to your next testing environment and repeat the process, adding additional tests or load as supported by the environment. After you have sufficiently tested your application in this way, you can use the deployment methods that you previously set up to deploy the application into production (see *Define CI/CD strategies* earlier in this guide). The article [Automating safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/) in the Amazon Builders' Library is an excellent resource that describes how Amazon automates code deployment. The number of environments that precede your production deployment will vary, depending on the complexity of your application and the types of dependencies it has.

## Load testing
<a name="load-testing"></a>

On the surface, load testing resembles integration testing. You test a discrete function of your application and its external dependencies to verify that it operates as expected. Load testing then goes beyond integration testing to focus on how the application functions under well-defined loads. Load testing requires verification of correct functionality, so it must occur after a successful integration test. It is important to understand how well the application responds under expected loads as well as how it behaves when the load exceeds expectations. This helps you  verify that you have implemented the necessary mechanisms to ensure that your application remains resilient under extreme load. For a comprehensive guide to load testing on AWS, see [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) in the AWS Solutions Library.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
