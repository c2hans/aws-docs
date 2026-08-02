---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_testing_resiliency_test_non_functional.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL12-BP04 Test scaling and performance requirements
<a name="rel_testing_resiliency_test_non_functional"></a>

 Use techniques such as load testing to validate that the workload meets scaling and performance requirements.

 In the cloud, you can create a production-scale test environment on demand for your workload. If you run these tests on scaled down infrastructure, you must scale your observed results to what you think will happen in production. Load and performance testing can also be done in production if you are careful not to impact actual users, and tag your test data so it does not comingle with real user data and corrupt usage statistics or production reports.

 With testing, ensure that your base resources, scaling settings, service quotas, and resiliency design operate as expected under load.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Test scaling and performance requirements. Perform load testing to validate that the workload meets scaling and performance requirements.
  +  [Distributed Load Testing on AWS: simulate thousands of connected users](https://aws.amazon.com/solutions/distributed-load-testing-on-aws/)
  +  [Apache JMeter](https://github.com/apache/jmeter?ref=wellarchitected)
    +  Deploy your application in an environment identical to your production environment and run a load test.
      +  Use infrastructure as code concepts to create an environment as similar to your production environment as possible.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Distributed Load Testing on AWS: simulate thousands of connected users](https://aws.amazon.com/solutions/distributed-load-testing-on-aws/)
+  [Apache JMeter](https://github.com/apache/jmeter?ref=wellarchitected)
