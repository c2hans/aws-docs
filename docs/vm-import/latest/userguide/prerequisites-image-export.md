---
source_url: https://docs.aws.amazon.com/vm-import/latest/userguide/prerequisites-image-export.html
---

# Prerequisites for exporting an image from Amazon EC2
<a name="prerequisites-image-export"></a>

To export a VM from Amazon EC2, first meet the following prerequisites.
+ Install the AWS CLI. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).
**Tip**
In [supported AWS Regions](https://docs.aws.amazon.com/cloudshell/latest/userguide/supported-aws-regions.html), you can also use [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) for a browser-based, pre-authenticated shell that launches directly from the AWS Management Console.
+ Create an Amazon Simple Storage Service (Amazon S3) bucket for storing the exported images or choose an existing bucket. The bucket must be in the Region where you want to export your VMs. Additionally, the bucket must belong to the AWS account where you are performing the export operation. For more information about S3 buckets, see the [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).
+ Create an IAM role named `vmimport`. For more information, see [Required service role](required-permissions.md#vmimport-role).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vm-import` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
