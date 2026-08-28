---
source_url: https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html
---

# Import a VM to Amazon EC2 as an image using VM Import/Export
<a name="vmimport-image-import"></a>

**Tip**
To import your virtual machines (VMs) with a console-based experience, you can use the *Import virtual machine images to AWS* template in the [Migration Hub Orchestrator console](https://console.aws.amazon.com/migrationhub/orchestrator). For more information, see the [*AWS Migration Hub Orchestrator User Guide*](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/import-vm-images.html).

You can use VM Import/Export to import virtual machine (VM) images from your virtualization environment to Amazon EC2 as Amazon Machine Images (AMI), which you can use to launch instances. Subsequently, you can export the VM images from an instance back to your virtualization environment. This enables you to leverage your investments in the VMs that you have built to meet your IT security, configuration management, and compliance requirements by bringing them into Amazon EC2.

**Topics**
+ [Export your VM from its virtualization environment](export-vm-image.md)
+ [Programmatic modifications made to VMs by VM Import/Export](import-modify-vm.md)
+ [Import your VM as an image](import-vm-image.md)
+ [Monitor an import image task](check-import-task-status.md)
+ [Cancel an import image task](cancel-upload.md)
+ [Create an EC2 instance from an imported image](import-vm-next-steps.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vm-import` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
