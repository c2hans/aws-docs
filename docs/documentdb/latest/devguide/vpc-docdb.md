---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/vpc-docdb.html
---

# Amazon VPC and Amazon DocumentDB
<a name="vpc-docdb"></a>

Amazon Virtual Private Cloud (Amazon VPC) makes it possible for you to launch AWS resources, such as Amazon DocumentDB instances, into a virtual private cloud (VPC).

When you use a VPC, you have control over your virtual networking environment. You can choose your own IP address range, create subnets, and configure routing and access control lists. There is no additional cost to run your cluster in a VPC.

Accounts have a default VPC. All new clusters are created in the default VPC unless you specify otherwise.

**Topics**
+ [DocumentDB clusters in a VPC](vpc-clusters.md)
+ [Accessing an Amazon DocumentDB cluster in a VPC](access-cluster-vpc.md)
+ [Create an IPv4-only VPC for use with a DocumentDB cluster](docdb-vpc-create-ipv4.md)
+ [Create a dual-stack VPC for use with a DocumentDB cluster](docdb-vpc-create-dual-stack.md)

Following, you can find a discussion about VPC functionality relevant to Amazon DocumentDB clusters. For more information about Amazon VPC, see the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
