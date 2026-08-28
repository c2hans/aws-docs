---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/physical-isolation.html
---

# Isolation on Physical Hosts
<a name="physical-isolation"></a>

Different streaming instances on the same physical host are isolated from each other as though they are on separate physical hosts. The hypervisor isolates CPU and memory, and the instances are provided virtualized disks instead of access to the raw disk devices.

When you stop or terminate a streaming instance, the memory allocated to it is scrubbed (meaning, it's set to zero) by the hypervisor before it is allocated to a new instance, and every block of storage is reset. This ensures that your data is not exposed to another instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
