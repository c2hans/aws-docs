---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

## AWS services in this solution
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [AWS Elemental MediaLive](https://aws.amazon.com/elemental-live/)  |  **Core.** Ingests an input feed and transcodes your content into one adaptive bitrate (ABR) HTTP Live Streaming (HLS) stream as output. |
|  [Amazon S3](https://aws.amazon.com/s3)  |  **Core.** Provides storage to host the encoded segments. |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Core.** Delivers your live stream to viewers with low latency and high transfer speeds. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Supporting.** Monitors S3 requests made to the distribution bucket. |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  |  **Supporting.** This solution is distributed as a [CloudFormation template and stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html), which deploy the AWS resources for the solution. |
|  [AWS IAM](https://aws.amazon.com/iam/)  |  **Supporting.** Allows for fine-grained access permissions. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting.** Provides application-level resource monitoring and visualization of resource operations and cost data. |
|  [AWS Elemental Link](https://aws.amazon.com/medialive/features/link/)  |  **Optional.** Device to connect a video source on-premises to MediaLive. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Live Streaming on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
