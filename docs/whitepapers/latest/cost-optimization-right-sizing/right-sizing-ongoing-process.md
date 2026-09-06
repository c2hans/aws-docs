---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/right-sizing-ongoing-process.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Right Sizing is an Ongoing Process
<a name="right-sizing-ongoing-process"></a>

 To achieve cost optimization, right sizing must become an ongoing process within your organization. It’s important to right size when you first consider moving to the cloud and calculate total cost of ownership. However, it’s equally important to right size periodically once you’re in the cloud to ensure ongoing cost-performance optimization.

 Why is it necessary to right size continually? Even if you right size workloads initially, performance and capacity requirements can change over time, which can result in underused or idle resources. Additionally, new projects and workloads require additional cloud resources, and overprovisioning is the likely outcome if there is no process in place to support right sizing and other cost-optimization efforts.

 You should right size your workloads at least once a month to control costs. You can make right sizing a smooth process by:
+  Having each team set up a right-sizing schedule and then report the savings to management.
+  Monitoring costs closely using AWS cost and reporting tools, such as [Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-explorer-what-is.html), [budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html), and [Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) in the Billing and Cost Management console.
+  Enforcing tagging for all instances so that you can quickly identify attributes such as the instance owner, application, and environment (development, testing, or production).
+  Understanding how to right size.

 We first describe the types of instances that AWS offers and then discuss key considerations for right sizing your instances.
