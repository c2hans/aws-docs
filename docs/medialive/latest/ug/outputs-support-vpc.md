---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/outputs-support-vpc.html
---

# Support for delivery in VPC
<a name="outputs-support-vpc"></a>

The following table specifies which MediaLive containers can be delivered to a destination in the VPC, when the channel that is set up for VPC delivery. For more information about VPC delivery, see [Delivering outputs via your VPC](delivery-out-vpc.md).

| MediaLive output type (output group) | Can be delivered to a destination in your VPC | Can be delivered to a destination outside your VPC |
| --- | --- | --- |
| Archive | A bucket, if Amazon S3 is set up with a VPC endpoint | Yes, if you associate Elastic IP addresses with the channel |
| CMAF Ingest | A server on Amazon EC2 | Yes, if you associate Elastic IP addresses with the channel |
| Frame Capture | A bucket, if Amazon S3 is set up with a VPC endpoint | Yes, if you associate Elastic IP addresses with the channel |
| HLS to an HTTP or HTTPS server | A bucket, if Amazon S3 is set up with a VPC endpoint | Yes, if you associate Elastic IP addresses with the channel |
| HLS to an Akamai server | A bucket, if Amazon S3 is set up with a VPC endpoint | Yes, if you associate Elastic IP addresses with the channel |
| HLS to MediaPackage, over HTTP | No | Yes, if you associate Elastic IP addresses with the channel |
| HLS to MediaStore | No | Yes, if you associate Elastic IP addresses with the channel |
| HLS to Amazon S3 | A bucket, if Amazon S3 is set up with a VPC endpoint | Yes, if you associate Elastic IP addresses with the channel |
| MediaConnect Router | Yes. MediaConnect Router output always delivers within a VPC. | No |
| MediaPackage | No | Yes, if you associate Elastic IP addresses with the channel |
| Microsoft Smooth | A server on Amazon EC2 | Yes, if you associate Elastic IP addresses with the channel |
| Multiplex | NoWhen the channel is set up for VPC delivery, it can't contain a multiplex output. | NoWhen the channel is set up for VPC delivery, it can't contain a multiplex output. |
| RTMP or RTMPS | A server on Amazon EC2 | Yes, if you associate Elastic IP addresses with the channel |
| SRT | With a specified IP address (caller mode) or allocated IP addresses (listener mode) | Yes, if you associate Elastic IP addresses with the channel |
| UDP | A server on Amazon EC2 | Yes, if you associate Elastic IP addresses with the channel |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
