---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/test-automation.html
---

# Test automation
<a name="test-automation"></a>

Automated testing with a specialized framework and tools can reduce human intervention and maximize quality. Automated performance testing is no different from automation tests such as unit testing and integration testing.

Use DevOps pipelines in the different stages for performance testing.

![Process diagram shows the five stages.](http://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/images/guide-img/7c6508f5-55cf-496c-a7ac-ba285b7b71ef/images/560075e2-ae27-45d7-851c-d1960c655b23.png)

The five stages for the test automation pipeline are:

1. **Set up** ‒ Use the test-data approaches described in the Test-data generation section for this stage. Generating realistic test data is critical to obtain valid test results. You must carefully create diverse test data that covers a wide range of use cases and closely matches live production data. Before running full-scale performance tests, you might need to run initial trial tests to validate the test scripts, environments, and monitoring tools.

1. **Test tool** ‒ To conduct the performance testing, select an appropriate load-testing tool, such as JMeter or ghz. Consider the best fit for your business needs in terms of simulating real-world user loads.

1. **Test run** ‒ With the test tools and environments established, run end-to-end performance tests across a range of expected user loads and durations. Throughout the test, closely monitor the health of the system being tested. This is typically a long-running stage. Monitor error rates for automatic test invalidation, and stop the test if there are too many errors.

   The load-testing tool provides insights into resource utilization, response times, and potential bottlenecks.

1. **Test reporting** ‒ Collect the test results along with application and test configuration. Automate collection of application configuration, test configuration, and results, which helps with recording the performance test–related data and storing it centrally. Maintaining performance data centrally helps with providing good insights and supports defining success criteria programmatically for your business.

1. **Clean up** ‒ After you complete a performance test run, reset the test environment and data to prepare for subsequent runs. First, you revert any changes made to the test data during the run. You must restore the databases and other data stores to their original state, reverting any new, updated, or deleted records generated during the test.

You can reuse the pipeline to repeat the test multiple times until the results reflect the performance that you want. You can also use the pipeline to validate that code changes don't break performance. You can run code-validation tests in off-business hours and use the test and observability data available for troubleshooting.

Best practices include the following:
+ Record the start and end time, and automatically generate URLs for logging, monitoring, and tracing systems. This helps you to filter observability data in that appropriate time window.
+ Inject test identifiers in the header while invoking the tests. Application developers can enrich their logging, monitoring, and tracing data by using the identifier as a filter in the backend.
+ Limit the pipeline to only one run at a time. Running concurrent tests generates noise that can cause confusion during troubleshooting. It's also important to run the test in a dedicated performance environment.

## Test-automation tools
<a name="automation-tools"></a>

Testing tools play an important part in any test automation. Popular choices for open source testing tools include the following:
+ [Apache JMeter](https://jmeter.apache.org/) is the seasoned power horse. Over the years, Apache JMeter has become more reliable and has added features. With the graphical interface, you can create complex tests without knowing a programming language. Companies such as BlazeMeter support Apache JMeter.
+ [K6](https://k6.io/) is a free tool that offers support, hosting of the load source, and an integrated web interface to organize, run, and analyze load tests.
+ The [Vegeta](https://github.com/tsenart/vegeta) load test follows a different concept. Instead of defining concurrency or throwing load at your system, you define a certain rate. The tool then creates that load independent of your system's response times.
+ [Hey](https://github.com/rakyll/hey) and [ab](https://httpd.apache.org/docs/2.4/programs/ab.html), the Apache HTTP server bench marking tool, are basic tools that you can use from the command line to run the specified load on a single endpoint. This is the fastest way to generate load if you have a server to run the tools on. Even a local laptop will perform, although it might be not powerful enough to produce high load.
+ [ghz](https://ghz.sh/) is a command line utility and [Go](https://golang.org/) package for load testing and bench marking [gRPC](https://grpc.io) services.

AWS provides the Distributed Load Testing on AWS solution. The solution creates and simulates thousands of connected users generating transactional records at a constant pace without the need to provision servers. For more information, see the [AWS Solutions Library](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/).

You can use AWS CodePipeline to automate the performance testing pipeline. For more information about automating your API testing by using CodePipeline, see the [AWS DevOps Blog](https://aws.amazon.com/blogs/devops/automating-your-api-testing-with-aws-codebuild-aws-codepipeline-and-postman/) and the [AWS documentation](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html).
