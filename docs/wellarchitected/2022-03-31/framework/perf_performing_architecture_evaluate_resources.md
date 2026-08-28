---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_performing_architecture_evaluate_resources.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF01-BP01 Understand the available services and resources
<a name="perf_performing_architecture_evaluate_resources"></a>

 Learn about and understand the wide range of services and resources available in the cloud. Identify the relevant services and configuration options for your workload, and understand how to achieve optimal performance.

 If you are evaluating an existing workload, you must generate an inventory of the various services resources it consumes. Your inventory helps you evaluate which components can be replaced with managed services and newer technologies.

 **Common anti-patterns:**
+  You use the cloud as a collocated data center.
+  You use shared storage for all things that need persistent storage.
+  You do not use automatic scaling.
+  You use instance types that are closest matched, but larger where needed, to your current standards.
+  You deploy and manage technologies that are available as managed services.

 **Benefits of establishing this best practice:** By considering services you may be unfamiliar with, you may be able to greatly reduce the cost of infrastructure and the effort required to maintain your services. You may be able to accelerate your time to market by deploying new services and features.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="perf01-bp01-implementation-guidance"></a>

 Inventory your workload software and architecture for related services: Gather an inventory of your workload and decide which category of products to learn more about. Identify workload components that can be replaced with managed services to increase performance and reduce operational complexity.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Architecture Center](https://aws.amazon.com/architecture/)
+  [AWS Partner Network](https://aws.amazon.com/partners/)
+  [AWS Solutions Library](https://aws.amazon.com/solutions/)
+  [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/)

 **Related videos:**
+  [Introducing The Amazon Builders’ Library (DOP328)](https://www.youtube.com/watch?v=sKRdemSirDM)
+  [This is my Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)

 **Related examples:**
+  [AWS Samples](https://github.com/aws-samples)
+  [AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
