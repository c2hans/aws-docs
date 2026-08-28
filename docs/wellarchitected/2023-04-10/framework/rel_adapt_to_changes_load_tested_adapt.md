---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_adapt_to_changes_load_tested_adapt.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL07-BP04 Load test your workload
<a name="rel_adapt_to_changes_load_tested_adapt"></a>

 Adopt a load testing methodology to measure if scaling activity meets workload requirements.

 It’s important to perform sustained load testing. Load tests should discover the breaking point and test the performance of your workload. AWS makes it easy to set up temporary testing environments that model the scale of your production workload. In the cloud, you can create a production-scale test environment on demand, complete your testing, and then decommission the resources. Because you only pay for the test environment when it's running, you can simulate your live environment for a fraction of the cost of testing on premises.

 Load testing in production should also be considered as part of game days where the production system is stressed, during hours of lower customer usage, with all personnel on hand to interpret results and address any problems that arise.

 **Common anti-patterns:**
+  Performing load testing on deployments that are not the same configuration as your production.
+  Performing load testing only on individual pieces of your workload, and not on the entire workload.
+  Performing load testing with a subset of requests and not a representative set of actual requests.
+  Performing load testing to a small safety factor above expected load.

 **Benefits of establishing this best practice:** You know what components in your architecture fail under load and be able to identify what metrics to watch to indicate that you are approaching that load in time to address the problem, preventing the impact of that failure.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Perform load testing to identify which aspect of your workload indicates that you must add or remove capacity. Load testing should have representative traffic similar to what you receive in production. Increase the load while watching the metrics you have instrumented to determine which metric indicates when you must add or remove resources.
  +  [Distributed Load Testing on AWS: simulate thousands of connected users](https://aws.amazon.com/solutions/distributed-load-testing-on-aws/)
    +  Identify the mix of requests. You may have varied mixes of requests, so you should look at various time frames when identifying the mix of traffic.
    +  Implement a load driver. You can use custom code, open source, or commercial software to implement a load driver.
    +  Load test initially using small capacity. You see some immediate effects by driving load onto a lesser capacity, possibly as small as one instance or container.
    +  Load test against larger capacity. The effects will be different on a distributed load, so you must test against as close to a product environment as possible.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Distributed Load Testing on AWS: simulate thousands of connected users](https://aws.amazon.com/solutions/distributed-load-testing-on-aws/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
