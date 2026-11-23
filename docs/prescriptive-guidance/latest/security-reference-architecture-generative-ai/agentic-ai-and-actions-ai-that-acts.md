---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/agentic-ai-and-actions-ai-that-acts.html
---

# Agentic AI and actions (AI that acts)

An agent uses a model to choose tools or steps to run. Constrain what it can read, run, or change through permissions and runtime controls.

Apply [model inference](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=model-inference), [application access](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=ai-application-access), and [retrieval](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=data-and-retrieval) controls. The framework places agent tool use, Model Context Protocol (MCP) tools, and Agent-to-Agent (A2A) interactions under **AI that acts**, including when the permitted operations are read-only.

![AWS SRA of AI Security AWS OU and account structure with AWS service reference - Agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/8cf62bc7-ac45-4921-ab1d-5e2b27a97328.png)

***Fig 5:*** ***AWS SRA of AI Security AWS OU and account structure with AWS service reference - Agentic AI***

## Choose controls by the tools' effects
<a name="choose-controls-by-the-tools-effects"></a>

**A read-only agent** can search documents or query systems. Apply [read-only tool access](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=read-only-tool-access) and the execution controls below.

**An agent with action permissions** can change records, run code, initiate transactions, or control a device. Apply [agent execution and action-capable tools](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=agent-execution-and-actions), including authorization outside the model, approval where consequences warrant it, and recovery from partial failures. Requiring human approval does not turn a write-capable tool into a read-only tool. For an example of how to implement human approval, see the AWS blog post [Human-in-the-loop constructs for agentic workflows in healthcare and life sciences](https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-constructs-for-agentic-workflows-in-healthcare-and-life-sciences/)**.**

Review tool authorization and execution boundaries in the [action-capable workload reference diagram](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=agent-execution-and-actions).

## Security considerations
<a name="security-considerations"></a>
+ Injected instructions can misuse otherwise valid tool permissions.
+ Reused sessions or delegated credentials can expose another user's data and authority.
+ Repeated calls, retries, and resumed tasks can exceed spending or operational limits.
+ Self-approval, altered requests, or duplicate runs can cause unauthorized actions.

## Design considerations
<a name="design-considerations"></a>
+ Distinguish a proposed action, an authorization decision, and a completed downstream effect in the investigation record.
+ A shared runtime approval reduces repeated infrastructure review; it does not approve every new agent's tools, data access, or business consequences.
