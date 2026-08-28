---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-processing.html
---

# Processing payments
<a name="payments-processing"></a>

After you complete the control plane setup, use the following workflows to create instruments, sessions, and process payments.

**Tip**
You can automate the steps on this page with the AgentCore Payments skill in the AWS agent toolkit. The skill is part of the **aws-agents** plugin and lets an AI coding agent create your Payment Manager, connector, credential provider, payment instrument, and session using the `agentcore` CLI, and add a process payment tool to your agent. For details, see the [quickstart](payments-getting-started.md) and the [AWS agent toolkit on GitHub](https://github.com/aws/agent-toolkit-for-aws/tree/main).

**Topics**
+ [Create a payment instrument](payments-create-instrument.md)
+ [Fund the wallet and grant agent permissions](payments-fund-wallet.md)
+ [Create a payment session](payments-create-session.md)
+ [Coinbase Bazaar via AgentCore Gateway](payments-connect-bazaar.md)
+ [Process a payment](payments-process-payment.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
