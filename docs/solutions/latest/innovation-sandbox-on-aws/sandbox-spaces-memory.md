---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/sandbox-spaces-memory.html
---

# Conversation memory

The solution keeps each user’s Sandbox Space conversations in AgentCore Memory, encrypted with the solution’s AWS KMS key. Memory is isolated by lease and by user. The agent reads and writes only the memory of the user who sent the message, on that lease, and a prompt can’t change which memory it uses. Administrators and managers can’t read another user’s conversations through the solution.
+  **Conversation history** is the list of user messages and agent replies. Each message expires 30 days after it is written.
+  **Long-term memory** is a set of facts that the agent extracts from the conversation to recall earlier work. The solution deletes it about 15 minutes after the lease terminates, so the records still exist during that time. The delay gives AgentCore time to finish extracting facts from the last messages. If the deletion fails after all retries, an Amazon CloudWatch alarm fires. For more information, see [Alarms](monitoring-alarms.md#solution-alarms).

For the user view, see [Conversation history](user-section.md#sandbox-spaces-history).
