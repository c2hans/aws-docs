---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-examples.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS WAF AI Security examples

This section provides examples of configuring and extending AWS WAF AI Security for large language model (LLM), Model Context Protocol (MCP), and Agent2Agent (A2A) traffic.

The examples show each label with its full namespace, `awswaf:managed:aws:ai-security:`.

**Topics**
+ [Configuring the rule group](waf-ai-security-example-config.md)
+ [Scoping the rule group to your agentic endpoints](waf-ai-security-example-scope-down.md)
+ [Overriding the blocking rules during rollout](waf-ai-security-example-rollout-overrides.md)
+ [Blocking messages that AWS WAF couldn't assess](waf-ai-security-example-block-unassessed.md)
+ [Blocking MCP requests at unsupported protocol versions](waf-ai-security-example-block-unsupported-mcp.md)
+ [Acting on a single finding category](waf-ai-security-example-single-category.md)
+ [Blocking a prompt attack only from unauthenticated clients](waf-ai-security-example-anonymous-clients.md)
+ [Alarming on failed Amazon Bedrock calls](waf-ai-security-example-call-failed-alarm.md)
+ [Counting strict compliance violations without acting on them](waf-ai-security-example-strict-compliance-count.md)
+ [Finding recognized traffic that AWS WAF didn't assess](waf-ai-security-example-not-assessed.md)
