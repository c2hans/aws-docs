---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/actor-agent-cognition.html
---

# From the actor model to agent cognition
<a name="actor-agent-cognition"></a>

The purpose and structure of software agents are grounded in ideas that emerged from early computation models, particularly the actor model that was introduced by Carl Hewitt in the 1970s (Hewitt et al. 1973).

The actor model treats computation as a collection of independent, concurrently executing entities called *actors*. Each actor encapsulates its own state, interacts solely through asynchronous message passing, and can create new actors and delegate tasks.

This model provided the conceptual foundation for decentralized reasoning, reactivity, and isolation—all of which underpin the behavioral architecture of modern software agents.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
