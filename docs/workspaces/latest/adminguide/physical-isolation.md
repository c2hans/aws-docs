---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/physical-isolation.html
---

# Isolation on physical hosts
<a name="physical-isolation"></a>

Different WorkSpaces on the same physical host are isolated from each other through the hypervisor. It is as though they are on separate physical hosts. When a WorkSpace is deleted, the memory allocated to it is scrubbed (set to zero) by the hypervisor before it is allocated to a new WorkSpace.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
