---
source_url: https://docs.aws.amazon.com/vm-import/latest/userguide/instance-import.html
---

# Instance import overview
<a name="instance-import"></a>

First, you'll need to prepare your virtual machine for export, and then export it using one of the supported formats. Next, you'll need to upload the VM image to Amazon S3, and then start the instance import task. After the import task is complete, you can create an AMI from the stopped instance. If you want, you can copy the AMI to other Regions so that you can launch instances in those Regions. You can also export a previously imported instance to your virtualization environment.

The following diagram shows the process of exporting a VM from your virtualization environment to Amazon EC2 as an instance.

![VM Import/Export instance import](http://docs.aws.amazon.com/vm-import/latest/userguide/images/vmimport-export-architecture-ami-copy.png)

Before you proceed with this process, see [VM Import/Export Requirements](vmie_prereqs.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vm-import` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
