---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html
---

# Using Amazon Linux 2023 outside of Amazon EC2
<a name="outside-ec2"></a>

 The Amazon Linux 2023 container images can be run in compatible container runtime environments. For more information on how to use Amazon Linux 2023 inside a container, see [AL2023 in containers](container.md).

 Amazon Linux 2023 (AL2023) can also be run as a virtualized guest outside of directly being run on Amazon EC2. There are currently KVM (`qcow2`), VMware (`OVA`), and Hyper-V (`vhdx`) images available.

**Note**
 The configuration of Amazon Linux 2023 images differs from Amazon Linux 2.
 If you are coming from [ Running Amazon Linux 2 as a virtual machine on premises ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-2-virtual-machine.html) you will need to adapt your configuration to be compatible with AL2023.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
