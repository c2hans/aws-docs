---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/security-vpc.html
---

# Securing your Amazon Neptune database with Amazon VPC
<a name="security-vpc"></a>

An Amazon Neptune DB cluster can *only* be created in an Amazon Virtual Private Cloud (Amazon VPC), and its endpoints are accessible within that VPC, usually from an Amazon Elastic Compute Cloud (Amazon EC2) instance running in that VPC. Alternatively, it can be accessed using a public endpoint. For more information on public endpoints, see [Neptune public endpoints](neptune-public-endpoints.md).

You can secure your Neptune data by limiting access to the VPC where your Neptune DB cluster is located, as described in [Connecting to an Amazon Neptune cluster](get-started-connecting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
