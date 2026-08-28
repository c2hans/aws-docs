---
source_url: https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-on-premises.html
---

# Using Amazon FSx with your on-premises data
<a name="fsx-on-premises"></a>

You can use FSx for Lustre to process your on-premises data with in-cloud compute instances. FSx for Lustre supports access over Direct Connect and VPN, enabling you to mount your file systems from on-premises clients.

**To use FSx for Lustre with your on-premises data**

1. Create a file system. For more information, see [Step 1: Create your FSx for Lustre file system](getting-started.md#getting-started-step1) in the getting started exercise.

1. Mount the file system from on-premises clients. For more information, see [Mounting Amazon FSx file systems from on-premises or a peered Amazon VPC](mounting-on-premises.md).

1. Copy the data that you want to process into your FSx for Lustre file system.

1. Run your compute-intensive workload on in-cloud Amazon EC2 instances mounting your file system.

1. When you're finished, copy the final results from your file system back to your on-premises data location, and delete your FSx for Lustre file system.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
