---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec05.html
---

# Excessive agency
<a name="gensec05"></a>

| GENSEC05: How do you avoid excessive agency for models? |
| --- |
|   |

 Excessive agency is an Open Worldwide Application Security Project (OWASP) Top 10 security threat for LLMs and is typically introduced to systems through agentic architectures. Agents are designed to take action on behalf of a user. The risk of excessive agency is that an agent could take actions beyond their intended purpose.

**Topics**
+ [GENSEC05-BP01 Implement least privilege access and permissions boundaries for agentic workflows](gensec05-bp01.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
