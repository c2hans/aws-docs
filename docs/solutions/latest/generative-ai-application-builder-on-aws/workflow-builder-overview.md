---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/workflow-builder-overview.html
---

# Workflow Builder
<a name="workflow-builder-overview"></a>

Workflow Builder enables multi-agent orchestration by creating a supervisor agent that delegates work to specialized Agent Builder agents. Each workflow consists of:
+  **Supervisor Agent**: The entrypoint agent that receives user requests and coordinates specialized agents
+  **Specialized Agents**: Agent Builder use cases that the supervisor can delegate tasks to
+  **Agents as Tools Pattern**: The supervisor registers each Agent Builder agent as a tool and autonomously selects which agents to use

| Feature | Agent Builder | Workflow Builder |
| --- | --- | --- |
|  **Purpose**  | Build and deploy single custom agents | Orchestrate multiple Agent Builder agents |
|  **Agent Type**  | Single agent with MCP tools | Supervisor agent \+ multiple Agent Builder agents |
|  **Tool Integration**  | MCP servers and Strands tools | Agent Builder agents registered as tools |
|  **Delegation**  | Direct tool invocation | Autonomous agent selection and delegation |
|  **Complexity**  | Single-agent tasks | Multi-step, multi-agent workflows |
|  **Agent Reuse**  | N/A | Reuses existing Agent Builder deployments |
|  **Best for**  | Focused, single-domain tasks | Complex workflows requiring multiple specializations |

**Note**
Workflows require at least 1 Agent Builder use case as a specialized agent agent
All specialized agents must be Agent Builder use cases deployed in GAAB

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
