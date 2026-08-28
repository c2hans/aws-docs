---
source_url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/increasing-mtbf.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Increasing MTBF
<a name="increasing-mtbf"></a>

 The final component to improving availability is increasing the MTBF. This can apply to both the software as well as the AWS services used to run it.

## Increasing distributed system MTBF
<a name="increasing-distributed-system-mtbf"></a>

 One way to increase MTBF is to reduce defects in the software. There are several ways to do this. Customers can use tools like [Amazon CodeGuru Reviewer](https://aws.amazon.com/codeguru/) to find and remediate common errors. You should also perform comprehensive peer code reviews, unit tests, integration tests, regression tests, and load tests on software before it is deployed to production. Increasing the amount of code coverage in tests will help ensure that even uncommon code execution paths are tested.

 Deploying smaller changes can also help prevent unexpected outcomes by reducing the complexity of change. Each activity provides an opportunity to identify and fix defects before they can ever be invoked.

 Another approach to preventing failure is [regular testing](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/test-reliability.html). Implementing a chaos engineering program can help test how your workload fails, validate recovery procedures, and help find and fix failure modes before they occur in production. Customers can use [AWS Fault Injection Simulator](https://aws.amazon.com/fis/) as part of their chaos engineering experiment toolset.

 Fault tolerance is another way to prevent failure in a distributed system. Fail-fast modules, retries with exponential backoff and jitter, transactions, and idempotency are all techniques to help make workloads fault tolerant.

 Transactions are a group of operations that adhere to the ACID properties. They are as follows:
+  **Atomicity** – Either all of the actions happen or none of them will happen.
+  **Consistency** – Each transaction leaves the workload in a valid state.
+  **Isolation** – Transactions performed concurrently leave the workload in the same state as if they had been performed sequentially.
+  **Durability** – Once a transaction commits, all of its effects are preserved even in the case of workload failure.

 Retries with [exponential backoff and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) allow you to overcome transient failures caused by Heisenbugs, overload, or other conditions. When transactions are idempotent, they can be retried multiple times without side effects.

 If we consider the effect of a Heisenbug on a fault-tolerant hardware configuration, we'd be fairly unconcerned since the probability of the Heisenbug appearing on both the primary and redundant subsystem is infinitesimally small. (See Jim Gray, "[Why Do Computers Stop and What Can Be Done About It?](https://pages.cs.wisc.edu/~remzi/Classes/739/Fall2018/Papers/gray85-easy.pdf)", June 1985, Tandem Technical Report 85.7.) In distributed systems, we want to achieve the same outcomes with our software.

 When a Heisenbug is invoked, it's imperative that the software quickly detects the incorrect operation and fails so that it can be tried again. This is achieved through defensive programming, and validating inputs, intermediate results, and output. Additionally, processes are isolated and share no state with other processes.

 This modular approach ensures that the scope of impact during failure is limited. Processes fail independently. When a process does fail, the software should use “process-pairs” to retry the work, meaning a new process can assume the work of a failed one. To maintain the reliability and integrity of the workload, each operation should be treated as an ACID transaction.

 This allows a process to fail without corrupting the state of the workload by aborting the transaction and rolling back any changes made. This allows the recovery process to retry the transaction from a known-good state and restart gracefully. This is how software can be fault-tolerant to Heisenbugs.

 However, you should not aim to make software fault-tolerant to Bohrbugs. These defects must be found and removed before the workload enters production since no level of redundancy will ever achieve correct outcome. (See Jim Gray, "[Why Do Computers Stop and What Can Be Done About It?](https://www.hpl.hp.com/techreports/tandem/TR-85.7.pdf)", June 1985, Tandem Technical Report 85.7.)

 The final way to increase MTBF is to reduce the scope of impact from failure. Using [fault isolation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/use-fault-isolation-to-protect-your-workload.html) through modularization to create fault containers is a primary way to do so as outlined earlier in *Fault tolerance and fault isolation*. Reducing the failure rate improves availability. AWS uses techniques like dividing services into control planes and data planes, [Availability Zone Independence](https://aws.amazon.com/builders-library/static-stability-using-availability-zones) (AZI), [Regional isolation](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), [cell-based architectures](https://www.youtube.com/watch?v=swQbA4zub20), and [shuffle-sharding](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding) to provide fault isolation. These are also patterns that can be used by AWS customers as well.

 For example, let's review a scenario where a workload placed customers into different fault containers of its infrastructure that serviced at most 5% of the total customers. One of these fault containers experiences an event that increased latency beyond the client timeout for 10% of requests. During this event, for 95% of customers, the service was 100% available. For the other 5%, the service appeared to be 90% available. This results in an availability of 1 − (5% *o**f* *c**u**s**t**o**m**e**r**s*×10% *o**f* *t**h**e**i**r* *r**e**q**u**e**s**t**s*) = 99.5% instead of 10% of requests failing for 100% of customers (resulting in a 90% availability).

**Rule 11**
Fault isolation decreases scope of impact and increases the MTBF of the workload by reducing the overall failure rate.

## Increasing Dependency MTBF
<a name="increasing-dependency-mtbf"></a>

 The first method to increase your AWS dependency MTBF is through using [fault isolation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/use-fault-isolation-to-protect-your-workload.html). Many AWS services offer a level of isolation at the AZ, meaning a failure in one AZ does not affect the service in a different AZ.

 Using redundant EC2 instances in multiple AZs increases subsystem availability. AZI provides a sparing capability inside a single Region, allowing you to increase your availability for AZI services.

 However, not all AWS services operate at the AZ level. Many others offer regional isolation. In this case, where the designed-for availability of the regional service doesn't support the overall availability required for your workload, you might consider a multi-Region approach. Each Region offers an isolated instantiation of the service, equivalent to sparing.

 There are various services that help make building a multi-Region service easier. For example:
+  [Amazon Aurora Global Database](https://aws.amazon.com/rds/aurora/global-database/)
+  [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/global-tables/)
+  [Amazon ElastiCache (Redis OSS) – Global Datastore](https://aws.amazon.com/elasticache/redis/global-datastore/)
+  [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/)
+  [Amazon S3 Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
+  [Amazon Route 53 Application Recovery Controller](https://aws.amazon.com/route53/application-recovery-controller/)

 This document doesn't delve into the strategies of building multi-Region workloads, but you should weigh the availability benefits of multi-Region architectures with the additional cost, complexity, and operational practices they require to meet your desired availability goals.

 The next method to increase dependency MTBF is by designing your workload to be statically stable. For example, you have a workload that serves product information. When your customers make a request for a product, your service makes a request to an external metadata service to retrieve product details. Then your workload returns all of that info to the user.

 However, if the metadata service is unavailable, the requests made by your customers fail. Instead, you can asynchronously pull or push the metadata locally to your service to be used to answer requests. This eliminates the synchronous call to the metadata service from your critical path.

 Additionally, because your service is still available even when the metadata service is not, you can remove it as a dependency in your availability calculation. This example is dependent on the assumption that the metadata doesn’t change frequently and that serving stale metadata is better than the request failing. Another similar example is [serve-stale](https://www.rfc-editor.org/rfc/rfc8767) for DNS that allows data to be kept in the cache beyond the TTL expiry and used for responses when a refreshed answer is not readily available.

 The final method to increase dependency MTBF is to reduce the scope of impact from failure. As discussed earlier, failure is not a binary event, there are degrees of failure. This is the effect of modularization; failure is contained to just the requests or users being serviced by that container.

 This results in fewer failures during an event which ultimately increases availability of the overall workload by limiting the scope of impact.

## Reducing common sources of impact
<a name="reducing-common-sources-of-impact"></a>

 In 1985, Jim Gray discovered, during a study at Tandem Computers, that failure was primarily driven by two things: software and operations. (See Jim Gray, "[Why Do Computers Stop and What Can Be Done About It?](https://www.hpl.hp.com/techreports/tandem/TR-85.7.pdf)", June 1985, Tandem Technical Report 85.7.) Even after 36 years later, this continues to be true. Despite advances in technology, there isn't an easy solution to these problems, and the major sources of failure haven't changed. Addressing failures in software was discussed in the beginning of this section, so the focus here will be operations and reducing the frequency of failure.

### Stability compared with features
<a name="stability-compared-with-features"></a>

 If we refer back to the failure rates for software and hardware graph in the section [Distributed system availability](distributed-system-availability.md), we can notice that defects are added in each software release. This means that any change to the workload introduces increased risk of failure. These changes are typically things like new features, which provides a corollary. Higher availability workloads will favor stability over new features. Thus, one of the simplest ways to improve availability is to deploy less often or deliver fewer features. Workloads that deploy more frequently will inherently have a lower availability than those that do not. However, workloads that fail to add features do not keep up with customer demand and can become less useful over time.

 So, how do we continue to innovate and release features safely? The answer is standardization. What is the correct way to deploy? How do you order deployments? What are the standards for testing? How long do you wait between stages? Do your unit tests cover enough of the software code? These are questions that standardization will answer and prevent issues caused by things like not load testing, skipping deployment stages, or deploying too quickly to too many hosts.

 The way that you implement standardization is through automation. It reduces the chance of human mistakes and lets computers do the thing they're good at, which is doing the same thing over and over the same way every time. The way you stick standardization and automation together is to set goals. Goals like no manual changes, host access only through contingent authorization systems, writing load tests for every API, and so on. Operational excellence is a cultural norm that can require substantial change. Establishing and tracking performance against a goal helps drive cultural change that will have a broad impact on workload availability. The [AWS Well-Architected Operational Excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) provides comprehensive best practices for operational excellence.

### Operator safety
<a name="operator-safety"></a>

 The other major contributor to operational events that introduce failure are people. Humans make mistakes. They might use the wrong credentials, enter the wrong command, press Enter too soon, or miss a critical step. Taking manual action consistently results in error, resulting in failure.

 One of the major causes for operator errors are confusing, unintuitive, or inconsistent user interfaces. Jim Gray also noted in his 1985 study that “interfaces that ask the operator for information or ask him to perform some function must be simple, consistent, and operator fault-tolerant.” (See Jim Gray, "[Why Do Computers Stop and What Can Be Done About It?](https://www.hpl.hp.com/techreports/tandem/TR-85.7.pdf)", June 1985, Tandem Technical Report 85.7.) This insight continues to be true today. There are numerous examples over the past three decades throughout the industry where a confusing or complex user interface, lack of confirmation or instructions, or even just unfriendly human language caused an operator to do the wrong thing.

**Rule 12**
Make it easy for operators to do the right thing.

### Preventing overload
<a name="preventing-overload"></a>

 The final common contributor of impact is your customers, the actual users of your workload. Successful workloads tend to get used, a lot, but sometimes that usage outpaces the workload’s ability to scale. There are many things that can happen, disks can become full, thread pools might get exhausted, network bandwidth might be saturated, or database connection limits can be reached.

 There is no failproof method to eliminate these, but proactive monitoring of capacity and utilization through Operational Health metrics will provide early warnings when these failures might occur. Techniques like [load-shedding](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload), [circuit breakers](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-interactions-in-a-distributed-system-to-mitigate-or-withstand-failures.html), and [retry with exponential backoff and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) can help minimize the impact and increase the success rate, but these situations still represent failure. Automated scaling based on Operational Health metrics can help reduce the frequency of failure due to overload, but might not be able to respond quickly enough to changes in utilization.

 If you need to ensure the continuously available capacity for customers, you have to make tradeoffs on availability and cost. One way to ensure lack of capacity doesn’t lead to unavailability is to provide each customer with a quota and ensure your workload’s capacity is scaled to provide 100% of the allocated quotas. When customers exceed their quota, they get throttled, which isn't a failure and doesn’t count against availability. You will also need to closely track your customer base and forecast future utilization to keep enough capacity provisioned. This ensures your workload isn't driven to failure scenarios through over consumption by your customers.
+  [Amazon Builders' Library – Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/)
+  [Amazon Builders' Library – Fairness in multi-tenant systems](https://aws.amazon.com/builders-library/fairness-in-multi-tenant-systems)

For example, let’s examine a workload that provides a storage service. Each server in the workload can support 100 downloads per second, customers are provided a quota or 200 downloads per second, and there are 500 customers. To be able to support this volume of customers, the service needs to provide capacity for 100,000 downloads per second, which requires 1,000 servers. If any customer exceeds their quota, they get throttled, which ensures sufficient capacity for every other customer. This is a simple example of one way to avoid overload without rejecting units of work.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
