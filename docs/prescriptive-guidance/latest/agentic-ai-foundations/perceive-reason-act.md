---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/perceive-reason-act.html
---

# The agent function: perceive, reason, act
<a name="perceive-reason-act"></a>

At the core of every software agent is a cognitive cycle that is often described as the *perceive, reason, act *loop. This process is illustrated in the following diagram. It defines how agents operate autonomously in dynamic environments.

![Perceive, reason, act loop.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/images/guide-img/bf0cde42-baef-4bee-8fff-ca482667d2b6/images/7b030bd9-cde6-4b69-a4b6-243702dc6c7f.png)

+ **Perceive**: Agents gather information (for example, events, sensor inputs, or API signals) from the environment and update their internal state or beliefs.
+ **Reason**: Agents analyze current beliefs, goals, and contextual knowledge by using a plan library or logic system. This process might involve goal prioritization, conflict resolution, or intention selection.
+ **Act**: Agents select and execute actions that move them closer to achieving their delegated goals.

This architecture supports the ability of agents to function beyond rigid programming and enables flexible, context-sensitive, and goal-directed behavior. It forms the mental framework that guides the broader purposes of software agents.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
