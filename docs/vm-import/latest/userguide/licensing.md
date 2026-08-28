---
source_url: https://docs.aws.amazon.com/vm-import/latest/userguide/licensing.html
---

# Licensing for your imported VMs
<a name="licensing"></a>

When you create a new VM Import task, you have two options for how to specify the license type for the operating system. You can specify a value for either the `--license-type` or the `--usage-operation` parameter. Specifying a value for both parameters will return an error. You can use `--usage-operation` to blend your operating system and SQL Server licenses.

**Important**
AWS VM Import/Export strongly recommends specifying a value for either the `--license-type` or `--usage-operation` parameter when you create a new VM Import task. This ensures your operating system is licensed appropriately and your billing is optimized. If you choose a license type that is incompatible with your VM, the VM Import task fails with an error message. For more information, see [Specify a licensing option for your import](licensing-specify-option.md).

**Topics**
+ [Licensing considerations](licensing-considerations.md)
+ [Specify a licensing option for your import](licensing-specify-option.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vm-import` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
