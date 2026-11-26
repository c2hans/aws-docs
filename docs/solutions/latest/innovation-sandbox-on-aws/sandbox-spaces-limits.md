---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/sandbox-spaces-limits.html
---

# Sandbox Spaces quotas

| Quota | Value | Where it applies |
| --- | --- | --- |
| Concurrent agent turns in a deployment | 10 | Reserved concurrency of the Worker Lambda function. Lambda throttles messages beyond this quota, and a message moves to the dead-letter queue after three receives. |
| Maximum duration of one turn | 15 minutes | Timeout of the Worker Lambda function. |
| Model calls in one turn | 25 | Agent runtime. A model call and the commands that it triggers count as one. When the quota is reached, the agent ends the turn with a message. |
| AWS CLI command timeout | 120 seconds | Agent runtime. |
| Command output that the model receives | 20,000 characters | Agent runtime. The agent tells the user when it cuts the output. |
| Connection record lifetime | 2 hours | Time to live of the connections table. |
| Conversation history retention | 30 days | Expiry of the AgentCore Memory events. |
| Delay before long-term memory deletion | 15 minutes | Delivery delay of the memory cleanup queue. |
| Token poll interval | 10 minutes | EventBridge Scheduler schedule. |
| Price refresh age | 24 hours | Age at which a stored model price is refreshed. |
