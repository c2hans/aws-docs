---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/selinux.html
---

# SELinux
<a name="selinux"></a>

By default, Security Enhanced Linux (SELinux) for AL2023 is `enabled` and set to `permissive` mode. In `permissive` mode, permission denials are logged but not enforced.

SELinux is a security feature of the Amazon Linux kernel, which was `disabled` in AL2. SELinux is a collection of kernel features and utilities that provides mandatory access control (MAC) architecture into the major subsystems of the kernel.

For more information, see [Setting SELinux modes for AL2023](selinux-modes.md).

For more information about SELinux repositories, tools, and policies, see [SELinux Notebook](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/toc.md), [Types of SELinux policy](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/types_of_policy.md#types-of-selinux-policy), and [SELinux Project ](https://github.com/SELinuxProject.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
