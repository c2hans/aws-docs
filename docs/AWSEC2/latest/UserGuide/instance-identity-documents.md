---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html
---

# Instance identity documents for Amazon EC2 instances
<a name="instance-identity-documents"></a>

Each instance that you launch has an instance identity document that provides information about the instance itself. You can use the instance identity document to validate the attributes of the instance.

The instance identity document is generated when the instance is stopped and started, restarted, or launched. You can access the instance identity document for an instance through the Instance Metadata Service (IMDS). For the instructions, see [Retrieve the instance identity document](retrieve-iid.md).

The instance identity document uses plaintext JSON format. It includes the following information.

| Data | Description |
| --- | --- |
| accountId | The ID of the AWS account that launched the instance. |
| architecture | The architecture of the AMI used to launch the instance (i386 \| x86\_64 \| arm64). |
| availabilityZone | The name of the Availability Zone in which the instance is running. For example, `us-east-1`. Keep in mind that Availability Zone names might differ across AWS accounts. |
| billingProducts | The billing products of the instance. |
| devpayProductCodes | Deprecated. |
| imageId | The ID of the AMI used to launch the instance. |
| instanceId | The ID of the instance. |
| instanceType | The instance type of the instance. |
| kernelId | The ID of the kernel associated with the instance, if applicable. |
| marketplaceProductCodes | The AWS Marketplace product code of the AMI used to launch the instance. |
| pendingTime | The date and time that the instance was launched. |
| privateIp | The private IP address of the instance. For IPv4-only and dual-stack instances, this contains the IPv4 address. For IPv6-only instances, this contains the IPv6 address. |
| ramdiskId | The ID of the RAM disk associated with the instance, if applicable. |
| region | The Region in which the instance is running. |
| version | The version of the instance identity document format. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
