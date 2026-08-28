---
source_url: https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent-learned-skills.html
---

# Learned Skills
<a name="about-aws-devops-agent-learned-skills"></a>

Learned skills are the knowledge that AWS DevOps Agent builds about your environment as it works—your topology, code dependencies, pipeline structure, and tool-use patterns. Four learned skills are available: Agent Space Understanding, Understanding Code Dependencies, Understanding Pipeline Topology, and Tool Use Best Practices.

**Important**
Learned skills are moving to memory. ** AWS DevOps Agent now maintains your learned skills as memory. You don't need to do anything—the move happens automatically the next time AWS DevOps Agent refreshes each learned skill. During the move, the console keeps showing a learned skill on the ** Skills ** tab until its memory is ready, and then points you to its new home on the ** Memories ** tab. After the move, you view and manage your learned skills on the ** Memories ** tab of the ** Knowledge ** page.

For what each learned skill contains, and for how AWS DevOps Agent builds and refreshes them, see [DevOps Agent Memories](about-aws-devops-agent-devops-agent-memories.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
