---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).

The Live Streaming on AWS with Amazon S3 solution tracks all assets via AWS CloudTrail. Logs from Medialive, Amazon S3, and Amazon CloudFront provide observability into the infrastructure and the rest of the solution components.

## Security
<a name="security1"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).

To help reduce latency and improve security, Live Streaming on AWS with Amazon S3 includes an Amazon CloudFront distribution with an origin access identity, which is a special CloudFront user that helps restrict access to the solution’s website bucket contents.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

The solution supports AWS Elemental Link, which offers a configuration-free, cost-efficient way to securely and reliably transfer video to MediaLive.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).

This solution uses MediaLive, which is currently available in specific AWS Regions only. To use an AWS Elemental Link device as an input, you must launch this solution in the AWS Region where the device is configured.

The solution is automatically tested and reviewed by solutions architects and subject matter experts for areas to experiment and improve.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).

The cost for running the solution varies based on a number of factors, including the encoded profile selected, the bitrate of the live stream, and the number of viewers.

Customers can measure the efficiency of the workloads, and the costs associated with delivery, by using Application Manager.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).

Live Streaming on AWS with Amazon S3 uses managed and serverless services, to minimize the environmental impact of the backend services. Customers can run this solution only during the live event and delete the stack after the program ends, reducing the carbon footprint compared to the footprint of continually operating on-premises servers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Live Streaming on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
