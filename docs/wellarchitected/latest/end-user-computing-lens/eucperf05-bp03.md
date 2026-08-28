---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp03.html
---

# EUCPERF05-BP03 Understand integrated storage capabilities (WorkSpaces)
<a name="eucperf05-bp03"></a>

 Most existing workloads, either physical or virtual, will make use of integrated storage that provides the system drive and data drives. For virtualized desktops and servers, this will be virtual drives created from hyperconverged storage. Some workloads, if not already virtualized, may also have fast boot and data drives (like SSD or NVMe) or additional integrated storage in the form of internal hard drives or externally-connected hard drives that deliver large or faster storage for specific applications.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance-12"></a>

 If any of the workloads you are migrating to AWS EUC services have been configured with and require high performance or additional high-density storage, carefully review the AWS instance types that provide higher performance storage. The Graphics G4 instance types offer a local NVMe instance store which may meet your requirements.

 This may also be an opportunity to review alternate networked AWS Storage solutions as they might provide the speed and density you require.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
