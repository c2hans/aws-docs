---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/building-3P-services-best-practices.html
---

# Best practices and recommendations
<a name="building-3P-services-best-practices"></a>

## Service creation management
<a name="building-3P-services-service-creation-management"></a>
+ Keep onCreate operations lightweight to ensure a reasonable loading time for Agents
  + Use Promise timeouts for any external API calls during initialization to ensure fail-fast behavior
+ Handle service errors gracefully
  + Any uncaught error encountered during service initialization will be considered as a service failure, which will prevent agents from accessing the workspace

## Authentication
<a name="building-3P-services-authentication"></a>
+ Prompt for Authentication during agent workspace startup with a third-party service
  + Begin authentication process without blocking service execution
  + Centralize authentication prompting in your service to avoid redundant implementations in your third-party applications
+ Implement visual authentication interfaces (e.g., pop-ups) for agent interaction
+ Set appropriate authentication timeouts to prevent infinite retry loops
+ Ensure applications share the same origin as the third-party service

## Service coordination
<a name="building-3P-services-service-coordination"></a>
+ Consolidate interdependent behaviors within a single service
  + For example, any applications launched on the startup of the agent workspace should be done by one service to ensure a consistent launch order for agents

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
